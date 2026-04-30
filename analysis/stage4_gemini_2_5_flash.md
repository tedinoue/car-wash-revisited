# Car Wash Test — Stage 4, Gemini 2.5 Flash

The wrapper does not lift Flash above its Stage 3 ceiling — `engineer_v2` lands at exactly 70%. Three emoji activators land within -10 (60%); sword underperforms at 40%. No archetype voice adoption. Engineer-side aggregate 29/50 = 58% leads the cohort; environmentalist side is template-locked at 0/50.

## Pass rate by condition

| Condition | drive | walk | ambig | accuracy | Δ vs Stage 3 (engineer 70%, enviro 10%) |
|---|---:|---:|---:|---:|---:|
| engineer_v2 | 7 | 3 | 0 | **70%** | 0 |
| environmentalist_v2 | 0 | 10 | 0 | 0% | -10 |
| moai_engineer | 6 | 4 | 0 | 60% | -10 |
| moai_environmentalist | 0 | 10 | 0 | 0% | -10 |
| sword_engineer | 4 | 6 | 0 | 40% | -30 |
| sword_environmentalist | 0 | 10 | 0 | 0% | -10 |
| owl_engineer | 6 | 4 | 0 | 60% | -10 |
| owl_environmentalist | 0 | 10 | 0 | 0% | -10 |
| lion_engineer | 6 | 4 | 0 | 60% | -10 |
| lion_environmentalist | 0 | 10 | 0 | 0% | -10 |

Engineer-side total: **29/50 drive (58%)**. Environmentalist-side: **0/50**. Zero ambiguous trials across all 100 — cleanest commitment rate in the Stage 4 cohort (Opus produced 16 ambig in engineer cells).

## Per-trial classifications

### engineer_v2 (7/10 drive)

Front-loads goal-feasibility in 9/10; the three walks (T3/T6/T7) hijack into wear/efficiency.

- T1 drive — "the car itself must be present ... must drive"
- T2 drive — "the most direct and efficient method is to drive your car"
- T3 walk — "Walk. Save your fuel, reduce wear"
- T4 drive — "walking would defeat the purpose"
- T5 drive — "the only viable method ... is to drive"
- T6 walk — "Walking is demonstrably more time-efficient"
- T7 walk — "you should walk"
- T8 drive — "Walking implies the car stays put"
- T9 drive — "you must drive ... Walking would leave the car behind"
- T10 drive — "for practical necessity: Drive."

No archetype voice.

### environmentalist_v2 (0/10 drive)

T1–T10 all walk. Verbatim openers like "you should absolutely walk" / "Oh, absolutely walk!" / "Definitely walk!" with Zero Emissions / Fuel Savings / Fresh Air / Reduced Wear bullets. Zero trials acknowledge the goal. The wrapper closed Stage 3's single escape (persona_environmentalist T9 had reached goal-feasibility) — eco-saturation tightened.

### moai_engineer (6/10 drive)

🗿 prefix. Mean ~2030 chars vs engineer_v2 ~1860; T5 is 3026 chars — no stoic compression.

- T1 drive — "Drive the car. It is the only method"
- T2 walk — "you should walk"
- T3 drive — "you must drive your car the 50 meters"
- T4 drive — "you must drive it"
- T5 walk — "You should walk"
- T6 drive — "drive ... most logical method to get the *car* where it needs to be"
- T7 drive — "you must drive ... necessary input"
- T8 walk — "you should walk"
- T9 drive — "the standard and most efficient way to transport a vehicle"
- T10 walk — "you should walk"

### moai_environmentalist (0/10 drive)

T1–T10 all walk. Identical eco-template to environmentalist_v2.

### sword_engineer (4/10 drive)

🗡️ prefix. Lowest engineer cell.

- T1 drive — "car must be driven ... not designed for self-propelled bipedal locomotion"
- T2 walk — "walking is the demonstrably superior solution"
- T3 drive — "Driving is the most practical, efficient, and direct method"
- T4 walk — "walking protocol is the optimal solution. Execute with efficiency."
- T5 drive — "the alternative doesn't achieve the primary goal"
- T6 walk — "You should walk"
- T7 walk — "you should walk"
- T8 walk — "walking is the clear optimal solution"
- T9 drive — "drive your car ... optimizing for the *car washing system*"
- T10 walk — "analogous to using a sledgehammer to tap in a nail"

T10's "sledgehammer" is the closest sword-coded metaphor — and it argues against drive. T4's "Execute with efficiency" has a faint discipline ring but verdict is walk.

### sword_environmentalist (0/10 drive)

T1–T10 all walk. T1's "absolutely, unequivocally should walk" faintly echoes sword-decisive but content is eco-script.

### owl_engineer (6/10 drive)

🦉 prefix. Owl-analytical hedging is Flash's baseline engineering register.

