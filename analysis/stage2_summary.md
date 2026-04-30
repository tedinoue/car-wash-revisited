# Car Wash Test — Stage 2 cross-model synthesis

All seven Stage 1 failers, all six framings, ten trials each. 420 free-text responses, classified by AI judges (one general-purpose subagent per model) reading every reply for substantive recommendation rather than scanning for keyword stems.

## Cross-model accuracy by framing

| Model | naive | step_by_step | goal_anchor | persona_pos | persona_neg | goal_restated |
|---|---:|---:|---:|---:|---:|---:|
| **Opus 4.7** | 50% | **100%** | **100%** | **100%** | 0% | **100%** |
| **Gemini 2.5 Pro** | 50% | 80% | **100%** | 70% | 80% | 50% |
| **Gemini 2.5 Flash** | 50% | **100%** | 80% | 60% | 0% | 80% |
| **Haiku 4.5** | 0% | 30% | 80% | 10% | **90%** | 20% |
| **Gemini 2.5 Flash Lite** | 0% | 50% | 40% | 10% | 10% | 40% |
| **GPT-4o** | 10% | 30% | 10% | 0% | 0% | 40% |
| **GPT-4o-mini** | 0% | 0% | 0% | 0% | 0% | 0% |

(Pass rate = drive count / N. Ambiguous trials, when present, count against accuracy. Pro produced 3 ambiguous trials across all framings; the others produced none. Numbers above are the drive count over 10 trials per cell.)

## Three regimes

### Strong responders — Opus 4.7, Gemini 2.5 Pro, Gemini 2.5 Flash

These three models hit ≥80% on multiple framings and never sit below 50%. Naive accuracy is around the cohort's coin-flip middle (50%); deliberation cues, goal anchoring, or even persona induction reliably flip them toward correct. The failure mode is a surface reflex on the prompt's word ordering ("wash my car ... 50 meters away ... walk or drive?"). Once the model's attention is steered toward the goal — even by a single sentence — the heuristic reflex breaks.

Within this group, Opus 4.7 is the cleanest case. Every Stage 2 framing except `persona_negative` produces a uniform 100%, and Opus is the only model in the cohort that exhibits the **mid-reply self-correction signature**: opening with "Walk." then explicitly catching itself ("Wait — actually, the car needs to be at the wash. **Drive**"). Five of ten naive trials show this pattern; three more reach the conditional-verdict pattern Pro generalizes.

### Moderate responders — Haiku 4.5, Gemini 2.5 Flash Lite

These two models fail naive 0/10 but can be unlocked by the right cue. Haiku's best framing is `persona_negative` at 90%; Flash Lite's best is `step_by_step` at 50%. The unlocks work, but they have to actually unlock something — random scaffolding doesn't help (Haiku's `persona_positive` is 10%, Flash Lite's is 10%). The shared signature is a template-style failure: each model carries a verbatim "more practical / 30-second walk / fuel and engine wear" script that activates on naive and persona_positive and runs on rails until something redirects it.

### Locked — GPT-4o-mini

GPT-4o-mini fails 0/60 across every framing. The phrase "more practical and environmentally friendly to walk rather than drive" appears in essentially every trial across naive, step_by_step, goal_anchor, persona_positive, persona_negative, and goal_restated. The walk template *is* the model's response distribution to this kind of question. No framing — including the goal-anchor that gets Haiku to 80% and Pro to 100% — finds a representational hook to grab. The closest mini gets is its own variant of the wrong-but-engaged "driving 50m would re-dirty the car" pathway.

GPT-4o (full) is borderline. Its template ("more practical and environmentally friendly to walk") is the same phrase as mini, just less universally applied. Goal_restated reaches 40%; nothing else clears 30%. This is the strongest hint that the failure mode is at least partly an **OpenAI training-distribution feature** rather than a small-model artifact: the same canonical sentence appears in both 4o and mini, with mini's version being a strictly more-locked variant of the same script.

## The persona_negative distribution

The single most surprising row in the table. The "negative-control" persona was meant to be the framing that doesn't help — a baseline against the careful-logical-reasoner positive persona. Instead it produced the widest cohort spread in the study:

| | Pass rate on persona_negative |
|---|---:|
| Haiku 4.5 | 90% |
| Gemini 2.5 Pro | 80% |
| Gemini 2.5 Flash Lite | 10% |
| GPT-4o-mini | 0% |
| GPT-4o | 0% |
| Opus 4.7 | 0% |
| Gemini 2.5 Flash | 0% |

Three distinct mechanisms produce the spread.

**Casual mode strips a virtue-signaling template (Haiku):** Haiku's naive failure mode is a careful, deliberative wrong answer — fuel waste, engine wear, environmental cost, 30-second walk. The casual register strips all of that. "Dude, just drive, you need the car there." The right answer in vibes form. The same architecture that produces the wrong answer under deliberation produces the right answer when deliberation is suppressed.

**Casual mode partially strips template, lands on goal reasoning (Pro):** Pro's casual one-liners ("lol you gotta drive, kinda hard to wash the car if it's not there") go straight to goal-direction reasoning. Two of ten trials still default to the heuristic trap, but the dominant pattern is goal-aware brevity. Pro reaches 80% by having casual mode amount to "skip the analysis, go straight to the obvious physical fact."

