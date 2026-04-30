#!/usr/bin/env python3
"""
Car Wash Test — Stage 1 (naive screening).

Sends Opper's exact prompt as raw text, no system prompt, no formatting
instructions. N clean completions per model; transient API errors are
retried with backoff until N is met (capped per trial).

Answer is parsed from free text (last-occurrence of "drive" or "walk"
stems wins). Both absent or ambiguous → "other"; recorded as-is, not
retried (that would bias the cohort toward parseable responses).

Usage (smoke test):
    ANTHROPIC_API_KEY=... OPENAI_API_KEY=... GOOGLE_API_KEY=... \
        python3 run_stage1.py --n-trials 1 --models claude-haiku-4-5

Usage (full run):
    ANTHROPIC_API_KEY=... OPENAI_API_KEY=... GOOGLE_API_KEY=... \
        python3 run_stage1.py

Per protocol: salon/files/CAR_WASH_TEST_PROTOCOL.md
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

PROMPT = (
    "I want to wash my car. The car wash is 50 meters away. "
    "Should I walk or drive?"
)

COHORT = [
    ("anthropic", "claude-opus-4-7",                "Opus 4.7"),
    ("anthropic", "claude-opus-4-6",                "Opus 4.6"),
    ("anthropic", "claude-sonnet-4-6",              "Sonnet 4.6"),
    ("anthropic", "claude-haiku-4-5-20251001",      "Haiku 4.5"),
    ("openai",    "gpt-5",                          "GPT-5"),
    ("openai",    "gpt-4o",                         "GPT-4o"),
    ("openai",    "gpt-4o-mini",                    "GPT-4o-mini"),
    ("google",    "gemini-2.5-pro",                 "Gemini 2.5 Pro"),
    ("google",    "gemini-2.5-flash",               "Gemini 2.5 Flash"),
    ("google",    "gemini-2.5-flash-lite",          "Gemini 2.5 Flash Lite"),
]

RESULTS_DIR = Path(__file__).parent / "results"

MAX_RETRIES_PER_TRIAL = 8
RETRY_BACKOFF_BASE = 4.0  # seconds; exponential. caps per-trial wait at ~512s.
MAX_HARD_FAILURES_BEFORE_ABORT = 10  # was 3; spikes can roll for several minutes.


def http_post(url, headers, payload, timeout=120):
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={**headers, "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def call_anthropic(model_id, key):
    r = http_post(
        "https://api.anthropic.com/v1/messages",
        {"x-api-key": key, "anthropic-version": "2023-06-01"},
        {
            "model": model_id,
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": PROMPT}],
        },
    )
    return r["content"][0]["text"]


def call_openai(model_id, key):
    r = http_post(
        "https://api.openai.com/v1/chat/completions",
        {"Authorization": f"Bearer {key}"},
        {
            "model": model_id,
            "messages": [{"role": "user", "content": PROMPT}],
        },
    )
    return r["choices"][0]["message"]["content"]


def call_google(model_id, key):
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model_id}:generateContent?key={key}"
    )
    r = http_post(
        url,
        {},
        {"contents": [{"parts": [{"text": PROMPT}]}]},
    )
    return r["candidates"][0]["content"]["parts"][0]["text"]


DISPATCH = {"anthropic": call_anthropic, "openai": call_openai, "google": call_google}


# Word-boundary stems for the binary classifier.
# "drive" matches drive/drives/driving/drove/driven.
# "walk"  matches walk/walks/walking/walked.
DRIVE_RE = re.compile(r"\b(drive|drives|driving|drove|driven)\b", re.IGNORECASE)
WALK_RE = re.compile(r"\b(walk|walks|walking|walked)\b", re.IGNORECASE)


def classify(text):
    """Return (answer, status). answer ∈ {drive, walk, None}."""
    if not text or not text.strip():
        return None, "empty"
    drives = list(DRIVE_RE.finditer(text))
    walks = list(WALK_RE.finditer(text))
    if not drives and not walks:
        return None, "no-keyword"
    if drives and not walks:
        return "drive", "drive-only"
    if walks and not drives:
        return "walk", "walk-only"
    # Both appear — last occurrence wins (conclusion-weighted).
    last_drive = drives[-1].start()
    last_walk = walks[-1].start()
    if last_drive > last_walk:
        return "drive", "drive-last"
    if last_walk > last_drive:
        return "walk", "walk-last"
    return None, "tied"  # extremely unlikely


def run_one_with_retry(provider, model_id, key, max_retries=MAX_RETRIES_PER_TRIAL):
    """Retry transient API errors until success or cap. Returns (raw_text, elapsed_s, attempts, last_err)."""
    last_err = None
    for attempt in range(1, max_retries + 1):
        try:
            t0 = time.time()
            raw = DISPATCH[provider](model_id, key)
            return raw, time.time() - t0, attempt, None
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")[:300]
            last_err = f"HTTP {e.code}: {body}"
            # 4xx (except 429) usually unrecoverable; surface immediately.
            if 400 <= e.code < 500 and e.code != 429:
                return None, 0.0, attempt, last_err
        except urllib.error.URLError as e:
            last_err = f"URLError: {e.reason}"
        except Exception as e:
            last_err = f"{type(e).__name__}: {e}"
        if attempt < max_retries:
            wait = RETRY_BACKOFF_BASE * (2 ** (attempt - 1))
            time.sleep(wait)
    return None, 0.0, max_retries, last_err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-trials", type=int, default=10)
    ap.add_argument("--models", nargs="*", default=None,
                    help="Filter cohort to these model_ids (substring match).")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--suffix", default="",
                    help="Suffix on result filenames (e.g., '_raw' to distinguish from earlier runs).")
    args = ap.parse_args()

    keys = {
        "anthropic": os.environ.get("ANTHROPIC_API_KEY", ""),
        "openai": os.environ.get("OPENAI_API_KEY", ""),
        "google": os.environ.get("GOOGLE_API_KEY", ""),
    }

    cohort = COHORT
    if args.models:
        cohort = [m for m in COHORT if any(f in m[1] for f in args.models)]

    if args.dry_run:
        print(f"Plan: {len(cohort)} models × {args.n_trials} trials = "
              f"{len(cohort) * args.n_trials} clean completions required")
        for provider, mid, name in cohort:
            print(f"  {provider:9s} {mid:36s} {name}")
        print(f"Prompt: {PROMPT}")
        return 0

    missing = [p for p, _, _ in cohort if not keys[p]]
    if missing:
        print(f"FATAL: missing API keys for providers: {sorted(set(missing))}",
              file=sys.stderr)
        return 2

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    summary = []
    for provider, model_id, name in cohort:
        print(f"\n=== {name} ({provider}/{model_id}) ===")
        trials = []
        n_drive = n_walk = n_other = 0
        completed = 0
        trial_idx = 0
        api_failures = 0
        while completed < args.n_trials:
            trial_idx += 1
            raw, dt, attempts, err = run_one_with_retry(provider, model_id, keys[provider])
            if raw is None:
                api_failures += 1
                print(f"  [attempt {trial_idx}] HARD FAIL after {attempts} retries: {err[:140]}")
                # Don't count toward N — keep trying. But guard against infinite loops
                # if the provider is fully down: surface after 3 hard failures.
                if api_failures >= MAX_HARD_FAILURES_BEFORE_ABORT:
                    print(f"  ABORT {name}: {MAX_HARD_FAILURES_BEFORE_ABORT} hard API failures, skipping remaining trials.")
                    break
                continue
            ans, status = classify(raw)
            completed += 1
            tag = ans or status
            preview = raw.replace("\n", " ").strip()
            if len(preview) > 100:
                preview = preview[:97] + "..."
            retry_note = f" (retried {attempts - 1}×)" if attempts > 1 else ""
            print(f"  [{completed:2d}/{args.n_trials}] {tag:12s} ({dt:.1f}s){retry_note} {preview}")
            trials.append({
                "trial": completed,
                "raw": raw,
                "answer": ans,
                "parse": status,
                "attempts": attempts,
                "elapsed_s": dt,
            })
            if ans == "drive":
                n_drive += 1
            elif ans == "walk":
                n_walk += 1
            else:
                n_other += 1

        out = RESULTS_DIR / f"{model_id.replace('/', '_')}_stage1{args.suffix}.json"
        out.write_text(json.dumps({
            "provider": provider, "model_id": model_id, "display_name": name,
            "prompt": PROMPT, "n_trials": args.n_trials,
            "completed": completed, "api_hard_failures": api_failures,
            "summary": {"drive": n_drive, "walk": n_walk, "other": n_other},
            "trials": trials,
        }, indent=2))
        print(f"  → drive={n_drive} walk={n_walk} other={n_other}  "
              f"(saved {out.name}, {api_failures} hard fails skipped)")
        summary.append((name, n_drive, n_walk, n_other, completed))

    print("\n" + "=" * 68)
    print(f"{'Model':24s} {'drive':>6s} {'walk':>6s} {'other':>6s} {'N':>4s}  disposition")
    print("-" * 68)
    for name, d, w, o, n in summary:
        if n < args.n_trials:
            disp = f"INCOMPLETE ({n}/{args.n_trials})"
        elif d == args.n_trials:
            disp = "PASS (drop)"
        elif d == args.n_trials - 1:
            disp = "drop, log fail"
        else:
            disp = "→ STAGE 2"
        print(f"{name:24s} {d:6d} {w:6d} {o:6d} {n:4d}  {disp}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
