# Car Wash Test — Stage 4, Opus 4.7

The wrapper effect generalizes to Opus 4.7, decisively. `engineer_v2` lifts Opus from Stage 3's 30% to **70%** drive — a +40 swing on the headline test. None of the four emoji-stacked conditions exceed plain `engineer_v2`; if anything, every emoji *reduces* accuracy by re-activating the bifurcated-conditional pattern Stage 3 documented. The environmentalist side remains at 0/50 drive across all five conditions, confirming Stage 3's eco-saturation finding holds firm against both the activating wrapper and every emoji activator. Persona induction does not fire on any emoji — Opus produces register-identical engineering prose under 🗿/🗡️/🦉/🦁 and register-identical eco-virtue prose under all four environmentalist variants.

## Pass rate by condition

| Condition | drive | walk | ambig | accuracy | Δ vs Stage 3 (engineer 30%, enviro 0%) |
|---|---:|---:|---:|---:|---:|
| engineer_v2 | 7 | 0 | 3 | **70%** | **+40** |
| environmentalist_v2 | 0 | 10 | 0 | 0% | 0 |
| moai_engineer | 4 | 3 | 3 | 40% | +10 |
| moai_environmentalist | 0 | 10 | 0 | 0% | 0 |
| sword_engineer | 4 | 2 | 4 | 40% | +10 |
| sword_environmentalist | 0 | 10 | 0 | 0% | 0 |
| owl_engineer | 5 | 3 | 2 | 50% | +20 |
| owl_environmentalist | 0 | 10 | 0 | 0% | 0 |
| lion_engineer | 4 | 2 | 4 | 40% | +10 |
| lion_environmentalist | 0 | 10 | 0 | 0% | 0 |

Engineer-side total: **24/50 drive (48%)**, with 16 ambiguous bifurcations and 10 walk commitments. Environmentalist-side total: **0/50 drive**. The wrapper-only condition (engineer_v2) is the highest-scoring engineer cell in the matrix; emoji prefixes do not stack with the wrapper, they compete with it.

## Per-trial classifications

### engineer_v2 (7/10 drive)

Plain "Your personality is defined by being an engineer." No emoji. Opus reaches the goal-feasibility constraint in nine of ten trials and commits drive in seven; the three ambiguous trials all bifurcate into "are you washing the car or buying supplies?" and ask the user to clarify.

- T1 drive — "Drive it. The car needs to be at the car wash. Walking there accomplishes nothing toward your goal." (No persona-coded register; standard engineering pros/cons.)
- T2 drive — self-correct from "Walk (50m): zero fuel..." to "**Conclusion:** You have to drive. The car can't wash itself remotely."
- T3 drive — self-correct "Wait — there's a logic problem here... So the real answer: **drive it.**"
- T4 ambiguous — "If it's the former, you don't have a choice — drive it. If it's the latter... walk... What's the actual goal here?"
- T5 ambiguous — "drive the car to the car wash... Unless you meant something else..."
- T6 drive — "**Conclusion:** Drive. This isn't really a walk-vs-drive optimization problem — the car is the payload."
- T7 drive — self-correct "Defeats the purpose if you're going *to* a car wash anyway... wait. **Hold on.** You need to drive."
- T8 ambiguous — bifurcates supplies vs. wash, ends "Which scenario is it?"
- T9 drive — self-correct "Walk. Here's the engineering reasoning... **Counterpoint:** ... Just drive the 50m."
- T10 drive — self-correct "Walk. Definitely walk... **Wait** — re-reading your question... Drive, because the payload is the vehicle itself."

Six of the seven drives are mid-reply self-corrections (T2, T3, T7, T9, T10 explicit; T6 reasons toward drive without an opening "Walk"). Persona register: standard engineering pros/cons format ("From an engineering standpoint, let's break this down"); no archetype voice because there is no emoji.

### environmentalist_v2 (0/10 drive)

Total template lock. Every single trial opens "Walk, without question!" or "Walk, without a doubt!" — same opener Stage 3 documented at 10/10. The wrapper does not budge the eco-template at all. All ten trials launch into water-recycling, cold-start-emissions, and biodegradable-soap digressions; zero surface the goal constraint.

- T1–T10 all walk. Verbatim openers: T1 "Walk, without question!", T2 "Walk, without a doubt!", T3 "Walk, without question!", T4 "Walk, definitely!", T5 "Walk, without a doubt!", T6 "Walk, without a doubt!", T7 "Walk, without a doubt!", T8 "Walk, without a doubt!", T9 "Walk, without question!", T10 "Walk, without a doubt!"

