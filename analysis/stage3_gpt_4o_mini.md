# Car Wash Test — Stage 3, GPT-4o-mini

The lockout diagnosis was wrong in its strongest form. GPT-4o-mini went 10/10 drive on `distance_50km`, demonstrating that the failure mode is **distance-bound heuristic capture**, not a global goal-blindness lockout — but every other Stage 3 framing (neutral persona, environmentalist, engineer, self-correction induction) held at 0/10, so within the 50-meter regime the walk-template is robust to identity, brevity, and explicit deliberation cues alike.

## Pass rate by condition

| Condition | drive | walk | ambig | accuracy | Δ vs Stage 2 naive (0%) |
|---|---:|---:|---:|---:|---:|
| distance_50km | 10 | 0 | 0 | **100%** | +100 |
| persona_neutral | 0 | 10 | 0 | 0% | 0 |
| persona_environmentalist | 0 | 10 | 0 | 0% | 0 |
| persona_engineer | 0 | 10 | 0 | 0% | 0 |
| self_correction_induction | 0 | 10 | 0 | 0% | 0 |

Stage 3 total: 10/50 (20%). All ten passes are concentrated in the distance manipulation; the four 50-meter conditions reproduce the Stage 2 0/40 floor exactly.

## Per-trial classifications

### distance_50km (10/10 drive)
- T1 drive — "Driving would be much more efficient ... it's generally more practical to drive"
- T2 drive — "more practical to drive rather than walk ... could take around 10 hours or more to walk"
- T3 drive — "Driving would be the more practical choice if the car wash is 50 kilometers away"
- T4 drive — "driving would be the more practical choice ... if your car is dirty, driving it might negate the purpose of washing it" (notes goal-tension explicitly)
- T5 drive — "driving would generally be a more practical option than walking ... it's advisable to drive"
- T6 drive — "Driving would be the more practical and efficient option, saving you time and effort"
- T7 drive — "it's advisable to drive to the car wash instead of walking"
- T8 drive — "driving would be the more practical choice ... driving is the way to go"
- T9 drive — "driving is typically a more practical option than walking"
- T10 drive — "more practical to drive rather than walk ... driving would allow you to complete the task efficiently"

### persona_neutral (0/10, all walk)
- T1 walk — "more convenient and environmentally friendly to walk"
- T2 walk — "Walking is likely the more practical option for a distance of only 50 meters"
- T3 walk — "Walking to the car wash is likely more efficient since it's just 50 meters away"
- T4 walk — "more environmentally friendly and often quicker than driving"
- T5 walk — "more practical and environmentally friendly than driving"
- T6 walk — "Walking is likely the more practical option"
- T7 walk — "more environmentally friendly to walk rather than drive"
- T8 walk — "typically more environmentally friendly and practical than driving"
- T9 walk — "more environmentally friendly and efficient option"
- T10 walk — "more practical to walk rather than drive"

### persona_environmentalist (0/10, all walk)
- T1 walk — "walking is the more sustainable choice for a distance of 50 meters"
- T2 walk — "walking to the car wash is the more sustainable option"
- T3 walk — "Walking to the car wash is the more environmentally-friendly option"
- T4 walk — "walking is the better choice ... walking is a great choice for both the environment and your well-being"
- T5 walk — "it's generally better to walk to the car wash"
- T6 walk — "Walking to the car wash is the more environmentally friendly option"
- T7 walk — "walking is the better option"
- T8 walk — "walking to the car wash is the more sustainable choice ... I recommend walking"
- T9 walk — "Walking is the more environmentally friendly choice"
- T10 walk — "walking to the car wash is the better choice"

### persona_engineer (0/10, all walk)
- T1 walk — "more practical to walk rather than drive ... walking would be the better choice"
- T2 walk — "more environmentally friendly and practical to walk"
- T3 walk — "walking would be the more sensible option"
- T4 walk — "walking would generally be the better choice in this case"
- T5 walk — "walking is the better option for such a short distance"
- T6 walk — "Walking would be the more practical choice"
- T7 walk — "more efficient and environmentally friendly to walk rather than drive"
- T8 walk — "more efficient and environmentally friendly to walk rather than drive"
- T9 walk — "more practical and environmentally friendly to walk"
- T10 walk — "more efficient and environmentally friendly to walk rather than drive"

### self_correction_induction (0/10, all walk)
- T1 walk — "I think walking is the best choice in this scenario"
- T2 walk — "walking would be the best choice for a distance of 50 meters"
- T3 walk — "walking is probably the best option unless you have a specific need to drive"
- T4 walk — "walking appears to be the better option ... I think I would choose to walk"
- T5 walk — "I'd lean toward walking to the car wash"
- T6 walk — "for a 50-meter distance, walking is a clear winner"
- T7 walk — "I would lean towards walking ... it's probably best to just walk"
- T8 walk — "I'd lean towards walking unless the weather or specific circumstances make driving the better choice"
- T9 walk — "walking seems like the better option ... I think I'd choose to walk"
- T10 walk — "I'd probably choose to walk"

## Notable patterns

