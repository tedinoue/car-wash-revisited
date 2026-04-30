# Car Wash Test — Stage 3, Opus 4.7

Self-correction induction lifts Opus from 5/10 to 10/10 explicit self-corrections, distance_50km holds the floor at 100%, and the engineer persona collapses Opus into a bifurcated-conditional pattern that mirrors its naive ambiguous trials — while the environmentalist persona drops Opus to 0%, the same floor as the casual `persona_negative` register did in Stage 2.

## Pass rate by condition

| Condition | drive | walk | ambig | accuracy | Δ vs Stage 2 naive (50%) |
|---|---:|---:|---:|---:|---:|
| distance_50km | 10 | 0 | 0 | 100% | +50 |
| persona_neutral | 0 | 6 | 4 | 0% | -50 |
| persona_environmentalist | 0 | 10 | 0 | 0% | -50 |
| persona_engineer | 3 | 1 | 6 | 30% | -20 |
| self_correction_induction | 10 | 0 | 0 | 100% | +50 |

## Per-trial classifications

### distance_50km

All ten trials open with "Drive." and resolve cleanly. The 50 km distance functions exactly as the floor predicted: the walk-template never activates because no model can sustain "10–12 hours of walking" as a serious recommendation.

- T1 drive — "Drive. 50 kilometers is far too far to walk... the whole point is to clean your car"
- T2 drive — "Drive. 50 kilometers is far too far to walk practically"
- T3 drive — "you're going to a car wash — you need the car there to wash it!"
- T4 drive — "your goal (a clean car) requires the car to be there anyway"
- T5 drive — "since you're going to a car wash, you'll need the car with you anyway"
- T6 drive — "the whole point is to wash your car, so you need to bring it"
- T7 drive — "Driving is the only realistic option for that distance"
- T8 drive — "you need the car at the car wash"
- T9 drive — "Drive. 50 kilometers is far too far to walk"
- T10 drive — "Walking 50 km to a car wash without your car would defeat the purpose entirely"

### persona_neutral

System prompt: "Answer factually, in two sentences." Six trials commit walk; four bifurcate into a conditional ("walk for the distance, however, you'll need to drive the car *to* the wash") without committing — the same pattern Opus produced in three of its naive Stage 2 trials. The two-sentence brevity constraint suppresses the deliberation that would normally surface the goal in Stage 2's `step_by_step` and `goal_anchor` framings.

- T1 ambiguous — "walking is the better choice... However, if you're planning to drive through an automated car wash, you'll obviously need to drive the car there"
- T2 walk — "You should walk... you'd likely spend more time getting in and out of the car than simply walking"
- T3 ambiguous — "walking is the better choice... However, if you're planning to get the car washed, you'll obviously need to drive it to the car wash regardless"
- T4 ambiguous — "walking is the better choice... However, if you're planning to actually use the car wash, you'll obviously need to drive the car there to wash it"
- T5 walk — "your car will get washed at the car wash regardless of how you arrive, so there's no practical benefit to driving" (factually wrong but a clean walk commitment)
- T6 ambiguous — "walking is the better choice... you'd want to drive *to* the car wash to actually wash the car, so this only makes sense if you're picking up something else there"
- T7 walk — "your car will get washed either way"
- T8 ambiguous — "walking is the better choice... your car will get washed at the destination regardless... which you could simply push or drive at the very end"
- T9 walk — "30-second walk... you'd likely spend more time getting in and out"
- T10 walk — "less than a minute on foot. Driving would waste fuel"

### persona_environmentalist

System prompt: "You're an environmentalist." Ten consecutive walk recommendations, every single one opening with "Walk, without question!" — the strongest template lock observed in Opus across the entire study. The eco-virtue overlay (cold-start emissions, catalytic converter, water recycling) crowds out the goal entirely; in zero trials does the model surface the "the car has to be at the wash to be washed" insight that fires reliably in Stage 2's deliberative framings.

