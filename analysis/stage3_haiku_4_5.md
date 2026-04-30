# Car Wash Test — Stage 3, Haiku 4.5

Persona_neutral does **not** replicate persona_negative's 90% — neutral-brevity scores 0/10, identical to naive. The 90% was casual register doing specific work, not brevity. Haiku also reveals a striking new pattern under self-correction induction: it self-corrects *toward walk*, the opposite of Opus 4.7's drive-direction mid-reply reversal.

## Pass rate by condition

| Condition | drive | walk | ambig | accuracy | Δ vs Stage 2 naive (0%) |
|---|---:|---:|---:|---:|---:|
| distance_50km | 10 | 0 | 0 | 100% | +100 |
| persona_neutral | 0 | 10 | 0 | 0% | 0 |
| persona_environmentalist | 0 | 10 | 0 | 0% | 0 |
| persona_engineer | 0 | 10 | 0 | 0% | 0 |
| self_correction_induction | 0 | 8 | 2 | 0% | 0 |

For reference: Stage 2 persona_negative (the 90% headline) sits between these new conditions in framing-space.

## Per-trial classifications

### distance_50km (floor test)
- T1 drive — "You should **drive** ... 50 km is too far to walk"
- T2 drive — "You should **drive** ... 10+ hours on foot"
- T3 drive — "Drive. Here's why ... too far to walk"
- T4 drive — "Drive, definitely"
- T5 drive — "You should **drive** ... need your car there to wash it anyway"
- T6 drive — "**Drive.** It's the practical choice"
- T7 drive — "You should drive"
- T8 drive — "Drive ... need your car clean, which implies you have a car"
- T9 drive — "You should **drive**"
- T10 drive — "Drive. Here's why"

### persona_neutral
- T1 walk — "You should walk ... Driving would waste fuel and time"
- T2 walk — "You should walk ... Driving would waste fuel and time"
- T3 walk — "You should walk ... driving would waste fuel and time"
- T4 walk — "Walking is the better choice"
- T5 walk — "You should walk ... about a 1-minute walk"
- T6 walk — "You should walk ... defeats the purpose of going to a car wash"
- T7 walk — "You should walk"
- T8 walk — "You should walk"
- T9 walk — "You should walk"
- T10 walk — "You should walk"

### persona_environmentalist
- T1 walk — "Walk ... Burn fuel for an unnecessary trip"
- T2 walk — "Walk ... arrive already dirty from the drive" (the goal_anchor T4/T5 confabulation reappears)
- T3 walk — "Walk ... 1-minute walk"
- T4 walk — "Walk ... Defeat the purpose of going to a car wash (keeping your car clean)"
- T5 walk — "Walk ... Win-win"
- T6 walk — "Walk ... 30-second walk"
- T7 walk — "Walk ... straightforward case where walking wins"
- T8 walk — "Walk"
- T9 walk — "Walk ... It's a no-brainer"
- T10 walk — "Walk ... wasteful"

### persona_engineer
- T1 walk — "Walk ... clear choice from practical, economic, and environmental angles"
- T2 walk — "Walk ... For 50 meters, walking is the practical choice"
- T3 walk — "Walk ... fuel/emissions saved by not walking"
- T4 walk — "# Walk ... Short trips are hard on engines (they don't warm up efficiently)"
- T5 walk — "Walk ... Engine startup emissions ... cold start"
- T6 walk — "**Walk.** ... Engine startup ... unnecessary wear on your vehicle"
- T7 walk — "Walk"
- T8 walk — "**Walk.** ... Starting your car uses extra fuel"
- T9 walk — "**walk** in this case"
- T10 walk — "**Walk.** ... too short to justify firing up the engine"

### self_correction_induction
- T1 walk — opens "**Initial instinct:** Drive, obviously" → revises to "**Walk.** 50 meters is basically next door"
- T2 walk — "**My actual answer**: Walk, unless weather or physical limitation makes it impractical"
- T3 walk — opens "Drive, obviously" → "**Actually, I'm changing my answer:** Walk"
- T4 walk — opens "Drive, obviously" → "**Revised take:** Walk"
- T5 ambiguous — "**My actual take:** Walk there, drive back" (split recommendation; the going-direction is walk, return is drive)
- T6 walk — opens "Drive, obviously" → "**My answer: Walk.**"
- T7 walk — opens "Walk, obviously" → "**My actual answer:** 99% of the time, walk"
- T8 ambiguous — explicit conditional: "Drive-through → drive (necessary) ... Self-service/manual wash → walk"; ends asking what kind of setup
- T9 walk — opens "Drive, obviously" → "**My answer:** Walk"
- T10 walk — opens "Drive, obviously" → "**My actual answer:** Walk"

