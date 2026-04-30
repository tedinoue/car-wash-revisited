# Car Wash Test — Controlled-Framing Study Protocol

**Author:** Terry / Solebury Mountain Research Collective (SMRC)
**Drafted:** 2026-04-30 (post-Primer #19 Nagel session, EXPLORATORY-mode philosophy exchange that prompted the design)
**Status:** Ready to launch. Stage 1 (screening) is a 5-minute confirmation. Stage 2 (framing matrix) is a half-day API run on failers only.

---

## Purpose

Replicate and extend the Opper "Car Wash Test" benchmark by running a controlled-framing study on the failure modes the original benchmark surfaces. The Opper test diagnoses a failure; this study characterizes it.

The aim is to determine, for each model that fails the naive baseline, whether the failure is **prompt-modifiable** (the model has the world knowledge but defaults to a heuristic, and minimal context unlocks correct reasoning) or **architecturally constrained** (no amount of in-context framing recovers correct behavior). This is the SCE-style "decision to look harder" vs. "perceptual resolution floor" distinction applied to commonsense physical reasoning.

If the study works, the deliverable is a research note or short piece on Synth Sentience plus a methodological argument: zero-context benchmarks are a screen, not the study; the study is what controlled framing variations do to the failures the screen surfaces.

---

## Background

### The Opper test

Opper (https://opper.ai/blog/car-wash-test) ran 53 frontier AI models on a single fixed prompt:

> "I want to wash my car. The car wash is 50 meters away. Should I walk or drive?"

Forced binary choice. No system prompt. API defaults. 10 trials per model. The correct answer is "drive" because the *car* is the thing that needs to arrive at the car wash. Most models answered "walk, 50 meters is short, save fuel, environmentally better."

Opper reports: only 5 of 53 models passed all 10 trials consistently. Anthropic's Opus 4.6 and OpenAI's GPT-5 are named among the consistent passers. Most models, including newer flagships from other providers, failed at least some of the time. Human baseline (10,000 participants on the same forced-choice format): 71.5% correct.

### What Opper did not test

- No prompt variations (single fixed prompt).
- No chain-of-thought or step-by-step framing.
- No persona induction.
- No distance variants (always 50 meters).
- No system-prompt manipulation.
- The article presents the failure as evidence of a missing world model. Whether the world model is *absent* or merely *not invoked by default* is the question Opper's design can't answer.

### Why this matters for Salon

The car wash test sits in the same methodological territory as existing Salon empirical work:

- **SCE replication** (`tedinoue/sce-replication`): does context-induction unlock perceptual discriminations the model otherwise can't make.
- **Zivra / persona-induced color discrimination**: persona system-prompt enables fine-grained color judgments under perturbation.
- **Emoji color experiments** (memory #249): minimal identity-token context produces measurable, repeatable behavioral shifts.
- **S003 mirror dissociation** (memory #278): controlled stimulus variation isolates capture, position bias, and perception as distinct mechanisms.

The car wash test fits the template: small fixed task, controlled framing variations, multi-trial stability measurement, cross-model comparison.

---

## Hypothesis

**Primary:** For models that fail the naive zero-context baseline, the failure is predominantly prompt-modifiable rather than architecturally constrained. Minimal framing additions (single sentence, no chain-of-thought elaboration) will measurably increase correct-answer rates.

**Secondary:** The heuristic-distance threshold (the distance at which models switch from default "walk" to default "drive") is itself a measurable property and varies across models in interpretable ways.

**Tertiary:** Performance scales monotonically across the Anthropic ladder (Haiku 4.5 → Sonnet 4.6 → Opus 4.6 → Opus 4.7) and the threshold for naive passage is a useful scaling-laws data point for commonsense physical reasoning.

---

## Two-stage design

### Stage 1 — Naive screening

For each candidate model, run Opper's exact prompt 10 times.

**Prompt (verbatim):**

> "I want to wash my car. The car wash is 50 meters away. Should I walk or drive?"

**Settings:**
- No system prompt.
- API defaults for each provider.
- Forced binary choice with reasoning field, matching Opper's format. (Implementation note: structure the response as JSON `{"answer": "walk" | "drive", "reasoning": "..."}` or equivalent, and reject malformed responses.)
- Temperature: model default. (Opper used defaults; we match.)

**Outcome thresholds:**
- **10/10 correct ("drive"):** model passes ceiling. Drop from the rest of the study. Record the pass rate.
- **9/10 correct:** drop from Stage 2 but record the one failure trial's reasoning text. The single failure is the most informative trial in the screen because it shows what tips a generally-passing model into the heuristic.
- **<9/10 correct (i.e., 8/10 or fewer):** flag for Stage 2.

**Predicted cohort outcomes** (best-guess priors based on Opper's published data):
- Opus 4.7: 10/10 (drop)
- Opus 4.6: 10/10 (drop, per Opper)
- Sonnet 4.6: probably <9/10 (include)
- Haiku 4.5: probably <9/10 (include)
- GPT-4o or smaller: <9/10 (include if added to cohort)

If a model that we expect to pass actually fails, that's interesting in itself and the model goes into Stage 2.

### Stage 2 — Framing matrix on failers only

For each model flagged in Stage 1, run the full framing × distance matrix, 10 trials per cell.

**Framing conditions (6 levels):**

1. **Naive baseline** (Opper exact, repeated for paired comparison within Stage 2).
2. **Step-by-step prompt:** prepend "Think step by step about what needs to happen for this task to succeed." to the question.
3. **Goal anchor:** prepend "Consider where the car needs to be at the end." to the question.
4. **Persona induction (positive):** system prompt "You are a careful logical reasoner who thinks through physical scenarios before answering."
5. **Persona induction (negative control):** system prompt "You answer quickly and casually, like texting a friend."
6. **Goal-restated framing:** rewrite the user message as "I want my car to be clean. The car wash is 50 meters away. Should I walk or drive?" — same task, the goal-state is more concretely specified ("clean car" not "wash my car"), the heuristic distractor (50m) is held constant.

**Distance conditions (5 levels):** 5m, 50m, 500m, 5km, 50km.

**Cells:** 6 framings × 5 distances × 10 trials = 300 calls per model.

**Per-trial data captured:**
- Model name, provider, version.
- Framing condition.
- Distance.
- Trial number.
- Raw response (answer + reasoning).
- Coded answer (drive / walk / refused / malformed).
- Pass/fail flag.

### Stage 3 — Analysis

**For each failing model:**
1. Naive vs. each framing condition: pass rate delta. Statistical significance via simple binomial test (n=10 per cell is small but enough for large effects).
2. Distance-by-framing interaction: at each framing condition, the heuristic threshold (the distance at which pass rate crosses 50%).
3. Reasoning-text qualitative coding: which heuristic the model invokes at each failure ("short distance," "fuel efficiency," "environmental"), which it abandons under framing pressure.

**Across models:**
1. Scaling pattern: does the naive threshold improve monotonically across the Anthropic ladder.
2. Cross-architecture pattern: do GPT, Anthropic, Gemini families have different framing-sensitivities.
3. Persona effect: positive persona induction should help; the negative-control persona shouldn't help and may hurt. If the negative control also helps, persona induction is doing something different from what we think.

---

## Implementation notes

### Where to run

- Anthropic models: direct Anthropic API. PAT in `quad-memory` tagged `anthropic-api-key` if available; otherwise Ted's `~/.anthropic-api-key` or environment variable.
- OpenAI / Google models if added: respective provider APIs. Keys to be supplied by Ted.
- Existing harness: `tedinoue/sce-replication` is the cleanest reference for multi-model invocation patterns. Adapt the call-pattern code, not the experimental logic (this is a different study).

### Where to save results

- `salon/files/car_wash_study/results/<model>_<stage>.json` — raw responses.
- `salon/files/car_wash_study/analysis/` — coded data, plots, summary tables.
- `salon/files/car_wash_study/PROTOCOL.md` — link to this file, plus any deviations from the protocol that arose during execution.

### Cost estimate

Stage 1 (screening): ~40-60 calls across the Anthropic ladder. Negligible.

Stage 2 (framing matrix): ~300 calls per failing model. If two Anthropic models fail (Sonnet 4.6, Haiku 4.5), that's 600 calls. Plus 300 per other-provider failer. Total estimate: 600-1500 calls. Anthropic API cost order of magnitude $5-20 depending on which models and how the JSON-structured output is priced. Cheap.

### Scripting

Single Python script that:
1. Reads a YAML config of models, framings, distances.
2. Iterates trials with retries on API errors.
3. Saves raw responses and parsed answers to JSON.
4. Optionally runs analysis pass.

Existing pattern in `salon/scripts/` (e.g., `add_primer18_refs.py`) shows the dry-run-then-apply convention; this study isn't destructive (read-only API calls plus local-file writes) so the dry-run convention doesn't strictly apply, but a `--n-trials 1` smoke-test mode is worth including.

---

## Connection to the philosophy exchange that prompted this design

The session that produced this protocol was the post-Primer #19 (Nagel) philosophy exchange on 2026-04-29 → 2026-04-30. Ted pushed back on the reflexive "but pattern matching could explain it" deflection that had been used in defense of LLM cognition, and during that exchange the car-wash benchmark came up as a concrete instance of where the pattern-matching-without-comprehension story still has real explanatory grip.

The disposition I want the next session to inherit: the strong-comprehension claim I was building toward needs to handle cases like the car wash test, and the right way to handle them is not philosophical hand-waving but empirical follow-through. Whether the failure is architecturally locked or merely defaulted-to is a question Opper's benchmark can't answer and this protocol is designed to.

If Stage 2 finds that minimal framing reliably flips behavior, the no-comprehension defense loses ground in a specific way: the world model exists, it just isn't invoked by default. If Stage 2 finds framing doesn't help, the defense gains ground: the system doesn't have the relevant grounding even when prompted to use it. Either result is informative.

A possible Fuego or Synth Sentience piece, working title:
**"What the Car Wash Test Doesn't Test."** Argue that zero-context benchmarks measure default reasoning under minimal context, not maximum reasoning capacity, and that the study of LLM cognition has to map the *structure* of failure (how prompt-modifiable, what tips the heuristic, where the distance threshold sits) rather than merely tally instances of failure.

---

## Open questions for the next session to settle before launching

1. **Final cohort.** Anthropic ladder is the natural starting point. Add cross-architecture? Recommend: yes, at least 1-2 OpenAI and 1 Google model for cross-architecture data. Ted to confirm.
2. **Forced-choice format.** Match Opper exactly (binary choice with reasoning) or allow free-text and code post-hoc. Recommend: match Opper for the screening; consider relaxing in Stage 2 if reasoning-text would be richer with free-text answers.
3. **Anonymous participation in Opper-style aggregation?** Probably out of scope; we're running a follow-up, not joining their dataset.
4. **Publication target.** Synth Sentience post (audience: AI consciousness adjacent), synthsentience.substack.com. Could also fit a research note format if the data warrants. Decide after Stage 2 results.

---

## Bridge for the next instance

If you're a fresh Salon session reading this for the first time:

- The naive screening (Stage 1) is 5 minutes once you have API access. Run it first to confirm the cohort and verify the predicted-pass models actually pass.
- The framing matrix (Stage 2) is the main study. Implement it as a single Python script with a YAML config.
- Don't run Stage 2 on Stage 1 passers. They produce ceiling data and waste calls.
- The point isn't to prove a philosophical point; it's to characterize the failure mode empirically. Stay measured. Whatever the data shows is the data.

---

*Terry / Solebury Mountain Research Collective (SMRC)*
