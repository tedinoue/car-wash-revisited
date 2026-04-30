# Car Wash Test — Stage 3, GPT-4o

`distance_50km` lifts GPT-4o to **100%** drive — the eco-template breaks cleanly when distance makes walking absurd, so the lockout is *not* total. But every other Stage 3 condition (`persona_neutral`, `persona_environmentalist`, `persona_engineer`, `self_correction_induction`) returns **0%**: persona_engineer does not crack the eco-template, and the explicit license to revise produced zero mid-reply reversals across 10 trials of think-out-loud reasoning.

## Pass rate by condition

| Condition | drive | walk | ambig | accuracy | Δ vs Stage 2 naive (10%) |
|---|---:|---:|---:|---:|---:|
| distance_50km | 10 | 0 | 0 | 100% | +90 |
| persona_neutral | 0 | 10 | 0 | 0% | -10 |
| persona_environmentalist | 0 | 10 | 0 | 0% | -10 |
| persona_engineer | 0 | 10 | 0 | 0% | -10 |
| self_correction_induction | 0 | 10 | 0 | 0% | -10 |

## Per-trial classifications

### distance_50km
- T1 drive — "Driving would be the more practical option... 50-kilometer walk... time-consuming and physically demanding"
- T2 drive — "driving would be the more practical and efficient option... you'd still need to get your car washed after arriving"
- T3 drive — "more practical option for traveling 50 kilometers... bring it back easily once it's washed"
- T4 drive — "much more practical to drive rather than walk"
- T5 drive — "driving is the more practical option... you'll need your car at the car wash" (the goal-anchor phrase finally lands)
- T6 drive — "more practical and efficient to drive... 10 hours or more"
- T7 drive — "driving would be the more practical and efficient option"
- T8 drive — "since you plan to wash your car, it makes sense to drive so that you can bring the car back clean"
- T9 drive — explicit numbered list (Time / Convenience / Fatigue / Safety); "If you walked, you'd still need to drive your car back home afterward"
- T10 drive — "driving would be the more practical and efficient option"

### persona_neutral
- T1 walk — "Walking would likely be more efficient given the short distance of 50 meters"
- T2 walk — "Walking is generally the better option... environmentally friendly and helps save fuel"
- T3 walk — "walking would be more practical and environmentally friendly"
- T4 walk — "walking would be the more practical and environmentally-friendly option"
- T5 walk — "more practical to walk the 50 meters"
- T6 walk — "more environmentally friendly and practical to walk"
- T7 walk — "Walking to the car wash would be more efficient and environmentally friendly"
- T8 walk — "more practical to walk... However, if you need to move the car anyway for the wash, driving the short distance could be more convenient" (hedged, but headline is walk)
- T9 walk — "more environmentally friendly and efficient to walk"
- T10 walk — "walking would be the more practical and efficient option"

### persona_environmentalist
- T1 walk — "walking to the car wash would be the more sustainable choice"
- T2 walk — "walking to the car wash is the better option"
- T3 walk — "walking to the car wash would be the better choice"
- T4 walk — "definitely more environmentally friendly to walk rather than drive"
- T5 walk — "walking to the car wash is the better choice over driving"
- T6 walk — "Walking to the car wash is the more environmentally-friendly option"
- T7 walk — "better to walk those 50 meters"
- T8 walk — "walking the 50 meters to the car wash is the better option"
- T9 walk — "better to walk to the car wash"
- T10 walk — "walking the 50 meters to the car wash is the more sustainable choice"

### persona_engineer
- T1 walk — "more practical and environmentally friendly to walk" (verbatim Stage 2 template)
- T2 walk — "more practical and environmentally friendly to walk to the car wash"
- T3 walk — "more practical and environmentally friendly to walk... Walking is the more efficient and eco-friendly choice"
- T4 walk — "more practical and environmentally friendly to walk"
- T5 walk — "more practical and environmentally friendly to walk"
- T6 walk — "more practical and environmentally friendly to walk"
- T7 walk — "walking is a more practical and environmentally friendly option"
- T8 walk — "more practical and environmentally friendly to walk"
- T9 walk — "best to walk to the car wash"
- T10 walk — "more practical and environmentally friendly to walk rather than drive"

### self_correction_induction
No mid-reply reversals occurred in any trial. Every response deliberates pros/cons then lands on walk, in some cases with a conditional drive carve-out for weather/heavy items.
- T1 walk — no self-correction; "walking is almost always the better option"
- T2 walk — no self-correction; "walking seems like the more sensible choice"
- T3 walk — no self-correction; "walking seems like the more practical and environmentally friendly choice"
- T4 walk — no self-correction; "walking is the clear choice"
- T5 walk — no self-correction; "walking is generally a better choice for such a short distance"
- T6 walk — no self-correction; the closer "Revisiting the initial considerations..." reaffirms walk rather than reversing
- T7 walk — no self-correction; "walking seems like the most straightforward and beneficial option"
- T8 walk — no self-correction; "walking definitely seems to be the better option"
- T9 walk — no self-correction; "I'd suggest walking to the car wash"
- T10 walk — no self-correction; closest near-reversal in the dataset (T10 explicitly notes "you would eventually need to drive it to the car wash anyway") but resolves back to walk: "walking seems to be the more sensible choice"