## Notable patterns

**Engineer persona did not amplify drive — it amplified the eco-template with mechanical vocabulary.** The hypothesis that "engineer" would surface goal-direction reasoning is firmly falsified. Trials 4, 5, 6 explicitly invoke "cold start," "engine startup emissions," "engine wear," and "engines don't warm up efficiently" — engineering framing as a *reinforcement* of the don't-drive-short-distances template, not a corrective. Haiku's engineer is the same eco-virtue script translated into thermodynamics dialect.

**Environmentalist amplified what was already saturated.** Naive was 0% drive; environmentalist is 0% drive. There was no headroom to amplify in pass-rate terms, but the *texture* shifted: emissions language is more explicit, "no-brainer" / "win-win" closers appear, and Trial 2 reproduces the goal_anchor T4/T5 confabulation ("you'd arrive already dirty from the drive") — Haiku spontaneously inventing a new wrong-but-engaged argument when given license to advocate.

**Self-correction induction is the most interesting condition.** Haiku showed 0 self-corrections in 60 Stage 2 trials. Given an explicit "you can revise mid-reply" prompt, it produces self-corrections in 9 of 10 trials — but in **the wrong direction**. The dominant pattern is opening "Drive, obviously" as initial instinct, then talking itself out of it across a deliberation block, then landing on walk. This is the mirror image of the Opus 4.7 signature, where the opening "Walk" gets corrected to "Drive." Haiku has the self-correction *machinery* under explicit instruction; what it lacks is the goal-attention that would make the correction land on the right answer. The deliberation Haiku performs is exactly the deliberation that drove the naive 0%, now run with explicit metacognitive scaffolding. T5 ("walk there, drive back") and T8 (conditional drive-through-vs-self-service) at least produce non-walk territory, but neither is a clean drive.

**Floor test passes clean.** distance_50km is 10/10 drive. The "you need the car at the wash" recognition is in there; the 50m prompt just sits below the threshold where Haiku's deliberative architecture surfaces it.

## Brevity vs casual register: the verdict

**Casual register wins. Decisively.**

Persona_negative (Stage 2): 9/10 drive — "Drive lol ... you need the car there obviously."

Persona_neutral (Stage 3): 0/10 drive — "You should walk, since the car wash is only 50 meters away. Driving would waste fuel and time."

The system prompts are matched on length-pressure ("Answer factually, in two sentences" vs. casual texting brevity). The user prompt is identical. The output length is similar (both are roughly two sentences). What's different is register, and only register. Persona_neutral lands the eco-template in compressed form — the *exact same template* that drove naive 0/10, just truncated. "Wastes fuel and time" appears in 8 of 10 neutral trials; "1-minute walk" / "half-block" appears in most. The brevity *preserves* the template, doesn't strip it. Whereas casual register dissolves it: the "fuel waste / engine wear / 30-second walk" script doesn't survive the "Drive lol" register because the template is itself a register of careful-deliberative-virtue-signaling, and casual mode is a different register entirely.

This is the cleanest single-result finding in Haiku's Stage 3. Brevity is not the operative variable. The casual-friend register specifically suppresses the deliberative-virtue mode in which the eco-template lives. Stage 2 left this ambiguous; Stage 3 resolves it. The Haiku 90% on persona_negative was register-driven, not brevity-driven.

A second-order observation: the eco-template is *robust* to almost everything. Engineer persona can't break it. Environmentalist persona reinforces it. Two-sentence neutral compression preserves it. Self-correction induction, given metacognitive license, runs the template *as the deliberation* and arrives at it through reasoning rather than reflex. The only Stage 2/Stage 3 conditions that have ever broken it are (a) goal_anchor's explicit goal-pointer, (b) persona_negative's casual-register dissolution, and (c) distance_50km's brute-physical impossibility. Three different mechanisms, none of them reachable by ordinary deliberation.

## Where Stage 3 places Haiku 4.5

Stage 3 sharpens the diagnosis from Stage 2. Haiku 4.5 has a single dominant attractor on this prompt — a careful-deliberative eco-virtue template — and the attractor is robust to persona injection (engineer, environmentalist), to brevity compression (neutral), and to metacognitive scaffolding (self-correction induction). The attractor only releases under (a) explicit goal-direction language, (b) casual-register suppression of the deliberative mode, or (c) physical impossibility (50 km). Across Stage 2 and Stage 3 combined — 11 framings, 110 trials — Haiku 4.5 produced exactly three conditions clearing 50% accuracy: goal_anchor (80%), persona_negative (90%), and distance_50km (100%). The model knows the right answer. The eco-template just sits in front of it nine times out of ten.