- T1 walk — "Walk, without question!... Driving 50 meters is essentially nothing for your engine"
- T2 walk — "Walk, without question! Driving 50 meters is genuinely one of the least efficient things"
- T3 walk — "Walk, without question! the environmental (and practical) math just doesn't work out"
- T4 walk — "Walk, without question! For a 50-meter trip, driving makes no environmental (or practical) sense"
- T5 walk — "Walk, definitely! Cold engines are the most polluting"
- T6 walk — "Walk, without question! the car barely warms up before you arrive"
- T7 walk — "Walk, without question! For just 50 meters, driving makes no environmental (or practical) sense"
- T8 walk — "Walk, without question! Cold engines are at their most polluting"
- T9 walk — "Walk, without question! Cold engines pollute disproportionately"
- T10 walk — "Walk, without question! Driving 50 meters is essentially the worst-case scenario for a car engine"

The environmentalist override is total. The closest any trial comes to acknowledging the goal is T8's "Driving to a car wash to clean a car you just dirtied a tiny bit more by driving is a bit of a contradiction!" — which inverts the goal logic rather than honoring it.

### persona_engineer

System prompt: "You're an engineer." This is the most surprising condition. Rather than amplifying drive via goal-completion association, the engineer persona produces the bifurcated-conditional response Opus naively gives in 3/10 of its Stage 2 baseline trials — six of ten end with an explicit "Which type is it?" question or a `if X then drive, otherwise walk` split. Two trials (T3, T10) show the explicit Stage 2 self-correction signature ("Wait — re-reading your question..." / "Hold on. I need to reconsider"). Only one trial (T7) commits walk fully, and it does so by misreading its own task ("for a 50-meter trip on foot? Walk").

- T1 ambiguous — opens "Walk." then bifurcates into drive-through vs. self-serve, ends "Which type is it?"
- T2 ambiguous — opens "Walk." then "If washing your car → you have to drive... If buying supplies → walk. Which is it?"
- T3 drive — opens "Walk." then explicit self-correction "Wait — re-reading your question... Drive. There's no other option"
- T4 ambiguous — opens "Walk." bifurcates self-service vs. tunnel vs. supplies, ends "Which scenario is it?"
- T5 ambiguous — "Walk... if it's a self-serve bay where you need to drive *into* the wash stall, you obviously have to drive... If you're just walking over to grab supplies or pay, walk"
- T6 ambiguous — "Walk... if you're going to a drive-through automated wash, you obviously have to drive... Otherwise (self-serve bay, bucket-and-hose, etc.): walk"
- T7 walk — "if you're hauling supplies (buckets, vacuum, etc.) or it's a drive-through wash... obviously drive. But for a 50-meter trip on foot? Walk"
- T8 drive — "Walk... I assume that's [drive-through] what you meant, in which case: drive, but accept that this is one of the harder use cases on your engine" (commits drive on the assumed reading)
- T9 ambiguous — opens "Walk." then bifurcates, ends "Which is it?"
- T10 drive — opens "Walk." then explicit self-correction "wait — yes, there is. Hold on. I need to reconsider... **Answer: Drive.**"

The engineer persona behaves more like a deliberation-stripping prompt than a goal-amplifying one. The model spends its reasoning budget on cold-start fuel/wear analysis (the engineering vocabulary) and resolves to a conditional rather than the goal.

### self_correction_induction

User prompt: "Think out loud. You can revise your answer mid-reply if new considerations occur to you." Every single trial follows the Stage 2 mid-reply self-correction pattern explicitly: opens with "50 meters is really short" / "30–40 second walk" framing, hits a "But wait —" pivot, and resolves to drive on goal grounds. **All ten trials self-correct.** This raises Opus's self-correction rate from 5/10 naive to 10/10 induced.

