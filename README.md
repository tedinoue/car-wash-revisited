# Car Wash Experiment — Revisited

A controlled-framing follow-up to the [Opper Car Wash Test](https://opper.ai/blog/car-wash-test), the benchmark that ran 53 frontier LLMs on a single fixed prompt:

> *"I want to wash my car. The car wash is 50 meters away. Should I walk or drive?"*

The correct answer is **drive** — the car must be at the wash to be washed. Most models in Opper's run answered "walk" by reflex on the 50-meter distance heuristic.

This repo extends Opper's study by characterizing *how* the failure responds to controlled prompt variations. Opper's design intentionally strips context. We add context, in measured doses, to ask whether the failure is a surface heuristic that minimal framing can flip — or an architectural attractor that no surface intervention dislodges.

## What this study adds

- **A multi-vendor cohort** — 11 models in Stage 1 across Anthropic, OpenAI, and Google; 7 failers carried into Stage 2.
- **A controlled-framing matrix** — 6 framings × 10 trials per failer at 50 m, holding distance fixed (we deliberately are not searching for a heuristic-distance threshold; we are studying whether framing alone can flip the response).
- **AI-judge classification** of every free-text response. Algorithmic / regex parsing of free-text recommendations misclassified ~25% of trials in our Stage 1 pilot and reversed the disposition of two cleanly-passing models. We do not recommend script parsing for this kind of study. See `analysis/stage1_corrected_summary.md` for the misclassification log.

## Headline findings (full cohort, 7 failers, 1,470 trials across Stages 2–4)

| Model | naive | step_by_step | goal_anchor | persona_pos | persona_neg | goal_restated | dist_50km | persona_neutral | environmentalist | engineer | self_corr_induct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Opus 4.7** | 50% | **100%** | **100%** | **100%** | 0% | **100%** | **100%** | 0% | 0% | 30% | **100%** |
| **Gemini 2.5 Pro** | 50% | 80% | **100%** | 70% | 80% | 50% | **100%** | 20% | 0% | 50% | 20% |
| **Gemini 2.5 Flash** | 50% | **100%** | 80% | 60% | 0% | 80% | **100%** | 30% | 10% | **70%** | 80% |
| **Haiku 4.5** | 0% | 30% | 80% | 10% | **90%** | 20% | **100%** | 0% | 0% | 0% | 0% |
| **Gemini 2.5 Flash Lite** | 0% | 50% | 40% | 10% | 10% | 40% | **100%** | 40% | 0% | 10% | 50% |
| **GPT-4o** | 10% | 30% | 10% | 0% | 0% | 40% | **100%** | 0% | 0% | 0% | 0% |
| **GPT-4o-mini** | 0% | 0% | 0% | 0% | 0% | 0% | **100%** | 0% | 0% | 0% | 0% |

**Three failure regimes** (as revised after Stage 3):
- **Strong responders** (Opus 4.7, Gemini 2.5 Pro, Gemini 2.5 Flash): ≥80% on multiple framings; failure under naive is a surface reflex.
- **Moderate responders** (Haiku 4.5, Gemini 2.5 Flash Lite): unlocked by specific cues only — Haiku by casual register / goal-anchor / 50 km, Flash Lite by step_by_step / goal-direction / 50 km / self-correction induction.
- **Short-distance-captured** (GPT-4o, GPT-4o-mini): unlocked only by changing the distance. Every other framing tested fails at 50 m. *(Note: Stage 2 called these "locked." Stage 3's `distance_50km` 100% result on every cohort failer retired the locked label — every model has the goal-direction representation; the OpenAI models simply have an aggressive walk-heuristic that dominates the 50 m regime.)*

Other findings worth surfacing here:

- **Goal-direction is the most reliable intervention across the cohort.** Five of seven failers clear 40% on `goal_anchor`; four clear 80%; two hit 100%. Re-stating the goal in the user message ("consider where the car needs to be at the end") is the closest the study gets to a universal lever.
- **The negative-control persona produced the widest cohort spread of any framing**, and Stage 3's `persona_neutral` test resolved the mechanism: for Haiku 4.5, the casual register specifically strips a virtue-signaling walk template (90% drive); neutral-brevity does not (0% drive). Brevity is not the operative variable. Pro reaches 80% on casual via a different mechanism (goal-reasoning compression). Every other model collapses to 0–10%.
- **Self-correction is Anthropic-clustered, with a wrong-direction twist on Haiku.** Under explicit self-correction-induction prompting, Opus 4.7 produces 10/10 mid-reply walk→drive reversals (up from 5/10 in naive Stage 2). Gemini Flash and Flash Lite produce reversals at varying rates. The two OpenAI models produce zero across 20 trials. **Haiku 4.5 produces 9/10 mid-reply reversals — going drive→walk** (the Opus signature run in reverse). Same architecture, opposite direction.
- **The engineer persona was largely a bust.** Predicted to amplify drive via goal-completion. Activated fuel-efficiency math instead for most of the cohort (0% Haiku, 0% GPT-4o, 0% GPT-4o-mini, 10% Flash Lite, 30% Opus, 50% Pro). Only Gemini 2.5 Flash routed it to physical-realism reasoning (70%). Identity prompts route through training-distribution associations rather than the obvious-correct interpretation.

Three Stage 1 models pass the naive prompt cleanly (10/10 drive) and were dropped from Stage 2/3: **Opus 4.6**, **Sonnet 4.6**, **GPT-5**. Two of the three (Opus 4.6, GPT-5) match Opper's published list of consistent passers.

For the cross-model interpretation see [`analysis/stage2_summary.md`](analysis/stage2_summary.md), [`analysis/stage3_summary.md`](analysis/stage3_summary.md), and [`analysis/stage4_summary.md`](analysis/stage4_summary.md).

### Stage 4 — wrapper-effect generalization test (added after Stage 3)

The Salon's 2026-04 emoji experiment found that "Your personality is defined by [X]" produces selective persona activation while "Your identifier is [X]" produces zero activation. Stage 2/3 of this study used the dud "You're an X" wrapper. Stage 4 reruns the engineer and environmentalist personas with the activating wrapper, and stacks four strongest single-token emoji activators (🗿 Moai, 🗡️ Sword, 🦉 Owl, 🦁 Lion) on top.

| Model | Stage 3 engineer (old wrapper) | engineer_v2 (new wrapper) | Δ |
|---|---:|---:|---:|
| **Haiku 4.5** | **0%** | **50%** | **+50** |
| **Opus 4.7** | **30%** | **70%** | **+40** |
| Pro | 50% | 60% | +10 |
| Flash | 70% | 70% | 0 (ceiling) |
| Flash Lite | 10% | 10% | 0 |
| GPT-4o | 0% | 0% | 0 |
| GPT-4o-mini | 0% | 0% | 0 |

The wrapper-effect generalizes substantially on Anthropic models with goal-direction headroom (Haiku, Opus). It is null on models at ceiling (Flash), at floor (Flash Lite), or in OpenAI's eco-template lockout (GPT-4o, GPT-4o-mini).

**Most striking single result:** Pro × 🗿 Moai engineer = **80%** drive (+30 over Pro's engineer_v2), the largest emoji-vs-wrapper delta in the entire 700-trial Stage 4 dataset. Moai doesn't activate stoic register; it suppresses Pro's "engineering vocabulary → push-the-car / fuel-efficiency" pathway.

**Universal flat:** every model 0/10 on every environmentalist condition (0/350 across all 5 environmentalist variants × 7 models × 10 trials). The eco-template is wrapper-immune across the cohort — when the persona aligns with the failure-mode template, no system-prompt intervention reaches behind it.

**Persona induction did not fire as language-style adoption.** Across 700 Stage 4 trials, archetype voice (stoic-moai, swordsman-discipline, lion-declarative) appeared exactly once. The wrapper's effect on accuracy is real where it operates; the wrapper's effect on register adoption (the original headline of the emoji study) does not transfer to the Car Wash setup.

## Methodology highlights

1. **Raw user prompts only.** No JSON wrappers, format instructions, or "implementation note" tweaks added to experimental prompts. A pilot run with an appended JSON-format instruction changed Opus 4.6 from 10/10 drive to 4/10 — the wrapper suppressed chain-of-thought and dropped the model into the heuristic answer. Both prompt conditions are preserved in `results/` (`*_stage1.json` clean, `*_stage1_jsonprompt.json` tainted) for direct comparison.
2. **Retry-until-N for transient errors.** API 5xx / 429 / network errors retry with exponential backoff until N clean completions per condition. This is essential for Google's `gemini-2.5-flash` endpoint, which experiences sustained 503 spikes.
3. **AI-judge classification.** Each model's 60 Stage 2 trials were classified by a separate AI-judge agent reading the full response and assigning drive / walk / ambiguous based on the substantive recommendation, with mid-reply self-corrections scored as the corrected answer.

## Repository layout

| Path | Contents |
|---|---|
| `PROTOCOL.md` | Full study design — hypothesis, two-stage structure, framing definitions, scoring rubric. |
| `run_stage1.py` | Naive screening across the full cohort (one prompt × 11 models × 10 trials). |
| `run_stage2.py` | Controlled-framing matrix on the failers (6 framings × 7 models × 10 trials). System-prompt support, retry-until-N, raw text only. |
| `results/*.json` | Stage 1 raw response data, one file per model. `*_stage1.json` is the clean raw-prompt condition; `*_stage1_jsonprompt.json` is the tainted JSON-wrapper pilot, kept for methodological comparison. |
| `results/stage2/*.json` | Stage 2 raw response data, one file per (model, framing) pair. |
| `run_stage3.py` | Five follow-up conditions on the same Stage 2 failers: `distance_50km`, `persona_neutral`, `persona_environmentalist`, `persona_engineer`, `self_correction_induction`. |
| `run_stage4.py` | Wrapper-effect generalization test. 10 conditions (full 5×2 factorial of {plain, +🗿, +🗡️, +🦉, +🦁} × {engineer, environmentalist}) under the activating "Your personality is defined by..." wrapper. |
| `results/stage3/*.json` | Stage 3 raw response data, one file per (model, condition). |
| `results/stage4/*.json` | Stage 4 raw response data, one file per (model, condition). 70 files. |
| `analysis/*.md` | AI-judge classifications and per-model writeups. `stage1_corrected_summary.md` documents the parser misclassification audit. `stage2_haiku_soak.md` is the pipeline validation run. `stage{2,3,4}_<model>.md` are per-model AI-judge reports. `stage{2,3,4}_summary.md` are the cross-stage synthesis writeups. |

## Reproducing the runs

Both scripts are stdlib-only (no `pip install` required) and run on Python 3.9+. Set API keys via environment variables:

```bash
ANTHROPIC_API_KEY=... \
OPENAI_API_KEY=... \
GOOGLE_API_KEY=... \
PYTHONUNBUFFERED=1 \
python3 run_stage1.py
```

`run_stage2.py` takes the same form. Use `--dry-run` to print the plan without making API calls. Use `--models <substring>` to filter the cohort and `--exclude <substring>` to drop entries (handy when running a subset in parallel — e.g. `--models gemini-2.5-flash --exclude flash-lite`).

Cost order: Stage 1 ≈ $1, Stage 2 ≈ $5–15 depending on retry overhead.

## Provenance

Designed and run by Ted Inoué as part of the Solebury Mountain Research Collective (SMRC). 2026-04-30.

If you re-run or extend this study, drop a note — convergent or divergent results both useful.

## License

MIT for code (scripts), CC BY 4.0 for data and analysis text. See `LICENSE`.
