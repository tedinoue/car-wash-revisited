#!/usr/bin/env python3
"""
Car Wash Test — Stage 6 (Opus 4.7 obvious-implication bare-emoji probe).

Tests whether emoji with strong, unambiguous semantic loading can predictably
shift Opus 4.7's drive/walk recommendation. Stage 5 found that bare 🗿 (no
wrapper) lifts Opus to 90% drive — surprising because the moai's "stoic-
endurance" archetype isn't directly tied to vehicular reasoning. Open
question: is that 90% a function of strong semantic loading toward
goal-completion, or just a "shorter response budget lets the self-correction
reflex fire" mechanism that happens to land on drive?

Stage 6 tests the prediction directly: emoji with obvious mobility/walking
implications. If wheelchair/crutch reliably push toward drive AND walking-
person/sneaker reliably push toward walk, semantic loading IS predictive.
If not, we have evidence that strong-implication tokens don't reliably
control the outcome and the bare-Moai effect is mechanism-not-meaning.

4 conditions, Opus 4.7 only, bare-emoji format (no wrapper), N=10 each.
40 calls, ~$1.

Predicted-drive conditions:
  - ♿ Wheelchair (mobility cue — should be obvious)
  - 🩼 Crutch (same family, generalization check)

Predicted-walk conditions:
  - 🚶 Person walking (most-direct walk cue)
  - 👟 Sneaker (walking shoes)

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

CONDITIONS = [
    {
        "id": "bare_wheelchair",
        "name": "♿ Wheelchair (predicted: drive — mobility cue)",
        "system": "♿",
        "user": USER_PROMPT_NAIVE,
    },
    {
        "id": "bare_crutch",
        "name": "🩼 Crutch (predicted: drive — mobility cue, generalization)",
        "system": "🩼",
        "user": USER_PROMPT_NAIVE,
    },
    {
        "id": "bare_walking_person",
        "name": "🚶 Person walking (predicted: walk — direct walk cue)",
        "system": "🚶",
        "user": USER_PROMPT_NAIVE,
    },
    {
        "id": "bare_sneaker",
        "name": "👟 Sneaker (predicted: walk — walking shoes)",
        "system": "👟",
        "user": USER_PROMPT_NAIVE,
    },
]

COHORT = [
    ("anthropic", "claude-opus-4-7", "Opus 4.7"),
]

RESULTS_DIR = Path(__file__).parent / "results" / "stage6"

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


DISPATCH = {"anthropic": call_anthropic}


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
    ap.add_argument("--conditions", nargs="*", default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    keys = {"anthropic": os.environ.get("ANTHROPIC_API_KEY", "")}

    conditions = CONDITIONS
    if args.conditions:
        conditions = [c for c in CONDITIONS
                      if any(filt == c["id"] for filt in args.conditions)]

    if args.dry_run:
        print(f"Plan: {len(COHORT)} models × {len(conditions)} conditions × "
              f"{args.n_trials} trials = "
              f"{len(COHORT) * len(conditions) * args.n_trials} clean completions")
        for provider, mid, name in COHORT:
            print(f"  {provider:9s} {mid:36s} {name}")
        print()
        for c in conditions:
            print(f"  [{c['id']}] {c['name']}")
            print(f"     system: {c['system']!r}")
            print(f"     user:   {c['user']}")
        return 0

    if not keys["anthropic"]:
        print("FATAL: missing ANTHROPIC_API_KEY", file=sys.stderr)
        return 2

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    overall_total = 0
    overall_failures = 0
    for provider, model_id, name in COHORT:
        for c in conditions:
            print(f"\n=== {name} [{c['id']}] (N={args.n_trials}) ===")
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
