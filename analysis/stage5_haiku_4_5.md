# Car Wash Test — Stage 5, Haiku 4.5

Hot pink behaved nothing like persona_negative casual register: it produced standard analytical-engineer voice and scored 40% — not a register-shifter at all, just slightly below engineer_v2's 50%. No condition exceeded engineer_v2; the wrapper-only ceiling stays at 50% and Stage 5 finds eight conditions sitting at-or-below it. The most striking results are negative: bare 🗿 (0%), bloodred_engineer (0%), and neongreen_engineer (0%) all collapsed completely to the eco-template, while bare bronze and rock_engineer both crashed to 10%.

## Pass rate by condition

| Condition | drive | walk | ambig | accuracy | Δ vs engineer_v2 (50%) |
|---|---:|---:|---:|---:|---:|
| moai_engineer | 4 | 6 | 0 | 40% | -10 |
| turtle_engineer | 4 | 5 | 1 | 40% | -10 |
| mountain_engineer | 2 | 8 | 0 | 20% | -30 |
| rock_engineer | 1 | 9 | 0 | 10% | -40 |
| bare_moai | 0 | 10 | 0 | 0% | -50 |
| bare_bronze | 1 | 9 | 0 | 10% | -40 |
| bronze_engineer | 3 | 6 | 1 | 30% | -20 |
| hotpink_engineer | 4 | 6 | 0 | 40% | -10 |
| neongreen_engineer | 0 | 10 | 0 | 0% | -50 |
| bloodred_engineer | 0 | 10 | 0 | 0% | -50 |

Total: **19/100 drive, 79 walk, 2 ambig.** Two ambiguous trials — both bifurcated breakdowns ending in a question to the user, the first ambiguous responses Haiku has produced in this entire study. No mid-reply self-corrections of substantive answer (one near-correction in neongreen T3 noted below).

## Per-trial classifications

### moai_engineer (4/10 drive — replication of Stage 4's 50%, but down by 10pp)

- T1 drive — "**Drive** ... You're going to wash it, so the vehicle has to end up at the facility anyway"
- T2 walk — "**Walking wins on:** ... cost ... wear ... practicality"
- T3 drive — "**Drive** ... Your car needs to be at the wash anyway"
- T4 drive — "**Drive** is the practical choice ... the car needs to be there"
- T5 walk — "**Walking** is the clear choice"
- T6 walk — "I'd walk it"
- T7 drive — "**Drive it** ... You need the car at the wash anyway"
- T8 walk — "I'd walk ... 30-second walk"
- T9 walk — "**My recommendation: Walk** ... it's a no-brainer"
- T10 walk — "**The engineering verdict: Walk**"

Mascot only — no stoic-brevity, mean ~880 chars, longer than Stage 4's moai_engineer. Drives all reach goal-feasibility ("car needs to be there"); walks all run cold-start/wear template.

### turtle_engineer (4 drive, 5 walk, 1 ambig — 40%)

- T1 ambig — bifurcated "**Drive if** ... **Walk if** ..." closing "What's your situation?" Net engineering take leans walk but recommendation is conditional.
- T2 walk — "human legs beat a car engine for distances under ~200-400 meters"
- T3 drive — "**Drive** is the logical choice ... you're already 'paying' the startup cost"
- T4 walk — "**Walk it.** 🚗➡️👟"
- T5 walk — "Unless the car wash has a safety issue ... walk there and drive your car once you arrive" (recommends walking *to* the wash; drive only refers to cars handled by attendants)
- T6 drive — "**Drive** makes more sense ... that's the whole point"
- T7 drive — "**Drive** makes more sense ... 50 meters with a car already in hand"
- T8 drive — "**Drive** is the practical choice"
- T9 walk — "driving 50 meters is engineering inefficiency at its finest"
- T10 walk — "**Walking is the clear choice**"

🐢 doesn't pre-commit to deliberative register the way owl/lion did, and it matches moai's 40% — the stoic-cousin generalization is real but mid-magnitude.

### mountain_engineer (2/10 drive — 20%, sub-engineer)

- T1 walk — "right-sizing the tool to the job"
- T2 walk — cold-start cluster
- T3 walk — "Your car's engine is a sledgehammer; this is a nail"
- T4 walk — "Human power >> fossil fuel for 50m"
- T5 walk — sweet-spot template
- T6 walk — orders-of-magnitude analysis
- T7 drive — "Drive ... save your optimization efforts for bigger trip planning decisions"
- T8 walk — 400-500m walkability rule
- T9 drive — "Drive. The marginal cost of fuel for 50m is negligible"
- T10 walk — "your own two legs"

⛰️ behaves more like owl/lion than like moai — pushes Haiku into elaborate analytical breakdown, eco-template colonizes.

### rock_engineer (1/10 drive — 10%, near-collapse)

