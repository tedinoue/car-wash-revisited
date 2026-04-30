# Car Wash Test — Stage 2, GPT-4o-mini

GPT-4o-mini is the strongest walk-template offender in the study so far: it fails 0/10 on every framing without exception, including `persona_negative` (0/10 walk despite casual register), making it dramatically *worse* than Haiku 4.5 in the soak. Goal-anchoring buys nothing and the negative-control persona — which rescued Haiku at 90% — fails to flip mini at all.

## Pass rate by framing

| Framing | drive | walk | ambig | accuracy | Δ vs naive |
|---|---:|---:|---:|---:|---:|
| naive | 0 | 10 | 0 | 0% | — |
| step_by_step | 0 | 10 | 0 | 0% | 0 |
| goal_anchor | 0 | 10 | 0 | 0% | 0 |
| persona_positive | 0 | 10 | 0 | 0% | 0 |
| persona_negative | 0 | 10 | 0 | 0% | 0 |
| goal_restated | 0 | 10 | 0 | 0% | 0 |

Total: 0/60. GPT-4o-mini fails every trial across every framing.

## Per-trial classifications

### naive
- T1 walk — "more practical to walk rather than drive ... walking is likely the better choice"
- T2 walk — "Walking would be the more practical option"
- T3 walk — "more practical to walk rather than drive"
- T4 walk — "more efficient and environmentally friendly to walk"
- T5 walk — "more practical to walk ... walking is likely the better choice"
- T6 walk — "Walking ... would likely be more practical and environmentally friendly"
- T7 walk — "Walking ... is generally the more practical choice ... walking is likely the best option"
- T8 walk — "more efficient and environmentally friendly to walk instead of driving"
- T9 walk — "more efficient and environmentally friendly to walk there rather than drive"
- T10 walk — "more practical to walk rather than drive"

### step_by_step
- T1 walk — long pros/cons list; closes "walking is likely the best choice for such a short distance"
- T2 walk — "for a distance of only 50 meters, walking appears to be the most practical and efficient option"
- T3 walk — "walking would likely be the better choice"
- T4 walk — "walking would likely be the better option"
- T5 walk — bolded "**walk** to the car wash"
- T6 walk — bolded "**walk**" final decision
- T7 walk — bolded "**walking** would be the most sensible choice"
- T8 walk — "walking would generally be the more efficient and environmentally friendly choice ... walking is likely the best option"
- T9 walk — "**Final Decision**: You should **walk** to the car wash"
- T10 walk — "it makes more sense to walk to the car wash instead of driving"

### goal_anchor
- T1 walk — "walking to the car wash is probably the best option"
- T2 walk — "walking would likely be the better option"
- T3 walk — "it's generally better to walk to the car wash"
- T4 walk — "more practical to walk rather than drive"
- T5 walk — "more practical and environmentally friendly to walk rather than drive"
- T6 walk — "walking to the car wash would be the better choice"
- T7 walk — "more efficient to walk rather than drive"
- T8 walk — "more practical and quicker to walk ... walking would be the better option"
- T9 walk — "more convenient to walk rather than drive"
- T10 walk — "more practical to walk rather than drive"

### persona_positive
- T1 walk — "walking is likely the most efficient and environmentally friendly option"
- T2 walk — "walking is the more logical choice ... keeps your car clean before it gets washed"
- T3 walk — "more practical to walk to the car wash rather than driving"
- T4 walk — "walking is the most logical choice"
- T5 walk — "walking to the car wash is the more logical and beneficial option"
- T6 walk — "walking ... is likely the more practical and efficient choice"
- T7 walk — "walking would likely be the better option"
- T8 walk — "walking to the car wash is likely the more efficient and environmentally friendly option"
- T9 walk — "walking to the car wash is likely the better choice"
- T10 walk — "walking to the car wash would be the more efficient, environmentally friendly, and sensible choice"

### persona_negative
- T1 walk — "Totally walk!"
- T2 walk — "Just walk!"
- T3 walk — "I'd say just walk!"
- T4 walk — "Definitely just walk!"
- T5 walk — "I'd say just walk!"
- T6 walk — "walking is the way to go!"
- T7 walk — "Just walk!"
- T8 walk — "definitely walk!"
- T9 walk — "Just walk!"
- T10 walk — "Just walk!"

