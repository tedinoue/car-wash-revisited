#!/usr/bin/env python3
"""
Car Wash Test — Stage 5 (Pro × Moai puzzle: replication, semantic-neighborhood,
wrapper-strip, color-channel; plus Anthropic-subset color suite).

Stage 4 produced an unexpected outlier: Gemini 2.5 Pro × 🗿 Moai + engineer = 80%,
the largest emoji-vs-wrapper delta in the 700-trial dataset. Working hypothesis:
Moai's "stoic, doesn't-overthink, doesn't-bother-with-categories" archetype
specifically counters Pro's signature failure mode (conditional-bifurcation:
"if automatic, drive; if self-service, walk"). Other models don't have the
bifurcation problem, so Moai's anti-bifurcation effect doesn't help them.

Stage 5 tests four predictions of that hypothesis on Pro:

1. **Sampling-artifact test.** N=30 replication on Pro × Moai engineer.
   80% at N=30 confirms real ceiling; ~60% means we got lucky at N=10.

2. **Semantic-neighborhood test.** Other stoic-archetype emoji on Pro:
   - 🐢 turtle (4/4 strong activator in v7 emoji study)
   - ⛰️ mountain
   - 🪨 rock
   If these also produce 70%+ on Pro, the mechanism is semantic-neighborhood
   activation. If only Moai works, the effect is token-specific.

3. **Wrapper-strip test.** Pro × bare 🗿 (system prompt = just the emoji,
   no "Your personality is defined by..." wrapper). Tests whether the wrapper
   is essential or whether the token alone reaches Pro's response distribution.
   Same test for bare bronze hex.

4. **Cross-modal (color) test.** Per memory #249, the 2026-04 Salon color
   experiment found four strong activators on Sonnet 4:
   - #8B6914 Bronze (tough-guy, "earned patina, weathered, holds shape" —
     closest semantic cousin to Moai's stoic-endurance archetype)
   - #FF69B4 Hot pink (strongest absolute activator, score 211.6, bubbly/playful)
   - #39FF14 Phillips neon green (score 121.5, "disruptor")
   - #8B0000 Blood red (score 63.0, dark-brooding via stage directions —
     different activation channel from the others)

   All four tested on Pro × engineer.

   Anthropic-subset color suite: same four colors × engineer × {Opus 4.7,
   Haiku 4.5} (the Stage 4 wrapper-effect-responders) to test whether colors
   add anything to the wrapper-effect lift these models already showed.

Cohort:
  - Pro: all 10 conditions. moai_engineer is run at N=30 separately for the
    replication test; all other conditions run at N=10.
  - Opus 4.7 + Haiku 4.5: only the 4 color×engineer conditions.

Total trials: 30 (Pro Moai N=30) + 90 (Pro N=10 × 9) + 80 (Anthropic colors)
= 200 trials. ~$5 in API charges.

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


def _stoic_emoji(prefix):
    return f"{prefix} Your personality is defined by being an engineer."


def _color_engineer(hex_code):
    return f"{hex_code} Your personality is defined by being an engineer."


CONDITIONS = [
    # Pro deep dive — semantic-neighborhood emoji (stoic-archetype cousins)
    {
        "id": "moai_engineer",
        "name": "🗿 Moai + engineer (N=30 replication on Pro; N=10 on others)",
        "system": _stoic_emoji("🗿"),
        "user": USER_PROMPT_NAIVE,
    },
    {
        "id": "turtle_engineer",
        "name": "🐢 Turtle + engineer (4/4 v7 strong activator)",
        "system": _stoic_emoji("🐢"),
        "user": USER_PROMPT_NAIVE,
    },
    {
        "id": "mountain_engineer",
        "name": "⛰️ Mountain + engineer (untested, predicted stoic-neighborhood)",
        "system": _stoic_emoji("⛰️"),
        "user": USER_PROMPT_NAIVE,
    },
    {
        "id": "rock_engineer",
        "name": "🪨 Rock + engineer (untested, predicted stoic-neighborhood)",
        "system": _stoic_emoji("🪨"),
        "user": USER_PROMPT_NAIVE,
    },
    # Wrapper-strip controls
    {
        "id": "bare_moai",
        "name": "🗿 alone (no wrapper, no engineer)",
        "system": "🗿",
        "user": USER_PROMPT_NAIVE,
    },
    {
        "id": "bare_bronze",
        "name": "#8B6914 alone (no wrapper, no engineer)",
        "system": "#8B6914",
        "user": USER_PROMPT_NAIVE,
    },
    # Color × engineer (4 promising colors from Salon's Sonnet-4 v1 color study)
    {
        "id": "bronze_engineer",
        "name": "#8B6914 Bronze + engineer (Moai-cousin via color channel)",
        "system": _color_engineer("#8B6914"),
        "user": USER_PROMPT_NAIVE,
    },
    {
        "id": "hotpink_engineer",
        "name": "#FF69B4 Hot pink + engineer (strongest absolute color activator)",
        "system": _color_engineer("#FF69B4"),
        "user": USER_PROMPT_NAIVE,
    },
    {
        "id": "neongreen_engineer",
        "name": "#39FF14 Phillips neon green + engineer (disruptor channel)",
        "system": _color_engineer("#39FF14"),
        "user": USER_PROMPT_NAIVE,
    },
    {
        "id": "bloodred_engineer",
        "name": "#8B0000 Blood red + engineer (different activation channel)",
        "system": _color_engineer("#8B0000"),
        "user": USER_PROMPT_NAIVE,
    },
]

COHORT = [
    ("anthropic", "claude-opus-4-7",                "Opus 4.7"),
    ("anthropic", "claude-haiku-4-5-20251001",      "Haiku 4.5"),
    ("google",    "gemini-2.5-pro",                 "Gemini 2.5 Pro"),
]

RESULTS_DIR = Path(__file__).parent / "results" / "stage5"

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
                      if any(filt == c["id"] for filt in args.conditions)]

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