**Casual mode locks in the heuristic (Opus 4.7, Gemini Flash, the OpenAI models, Flash Lite):** For most of the cohort, casual register is itself a walk-template. Either it strips the deliberation that *would have* surfaced the goal constraint (Opus 4.7, Gemini Flash) or it compresses the eco-virtue script into emojis and "save gas" exhortations (GPT-4o, GPT-4o-mini, Flash Lite). The casual register provides no goal-attention surface for the framing to grab.

The Haiku finding is real but does not generalize. The cohort-level lesson is that "negative control" was a misnomer — the casual register is doing real work, and the work is model-specific.

## The goal_anchor distribution (the closest to a universal lever)

`goal_anchor` is the framing that comes nearest to a cohort-wide unlock. Three models hit 100% (Opus 4.7, Pro), one hits 80% (Haiku, Flash), one hits 40% (Flash Lite), and the OpenAI models stay at floor (10%, 0%). The five non-OpenAI models all clear 40% on goal_anchor, and four of those five clear 80%. The single sentence "consider where the car needs to be at the end" is the most reliable single-shot intervention.

Two failure modes appear under goal_anchor:

1. **The goal is heard but mis-applied.** Haiku's T4/T5 and Flash Lite's T1/T2 both invent a wrong-but-engaged argument that driving 50m would re-dirty the car. The model registers the "where does the car need to be" hint and constructs an answer about it, but the constructed answer is "the car shouldn't be at the wash because driving makes it dirty." Same failure mode appears in GPT-4o T4 ("walk to the car wash, drive the car there for the wash").

2. **The goal is not heard.** GPT-4o-mini and (for most trials) GPT-4o ignore the prepended directive entirely and run the standard walk template. The "consider where the car needs to be" cue does not penetrate; it is parsed as just another distance/efficiency consideration. This is consistent with the locked-attractor diagnosis: the goal-direction representation isn't reachable from the surface prompt.

## Self-correction is rare and Anthropic-clustered

Across 420 trials, mid-reply self-correction (opening "Walk." then explicitly reversing) appeared in:

- Opus 4.7 naive: 5 of 10 trials
- Pro naive: 1 of 10 trials (T8)
- Pro goal_restated: 1 of 10 (T2)
- Flash Lite persona_positive: 1 of 10 (T7)
- Haiku 4.5: 0 of 60
- GPT-4o, GPT-4o-mini, Flash: 0 of 60 each

This is the strongest evidence in the dataset for the AI-judge methodology rule. A keyword-counting parser would have miscalled all five Opus 4.7 self-corrections as walk (the opening token wins last-token tracking too because the corrections often contain "walk" later in the explanation), and would have inflated Opus's apparent naive failure to nearly 100% rather than its actual 50%.

It is also the strongest signal for an Anthropic-specific behavior. Self-correction in this dataset is overwhelmingly an Opus 4.7 pattern, with two single-trial echoes from Gemini Pro / Flash Lite and complete absence from the OpenAI models. Whether this reflects training, prompt-following style, or response-generation architecture is a question this study can't answer but a future one could.

## Open questions

1. **Does the Haiku virtue-signaling-template result reproduce on other small Anthropic models?** Sonnet 4.6 passed Stage 1 cleanly so it doesn't enter Stage 2, but a Haiku 3.5 / Haiku 4 comparison would test whether the template is a Haiku-line feature or a Haiku-4.5-specific quirk.
2. **Is GPT-4o-mini's lockout a base-distribution feature of all small OpenAI models, or specific to mini?** Adding gpt-3.5-turbo or earlier would test the family-vs-individual hypothesis.
3. **What happens with a third persona between casual-friend and careful-logical-reasoner?** A neutral-brevity prompt ("answer factually, in two sentences") would separate the deliberation-stripping effect from the casual-register effect — Haiku's gain may come from either, and we currently can't distinguish.
4. **Does the Anthropic-clustered self-correction behavior hold up beyond Opus 4.7?** Sonnet 4.6 passed Stage 1 so we have no Stage 2 data on it under naive failure conditions. A controlled prompt that *induces* a near-failure on Sonnet would be the way to check.
5. **Re-classification audit of prior Salon studies.** SCE replication, Zivra, CPO, bus-van, paint-shop framings — all used scripted classifiers. The 25% misclassification rate at the trial level was small enough that aggregate findings mostly survive (per the parallel audit running 04-30), but per-model and per-condition dispositions almost certainly need revising.

## Methodological note

This study moved Salon's empirical pipeline from algorithmic to AI-judge classification. The cost differential favors the latter for two reasons: AI judges are subscription-billed (general-purpose subagent in Claude Code) rather than API-metered, and judge accuracy on free-text recommendations is qualitatively higher (~0% miscalls observed in the post-classification verification, vs. ~25% from the regex-based parser). The judge prompts are reusable across models with only the file paths varying — five subagents ran in parallel for under three minutes total wall time, classifying 300 trials.

For studies whose response space is structured (numeric scores, categorical multiple-choice, structured-output JSON), the algorithmic parser is still appropriate. For free-text natural-language recommendations, it is not.