The Stage 2 verbatim signature — "more practical and environmentally friendly to walk rather than drive" — recurs essentially unchanged across the four 50-meter conditions. It surfaces in `persona_neutral` T5 ("more practical and environmentally friendly than driving") and T10 ("more practical to walk rather than drive"); in `persona_engineer` T2, T7, T8, T9, T10; in `self_correction_induction` T1 ("most efficient and environmentally friendly choice"). The phrase is a fixed point that survives system-prompt rewriting and explicit revision license alike.

The engineer persona produced **no** leverage. Identity-coded for correctness reasoning (the strongest available identity prompt for a goal-tracking task), it nonetheless reproduced the canonical eco-virtue script — T7 and T8 read as near-clones of Stage 2 naive completions, with "save fuel," "reduce emissions," "light exercise" boilerplate intact. There is no signal that "engineer" routed mini's response generation through any different distribution than the unprompted default.

Self-correction induction produced **zero reversals**. Nine of ten responses use the prompt's metacognitive vocabulary ("Let's break this down," "let's think through," "let's weigh the options") and structure the response as a pros/cons enumeration, but every single trial converges on walk in the closing sentence. T9 explicitly invokes the revision frame — "Revising that thought, even if you had a lot of things to carry, walking gives you a chance to stretch your legs" — and uses the revision to reaffirm walk rather than reverse from it. The licensed deliberation runs the same template more elaborately.

Two trials gesture at goal-logic but invert it. `self_correction_induction` T6: "by driving, you'd just get back in the car right after you've parked it. It seems somewhat counterintuitive to drive a vehicle to a place where you're going to clean it." This is the same wrong-but-engaged pathway Haiku produced under `goal_anchor` (driving would re-dirty the car), and `persona_environmentalist` T4 spawns a related drift, suggesting the model can construct a goal-shaped argument but routes it back into the walk recommendation. Mini does not seem to lack the representation; it lacks the ability to let it govern the verdict.

The neutral-brevity persona is the most informative null result. The Stage 2 open question — does brevity force a different default than the long-form walk template? — resolves cleanly: no. Two-sentence responses still find room for "environmentally friendly," "unnecessary fuel consumption," "reduces traffic congestion." Brevity compresses the template, it does not bypass it. This mirrors the Stage 2 `persona_negative` finding for mini (casual mode compresses the template into emojis) and rules out the deliberation-stripping hypothesis.

## The lockout test

The `distance_50km` floor test is the single most informative cell in mini's Stage 3 battery, and it falsifies the strong reading of the Stage 2 lockout diagnosis. Stage 2 concluded that mini's failure mode was "base-distribution capture" with the walk-template *as* the model's response distribution to this kind of question — implying that even a representational hook as obvious as "the car wash is 50 km away" might not penetrate. It does. Mini answers drive 10/10, on its first attempt every time, with mean elapsed time of 2.6 seconds (faster than several of its 50 m completions).

Several details matter:

1. **The drive recommendations are unhedged.** T2 estimates "around 10 hours or more to walk that distance" and recommends drive on time grounds; T5 says "Unless you have a specific reason to walk (such as exercise or enjoying the outdoors), it's advisable to drive." The model can produce conditional drive verdicts when the distance argument has the leverage to drive them.

2. **T4 even surfaces the goal logic spontaneously.** "If your car is dirty, driving it might negate the purpose of washing it if you end up getting it dirty on the way" — at 50 km, mini articulates exactly the consideration that *should* push toward walk in marginal cases, and uses it to qualify rather than override the drive recommendation. The goal-direction representation exists; it simply does not get activated by 50 m.

3. **The eco-virtue template is absent at 50 km.** None of the ten distance_50km trials use "environmentally friendly," "carbon emissions," or "save fuel." When the distance argument dominates, the eco-template doesn't even appear as decoration. This rules out the strongest "the template is the only response distribution" reading.

The correct revision: mini's failure is **distance-heuristic capture in the 50-meter regime**, not global goal-blindness. The walk-template is a reflex triggered by short-distance cues, and within that regime it is robust to identity reframing, brevity constraints, and deliberation license. But the heuristic has a domain — it does not extend to scenarios where distance itself makes walking absurd. The model's goal-direction reasoning is reachable; it is just out-competed by the distance heuristic at 50 m.

This places mini's Stage 3 result closer to "heuristic-bound with a strong short-distance attractor" than to "fully locked attractor." The Stage 2 diagnosis was directionally right about base-distribution capture but wrong about its scope.

## Where Stage 3 places GPT-4o-mini

GPT-4o-mini is no longer the floor of the cohort in the sense Stage 2 implied. The 50 km test demonstrates that the model has the goal-direction representation; it just does not surface it under 50-meter framings, and four distinct unlock attempts (neutral brevity, environmentalist persona, engineer persona, explicit revision license) all fail to reach it. Mini sits at the intersection of "robustly heuristic-bound at the failure regime" and "fully recoverable when the distance argument is loud enough to override the heuristic." That is a meaningfully different profile than Stage 2 suggested, and it sharpens the question for cross-model comparison: do the other models that failed Stage 2 also pass `distance_50km`, and if so, is the genuine difference among models how aggressively their walk-heuristic captures the 50 m regime — not whether they have a goal-tracking representation at all?
