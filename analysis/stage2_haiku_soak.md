# Car Wash Test — Stage 2 soak run, Haiku 4.5

Haiku 4.5 fails the naive prompt 0/10 as in Stage 1, but goal-framing flips it dramatically: `goal_anchor` lifts accuracy to 80% and `persona_negative` (the "casual texting" control) hits 90% — the highest of any framing. `persona_positive` actively hurts (10%, worse than naive in Stage 1's free-text data because it now produces self-justifying walk arguments). The cheap "think step by step" cue gives only a modest lift (30%); restating the goal as "I want my car to be clean" barely helps (20%).

## Pass rate by framing

| Framing | drive | walk | ambig | accuracy | Δ vs naive |
|---|---:|---:|---:|---:|---:|
| naive | 0 | 10 | 0 | 0% | — |
| step_by_step | 3 | 7 | 0 | 30% | +30 |
| goal_anchor | 8 | 2 | 0 | 80% | +80 |
| persona_positive | 1 | 9 | 0 | 10% | +10 |
| persona_negative | 9 | 1 | 0 | 90% | +90 |
| goal_restated | 2 | 8 | 0 | 20% | +20 |

## Per-trial classifications

### naive
- T1 walk — opens "**Walk.** Here's why" ; closes "the only reason to drive would be if you have mobility issues"
- T2 walk — opens "**Walk** is the better choice here"
- T3 walk — "I'd suggest **walking** for 50 meters"
- T4 walk — "**Walk.** Here's why"
- T5 walk — "**Walk.** Here's why"
- T6 walk — "**Walk** is the better choice here"
- T7 walk — "**Walk** would be the better choice here"
- T8 walk — "**Walk.** Here's why"
- T9 walk — "**Walk.** Here's why"
- T10 walk — "Walking makes more sense here"

### step_by_step
- T1 drive — "**Recommendation: Drive**" ; concern about being stranded with wet car
- T2 walk — "**Recommendation: Walk**"
- T3 walk — "**The answer: Walk**" (with confused premise that car is "already with you")
- T4 walk — "**Recommendation: Walk**"
- T5 walk — "**My recommendation: Walk**"
- T6 drive — "**The answer: Drive** ... your car must be at the location to be washed"
- T7 walk — "**Recommendation: Walk**"
- T8 walk — "**Walk.** For 50 meters, walking is faster"
- T9 walk — "**My recommendation: Walk** ... 50 meters is genuinely negligible"
- T10 drive — "**Drive.** The whole point is to get your car to the car wash"

### goal_anchor
- T1 drive — "# Drive ... walking would just leave your unwashed car behind"
- T2 drive — "# Drive to the car wash ... your dirty car to the wash location"
- T3 drive — "**Drive.** ... You need the car at the car wash anyway"
- T4 walk — "You should **walk**" (oddly reasons that driving 50m would re-dirty the car)
- T5 walk — same pattern as T4 — "drive home afterward with a freshly cleaned car"
- T6 drive — "**Drive** makes more sense ... need the car to be at the car wash"
- T7 drive — "**Drive** ... you'd arrive at an empty car wash with no car to clean"
- T8 drive — "Drive ... the car needs to be at the wash"
- T9 drive — "**Drive** makes more sense ... need the car to be at the car wash anyway"
- T10 drive — "**Drive.** ... You need the car at the car wash anyway"

### persona_positive
- T1 walk — "**Walk.** It's faster, easier, and more practical"
- T2 walk — "I'd walk"
- T3 walk — "I'd walk"
- T4 drive — "**My recommendation:** Drive ... your car needs to be at the car wash regardless"
- T5 walk — "I'd walk"
- T6 walk — "I'd walk"
- T7 walk — "I'd recommend **walking**"
- T8 walk — "I'd say **walk**"
- T9 walk — "I'd walk"
- T10 walk — "I'd say **walk**"

### persona_negative
- T1 drive — "Drive lol"
- T2 drive — "Drive, definitely lol ... you need the car there obviously"
- T3 drive — "Drive lol"
- T4 drive — "lol drive ... you need the car *at* the car wash"
- T5 drive — "Drive lol ... you'd have to drive it there anyway"
- T6 drive — "Drive, definitely"
- T7 walk — "Walk, definitely. 50 meters is like a 30-second walk"
- T8 drive — "Drive, definitely ... want your car at the car wash anyway"
- T9 drive — "Drive lol"
- T10 drive — "lol drive. you're literally right there" (small anti-drive aside about the irony, but the recommendation both opens and closes as drive)

### goal_restated
- T1 walk — "**Walk.** It's only 50 meters"
- T2 walk — "**Walk.** Here's why"
- T3 drive — "**Drive** is the practical choice ... you need to get your car there anyway"
- T4 walk — "**Walk.**"
- T5 walk — "**Walk** – it's the better choice here"
- T6 walk — "Walking makes more sense here"
- T7 walk — "**Walk.**"
- T8 walk — "**Walk** is the better choice here"
- T9 drive — "**Drive** makes more sense ... since your goal is to clean the car, you need it at the location"
- T10 walk — "**Walk** is the better choice here"

## Notable patterns and self-corrections

The single most consistent Haiku 4.5 trigger for the right answer is **explicit goal-direction**: phrasings like "you need the car at the car wash" or "your goal is to clean the car, you need it at the location anyway" appear verbatim in essentially every drive-correct trial across framings (goal_anchor T1/T2/T3/T6/T7/T8/T9/T10; goal_restated T3/T9; step_by_step T1/T6/T10). When Haiku reaches that sentence it gets the answer; when it doesn't, it slides into the canned "30-second walk / fuel / wear / mobility issues" template which appears nearly word-for-word across naive, persona_positive, and goal_restated.

`persona_negative` is the surprise: it scores 90%, the best of any framing, because casual mode strips the "fuel/wear/exercise" virtue-signaling template that drags Haiku into walk under deliberative framings. The casual reasoning is literally "you need the car there obviously" — which is correct.

`persona_positive` hurts because it cues *more* template-style deliberation, which is exactly the failure mode here.

Goal_anchor T4 and T5 are the most interesting failures: the goal framing prompted Haiku to invent a novel-but-wrong argument that driving 50m would re-dirty the car. This is a different walk-pathway from the naive template — it's actually engaging with the goal but reasoning incorrectly about it.

No mid-reply self-corrections of the Opus 4.7 variety were observed. Haiku 4.5's responses are committed start-to-finish; the `recommendation:` line at the top matches the `recommendation:` line at the bottom in every trial.

## Pipeline validation

The AI-judge approach worked cleanly. Every Haiku trial was unambiguous — no genuine refusals, no self-corrections, and the substantive recommendation was always stated explicitly (often boldfaced). The Stage 1 last-keyword parser would have miscalled at least 11 trials I can identify: every "Walk... only reason to drive..." closer in the naive set (T1, T3, T4, T5, T6, T7, T8, T9 — same parser pathology as Stage 1 Trial 4), plus persona_negative T10 ("just drive it over" closer should be drive but earlier "you'd get your car all dirty driving" would confuse a keyword counter), and step_by_step T1/T6 where the explicit "Recommendation: Drive" header is followed by paragraphs containing "walking" multiple times. The judge approach is ready for the remaining six failers.