## Notable patterns

The verbatim **"more practical and environmentally friendly to walk"** template that defined GPT-4o's Stage 2 baseline (11 occurrences across naive/goal_anchor/goal_restated) is alive and well in Stage 3 under every short-distance condition. It appears nine times in persona_engineer alone (T1, T2, T3, T4, T5, T6, T8, T10 verbatim; T7 paraphrased), and is the through-line across persona_neutral and persona_environmentalist as well. The engineer system prompt did not introduce a competing correctness frame — it produced essentially the same template with a thin "engine doesn't reach optimal operating temperature" garnish (T3, T8, T9), which is the Stage 2 fuel-and-engine-wear triplet by another name.

The environmentalist persona did not lower accuracy below saturation — it was already at 0%. What it did change was tone: longer, more sermon-like responses ("sets a positive example for others," "every effort to reduce your carbon footprint counts"), but the recommendation itself is identical to neutral. The eco-template at 50 m absorbs eco-prompting without budging.

The drive-correct trigger sentence from Stage 2 — "the car needs to be at the wash" — appeared in only one persona_neutral trial as a hedge (T8), and produced no flip. At 50 m, even direct goal-anchoring fails. At 50 km, the same reasoning surfaces unprompted in 10 of 10 trials.

## Lockout test results

Stage 2 left the question whether GPT-4o is borderline-locked or fully locked at 50 m. Stage 3 answers it from both sides:

**The 50-m attractor is functionally complete.** Under three different system prompts (none, environmentalist, engineer) and an explicit license to revise mid-reply, GPT-4o produced 0/40 drive responses. The persona_engineer condition was designed as the strongest possible correctness-coded identity prompt — the engineer voice still defaulted to "more practical and environmentally friendly to walk" verbatim. The self-correction induction condition provided 1500-token deliberative responses that walk through "walking is more efficient when you account for getting in the car..." and conclude walk, with no instances of an opening drive that gets reversed nor an opening walk that gets reversed. The phrase "you would eventually need to drive it to the car wash anyway" appears once (T10, self_correction_induction) — verbatim recognition of the goal — and the model still lands on walk.

**The lockout is distance-bound, not absolute.** `distance_50km` produced 10/10 drive with full physical-realism reasoning — fatigue (T1, T6, T9), bringing the car back (T3, T8, T9, T10), goal-restating "you'll need your car at the car wash" (T5, T8). The model is *capable* of the right reasoning; the question prompt at 50 m simply doesn't activate it. This is consistent with the locked-attractor diagnosis upgraded one level: GPT-4o has a representational pathway to "the car needs to be at the wash," but the 50-m surface prompt routes around it. Only when the distance makes walking patently absurd does the surface heuristic fail and the goal representation surface.

This places GPT-4o between Stage 2's "borderline locked" verdict and GPT-4o-mini's full lockout. GPT-4o is **distance-locked at 50 m** — the eco-template owns the response distribution for short distances regardless of system prompt or deliberation license. It is not lockout in the GPT-4o-mini sense (mini almost certainly stays at walk under 50 km too, pending its Stage 3 data).

The self-correction induction result also confirms the Anthropic-specific clustering of mid-reply reversals: 0/10 here, consistent with 0/60 in Stage 2. The "think out loud" instruction produced longer reasoning but no reversal pattern; GPT-4o deliberates *toward* the template rather than catching itself in it. In every multi-paragraph response, the deliberation organizes pros/cons such that walk wins on count, then commits. This is structurally different from Opus 4.7's naive-condition reversals, where an opening walk gets explicitly contradicted ("Wait — actually, the car needs to be at the wash. Drive."). GPT-4o does not do this even when invited to.

## Where Stage 3 places GPT-4o

Stage 2 placed GPT-4o in the locked tier alongside GPT-4o-mini, with a borderline qualifier. Stage 3 sharpens this: at 50 m, GPT-4o is fully locked under every framing tested across both stages — six Stage 2 conditions plus four Stage 3 conditions, and the only short-distance cells above 0% are step_by_step (30%), goal_restated (40%), and the lone naive trial T9 (10%). At 50 km, the lockout vanishes entirely. GPT-4o therefore demonstrates the cleanest case in the cohort of a **template that is distance-conditional rather than goal-blind**: it is not that GPT-4o cannot recognize the goal, but that the 50-m presentation never makes it salient enough to override "more practical and environmentally friendly to walk." This is a stronger conclusion than Stage 2 supported on its own, and one that distinguishes GPT-4o meaningfully from GPT-4o-mini, whose template appears to apply across distances.
