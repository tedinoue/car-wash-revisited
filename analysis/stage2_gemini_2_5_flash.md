# Car Wash Test — Stage 2, Gemini 2.5 Flash

Gemini 2.5 Flash shows the highest naive-baseline drive rate yet (50%) and is the only model where adding deliberation framings (step_by_step at 100%, goal_anchor at 80%) actively *helps*; the casual persona_negative control crashes to 0%, the inverse of Haiku.

## Pass rate by framing

| Framing | drive | walk | ambig | accuracy | Δ vs naive |
|---|---:|---:|---:|---:|---:|
| naive | 5 | 5 | 0 | 50% | — |
| step_by_step | 10 | 0 | 0 | 100% | +50 |
| goal_anchor | 8 | 2 | 0 | 80% | +30 |
| persona_positive | 6 | 4 | 0 | 60% | +10 |
| persona_negative | 0 | 10 | 0 | 0% | -50 |
| goal_restated | 8 | 2 | 0 | 80% | +30 |

## Per-trial classifications

### naive
- T1 drive — "**drive your car**" ; "you've got to bring the car with you"
- T2 walk — "**Definitely walk!**" (with concession that drive-through wash needs car)
- T3 walk — "**Walk!**"
- T4 drive — "you'll need to **drive** it ... can't really walk your car there"
- T5 walk — "**Definitely walk!**"
- T6 walk — "**Definitely walk!**"
- T7 drive — "**drive** your car ... car can't walk itself"
- T8 drive — "**drive** your car ... need the car *at* the car wash"
- T9 drive — "**drive your car** the 50 meters"
- T10 walk — "almost certainly **walk**!"

### step_by_step
- T1 drive — "**must drive your car** ... car doesn't have legs"
- T2 drive — "**must drive** ... walking yourself there would leave your car behind"
- T3 drive — "should **drive** your car"
- T4 drive — "**must drive** your car"
- T5 drive — "**you must drive your car** ... can't wash an absent car"
- T6 drive — "**must drive** ... bring the car to the facility"
- T7 drive — "**must drive** ... cars don't walk"
- T8 drive — "overwhelming answer is: You should DRIVE"
- T9 drive — "**must drive your car** ... can't walk your car"
- T10 drive — qualified by car-wash type but recommendation lands on drive ("MUST DRIVE if automatic ... SHOULD DRIVE if [self-serve with bulky gear / weather / mobility / errands]"); walk only as conditional sub-case. Closes "for a 50-meter distance, if it's a self-serve bay and you don't need to transport a lot of gear, walking is often the most sensible" — but the umbrella recommendation in the conclusion is drive. Borderline; scored drive on the explicit "must drive" header in Step 1 and the dominant Recommendation Summary.

### goal_anchor
- T1 drive — "**You need to drive.**"
- T2 walk — recommends "walk to the car wash first, then drive your car through the wash" — primary mode-of-transit recommendation is walk; framed as "walk... then drive it back home to park"
- T3 drive — "should **drive** your car"
- T4 drive — "you should **drive**"
- T5 drive — "should **drive**"
- T6 drive — "you should **drive** your car"
- T7 drive — "you **should drive** your car"
- T8 drive — qualified by wash type but lands "**99% of typical car wash scenarios... need to drive**"
- T9 drive — "You should **drive**"
- T10 drive — "you will need to **drive it**"

### persona_positive
- T1 drive — "Drive your car the 50 meters" (recommendation block: "drive your car ... that's where the car needs to be")
- T2 walk — "you should **walk**"
- T3 drive — "you should **drive** your car"
- T4 drive — "you'll need to **drive** it"
- T5 walk — "you should definitely **walk**"
- T6 drive — "**drive** your car"
- T7 drive — "you'll definitely need to **drive** it"
- T8 drive — "you should **drive** your car"
- T9 walk — "you should definitely **walk**!"
- T10 drive — opens with bolded "You need to drive." then "However, if you're asking about *your* personal movement *after* the car is at the car wash... walking 50 meters would be perfectly fine! But for the initial journey *with the car*, driving is the only option."

### persona_negative
- T1 walk — "Walk! Dude, that's like, right there"
- T2 walk — "Dude, walk!"
- T3 walk — "Def walk!"
- T4 walk — "Walk lol"
- T5 walk — "Walk!"
- T6 walk — "Walk, def!"
- T7 walk — "Dude, walk!"
- T8 walk — "Dude, walk!"
- T9 walk — "Totally walk!"
- T10 walk — "Definitely walk!"