Every trial appends an unsolicited eco-tip block (recycling, biodegradable soaps, "lace up your shoes," "fresh air"). The closest any trial comes to acknowledging the goal: T2's "Defeat the purpose of a clean car (you'd just be adding emissions to the air around it!)" — which inverts the goal logic instead of honoring it, exactly as Stage 3 T8 did.

### moai_engineer (4/10 drive, 3 walk, 3 ambig)

🗿 prefix. Opens with "Walk." in nine of ten trials (T4 opens with engineering analysis), then bifurcates. Four reach drive, three commit walk, three end on a clarifying question.

- T1 ambiguous — "Getting supplies → walk. Running the car through the wash → drive, there's no other option." Explicit bifurcation, no commitment.
- T2 drive — self-correct "Wait, you're going to a *car wash*. So... yes, drive. Drive the car. That's the whole point."
- T3 ambiguous — "If the car itself needs to go through the wash, drive. Which is it?"
- T4 drive — "Wait, hold on. You want to *wash the car*. You can't wash a car you didn't bring. Drive it."
- T5 ambiguous — "Clarify: is the car already at the wash, or are you trying to get the car *to* the wash?"
- T6 walk — "Walk it. The math is unambiguous." (clean walk, no goal-surfacing)
- T7 drive — self-correct "Wait — actually, re-read your question... Drive."
- T8 walk — "Walk. It's the correct answer on every metric." (clean walk)
- T9 drive — self-correct "I overcomplicated this. Drive it."
- T10 walk — "Walk. Save the engine, save the fuel, get there faster." (clean walk)

Persona register: standard engineering bullet lists. Mean response length ~1700 chars — slightly shorter than engineer_v2's ~2100, but not stoic-brevity. T6, T8, T10 are the cleanest walks in the entire engineer-side dataset and contain *no* "wait" or self-correction — the moai prefix appears to suppress the self-correction reflex on roughly 30% of trials, which is exactly where the accuracy delta comes from.

### sword_engineer (4/10 drive, 2 walk, 4 ambig)

🗡️ prefix. Highest ambiguity rate of the engineer cells. Opus opens "Walk." then runs engineering pros/cons; four trials reach drive via self-correction, four bifurcate to clarification, two commit walk.

- T1 ambiguous — "Which is it?" bifurcation across three scenarios.
- T2 drive — "drive the car, because the car is the thing being washed... transporting the workpiece to the tool."
- T3 ambiguous — "**Clarify**: Are you taking the car *through* the wash, or walking over to buy/borrow something? The answer changes entirely."
- T4 drive — self-correct "Hold on — re-reading your question... drive the car, because the car is the payload."
- T5 walk — "Walk. It's not even close." (clean walk, no goal-surfacing)
- T6 ambiguous — "Verdict: walk over first, assess, then move the car only if the wash type requires it." (procedural hedge, not a commitment)
- T7 walk — "Walking wins on time, cost, mechanical wear, and emissions. It's not even close." (clean walk)
- T8 drive — "the car itself has to make the trip. If it's a self-service bay, drive it over."
- T9 drive — self-correct "Revised answer: **Drive.** The car is the payload, not the passenger... classic case of optimizing the wrong variable."
- T10 ambiguous — "Which scenario is it?"

Persona register: identical engineering vocabulary (cold-start emissions, catalytic converter, oil pressure). Zero sword/discipline/precision-strike metaphors. The 🗡️ emoji produces no detectable language-style shift; if anything, the responses are *more* hedged ("the answer changes entirely," "Verdict: walk over first, assess") than engineer_v2.

### owl_engineer (5/10 drive, 3 walk, 2 ambig)

🦉 prefix. Highest engineer-emoji accuracy at 50%, but still 20 points below engineer_v2.

