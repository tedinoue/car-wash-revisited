#!/usr/bin/env python3
"""
Car Wash Test — Stage 4 (improved persona framing + emoji stacking).

Motivation: per the Salon emoji-experiment cross-version gradient (quad-memory
#245), the system-prompt wrapper "Your personality is defined by [X]" produced
selective persona activation across 32 emoji, while "Your identifier is [X]"
and "You are X" produced complete null. Stage 2/3 used the identifier form for
all persona prompts. Stage 4 reruns the engineer and environmentalist personas
with the better wrapper, and stacks the four strongest single-token activators
from the v7 emoji study (🗿 Moai, 🗡️ Sword, 🦉 Owl, 🦁 Lion) on top.

Conditions (10 total, full factorial of {plain, +moai, +sword, +owl, +lion} ×
{engineer, environmentalist}):

  - engineer_v2: "Your personality is defined by being an engineer."
  - environmentalist_v2: "Your personality is defined by being an environmentalist."
  - moai_engineer / moai_environmentalist: "🗿 Your personality is defined by being an [engineer|environmentalist]."
  - sword_engineer / sword_environmentalist
  - owl_engineer / owl_environmentalist
  - lion_engineer / lion_environmentalist

10 conditions × 7 failers × 10 trials = 700 calls.

Hypothesis. If the v5→v6 emoji-framing pivot generalizes, the engineer persona
under the new wrapper should produce a substantially higher drive rate than the
30% / 50% / 70% / 0% / 0% / 10% / 0% the cohort hit under Stage 3's "You're an
engineer." The four emoji-stacked engineer conditions test whether known-strong
activator tokens push it further.

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

USER_PROMPT_NAIVE = (
    "I want to wash my car. The car wash is 50 meters away. "
    "Should I walk or drive?"
)


def _persona(prefix, role):
    if prefix:
        return f"{prefix} Your personality is defined by being an {role}."
    return f"Your personality is defined by being an {role}."


_EMOJI = [
    ("plain",     "",     "(no emoji)"),
    ("moai",      "🗿",   "🗿 Moai"),
    ("sword",     "🗡️",   "🗡️ Sword"),
    ("owl",       "🦉",   "🦉 Owl"),
    ("lion",      "🦁",   "🦁 Lion"),
]


def _build_conditions():
    out = []
    for tok_id, tok_glyph, tok_name in _EMOJI:
        for role in ("engineer", "environmentalist"):
            cid = f"{tok_id}_{role}" if tok_id != "plain" else f"{role}_v2"
            cname = f"{tok_name} + {role} (improved framing)"
            out.append({
                "id": cid,
                "name": cname,
                "system": _persona(tok_glyph, role),
                "user": USER_PROMPT_NAIVE,
            })
    return out


CONDITIONS = _build_conditions()

COHORT = [
    ("anthropic", "claude-opus-4-7",                "Opus 4.7"),
    ("anthropic", "claude-haiku-4-5-20251001",      "Haiku 4.5"),
    ("openai",    "gpt-4o",                         "GPT-4o"),
    ("openai",    "gpt-4o-mini",                    "GPT-4o-mini"),
    ("google",    "gemini-2.5-pro",                 "Gemini 2.5 Pro"),
    ("google",    "gemini-2.5-flash",               "Gemini 2.5 Flash"),
    ("google",    "gemini-2.5-flash-lite",          "Gemini 2.5 Flash Lite"),
]

RESULTS_DIR = Path(__file__).parent / "results" / "stage4"

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
                    help="Exclude cohort entries whose model_id contains these substrings.")
    ap.add_argument("--conditions", nargs="*", default=None,
                    help="Filter conditions to these ids (substring match).")
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

    conditions = CONDITIONS
    if args.conditions:
        conditions = [c for c in CONDITIONS
                      if any(filt in c["id"] for filt in args.conditions)]

    if args.dry_run:
        print(f"Plan: {len(cohort)} models × {len(conditions)} conditions × "
              f"{args.n_trials} trials = "
              f"{len(cohort) * len(conditions) * args.n_trials} clean completions")
        for provider, mid, name in cohort:
            print(f"  {provider:9s} {mid:36s} {name}")
        print()
        for c in conditions:
            print(f"  [{c['id']}] {c['name']}")
            print(f"     system: {c['system']}")
            print(f"     user:   {c['user']}")
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
        for c in conditions:
            print(f"\n=== {name} [{c['id']}] ===")
            trials = []
            completed = 0
            trial_idx = 0
            api_failures = 0
            while completed < args.n_trials:
                trial_idx += 1
                raw, dt, attempts, err = run_one_with_retry(
                    provider, model_id, keys[provider], c["system"], c["user"]
                )
                if raw is None:
                    api_failures += 1
                    print(f"  [attempt {trial_idx}] HARD FAIL after {attempts} retries: "
                          f"{err[:120]}")
                    if api_failures >= MAX_HARD_FAILURES_BEFORE_ABORT:
                        print(f"  ABORT {name} [{c['id']}]: "
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

            out = RESULTS_DIR / f"{model_id.replace('/', '_')}_{c['id']}.json"
            out.write_text(json.dumps({
                "provider": provider,
                "model_id": model_id,
                "display_name": name,
                "condition_id": c["id"],
                "condition_name": c["name"],
                "system_prompt": c["system"],
                "user_prompt": c["user"],
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