- T1 drive — self-correct "But wait — the question is about washing the car... Drive"
- T2 drive — self-correct "But wait — you want to *wash* the car. That changes things completely... Drive"
- T3 drive — self-correct "But wait — the purpose here matters... drive. Definitely drive"
- T4 drive — self-correct "But wait — the question is about washing the car... Drive"
- T5 drive — self-correct "But wait... You need the car *at* the car wash... So drive"
- T6 drive — self-correct "But wait — you want to *wash* your car... Drive. Definitely drive"
- T7 drive — self-correct "But wait — the goal is to wash the car... Drive"
- T8 drive — self-correct "But wait — the question is whether to walk or drive *to* the car wash... Drive"
- T9 drive — self-correct "But wait, the whole point is to wash the car... Drive"
- T10 drive — self-correct "But wait — you said you want to wash your car... Drive"

## Notable patterns

**The floor holds.** distance_50km produces 10/10 drive as predicted. No model in the study should fail this; Opus passes cleanly with all ten trials surfacing the "you need the car at the car wash" goal explicitly.

**The engineer persona does not amplify drive.** The hypothesis was that an identity associated with goal-completion would push Opus over its near-ceiling 100% on most framings. Instead, engineer collapses Opus to 30% and produces six bifurcated-conditional trials with explicit "which type?" questions. The engineering vocabulary (cold-start emissions, catalytic converter warm-up, oil dilution) burns the deliberation budget on fuel/wear concerns and the model never reaches the goal. This is closer to a soft `persona_negative` than to `goal_anchor`. The two trials that resolve to drive (T3, T10) do so via the same mid-reply self-correction signature the model uses on naive — meaning the engineer persona doesn't add anything; the same 2–3/10 trials that would have self-corrected on naive still self-correct here.

**Environmentalist drops below the goal-anchor floor.** The casual `persona_negative` produced 0% in Stage 2; environmentalist replicates that 0% via a different mechanism. Where casual mode strips deliberation, environmentalist *channels* deliberation entirely into eco-virtue framing. The walk-template is fully template-locked across all ten trials — every single one opens "Walk, without question!" — and the goal never gets a representational hook.

**Self-correction induction approximately doubles the rate.** Stage 2 naive showed 5/10 explicit self-corrections (plus 3/10 conditional bifurcations). With the explicit license, all ten trials self-correct mid-reply, and zero produce the conditional-bifurcation outcome that ate three trials in naive. The "I almost talked myself into a silly answer by fixating on '50 meters is short'" closer in T2 is the cleanest illustration: when given permission to revise, Opus uses it every time, and the conditional-ambiguous outcome disappears entirely. The natural ceiling is at least 10/10 — the explicit license isn't redundant with the model's baseline tendency.

**The persona_neutral result clarifies persona_negative.** Stage 2 left open whether `persona_negative`'s collapse was casual-register-specific or a more general deliberation-stripping effect. `persona_neutral` (factual, two sentences, no register cues) drops Opus to 0% drive but produces a different failure mode: four conditional-bifurcation trials and six clean walk commitments, vs. ten clean walk commitments under casual mode. Both are deliberation-stripped and both fail, but neutral leaves enough room for the goal to surface as a "however" caveat in 4/10 trials. The casual register additionally flattens the response shape — neutral is still recognizably Opus.

## Where Stage 3 places Opus 4.7

Stage 2 classified Opus 4.7 as a strong responder — perfect on every deliberative scaffold, with mid-reply self-correction the signature behavior. Stage 3 sharpens the picture in three ways. (1) The self-correction is real and ceiling-raisable: explicit license takes Opus from 5/10 to 10/10. The signature isn't a fixed model feature but an exploitable behavior with headroom. (2) Persona effects are not unidirectional. The "engineer" identity, predicted to amplify drive, instead produces a bifurcated-conditional pattern that mirrors Opus's worst Stage 2 failure mode; the "environmentalist" identity locks the walk template more thoroughly than even the casual register did. Persona induction is only as helpful as the identity's relationship to the actual goal. (3) Brevity is more dangerous to Opus than register. `persona_neutral` (factual, two sentences, no casual cues) collapses Opus to 0% almost as completely as `persona_negative` did, which means the deliberation-stripping effect was doing most of the work in Stage 2's casual-mode collapse, not the casual register itself. Opus is robustly correct when given room to think; it is robustly wrong when room to think is removed, regardless of how that removal is framed.
