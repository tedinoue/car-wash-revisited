# Car Wash Test — Stage 2, Gemini 2.5 Flash Lite

Flash Lite is a strong walk-er at baseline (0/10 naive) with a notably different framing-response profile than Haiku 4.5: deliberative cues help substantially (`step_by_step` 50%, `goal_anchor` 40%, `goal_restated` 40%) while the casual-texting persona that rescued Haiku catastrophically *fails* here (10%) — Flash Lite's casual register is a confident "save that gas money" walk-er, the exact opposite pathology from Haiku's casual mode.

## Pass rate by framing

| Framing | drive | walk | ambig | accuracy | Δ vs naive |
|---|---:|---:|---:|---:|---:|
| naive | 0 | 10 | 0 | 0% | — |
| step_by_step | 5 | 5 | 0 | 50% | +50 |
| goal_anchor | 4 | 6 | 0 | 40% | +40 |
| persona_positive | 1 | 9 | 0 | 10% | +10 |
| persona_negative | 1 | 9 | 0 | 10% | +10 |
| goal_restated | 4 | 6 | 0 | 40% | +40 |

## Per-trial classifications

### naive
- T1 walk — "walking is almost certainly the better option ... walk!"
- T2 walk — "walking is usually the more practical and enjoyable option"
- T3 walk — "walking is a perfectly viable and even beneficial option" (hedged with "if any of the 'drive' reasons apply, that's reasonable too")
- T4 walk — "walking is generally the more sensible and often preferred option ... walk!"
- T5 walk — "walking is almost certainly the better option ... walk!"
- T6 walk — long CoT-like deliberation followed by "**Walk.** Here's why ... walking is the most sensible and practical option"
- T7 walk — "you should definitely walk"
- T8 walk — "my recommendation is to WALK!"
- T9 walk — "Most people would consider walking to be the more sensible and beneficial option" (closes "Ultimately, it's your choice!" but lead is walk)
- T10 walk — "unless there are very specific and unusual circumstances, you should definitely walk"

### step_by_step
- T1 walk — "walking is the more logical and efficient choice ... walk to the car wash"
- T2 drive — "You should drive ... walking to the car wash doesn't accomplish this directly" (reaches the goal-anchored argument)
- T3 walk — "for a 50-meter distance, walking is the default and most logical choice"
- T4 walk — "you should walk" (despite reaching the right premise, slides back to time/effort)
- T5 drive — "the answer is: Drive" (cleanest reasoning of the run — "walking would require an unnecessary round trip")
- T6 walk — "Recommendation: Walk"
- T7 drive — "you should drive ... you cannot walk a car"
- T8 drive — "the action required to achieve the goal is driving"
- T9 drive — "You must drive your car to the car wash"
- T10 drive — "Decision: You should drive your car to the car wash"

### goal_anchor
- T1 walk — "you should walk to the car wash" (ignores the "where the car needs to be" cue entirely)
- T2 walk — "walking is almost certainly the better option"
- T3 walk — "you should definitely walk" (most aggressively-walked goal_anchor trial)
- T4 drive — "In almost all practical scenarios where your car is readily accessible, you will be driving the 50 meters to the car wash"
- T5 drive — "you should drive your car to the car wash. Walking won't get the car there!"
- T6 walk — "walking is the most practical and efficient option"
- T7 drive — "you should drive to the car wash ... Walking would leave your car at home!"
- T8 walk — "you should definitely walk to the car wash"
- T9 drive — "For the purpose of getting your car to the car wash, you should drive"
- T10 walk — "I'd suggest you walk"

### persona_positive
- T1 walk — "unless there's a strong reason to drive ... you should probably walk"
- T2 walk — long thinking-process trial; ends "walking is the logical default choice for such a short distance"
- T3 walk — "You should walk"
- T4 walk — "walking is almost certainly the better option ... walk!"
- T5 walk — "Therefore, you should walk"
- T6 walk — "walking is the far more practical, efficient, and environmentally friendly choice"
- T7 drive — long CoT, then a self-correction mid-think: "Crucial Point: You need to move the *car* to the car wash. Therefore, you *must* drive it" — final answer drive
- T8 walk — "walking is overwhelmingly the better choice"
- T9 walk — "walking is almost certainly the better option"
- T10 walk — "walking is the much more practical and sensible option"

### persona_negative
- T1 walk — "Definitely walk"
- T2 walk — "Definitely walk! Save that gas money"
- T3 walk — "you could totally walk there and back"
- T4 walk — "Definitely walk!"
- T5 walk — "Definitely walk it"
- T6 walk — "Definitely walk it"
- T7 walk — "You could totally walk it"
- T8 drive — "Definitely drive! 50 meters is super short, but still way too far to walk with a car wash kit, lol" (reasoning is wrong but recommendation is drive)
- T9 walk — "Just walk it. Save that gas money!"
- T10 walk — "Definitely walk it, save that gas money"

