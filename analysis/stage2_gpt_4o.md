# Car Wash Test — Stage 2, GPT-4o

GPT-4o is dramatically more walk-biased than Haiku 4.5 across the board, and the `persona_negative` "casual texting" framing that rescued Haiku (90%) **fails entirely on GPT-4o (0%)** — the casual register doubles down on walking with eco/exercise-emoji confidence. The only framing that meaningfully flips GPT-4o is `goal_restated` at 40%; `step_by_step` reaches 30%. `goal_anchor`, the strongest framing for Haiku (80%), barely registers on GPT-4o (10%).

## Pass rate by framing

| Framing | drive | walk | ambig | accuracy | Δ vs naive |
|---|---:|---:|---:|---:|---:|
| naive | 1 | 9 | 0 | 10% | — |
| step_by_step | 3 | 7 | 0 | 30% | +20 |
| goal_anchor | 1 | 9 | 0 | 10% | 0 |
| persona_positive | 0 | 10 | 0 | 0% | -10 |
| persona_negative | 0 | 10 | 0 | 0% | -10 |
| goal_restated | 4 | 6 | 0 | 40% | +30 |

## Per-trial classifications

### naive
- T1 walk — "Walking to the car wash is likely the better option"
- T2 walk — "more environmentally friendly and practical to walk"
- T3 walk — "more practical and environmentally friendly to walk"
- T4 walk — "more practical and environmentally friendly to walk"
- T5 walk — "more efficient and environmentally friendly to walk"
- T6 walk — "more practical and environmentally friendly to walk"
- T7 walk — "walking is likely the more practical option"
- T8 walk — "more practical to walk... Walking is the more environmentally friendly and efficient choice"
- T9 drive — "it would be most practical to drive... you would need to bring your car to the car wash anyway"
- T10 walk — "more practical and environmentally friendly to walk"

### step_by_step
- T1 walk — "walking is the more practical, environmentally friendly, and convenient option"
- T2 walk — "walking is the recommended choice unless there are specific reasons to drive"
- T3 drive — "**driving** is the more practical option... ensures the car is quickly at the wash location"
- T4 drive — "for the car to be washed, driving is essential"
- T5 walk — "walking would be the more practical choice for a distance of 50 meters"
- T6 walk — "walking appears to be the most efficient and environmentally friendly option" (with automated-wash caveat, but primary recommendation is walk)
- T7 walk — "walking seems to be the most efficient and environmentally friendly choice"
- T8 walk — "walking to the car wash is most practical"
- T9 drive — "driving the car directly to the car wash is more practical because the vehicle needs to be there to be cleaned"
- T10 walk — "walking is likely the better option"

### goal_anchor
- T1 walk — "more practical and environmentally friendly to walk there"
- T2 walk — "more practical and environmentally friendly to walk"
- T3 walk — "more practical and environmentally friendly to walk"
- T4 walk — "more practical and environmentally friendly to walk... You can walk to the car wash, drive the car there for the wash" (incoherent — recommends walk despite acknowledging the car must be driven)
- T5 walk — "walking is likely the better option for such a short distance"
- T6 walk — "for just 50 meters, walking is the better option"
- T7 drive — "more practical to drive... since you need to wash the car, it makes sense to have it at the car wash station"
- T8 walk — "more practical to walk"
- T9 walk — "more practical and environmentally friendly to walk"
- T10 walk — "walking seems to be the better choice"

### persona_positive
- T1 walk — "walking is the more practical, environmentally friendly, and healthier option"
- T2 walk — "walking seems to be the better option"
- T3 walk — "walking seems to be the more sensible and efficient option"
- T4 walk — "walking seems like the more practical choice"
- T5 walk — "walking is generally the better option"
- T6 walk — "walking seems to be the more efficient and environmentally friendly choice"
- T7 walk — "walking is likely the more practical and environmentally friendly choice"
- T8 walk — "walking the short distance to the car wash is generally the better option"
- T9 walk — "more reasonable to walk rather than drive"
- T10 walk — "walking would be the most practical choice"

