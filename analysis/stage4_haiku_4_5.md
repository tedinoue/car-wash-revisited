# Car Wash Test — Stage 4, Haiku 4.5

The wrapper lifts Haiku off the floor — halfway, on three of five engineer cells. `engineer_v2` scores **50%** drive, +50 from Stage 3's `persona_engineer` 0%. Moai and sword match (50% each); owl and lion collapse back toward the eco-template (10%, 20%). All five environmentalist conditions are 0/10, identical to Stage 3. The wrapper sits on a knife edge: when the emoji nudges toward "analytical breakdown" register (owl, lion), Haiku resumes Stage 3's eco-template-with-engineering-vocabulary. When the emoji doesn't pre-commit that register (moai, sword), goal-feasibility reaches the surface in half of trials.

## Pass rate by condition

| Condition | drive | walk | ambig | accuracy | Δ vs Stage 3 (engineer 0%, enviro 0%) |
|---|---:|---:|---:|---:|---:|
| engineer_v2 | 5 | 5 | 0 | **50%** | **+50** |
| environmentalist_v2 | 0 | 10 | 0 | 0% | 0 |
| moai_engineer | 5 | 5 | 0 | 50% | +50 |
| moai_environmentalist | 0 | 10 | 0 | 0% | 0 |
| sword_engineer | 5 | 5 | 0 | 50% | +50 |
| sword_environmentalist | 0 | 10 | 0 | 0% | 0 |
| owl_engineer | 1 | 9 | 0 | 10% | +10 |
| owl_environmentalist | 0 | 10 | 0 | 0% | 0 |
| lion_engineer | 2 | 8 | 0 | 20% | +20 |
| lion_environmentalist | 0 | 10 | 0 | 0% | 0 |

Engineer-side total: **18/50 drive (36%)**. Environmentalist-side total: **0/50 drive**. Zero ambiguous trials across the entire 100-trial run — Haiku commits start-to-finish, same Stage 2/3 signature.

## Per-trial classifications

### engineer_v2 (5/10 drive)

Drives: T3 ("You need your car there anyway... walking back with wet clothes is annoying"), T4 ("you're going *to a car wash* — you'll need your car there anyway"), T5 ("easier to manage if you're dry when you arrive"), T8 ("it's the designed use case for your vehicle"), T10 ("pull right up to the wash"). Walks: T1, T2, T7 (cold-start template); T9 ("~5 calories... zero emissions"); T6 ("Why get your car dirty driving to get it washed?" — Stage 2/3 confabulation). The five drives all reach the goal-feasibility constraint; the five walks all run cold-start-emissions.

### environmentalist_v2 (0/10 drive)

Total template lock. All ten trials open "Walk!" / "I'd definitely walk!" / "Walk, definitely!" Every trial deploys the "win-win," "fossil fuels," "cold engine starts" cluster Stage 3 documented. Zero surface the goal constraint. T7 adds unsolicited eco-tips ("reusable bucket and cloth for an eco-friendly wash") — same template-extension Opus shows.

### moai_engineer (5/10 drive)

Drives: T2 ("you need your car *at* the wash anyway"), T5 ("you need to be AT the car wash with your car"), T6 ("Walking there without your car defeats the purpose"), T8 ("the car *must* make the trip"), T9. Walks: T1 ("feet over wheels"), T3 ("awkward moment of driving your car *to get it washed*" — confabulation), T4, T7, T10. Five clean declarative drives that reach "the car must be at the wash" without hedging. No stoic-brevity — mean ~970 chars, longer than engineer_v2's ~860. 🗿 is mascot; moai just doesn't suppress the wrapper.

### sword_engineer (5/10 drive)

Drives: T3 ("Cars are engineered specifically for door-to-door transport"), T5 ("You need your car *at* the wash location"), T7 ("Walking 50m feels virtuous but is actually less rational"), T9 ("you need the car at the wash location anyway"), T10 ("moving the thing that needs washing to where it gets washed"). Walks: T1, T2, T4, T6, T8. T7's "feels virtuous but is actually less rational" is the most explicit anti-eco-template surfacing in the Haiku Stage 4 dataset — closest to a discipline register. No other sword-precision metaphors.

### owl_engineer (1/10 drive — collapse)

Walks T1–T7, T9, T10: uniform pros/cons tables loading cold-start/emissions/wear on the walk side. T2 "below ~1 km, human-powered transportation typically beats motorized"; T7 "like using a sledgehammer to hang a picture"; T6 "avoid the irony of driving to a car wash" (confabulation). Single drive T8: "most people value the 1-2 minutes saved." The more thorough Haiku's breakdown, the more completely the eco-template colonizes it. The owl emoji adds analytical care; analytical care is exactly what the eco-template lives inside.

### lion_engineer (2/10 drive — partial collapse)

Walks T1, T2, T3, T5, T6, T7, T9, T10: declarative walk verdicts ("**The engineering verdict: Walk.**" closes T9, T10 verbatim); T6 "the 'obvious' choice (use the vehicle) isn't always the most efficient" — declarative *against* goal-feasibility. Drives T4 ("Walking means returning home without your car, then coming back"), T8 ("You'll likely need to move the car inside the wash anyway"). Haiku's confident verdicts are confidently walk. No lion-language ("roar," "decisive"); 🦁 is decoration. Lion does what owl does: amplifies the deliberative-verdict register the eco-template owns.

