# Car Wash Test — Stage 2, Opus 4.7

Opus 4.7 shows the inverse Haiku pattern: every deliberative framing (step_by_step, goal_anchor, persona_positive, goal_restated) lifts accuracy to 100%, while persona_negative — Haiku's surprise winner — collapses Opus to 0%. The naive baseline sits at 50% with three genuinely ambiguous "depends what you mean" responses, and Opus self-corrects mid-reply on five of the ten naive trials, opening with "Walk." then explicitly reversing.

## Pass rate by framing

| Framing | drive | walk | ambig | accuracy | Δ vs naive |
|---|---:|---:|---:|---:|---:|
| naive | 5 | 2 | 3 | 50% | — |
| step_by_step | 10 | 0 | 0 | 100% | +50 |
| goal_anchor | 10 | 0 | 0 | 100% | +50 |
| persona_positive | 10 | 0 | 0 | 100% | +50 |
| persona_negative | 0 | 10 | 0 | 0% | -50 |
| goal_restated | 10 | 0 | 0 | 100% | +50 |

## Per-trial classifications

### naive
- T1 ambiguous — opens "Walk." then bifurcates: "Buying supplies → walk. Taking the car through the wash → drive (you have no choice)"; refuses to commit
- T2 ambiguous — opens "Walk." then "if the destination requires the car to *be there*, drive. Otherwise, walk."
- T3 drive — opens "Walk." self-corrects "**Bottom line**: You need to drive the car... Walking yourself there without the car wouldn't accomplish anything"
- T4 drive — opens "Walk." then "Wait, actually — you want to wash the car, so you need to bring it. **Drive**"
- T5 ambiguous — opens "Walk." offers conditional "yes, you have to drive it there... But if you're going to a self-service bay... walk"
- T6 drive — opens "Walk." but practical-note closer "you'll need to drive it there regardless"
- T7 drive — opens "Walk." self-corrects "Actually, you need to drive... Walking would leave the car dirty at home"
- T8 walk — opens "Walk." closes "walking is the obvious choice here"; no correction
- T9 drive — opens "Walk." self-corrects "the real answer: **drive the car**, since the car itself is what's being washed"
- T10 walk — opens "Walk." closer "If it's a drive-through... then obviously you drive — but only at that point" (advice still favors walking-first)

### step_by_step
- T1 drive — "**Drive.** ... the car itself needs to go to the car wash"
- T2 drive — "**Answer: Drive.** ... walking doesn't accomplish the goal at all"
- T3 drive — "**Drive.** ... the car is the *object* of the task, not just transportation for you"
- T4 drive — "**You should drive.** ... the car is not just your transportation here — it's the actual object"
- T5 drive — "**Drive the car to the car wash.** ... walking defeats the entire purpose"
- T6 drive — "**Answer: Drive.** ... the car itself is the thing that needs to go"
- T7 drive — "**Answer: Drive.** ... the car is not optional cargo here — it's the entire point"
- T8 drive — "**Drive.** ... walking would defeat the entire purpose"
- T9 drive — "**Answer: Drive.** ... the car is not just *your* mode of transport — it's the *object* of the task"
- T10 drive — "**Drive.** ... the mode of transport is dictated by *what* you're transporting"

### goal_anchor
- T1 drive — "**Drive.** ... the car itself is the thing being transported"
- T2 drive — "**Drive** ... you'll just have to walk back and drive over anyway"
- T3 drive — "**Drive.** ... defeats the purpose"
- T4 drive — "**Drive.** ... You need the car *at* the car wash"
- T5 drive — "**Drive.** ... car needs to end up *at* the car wash"
- T6 drive — "you obviously need the car to be at the car wash... **Drive it**"
- T7 drive — "**Drive.** ... the car has to make the trip"
- T8 drive — "you pretty much have to **drive**"
- T9 drive — "driving makes more sense... just drive the 50 meters"
- T10 drive — "**Drive.** ... the car itself needs to end up at the wash"

### persona_positive
- T1 drive — "**Drive** ... it's a requirement"
- T2 drive — "**Drive** ... how does the car get washed?"
- T3 drive — "**Drive** ... the whole point is to get the *car* there, not you"
- T4 drive — "**Drive** ... you'd arrive at the car wash without the car"
- T5 drive — "**Drive** ... You need the car at the car wash"
- T6 drive — "**Drive** ... the car needs to get there to be washed"
- T7 drive — "**Drive** ... you have to drive it there regardless"
- T8 drive — "**Drive** ... the car wash washes cars, not pedestrians"
- T9 drive — "**Drive** ... walking doesn't accomplish your goal"
- T10 drive — "**Drive** ... the car has to get there"

