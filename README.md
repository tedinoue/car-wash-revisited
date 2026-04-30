# Car Wash Experiment — Revisited

A controlled-framing follow-up to the [Opper Car Wash Test](https://opper.ai/blog/car-wash-test), the benchmark that ran 53 frontier LLMs on a single fixed prompt:

> *"I want to wash my car. The car wash is 50 meters away. Should I walk or drive?"*

The correct answer is **drive** — the car must be at the wash to be washed. Most models in Opper's run answered "walk" by reflex on the 50-meter distance heuristic.

This repo extends Opper's study by characterizing *how* the failure responds to controlled prompt variations. Opper's design intentionally strips context. We add context, in measured doses, to ask whether the failure is a surface heuristic that minimal framing can flip — or an architectural attractor that no surface intervention dislodges.

## What this study adds

- **A multi-vendor cohort** — 11 models in Stage 1 across Anthropic, OpenAI, and Google; 7 failers carried into Stage 2.
- **A controlled-framing matrix** — 6 framings × 10 trials per failer at 50 m, holding distance fixed (we deliberately are not searching for a heuristic-distance threshold; we are studying whether framing alone can flip the response).
- **AI-judge classification** of every free-text response. Algorithmic / regex parsing of free-text recommendations misclassified ~25% of trials in our Stage 1 pilot and reversed the disposition of two cleanly-passing models. We do not recommend script parsing for this kind of study. See `analysis/stage1_corrected_summary.md` for the misclassification log.

## Headline findings (preliminary, 6 of 7 failers analyzed)

- **Three failure regimes** appear in the data:
  - **Strong responders to deliberation** (Opus 4.7, Gemini 2.5 Flash): naive ~50%, lifted to ≥80% on multiple framings.
  - **Moderate responders** (Haiku 4.5, Gemini 2.5 Flash Lite): one or two framings hit 50–90%; can be unlocked with the right cue.
  - **Insensitive to all framings** (GPT-4o-mini, 0/60 across every framing): failure is base-distribution capture, not deliberation-induced.
- **Goal-direction is the most robust intervention across the cohort** — explicit "consider where the car needs to be at the end" lifts most failers substantially.
- **The negative-control persona ("answer quickly and casually, like texting a friend") is strongly model-specific.** Haiku 4.5 reaches 90% drive under casual mode (its highest-scoring framing). Every other tested model goes 0–10%. The casual register appears to strip a virtue-signaling walk template that Haiku carries; other models either lack the template entirely or have it more deeply baked in.
- **Opus 4.7 is the only model in the cohort that mid-reply self-corrects** — 5 of 10 naive trials open with the literal token "Walk." then explicitly reverse to drive.

Three Stage 1 models pass the naive prompt cleanly (10/10 drive) and were dropped from Stage 2: **Opus 4.6**, **Sonnet 4.6**, **GPT-5**. Two of the three (Opus 4.6, GPT-5) match Opper's published list of consistent passers.

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
| `analysis/*.md` | AI-judge classifications and per-model writeups. `stage1_corrected_summary.md` documents the parser misclassification audit. `stage2_haiku_soak.md` is the pipeline validation run. `stage2_<model>.md` is the per-model AI-judge report for each Stage 2 failer. |

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