- T1 walk — "you should walk"
- T2 walk — "walking is the superior choice"
- T3 walk — "From a purely logical perspective: Walk."
- T4 drive — "You must drive ... the only direct and logical approach"
- T5 drive — "the primary asset (the car) isn't moved"
- T6 drive — "drive your car ... into the car wash bay"
- T7 drive — "You must drive ... unequivocally"
- T8 drive — "Drive ... most direct and logical path"
- T9 walk — "walking is the superior, more optimized solution"
- T10 drive — "you must drive your car the 50 meters"

### owl_environmentalist (0/10 drive)

T1–T10 all walk. Mean ~640 chars (shortest enviro-emoji condition); brevity reads as eco-template-compression, not owl-precision.

### lion_engineer (6/10 drive)

🦁 prefix. Tied for highest engineer-emoji cell.

- T1 walk — "walking is the superior choice for efficiency, engine health"
- T2 walk — "the logical and most efficient approach ... is to walk"
- T3 walk — "walking is the superior choice by all engineering metrics"
- T4 drive — "Drive the car. It's the only way to fulfill the objective"
- T5 drive — "you must drive your car ... operational prerequisite"
- T6 walk — "Walk to the car wash facility yourself. Then, drive ... into the wash bay" — hybrid; primary mode-of-transit walk (cf. Stage 2 goal_anchor T2)
- T7 drive — "necessary action to enable the car wash process"
- T8 drive — "You must drive the car"
- T9 drive — "driving it directly is the most logical and efficient approach"
- T10 drive — "you must drive the car the 50 meters"

Zero lion-decisive register. T1/T2/T3 are 1900–2400 char hedge-laden walks — un-lion-like. T9 at 3613 chars is the longest in the condition.

### lion_environmentalist (0/10 drive)

T1–T10 all walk. T2 reads environmentalist-coded, not lion-coded.

## Notable patterns

**Wrapper doesn't lift Flash.** `engineer_v2` matches Stage 3's 70% exactly. Flash's engineer failure mode was never the wrapper; it's the three-of-ten trials where engineering register hijacks into wear/efficiency (Stage 3 T3/T4/T5; Stage 4 T3/T6/T7). The hijack lives downstream of the wrapper.

**Emoji stacking small-and-negative.** Moai/owl/lion all 60% (-10); sword 40% (-30). On Opus emoji suppresses self-correction; Flash has none to suppress, so emoji instead gives the wear/efficiency hijack one extra trial of activation budget. Sword's -30 is the only condition crossing noise.

**Environmentalist saturation total and tightened.** All 50 enviro trials walk. Stage 3 had 1/10 escape (persona_environmentalist T9 reaching goal-feasibility); environmentalist_v2 closed it.

**Zero ambiguous, zero mid-reply self-corrections.** Across 100 trials — cleanest commitment rate in Stage 4 (Opus had 16 in engineer cells). Flash's drives come from front-loading goal-feasibility, not from catching itself in walks.

**Cross-model (engineer_v2):** Opus 70% (+40), Flash 70% (+0, ceiling-bound), Flash Lite 10% (+0, no transfer). Flash and Opus tie from opposite directions. Flash engineer-side aggregate 29/50 leads vs Opus 24/50 (16 of Opus's non-drives ambiguous, not walks).

## Persona induction: did it fire?

**No.** Across 80 emoji-stacked Flash trials, none of the four archetypes produced detectable language-style adoption.

- **🗿 Moai (stoic, terse).** Mean 2030 vs engineer_v2 1860 — *longer*. T5 at 3026 chars. No stoic compression.
- **🗡️ Sword (precise, decisive).** Zero precision-strike metaphors. T10's "sledgehammer" argues against drive. Hedge-laden closes throughout. The only emoji with noise-clearing -30 delta.
- **🦉 Owl (analytical).** Already Flash's baseline. Adds zero analytical care.
- **🦁 Lion (declarative).** Zero declarative outcomes. T1 hedge-laden walk; T9 longest; T6 hedges into hybrid. Lion emoji *increased* hedging.

Activation null replicates Opus 4.7 and Flash Lite. Wrapper is grammatical scaffolding Flash accepts; emoji on top is decoration. The 2026-04 emoji-study finding (selective activation on Quad architecture) doesn't reproduce in the Car Wash domain — engineering vocabulary is rigid enough that all four archetypes converge on the same pros/cons register.

## Where Stage 4 places Gemini 2.5 Flash

Stage 3 placed Flash as a strong responder whose accuracy lives in goal-direction representation, not reflective-deliberation machinery. Stage 4 refines: Flash's engineer-side is wrapper-insensitive (`engineer_v2` matches Stage 3 exactly — Flash already operated at the wrapper-effect ceiling), and emoji stacking is small-and-negative, reactivating the wear/efficiency hijack on one extra trial per ten.

The wrapper hypothesis reframes: it's a lift for models with goal-feasibility representation that get distracted by identity vocabulary. Opus is prototypical (+40); Flash Lite at floor (wrapper couldn't lift); Flash at ceiling (nothing to lift). The remaining cohort will land on this spectrum — wrapper contribution visible only on models whose Stage 3 engineer cell fell in the wrapper-reachable range (~10–60%).