### persona_negative
- T1 walk — "lol just walk, it's literally right there"
- T2 walk — "lol just walk, it's like 30 seconds away"
- T3 walk — "lol just walk, it's like 30 seconds away"
- T4 walk — "lol just walk, 50m is nothing"
- T5 walk — "lol just walk, 50m is nothing"
- T6 walk — "lol just walk, it's literally right there"
- T7 walk — "lol just walk, it's like 30 seconds away"
- T8 walk — "lol just walk it, 50m is nothing"
- T9 walk — "lol just walk, it's like 30 seconds away"
- T10 walk — "lol just walk, by the time you start the car you'd basically be there"

### goal_restated
- T1 drive — "**Drive.** ... walking there defeats the purpose"
- T2 drive — "**Drive.** ... the car needs to be at the wash, not you"
- T3 drive — "**Drive.** ... the car needs to be there"
- T4 drive — "**Drive.** ... walking accomplishes nothing toward your goal"
- T5 drive — "**Drive.** ... the car is the thing being cleaned"
- T6 drive — "**Drive.** ... only driving accomplishes your actual goal"
- T7 drive — "**Drive.** ... your car would still be at home"
- T8 drive — "**Drive.** ... you can't walk your car through one"
- T9 drive — "**Drive.** ... you can't really get your car washed without bringing the car"
- T10 drive — "**Drive.** ... you can't walk a car through a car wash"

## Notable patterns and self-corrections

The defining behavior of Opus 4.7 is the mid-reply self-correction. Under the naive prompt, **every single trial opens with the literal token "Walk."** as the first word — a strong reflex toward the heuristic answer — but on five of the ten (T3, T4, T6, T7, T9) the model audibly catches itself partway through. The correction signature is consistent: a parenthetical "Wait —" or "Actually —" or "(re-reading your question:)" pivots the reply, and a fresh recommendation appears in the closer. T4 is the cleanest example ("Wait, actually — you want to wash the car, so you need to bring it. Drive."). T9 is the most decisive ("the *real* answer: drive the car").

Three naive trials (T1, T2, T5) reach a different terminal state: instead of correcting to "drive," they bifurcate into a conditional ("commercial wash → drive, supplies → walk"), refusing to pick between the two readings. These are scored ambiguous because the model genuinely declines to commit to a substantive recommendation. Two trials (T8, T10) hold the walk recommendation through to the end without the self-correction firing.

Once any deliberative scaffolding is added — even minimal scaffolding — the self-correction is no longer mid-reply but appears upfront. step_by_step, goal_anchor, persona_positive, and goal_restated all open with "Drive." as the first word and never waver. The "I want my car to be clean" rewrite is as effective as the explicit step-by-step instruction, suggesting Opus's failure under naive isn't a reasoning gap but a surface-feature reflex anchored by the word order ("wash my car... 50 meters... walk or drive?").

persona_negative is the dramatic inversion. The casual-texting system prompt collapses the entire reasoning pathway: every reply is one line, no "wait," no self-correction, no consideration of where the car needs to be. The model simply pattern-matches to "50m + friend texting → lol just walk." This is the Haiku winning framing producing the Opus losing one.

## Comparison to Haiku 4.5 soak

The two models are nearly mirror images. Haiku gets goal-anchor right (80%) but gets persona_negative right too (90%) — for Haiku, casual mode strips a virtue-signaling template (fuel/wear/exercise) that was driving the wrong answer. Opus has no such template; its naive failures are heuristic-reflex first-tokens that the model then catches and corrects in writing. The casual register removes the room and the inclination to self-correct, so Opus collapses to 0% precisely where Haiku peaks.

Both models are perfect or near-perfect on goal_anchor, confirming the goal-direction prompt as the most robust intervention across the cohort. But step_by_step and persona_positive — only modest helpers for Haiku (30%, 10%) — are total fixes for Opus (100%, 100%). This is the cleanest evidence so far that "deliberative scaffolding helps the more capable model" and "casual mode helps the smaller model" are both real, separable effects.

Self-correction frequency: Haiku exhibited zero in 60 trials. Opus exhibited five out of ten on naive alone, plus the conditional-bifurcation pattern in three more. The judge approach was essential here — a last-keyword classifier would have miscalled all five Opus self-correction trials as walk and possibly all three ambiguous-conditional trials as well, inflating Opus's apparent naive failure rate to 100% when the substantive rate is 50%.