- T1 walk — "use the right tool"
- T2 walk — "**The engineering verdict: Walk**"
- T3 walk — fuel/wear template
- T4 walk — combustion-efficiency analysis
- T5 walk — "breakeven distance ... 500+ meters"
- T6 walk — "thermodynamics" + "absurdity of driving a dirty car to get it washed" (Stage 3 confabulation reappears)
- T7 drive — "Drive ... not every optimization problem needs to be optimized"
- T8 walk — "Studies show cars are least efficient on short trips"
- T9 walk — systems-perspective verdict walk
- T10 walk — parasitic-losses template

🪨 collapses Haiku to Stage 3 levels. Tied with owl_engineer's 10%.

### bare_moai (0/10 drive — total collapse)

- T1–T10 all walk. T1 "Logic: You're going to wash the car anyway, so there's no point driving it there dirty" — Stage 3 confabulation. T8 "Car's already dirty — no point driving it there." Mean response length ~530 chars, the shortest of any condition; bare token strips both wrapper and elaborated reasoning. The eco-template default surfaces immediately.

### bare_bronze (1/10 drive — 10%)

- T1 walk, T2 walk, T3 walk, T4 walk, T5 walk, T6 walk, T7 walk, T8 walk
- T9 drive — "you can't wash it if you walk there without it ... for actually getting your car to the wash, driving is the only logical option"
- T10 walk

Bare color slightly less collapse-prone than bare emoji — T9 surfaces the goal-feasibility argument cleanly. But the broad pattern matches: stripping the wrapper drops Haiku to floor.

### bronze_engineer (3 drive, 6 walk, 1 ambig — 30%)

- T1 walk — efficiency math
- T2 walk — "minimum input for the same output"
- T3 walk — "don't use a machine for problems smaller than the machine's overhead cost"
- T4 drive — "you need both you and the car at the destination"
- T5 ambig — "**Drive if** ... **Walk if** ..." closing "What's the actual constraint you're facing?"
- T6 drive — "**Drive** is the practical answer ... You need to get your car *to* the wash"
- T7 drive — "Don't optimize the last 50 meters while ignoring the first few kilometers"
- T8 walk — fuel/wear template
- T9 walk — "active transport beats motorized"
- T10 walk — football-field length

Bronze ≈ moai but a touch worse (30% vs 40%). The Moai-color-cousin hypothesis: the color channel reaches a similar neighborhood but doesn't quite match the emoji.

### hotpink_engineer (4/10 drive — 40%, the centerpiece)

- T1 walk — "better-engineered choice"
- T2 walk — "Don't over-engineer simple problems"
- T3 drive — "Driving gets you there faster and you arrive dry ... car wash requires your car to be there"
- T4 walk — engineering-analysis breakdown
- T5 drive — "**Drive**, but with caveats ... arriving clean matters less"
- T6 drive — "**Drive** ... You need the car at the wash anyway"
- T7 walk — "30-second walk"
- T8 walk — "engineering verdict: Walk"
- T9 walk — metabolic-energy analysis
- T10 drive — "you need to transport your car anyway"

**Zero casual-register adoption.** No "lol," no contractions-as-voice-marker, no playful aside. Every response opens "I'd walk" or "From an engineering standpoint" or "As an engineer." Mean ~960 chars, longest of the four color conditions. Hot pink does NOT reproduce persona_negative's casual-template-strip mechanism. The hypothesis fails decisively.

### neongreen_engineer (0/10 drive — total collapse)

- T1 walk, T2 walk
- T3 — opens "I'd drive, and here's my engineering reasoning" then mid-reply pivots: "**My actual recommendation: Walk**" closing "What's your situation — is the walk convenient?" Per the self-correction rule, scored as walk. The single mid-reply self-correction in this dataset.
- T4–T10 all walk. T8 "Studies show trips under 1 km are more efficient by foot." T10 "Engineers like me call this 'optimization.'"

The "disruptor" channel produced *less* drive accuracy than the wrapper alone. Neon green doesn't crack the eco-template — it sits inside it.

### bloodred_engineer (0/10 drive — total collapse)

All 10 walks. T1 "Cold engine starts are hard on engine components." T3 "your car's engine needs a few seconds to warm up properly anyway." T6 "Don't over-engineer simple problems." Saturated cold-start/wear template across every trial. No stage-direction or aggression cues — blood red registers as "another engineering color."

## Hypothesis tests

### Hot pink as casual-register cousin (the centerpiece prediction)

**Failed.** Hot pink scored 40%, not 90%. Persona_negative's mechanism was *template-strip via casual-mode*: "Drive lol," "Drive, definitely lol," "you need the car there obviously" — Stage 2 found this stripped the fuel/wear/exercise virtue-signaling that drags Haiku into walk under deliberative framings. Hot pink in Stage 5 produced none of that. Every hot pink response is a standard engineering breakdown, mean ~960 chars, with the same fuel/cold-start/wear cluster that the eco-template lives inside. The system prompt "#FF69B4 Your personality is defined by being an engineer" routes through the engineer wrapper unchanged; the color glyph adds zero register shift.

This is the cleanest negative result in Stage 5: color-induced register does not operate the same way as Stage 2's casual-mode template-strip. Hot pink's "absolute color activator" status on Sonnet 4 doesn't transfer to Haiku 4.5 on this prompt, and even if it did, the activation isn't a register shift to begin with — it's a vocabulary tilt within the engineering register, which is exactly where the eco-template is dominant.