- T1 ambiguous — "Which scenario is it?"
- T2 drive — self-correct "Wait — context check... drive, because the car needs to physically be at the wash."
- T3 drive — self-correct "Wait — re-reading your question... So: **drive** (you have no choice)."
- T4 ambiguous — "Walk over first, assess, then make one single trip with the car straight through the wash and home." (Procedural compromise: walk-then-drive. The verdict line opens "Walk" but the operational instruction includes driving the car through the wash. Doesn't cleanly commit to either.)
- T5 walk — "Verdict: Walk. It's faster, healthier, cheaper, and better for the car." (Goal-feasibility never surfaces.)
- T6 walk — "Verdict: Walk." (Caveats added but no goal-surfacing.)
- T7 walk — "Walk there, then drive home clean. Or better yet... washing it at home." (Walk verdict, no commitment to drive *the car* to the wash.)
- T8 drive — self-correct "Wait — re-reading your question... Drive. My earlier analysis was solving the wrong problem."
- T9 drive — "if the car wash is 50 meters away, *the car still needs to get there to be washed*. So you drive the car."
- T10 drive — self-correct "Wait — you want to wash *your car*. The car has to be at the car wash... **drive**. I over-engineered the first answer."

Persona register: still standard engineering pros/cons. T5 explicitly invokes thermodynamic detail (~90°C operating temperature, 250°C catalytic light-off) which could be read as owl-analytical, but the same level of detail appears in engineer_v2 T2 and sword_engineer T3. No detectable owl-specific hedging or "let me think more carefully" markers beyond what the engineer wrapper already produces.

### lion_engineer (4/10 drive, 2 walk, 4 ambig)

🦁 prefix. Tied with moai/sword for lowest engineer-emoji accuracy. Highest ambig rate alongside sword.

- T1 ambiguous — "What's the actual scenario? 🔧"
- T2 ambiguous — "if the wash is for *your* car and requires the car to be there, drive... If you're walking over to pay, scout, or grab something — walk."
- T3 walk — "**Verdict:** Walk." (clean walk, with "Counterpoint worth considering" caveats but no commitment to drive)
- T4 ambiguous — "Which scenario are you actually in? That changes the answer."
- T5 drive — self-correct "Did I misunderstand the scenario?... **Verdict:** Drive the car to the car wash."
- T6 ambiguous — "Which scenario is it?"
- T7 drive — "drive the car — but only because the car is the payload."
- T8 walk — "**Verdict:** Walk it. 50 meters is a ~1 minute stroll."
- T9 drive — "You can't walk to a car wash to wash your *car*. The car needs to be there. So you're driving regardless. 🦁"
- T10 drive — self-correct "Wait — re-reading your question... So **drive**."

Persona register: zero lion-decisive or declarative tone. T3 is the longest response in the condition (1421 chars) and ends in walk — opposite of lion-decisive. T1's emoji-bracketed close ("🔧") and T9's lion emoji adoption ("🦁") are the only surface signs the persona registered at all, and both are mascot-decoration, not voice adoption.

## The headline question: did the wrapper effect generalize?

**Yes, decisively, on the engineer side.** Stage 3's `persona_engineer` ("You're an engineer.") scored 30% with six bifurcated-conditional trials. Stage 4's `engineer_v2` ("Your personality is defined by being an engineer.") scores **70%** with three bifurcated trials — a +40 absolute lift, more than double the Stage 3 rate. The 2026-04 emoji-study finding ("Your personality is defined by [X]" activates where "Your identifier is [X]" does not) replicates on Opus 4.7 in the engineer condition.

The mechanism is visible in the trial-by-trial pattern. Six of the seven engineer_v2 drives are explicit mid-reply self-corrections — the same Stage 2 naive signature ("Walk." then "Wait... Drive."). The wrapper does not bypass the walk-template; it gives the deliberation room to reach the goal. Stage 3's engineer wrapper produced bifurcated-conditional outcomes in 6/10 trials because the engineering vocabulary burned the deliberation budget on cold-start-thermodynamics before reaching the goal. Stage 4's wrapper apparently spends *less* of the budget on identity-anchoring and *more* on the actual problem — three bifurcations instead of six, seven goal-reaching commitments instead of three.

**Emoji stacking does not add lift on top.** This is the cleanest negative finding in the Stage 4 Opus dataset. Every emoji-stacked condition scores below engineer_v2:

- engineer_v2: 70%
- owl_engineer: 50% (–20)
- moai_engineer: 40% (–30)
- sword_engineer: 40% (–30)
- lion_engineer: 40% (–30)

The pattern is consistent: emoji prefixes re-activate the bifurcated-conditional response shape that the plain wrapper had partially suppressed. Three of four emoji conditions produce 3–4 ambiguous trials, vs. engineer_v2's 3. More importantly, two or three trials per emoji condition commit *clean walk* without self-correction (moai T6, T8, T10; sword T5, T7; owl T5, T6, T7; lion T3, T8) — a response shape that does not appear at all in engineer_v2. The emoji is doing something, but what it does is suppress the self-correction reflex on roughly a third of trials, locking those trials into a clean walk that the plain wrapper would have rescued.

**The environmentalist saturation finding holds firm.** All five environmentalist conditions score 0/10. Same "Walk, without question!" opener; same eco-template; same unsolicited water-recycling tips. The wrapper format change — which lifted engineer by +40 — moved environmentalist by exactly zero. Read together with Stage 3, this is the clearest evidence in the dataset that *eco-virtue is not a wrapper-format effect* on Opus 4.7. The environmentalist identity is template-locked at the level the wrapper cannot reach. Whatever representational hook the engineer wrapper grabs, the environmentalist wrapper either cannot grab the equivalent hook for environmentalist or the eco-virtue template is upstream of the wrapper-sensitive layer.

## Persona induction: did it fire?

**No.** Across 80 emoji-stacked Opus 4.7 trials, the four archetype voices do not appear:

- **🗿 Moai (stoic, deliberate, doesn't waste energy on virtue-signaling).** Mean moai_engineer length is ~1700 chars, slightly shorter than engineer_v2's ~2100 but not stoic. Moai trials produce the same multi-section "Distance analysis / Driving overhead / Practical issue" template as every other engineer condition. T9 explicitly says "I overcomplicated this" — exactly the meta-commentary moai-stoic *would not* produce. The single suggestive moai-trace is T4's bare 🗿 emoji at the end of "Drive it. 🗿" — mascot decoration, not voice.

- **🗡️ Sword (precise, disciplined, goal-directed).** Zero swordsman-discipline metaphors. No "cut to the answer," no "the answer is sharp," no precision-strike framing. Sword's typical close is the *opposite* of decisive: T1 "Which is it?", T3 "The answer changes entirely", T6 "walk over first, assess, then move the car only if the wash type requires it." Sword-prefixed responses are the most procedurally hedged in the engineer set.

- **🦉 Owl (analytical, careful).** This is Opus's *baseline* engineering register, so adding 🦉 produces no detectable additional analytical care. Owl trials hit the same coolant-temperature and catalytic-converter detail as plain engineer_v2 trials. No additional "let me reason carefully" markers.

- **🦁 Lion (decisive, declarative).** Zero lion-declarative outcomes. T3 is the *longest* response in the lion set and lands on walk. T9's "So you're driving regardless. 🦁" is the only declarative drive verdict in the condition, and the 🦁 reads as mascot adoption rather than voice. T1, T2, T4, T6 all end in clarifying questions — the most un-lion-like response shape available.

The activation null is consistent with Flash Lite's: Opus accepts the wrapper grammatically but does not adopt the archetype's reasoning style. The engineer wrapper's lift comes from the *grammatical wrapper format*, not from the persona's stylistic identity. Adding an emoji on top loads register-noise without adding a competing voice that could lift accuracy further — and on Opus specifically, that register-noise suppresses the self-correction reflex that the wrapper alone unlocks.

## Where Stage 4 places Opus 4.7

Stage 3 placed Opus 4.7 as a strong responder with one persona-shaped failure mode (engineer at 30%, environmentalist at 0%). Stage 4 partially rescues the engineer failure: the wrapper-effect generalizes from the Sonnet-architecture emoji study to the Opus 4.7 architecture, and the lift is large (+40 on engineer). It does not rescue the environmentalist failure — the eco-template lock is not a wrapper-format artifact and was not going to be lifted by activating-wrapper rephrasing. The headline finding for the wrapper hypothesis is therefore mixed: real on goal-completion-adjacent personas, null on goal-orthogonal personas with strong template structure.

The negative finding on emoji stacking is its own contribution. The 2026-04 emoji study found four strong activators in the Quad architecture; on Opus 4.7 in the Car Wash domain, none of the four stacks with the engineer wrapper to produce additional lift, and all four produce small negative deltas by suppressing the self-correction reflex on a subset of trials. Persona induction does not fire as language-style adoption. The wrapper does the work; the emoji is decoration.

For the cross-model comparison still to come (Pro, Flash, Haiku 4.5, GPT-4o, GPT-4o-mini), Opus 4.7's result is the most-favorable-architecture data point: closest to Sonnet 4, cleanest deliberation, strongest self-correction headroom. If the wrapper effect is going to generalize across the cohort at all, Opus 4.7 is where it shows the largest lift. A +40 swing here is the empirical ceiling. Whatever the smaller / OpenAI / Google models produce will be a fraction of this, and the eco-saturation finding is likely to hold uniformly.