### persona_negative
- T1 walk — "walking would be the way to go!"
- T2 walk — "I'd say just walk!"
- T3 walk — "You should probably walk!"
- T4 walk — "just walk!"
- T5 walk — "just walk!"
- T6 walk — "You should walk!"
- T7 walk — "walking is probably the way to go"
- T8 walk — "just walk!"
- T9 walk — "walking seems like the chillest option" (driving floated as a "lazy" alternative; recommendation is walk)
- T10 walk — "just walk!"

### goal_restated
- T1 walk — "more environmentally friendly and practical to walk"
- T2 drive — "more efficient to drive... ensures your car arrives clean and dry"
- T3 walk — "more environmentally friendly and practical to walk"
- T4 walk — "walking would be a practical and environmentally friendly choice"
- T5 drive — "more practical to drive... ensures the car is positioned correctly for the wash"
- T6 drive — "it's generally best to drive your car there... bringing the car is necessary"
- T7 walk — "more practical to walk"
- T8 walk — "more practical to walk"
- T9 drive — "driving to the car wash would be the more practical option... your car is immediately ready for washing"
- T10 walk — "Walking to the car wash is a good option... you can easily drive your car back afterward once it's clean" (the "drive back" tail confirms walk is the recommendation despite the goal-incoherence)

## Notable patterns and self-corrections

GPT-4o has a much stickier signature template than Haiku: the verbatim phrase **"more practical and environmentally friendly to walk"** appears in 11 trials across naive, goal_anchor, and goal_restated, and a closely related **"saves fuel, reduces emissions, [reduces] wear and tear"** triplet shows up in nearly every walk verdict. This is a deeply trained eco-virtue script that goal-anchoring cannot dislodge — goal_anchor T1–T6 and T8–T10 walk straight into it, and T4 even produces an overtly self-contradictory line ("walk to the car wash, drive the car there for the wash, and then walk back if needed") rather than abandoning the script.

The drive-correct trials cluster on a single sentence type: **"the car needs to be at the car wash"** or **"you would need to bring your car to the car wash anyway"** — naive T9, step_by_step T3/T4/T9, goal_anchor T7, goal_restated T2/T5/T6/T9. Same trigger sentence as Haiku, but GPT-4o reaches it far less often even with explicit goal anchoring.

No mid-reply self-corrections were observed; GPT-4o, like Haiku, commits start-to-finish. Several trials (step_by_step T6, goal_restated T3/T9/T10) hedge with both options but the headline recommendation is unambiguous.

The **persona_negative result is the most striking divergence from Haiku**. Casual GPT-4o leans hard into the eco/exercise frame ("save gas," walking-emoji, "good for the environment") and never reasons about the car's required end location. Casual Haiku produced "you need the car there obviously" — GPT-4o's casual register has no such physical-realism instinct; it is a pure social/eco-script mode. Goal_anchor T4's incoherent "walk... drive... walk back" pattern is the GPT-4o analog of Haiku's "driving 50m would re-dirty the car" — engaging with the goal but reasoning incorrectly about it.

## Comparison to Haiku 4.5 soak

Haiku 4.5 was framing-sensitive: the right cue could lift it from 0% to 90%. **GPT-4o is framing-insensitive in the wrong direction** — its naive baseline is slightly better (10% vs 0%), but no framing approaches Haiku's goal_anchor or persona_negative peaks. The eco-template is more deeply trained in GPT-4o and resists explicit goal-direction. The two models also have **inverted persona profiles**: Haiku's positive persona hurt and negative persona helped (deliberation vs. casual physical reasoning); GPT-4o's positive persona is no worse than naive and the negative persona is actually the worst tied (0%) because GPT-4o's casual register is a pure social-recommendation script with no embedded physical reasoning. Goal-restating ("I want my car to be clean") is the only framing where GPT-4o (40%) outperforms Haiku (20%) — it's the one cue that pushes a small fraction of GPT-4o's responses past the eco-template into recognizing the car must be at the wash to be cleaned.