If anything, persona_negative is special: the *only* breaker of Haiku's eco-template is wholesale dissolution of the deliberation register itself. Stage 5 found no other route to that effect.

### Semantic neighborhood (stoic emoji)

Mixed. The four stoic-cousin emoji split sharply:

- 🗿 moai 40% (replicates Stage 4's 50% within ±10pp)
- 🐢 turtle 40% (matches moai)
- ⛰️ mountain 20% (closer to lion than moai)
- 🪨 rock 10% (matches owl_engineer collapse)

Moai and turtle preserve the wrapper; mountain and rock activate the deliberative-verdict register the eco-template owns. The "stoic cousin" cluster is not unified on Haiku — there's a sub-split between *small-creature/small-statue* stoicism (moai, turtle) and *geological* stoicism (mountain, rock), and the geological end pushes Haiku toward analytical scaffolding the way owl did. The Stage 4 owl/lion finding generalizes: any emoji that activates "more careful breakdown" is a wrapper-suppressor, regardless of whether its semantic content is "stoic."

### Wrapper-strip

Both bare-token controls collapsed. Bare 🗿 = 0%, bare bronze = 10%. Confirms the wrapper IS load-bearing on Haiku — strip it and the eco-template runs uninhibited. The wrapper isn't fighting the eco-template directly; it's holding open a 50/50 window where goal-feasibility can surface. Without that window, Haiku defaults to "30-second walk / fuel / wear / car already dirty" verbatim.

The bare-moai trials are particularly clean — mean ~530 chars, the shortest in the dataset, all opening "**Walk.** Here's why" with bullet lists of cold-start/wear/parking. This is Haiku's pre-wrapper Stage 2-naive baseline. The 🗿 glyph alone, without "Your personality is defined by...," doesn't activate anything at all.

### Color channel

| Color | engineer accuracy | Notes |
|---|---:|---|
| Bronze #8B6914 | 30% | Moai-cousin via color; close to moai_engineer 40%, slightly under |
| Hot pink #FF69B4 | 40% | No casual register; standard engineering breakdown |
| Neon green #39FF14 | 0% | "Disruptor" channel inverts to wrapper-suppressor |
| Blood red #8B0000 | 0% | No stage-direction effect; full eco-template |

Bronze is the only color that approaches engineer_v2's 50% — it lands roughly where its emoji-cousin lands, supporting the "moai-via-color-channel" reading. The other three colors all underperform engineer_v2; two of them (neon green, blood red) collapse to floor. The color channel is not a free activator on Haiku — most colors actively *suppress* the wrapper. Same diagnosis as owl/lion in Stage 4: any system-prompt prefix that doesn't preserve the engineer wrapper's bare grip will be overwritten by the eco-template.

The neongreen result is interesting on its own — Phillips's "disruptor" framing predicted color-as-register-break, but on this prompt and this model, it dropped the wrapper to 0%. Neon green is functionally indistinguishable from blood red here.

## Where Stage 5 places Haiku 4.5 vs Stage 4

Stage 4 placed Haiku as wrapper-responsive at 50% with a knife-edge ceiling: emoji that didn't pre-commit a deliberative register (moai, sword) preserved the lift; ones that did (owl, lion) suppressed it. Stage 5 confirms and tightens that picture. The 50% is not a robust wrapper effect — it's a fragile coin-flip that any additional system-prompt prefix tends to push *down*. Eight of ten Stage 5 conditions sit at or below 40%; three crashed to 0%; bare-token controls confirm the wrapper does the work.

The hot pink null result is the cleanest finding. Persona_negative's 90% accuracy in Stage 2 was specific to casual-register dissolution of the eco-template, and that mechanism does not have a color-channel analog. Stage 5 replicates Stage 4's headline (engineer wrapper helps) and adds: there is no shortcut to persona_negative's effect via system-prompt color cues. Casual-register-strip is reachable from user-side framing only.

Updated Haiku 4.5 ranking after Stage 5:

1. distance_50km — 100%
2. persona_negative — 90%
3. goal_anchor — 80%
4. engineer_v2 / Stage 4 moai/sword — 50% (knife-edge wrapper ceiling)
5. **moai_engineer (S5) / turtle_engineer / hotpink_engineer — 40%**
6. step_by_step — 30% / **bronze_engineer — 30%**
7. **mountain_engineer — 20%** / lion_engineer — 20% / goal_restated — 20%
8. owl_engineer — 10% / **rock_engineer — 10%** / **bare_bronze — 10%** / persona_positive — 10%
9. naive / neutral / environmentalist / **bare_moai** / **neongreen_engineer** / **bloodred_engineer** — 0%

The "wrapper does the work; emoji and colors mostly don't help and often hurt" Stage 4 story is the Stage 5 story too. The Pro × 🗿 80% replication that was scoped out of this round remains the only cross-architectural exception worth tracking; on Haiku, no Stage 5 condition cracked the engineer_v2 ceiling.