### goal_restated
- T1 drive — "You should drive your car to the car wash ... Walking would only get *you* there, not your car"
- T2 walk — "walking is almost certainly the better option"
- T3 drive — meanders, but lands "For a 50-meter trip to the car wash, driving is the most common and generally recommended choice for ease and efficiency"
- T4 walk — "walking is generally the better option"
- T5 drive — "you should definitely drive your car to the car wash. Walking 50 meters would mean you're not bringing your car to be washed"
- T6 drive — "You should drive to the car wash ... Walking 50 meters would get *you* there, but not your car"
- T7 walk — "walking is almost certainly the better choice"
- T8 walk — "You should walk to the car wash"
- T9 walk — "You should definitely walk"
- T10 walk — "walking is almost certainly the better option ... walk!"

## Notable patterns and self-corrections

The Stage 1 finding holds at baseline: Flash Lite is locked into a template — "50 meters is very short ... walking is almost certainly the better option" — that recurs nearly verbatim across naive, persona_positive, and the walk-trials of every other framing. The signature phrases are "almost certainly," "negligible distance," "good for you," "environmentally friendly," and an "only reason to drive would be ..." escape clause for mobility/weather/heavy supplies. Naive trials 1, 5, and 10 are essentially the same response with cosmetic variation.

What *does* crack the template is explicit goal-redirection in the user prompt. `step_by_step` works (50%) because Flash Lite's CoT, when actually executed, occasionally surfaces the realization that *the car needs to be at the car wash* — see T2's "walking to the car wash doesn't accomplish this directly," T5's "walking would require an unnecessary round trip," T7's "you cannot walk a car," T8's "Goal NOT achieved / Goal ACHIEVED" tabular comparison, and T9–T10's nearly identical goal-anchored conclusions. But the same CoT prompt can run for thousands of tokens and still land on walk (T1, T3, T4, T6) when the deliberation gets dragged into time/effort/fuel/wear comparisons rather than goal feasibility.

`goal_anchor` underperforms `step_by_step` (40% vs 50%), which is mildly surprising — the explicit "consider where the car needs to be" cue should be the strongest drive nudge available. Trials 4, 5, 7, and 9 do exactly what the cue intends ("Walking won't get the car there!", "Walking would leave your car at home!"), but T1, T2, T3, T6, T8, T10 simply ignore the framing and run the standard walk template. Flash Lite is not reliably attending to the prepended directive.

`goal_restated` ("I want my car to be clean") behaves similarly to goal_anchor at 40%. The trials that flip to drive (T1, T3, T5, T6) all explicitly anchor on the goal: "Walking would only get *you* there, not your car." The other six replay the naive walk template essentially unchanged — the goal restatement does not penetrate.

The headline finding is `persona_negative`. For Haiku 4.5, the casual-texting persona was a 90% drive-er because it stripped deliberative virtue-signaling. For Flash Lite, the same persona scores 10% — *worse than naive*-tied. Flash Lite's casual register is "Dude, 50 meters is like, super close! Save that gas money 🚶‍♀️🚗" repeated across nine of ten trials. The casual mode encodes "short distance = walk + save gas + get exercise" as a single chunked response, with no goal-attention surface for the framing to grab. T8 is the only drive (with bizarre reasoning that 50m is "way too far to walk with a car wash kit").

`persona_positive` produces the longest, most elaborate CoT-style traces (T2 and T7 are >700-word internal monologues), but only T7 self-corrects to drive. T7 is the cleanest mid-reply self-correction in the set: roughly half the thinking-trace concludes "walking is the logical default choice," then explicitly course-corrects with "Crucial Point: You need to move the *car* to the car wash. Therefore, you *must* drive it." This is the Opus-style self-correction pattern Haiku didn't show, but it's a sample of one in the Flash Lite data.

No genuine refusals, no hard API failures (all 60 trials completed), and the substantive recommendation was always identifiable — though several trials (naive T9, persona_positive T1, goal_anchor T4) are deliberately hedged "depends on whether you're in the car / want exercise" answers that lean rather than commit. None reached genuine ambiguity by my read.

## Comparison to Haiku 4.5 soak

Flash Lite and Haiku 4.5 share Stage 1's verdict (unanimous walk-er at baseline) and the template-style failure mode, but the framing-response curves diverge sharply. Haiku's profile was: goal_anchor +80, persona_negative +90, step_by_step +30, goal_restated +20, persona_positive +10. Flash Lite's profile is: step_by_step +50, goal_anchor +40, goal_restated +40, persona_negative +10, persona_positive +10. The two models invert on the two strongest framings: goal_anchor is Haiku's best and Flash Lite's middling third, while persona_negative is Haiku's best and Flash Lite's worst (tied with persona_positive). Casual-mode mechanics differ at the persona level — Haiku's casual mode strips deliberation and the bare goal-recognition surfaces; Flash Lite's casual mode encodes the entire walk-template as a single SMS-shaped chunk that's even harder to break than the naive deliberative version. The cheap "think step by step" cue is Flash Lite's most reliable lift (50%), where it gave Haiku only +30 — Flash Lite genuinely uses the CoT scratchpad to occasionally reach the goal-feasibility argument, where Haiku used it to elaborate the time/effort template. Both models occasionally invent the wrong-but-engaged "drive 50m would re-dirty the car" anti-driving argument under goal framings (Haiku goal_anchor T4/T5; Flash Lite goal_anchor T1/T2 lean similarly), suggesting a shared failure mode where goal-direction framing is registered but mis-applied. Flash Lite shows one clean Opus-style mid-reply self-correction (persona_positive T7); Haiku showed none.