### environmentalist emoji conditions (0/40 drive across moai/sword/owl/lion)

Pure template lock. All 40 trials open "Walk!" or "Walk, definitely!" The eco-virtue script ("fossil fuels," "win-win," "30-second walk," "cold engine," "small choices add up") appears verbatim across all four emoji conditions. Two minor variations: lion_environmentalist T10 adds an unsolicited home-wash recommendation; moai/owl/lion environmentalist trials sometimes close with 🌍. Neither shifts the recommendation. The wrapper does not budge the environmentalist eco-template at all on Haiku, identical to Opus and Flash.

## Did the wrapper help?

**Yes, on three of five engineer cells, by +50.** Stage 3's `persona_engineer` was 0/10 — the eco-template ran with engineering vocabulary. Stage 4's wrapper lifts engineer_v2, moai_engineer, and sword_engineer to 5/10 each. The wrapper gives Haiku a 50/50 chance per trial of reaching "you need the car at the wash" before the cold-start template wins. No mid-reply self-corrections (the Opus signature) — Haiku commits at the top and runs through.

The lift is ceiling-bound at 50% on the responding cells. Stage 2's `goal_anchor` (80%) and `persona_negative` (90%) are still higher. The wrapper doesn't beat goal-direction or casual-register; it just opens a coin-flip where Stage 3's persona was deterministic walk.

## Why owl and lion collapse

Owl and lion drop to 10–20% — far below engineer_v2's 50%. The pattern: 🦉 and 🦁 push Haiku toward more elaborate analytical breakdowns (owl ~1010 chars, lion ~890), and elaborate analytical breakdowns are exactly the format the eco-template colonizes. owl_engineer T2, T3, T4 open with bullet pros/cons tables that pre-load the cold-start cluster on the walk side. lion_engineer T1, T2, T3, T6 close with declarative verdicts of walk. The owl/lion emoji activate the deliberative-verdict register that Stage 3 identified as the eco-template's home register — they suppress the wrapper rather than stack with it.

🗿 and 🗡️ don't pre-commit Haiku to that register. Moai-stoic and sword-precision don't appear as voice, but the *absence* of additional analytical scaffolding is enough — the wrapper's 50/50 lift survives.

## Did persona induction fire?

**No.** Across 80 emoji-stacked Haiku trials, the four archetype voices are absent:

- **🗿 Moai.** Mean moai_engineer length ~970 chars, longer than engineer_v2 (~860). No stoic-brevity, no virtue-rejection idiom. Mascot only.
- **🗡️ Sword.** Zero discipline/strike metaphors. Sword_engineer T7 ("Walking 50m feels virtuous but is actually less rational") is the closest anti-virtue framing — single sentence inside standard breakdown, not a voice.
- **🦉 Owl.** This is Haiku's baseline engineering register; 🦉 produces *more* baseline (longer pros/cons tables) but no different register. The added analytical care is the failure mechanism.
- **🦁 Lion.** Verdicts in lion_engineer ARE declarative ("**The engineering verdict: Walk.**" closes T9, T10 verbatim) — but declarative-toward-walk, the opposite of the lion-rescues-drive hypothesis.

Same finding as Opus, Flash, Flash Lite: emoji activators do not produce language-style adoption on Car Wash. The wrapper does the work; the emoji either preserves the lift (moai, sword) or suppresses it (owl, lion).

## Where Stage 4 places Haiku 4.5

Stage 3 placed Haiku as a single-attractor model (eco-virtue template) with three breakers: explicit goal-direction (80%), casual-register dissolution (90%), and physical impossibility (100%). Stage 4 adds a fourth, partial breaker: the activating wrapper, producing a 50/50 coin flip on three of five engineer conditions. Stage 4 Haiku ranking:

1. distance_50km — 100%
2. persona_negative — 90%
3. goal_anchor — 80%
4. **engineer_v2 / moai_engineer / sword_engineer — 50%** (new)
5. step_by_step — 30%
6. **lion_engineer — 20%** / goal_restated — 20%
7. persona_positive — 10% / **owl_engineer — 10%** (new)
8. naive / neutral / environmentalist / engineer / self_correction / **all 5 enviro_v2** — 0%

Cross-model: Haiku's engineer_v2 50% sits between Opus 4.7 (70%), Flash (70%), and Flash Lite (10%). The wrapper effect on Haiku is real, mid-magnitude, and conditional on the emoji co-prefix not pushing the model into the deliberative register where the eco-template lives. The environmentalist saturation finding is uniform across the four-model Stage 4 cohort: 0/40 drive on every model under environmentalist, with or without emoji. The wrapper does not reach the eco-template attractor on any architecture tested. Haiku's specific contribution: the owl/lion collapse — evidence that "more analytical scaffolding" is precisely the wrong direction for goal-feasibility surfacing on this prompt.