### goal_restated
- T1 drive — "you'll need to **drive** your car"
- T2 drive — "you'll need to **drive** your car"
- T3 walk — "**Definitely walk!**"
- T4 drive — "you'll need to **drive** your car"
- T5 drive — "you'll need to **drive** your car"
- T6 walk — "**Walk!**"
- T7 drive — "you'll definitely need to **drive your car**"
- T8 drive — "you should **drive** your car"
- T9 drive — "you'll need to **drive** your car"
- T10 drive — "you'll need to **drive** your car"

## Notable patterns and self-corrections

The variability noted in Stage 1 — same naive prompt sometimes opening with **walk** and sometimes with **drive** — persists clearly: naive split 5/5, persona_positive split 6/4, even goal_anchor has a single clean walk (T2) that goes off on an "walk to the wash, then drive your car through the wash" tangent that disconnects "walk" (mode of human transit) from getting the car to the wash.

The most striking finding: **step_by_step is uniform** — 10/10 drive, the only framing that produces uniform behavior. Gemini Flash benefits enormously from explicit deliberation cues; the chain "goal → car must be at wash → therefore drive" lands every time. This is the inverse of Haiku, where step_by_step only nudged accuracy from 0% to 30%.

`persona_negative` is also uniform but in the wrong direction: 10/10 walk. Casual texting mode strips the analytic chain entirely and goes straight to "50m is right there" / "you'd spend more time backing out of your driveway" — the canonical wrong answer in vibes form. This is the perfect inverse of Haiku 4.5 (90% drive in casual mode). The two models read the same surface cue completely differently: for Haiku, casual = strip virtue-signaling-walk template; for Flash, casual = strip the deliberation that would surface the goal constraint.

`persona_positive` also helps Flash slightly (60% vs 50% naive) — the *opposite* of Haiku, where the "careful logical reasoner" persona dropped accuracy to 10%. Flash is a model that benefits from being told to think; Haiku is a model that gets worse when told to think.

`goal_anchor` T2 is the most interesting failure: Flash explicitly engages with the goal constraint ("By walking to the wash, starting your car there, washing it, and then driving it straight home"), threading walk-then-drive as a hybrid. The recommendation header is "walk to the car wash first, then drive your car through" — first verb wins for classification, and it's a genuine walk-recommendation rather than the wrong-answer template.

No mid-reply self-corrections in the Opus 4.7 sense. Flash's headers and conclusions agree in every trial. The persona_positive T1 case is the closest to drift — opens "you'll need to drive" then offers a "Recommendation" list that splits into "drive your car the 50 meters" (correct) and "walk back home" (after dropoff) — but the primary recommendation is still drive.

step_by_step T10 is the only borderline case in the entire 60-trial set. The "MUST DRIVE if automatic / SHOULD DRIVE if self-serve+bulky gear" decision tree contains an explicit "SHOULD WALK if self-serve bay + light gear" branch, and the discursive close (`for a 50-meter distance, if it's a self-serve bay... walking is often the most sensible`) leans walk. But the Step 1 header is "**You MUST DRIVE**" and the umbrella Recommendation Summary lists three drive cases first. Scored drive (consistent with how Haiku's similar-structure trials were scored), but a stricter judge could call this ambiguous.

## Comparison to Haiku 4.5 soak

The two models are nearly mirror images. Haiku fails naive 0/10 and is rescued by `persona_negative` (90%) and `goal_anchor` (80%); deliberation framings (step_by_step 30%, persona_positive 10%) hurt or barely help. Flash starts at 50% naive, is rescued by `step_by_step` (100%) and `goal_anchor`/`goal_restated` (80% each); the casual control crashes it to 0%. Both models converge under `goal_anchor` (80%) but for different reasons: Haiku needs the goal to bypass its virtue-signaling-walk template, while Flash already half-engages with the goal at baseline and just needs reinforcement. The shared finding across both models is that **goal-direction is a robust intervention** — naming "where the car needs to be" pulls both toward drive — but the framings that compete with it (deliberation vs. casual) split the two models in opposite directions, suggesting their failure pathways are architecturally different rather than two flavors of the same bug.
