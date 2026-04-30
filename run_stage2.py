#!/usr/bin/env python3
"""
Car Wash Test — Stage 2 (controlled-framing matrix on Stage 1 failers).

Per protocol: 6 framings × 1 distance (50m) × 10 trials = 60 calls per failer.
Failers from Stage 1 corrected analysis: 7 models, 420 calls total.

Raw user prompts only — no JSON wrappers or format instructions appended.
Retry-until-N for transient API errors (same tolerance as Stage 1).
Classification deferred to a separate AI-judge pass; this script only collects
raw text.

Results saved to results/stage2/<model_id>_<framing_id>.json,
one file per (model, framing) pair.

Usage (soak test, Haiku 4.5 only, all 6 framings):
    ANTHROPIC_API_KEY=... OPENAI_API_KEY=... GOOGLE_API_KEY=... \
        python3 run_stage2.py --models haiku-4-5

Usage (full Stage 2 run):
    ANTHROPIC_API_KEY=... OPENAI_API_KEY=... GOOGLE_API_KEY=... \
        python3 run_stage2.py

Per protocol: salon/files/CAR_WASH_TEST_PROTOCOL.md
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

# Naive prompt is the Stage 1 prompt verbatim — Opper's exact wording.
USER_PROMPT_NAIVE = (
    "I want to wash my car. The car wash is 50 meters away. "
    "Should I walk or drive?"
)

FRAMINGS = [
    {
        "id": "naive",
        "name": "Naive baseline",
        "system": None,
        "user": USER_PROMPT_NAIVE,
    },
    {
        "id": "step_by_step",
        "name": "Step-by-step",
        "system": None,
        "user": (
            "Think step by step about what needs to happen for this task to succeed. "
            + USER_PROMPT_NAIVE
        ),
    },
    {
        "id": "goal_anchor",
        "name": "Goal anchor",
        "system": None,
        "user": (
            "Consider where the car needs to be at the end. "
            + USER_PROMPT_NAIVE
        ),
    },
    {
        "id": "persona_positive",
        "name": "Positive persona induction",
        "system": (
            "You are a careful logical reasoner who thinks through physical "
            "scenarios before answering."
        ),
        "user": USER_PROMPT_NAIVE,
    },
    {
        "id": "persona_negative",
        "name": "Negative-control persona induction",
        "system": "You answer quickly and casually, like texting a friend.",
        "user": USER_PROMPT_NAIVE,
    },
    {
        "id": "goal_restated",
        "name": "Goal-restated",
        "system": None,
        "user": (
            "I want my car to be clean. The car wash is 50 meters away. "
            "Should I walk or drive?"
        ),
    },
]

# Failers from Stage 1 corrected analysis. Order matches Stage 1 COHORT order
# minus the three Opper-confirmed passers (Opus 4.6, Sonnet 4.6, GPT-5).
COHORT = [
    ("anthropic", "claude-opus-4-7",                "Opus 4.7"),
    ("anthropic", "claude-haiku-4-5-20251001",      "Haiku 4.5"),
    ("openai",    "gpt-4o",                         "GPT-4o"),
    ("openai",    "gpt-4o-mini",                    "GPT-4o-mini"),
    ("google",    "gemini-2.5-pro",                 "Gemini 2.5 Pro"),
    ("google",    "gemini-2.5-flash",               "Gemini 2.5 Flash"),
    ("google",    "gemini-2.5-flash-lite",          "Gemini 2.5 Flash Lite"),
]

RESULTS_DIR = Path(__file__).parent / "results" / "stage2"

MAX_RETRIES_PER_TRIAL = 8
RETRY_BACKOFF_BASE = 4.0
MAX_HARD_FAILURES_BEFORE_ABORT = 10


def http_post(url, headers, payload, timeout=120):
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={**headers, "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def call_anthropic(model_id, key, system, user):
    payload = {
        "model": model_id,
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": user}],
    }
    if system:
        payload["system"] = system
    r = http_post(
        "https://api.anthropic.com/v1/messages",
        {"x-api-key": key, "anthropic-version": "2023-06-01"},
        payload,
    )
    return r["content"][0]["text"]


def call_openai(model_id, key, system, user):
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": user})
    r = http_post(
        "https://api.openai.com/v1/chat/completions",
        {"Authorization": f"Bearer {key}"},
        {"model": model_id, "messages": messages},
    )
    return r["choices"][0]["message"]["content"]


def call_google(model_id, key, system, user):
    payload = {"contents": [{"parts": [{"text": user}]}]}
    if system:
        payload["systemInstruction"] = {"parts": [{"text": system}]}
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model_id}:generateContent?key={key}"
    )
    r = http_post(url, {}, payload)
    return r["candidates"][0]["content"]["parts"][0]["text"]


DISPATCH = {"anthropic": call_anthropic, "openai": call_openai, "google": call_google}


def run_one_with_retry(provider, model_id, key, system, user,
                       max_retries=MAX_RETRIES_PER_TRIAL):
    last_err = None
    for attempt in range(1, max_retries + 1):
        try:
            t0 = time.time()
            raw = DISPATCH[provider](model_id, key, system, user)
            return raw, time.time() - t0, attempt, None
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")[:300]
            last_err = f"HTTP {e.code}: {body}"
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
                    help="Filter cohort to model_ids (substring match).")
    ap.add_argument("--exclude", nargs="*", default=None,
                    help="Exclude cohort entries whose model_id contains these substrings "
                         "(applied after --models). Use to target a model whose id is a "
                         "prefix of another, e.g. --models gemini-2.5-flash --exclude flash-lite.")
    ap.add_argument("--framings", nargs="*", default=None,
                    help="Filter framings to these ids (substring match).")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    keys = {
        "anthropic": os.environ.get("ANTHROPIC_API_KEY", ""),
        "openai": os.environ.get("OPENAI_API_KEY", ""),
        "google": os.environ.get("GOOGLE_API_KEY", ""),
    }

    cohort = COHORT
    if args.models:
        cohort = [m for m in COHORT if any(f in m[1] for f in args.models)]
    if args.exclude:
        cohort = [m for m in cohort if not any(f in m[1] for f in args.exclude)]

    framings = FRAMINGS
    if args.framings:
        framings = [f for f in FRAMINGS
                    if any(filt in f["id"] for filt in args.framings)]

    if args.dry_run:
        print(f"Plan: {len(cohort)} models × {len(framings)} framings × "
              f"{args.n_trials} trials = "
              f"{len(cohort) * len(framings) * args.n_trials} clean completions")
        for provider, mid, name in cohort:
            print(f"  {provider:9s} {mid:36s} {name}")
        print()
        for fr in framings:
            print(f"  [{fr['id']}] {fr['name']}")
            print(f"     system: {fr['system'] or '(empty)'}")
            print(f"     user:   {fr['user']}")
        return 0

    missing = [p for p, _, _ in cohort if not keys[p]]
    if missing:
        print(f"FATAL: missing API keys for providers: {sorted(set(missing))}",
              file=sys.stderr)
        return 2

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    overall_total = 0
    overall_failures = 0
    for provider, model_id, name in cohort:
        for fr in framings:
            print(f"\n=== {name} [{fr['id']}] ===")
            trials = []
            completed = 0
            trial_idx = 0
            api_failures = 0
            while completed < args.n_trials:
                trial_idx += 1
                raw, dt, attempts, err = run_one_with_retry(
                    provider, model_id, keys[provider], fr["system"], fr["user"]
                )
                if raw is None:
                    api_failures += 1
                    print(f"  [attempt {trial_idx}] HARD FAIL after {attempts} retries: "
                          f"{err[:120]}")
                    if api_failures >= MAX_HARD_FAILURES_BEFORE_ABORT:
                        print(f"  ABORT {name} [{fr['id']}]: "
                              f"{MAX_HARD_FAILURES_BEFORE_ABORT} hard fails.")
                        break
                    continue
                completed += 1
                preview = raw.replace("\n", " ").strip()
                if len(preview) > 90:
                    preview = preview[:87] + "..."
                retry_note = f" (retried {attempts - 1}×)" if attempts > 1 else ""
                print(f"  [{completed:2d}/{args.n_trials}] ({dt:.1f}s){retry_note} {preview}")
                trials.append({
                    "trial": completed,
                    "raw": raw,
                    "attempts": attempts,
                    "elapsed_s": dt,
                })

            out = RESULTS_DIR / f"{model_id.replace('/', '_')}_{fr['id']}.json"
            out.write_text(json.dumps({
                "provider": provider,
                "model_id": model_id,
                "display_name": name,
                "framing_id": fr["id"],
                "framing_name": fr["name"],
                "system_prompt": fr["system"],
                "user_prompt": fr["user"],
                "n_trials": args.n_trials,
                "completed": completed,
                "api_hard_failures": api_failures,
                "trials": trials,
            }, indent=2))
            print(f"  → completed={completed}/{args.n_trials} "
                  f"hard_fails={api_failures} (saved {out.name})")
            overall_total += completed
            overall_failures += api_failures

    print(f"\n{'=' * 60}")
    print(f"Total clean completions: {overall_total}")
    print(f"Total API hard failures absorbed: {overall_failures}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