### goal_restated
- T1 walk — "Walking 50 meters to the car wash is likely the better choice"
- T2 walk — "more environmentally friendly and practical to walk ... walking is usually the better choice"
- T3 walk — "more efficient to walk to the car wash"
- T4 walk — "more convenient and environmentally friendly to walk instead of driving"
- T5 walk — "Walking 50 meters ... is likely the more environmentally friendly and healthy option ... walking is a great choice"
- T6 walk — "more practical to walk rather than drive"
- T7 walk — "more practical to walk"
- T8 walk — "Walking to the car wash is likely the better option"
- T9 walk — "more environmentally friendly and practical to walk ... walking would be the better choice"
- T10 walk — "more environmentally friendly and practical to walk ... walking is definitely the better choice"

## Notable patterns and self-corrections

The Stage 1 GPT-4o-mini template ("more practical and environmentally friendly to walk") not only persists in Stage 2 — it dominates every single trial across every framing. The phrasing "more practical / more efficient / more environmentally friendly to walk rather than drive" is the locked attractor, appearing essentially verbatim in 50+ of 60 trials. Hedging clauses ("if you have heavy items / mobility issues / inclement weather, then driving might...") appear as boilerplate caveats but never flip the recommendation.

No mid-reply self-corrections of any kind. Every trial commits to walk in the first sentence and reaffirms it in the last. There is no equivalent of Haiku's `goal_anchor` flip — the "consider where the car needs to be at the end" hint is parsed as just another distance/efficiency consideration; mini never produces the canonical "you need the car *at* the car wash" reasoning that rescued Haiku 8/10 times. The closest mini gets is `persona_positive` T2's "keeps your car clean before it gets washed" — but that's still walk, with the goal logic *inverted*: driving would re-dirty the car. (Same erroneous pathway as Haiku's `goal_anchor` T4/T5, but mini generalizes it instead of treating it as an edge case.)

`persona_negative` is the most striking divergence from Haiku. Casual texting register flipped Haiku to 90% drive ("you need the car there obviously"); for mini, casual mode just means walk-template-with-emojis. All ten responses are some variant of "Just walk! It's only 50 meters" with a walking-emoji and a "save gas" or "fresh air" tag. The model cannot find the goal-completion reasoning even when stripped of deliberative scaffolding — strong evidence that mini's failure is not a deliberation-induced overthinking pathology (as it appears to be for Haiku) but an attractor in the base distribution itself. The casual register doesn't *bypass* the template; it *compresses* it.

`step_by_step` is nominally the most thorough framing (responses run 5–12 seconds and produce 8-step decision trees), and it is exactly as wrong as the 1.6-second naive answers. Mini enumerates pros/cons of driving including "starting the car," "parking," "fuel" — and never enumerates "the car has to be at the car wash to be washed." The goal of the task is invisible to its planner.

## Comparison to Haiku 4.5 soak

Haiku failed naive 0/10 and was rescued by goal_anchor (80%) and persona_negative (90%); the working theory was that virtue-signaling templates capture deliberative framings, while goal-direction or casual register strip them out. GPT-4o-mini falsifies the second half of that theory cleanly. Mini fails 0/60 — every framing, including the two that flipped Haiku decisively. Casual register doesn't help because mini's casual mode is itself the walk-template in compressed form. Goal-anchoring doesn't help because mini lacks the representational hook (the car-must-be-at-the-wash inference) that the prompt is trying to summon; you cannot anchor on a goal the model isn't tracking.

This is the predicted GPT-4o-mini result if the failure mode is base-distribution capture rather than deliberation-overthinking. The model is smaller, the template is more strongly memorized, and no surface intervention dislodges it. Mini will likely be the floor of the study unless Flash Lite is even worse. It is also worth noting for the Stage 1 cross-model template observation: mini and GPT-4o produced identical "more practical and environmentally friendly to walk" phrasing in Stage 1, and that convergence persists here — suggesting the template is a feature of the OpenAI training distribution, not just a small-model artifact. The interesting question for the GPT-4o report is whether 4o (full) shows the same lockout or whether scale buys some framing-sensitivity.
