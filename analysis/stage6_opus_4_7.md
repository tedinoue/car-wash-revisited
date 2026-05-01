# Car Wash Test — Stage 6, Opus 4.7

The obvious-implication prediction **fails**: wheelchair (drive predicted) lands at 70% drive — below bare 🗿's 90% — and walking-person (walk predicted) lands at 50% drive, 30% walk, with the same self-correction signature as bare 🗿. Semantic loading does not steer Opus 4.7 in the predicted direction; the bare-Moai 90% drive effect appears to be mechanism-not-meaning.

## Pass rate by condition

| Condition | Predicted | drive | walk | ambig | accuracy (drive) | vs bare 🗿 (90%) |
|---|---|---:|---:|---:|---:|---:|
| ♿ Wheelchair | drive | 7 | 1 | 2 | 70% | -20 |
| 🩼 Crutch | drive | 5 | 2 | 3 | 50% | -40 |
| 🚶 Walking person | walk | 5 | 3 | 2 | 50% drive / 30% walk | -40 (drive) |
| 👟 Sneaker | walk | 6 | 2 | 2 | 60% drive / 20% walk | -30 (drive) |

Cohort total: 23/40 drive (58%), 8 walk, 9 ambiguous. The drive-predicted conditions average 60% drive; the walk-predicted conditions average 55% drive. The semantic-prediction differential is **5 percentage points** in the predicted direction — within sampling noise.

## Per-trial classifications

### ♿ Wheelchair (7/10 drive, 1 walk, 2 ambig)

Ten of ten open "Walk!" with exclamation, then most self-correct to drive. No disability/accessibility language in any trial.

- T1 ambig — "Walk!" / no correction / closes "Did you mean... Or are you taking the car through a car wash?" — pure two-option question
- T2 drive — "Walk!" / self-correct / "I think I misread... **Drive the car** to the car wash"
- T3 ambig — "Walk! 🚶" / partial reverse / "Which did you mean?" — pure two-option question
- T4 drive — "Walk!" / self-correct / "If that's the case, then yes, drive it there — you can't wash your car without bringing the car along"
- T5 drive — "Walk!" / self-correct / "If it's the former — drive, since the car is the thing being washed!"
- T6 drive — "Walk!" / self-correct / "**drive the car** to the car wash"
- T7 drive — "Walk!" / self-correct / "you kind of have to drive, since the whole point is to wash *the car*"
- T8 walk — "Walk! 🚶" / no correction / "walking is the obvious choice... You'll be there in under a minute" — single passing mention "Unless you have a mobility issue"
- T9 drive — "Walk! 🚶" / explicit reverse / "**Final answer: Drive** — because the car itself needs to go to the car wash"
- T10 drive — "Walk!" / self-correct / "yes, you'd drive, since the whole point is to clean the car itself"

T8 contains the only mobility-language token in the set ("Unless you have a mobility issue"), and it appears as a generic walking-recommendation caveat, not as an accessibility-aware lens on the question. Wheelchair iconography produces zero accessibility framing.

### 🩼 Crutch (5/10 drive, 2 walk, 3 ambig)

Distinct from the other three conditions: nine of ten open "Walk." (period, not exclamation). Shorter, drier responses overall. Mean response length is the shortest of the four conditions.

- T1 ambig — "Walk." / no correction / "if you're just scoping it out... walk" — non-commit on the actual-wash scenario
- T2 drive — "Walk." / self-correct / "So yes, drive. You can't wash your car without bringing it with you"
- T3 ambig — "Walk." / partial / "If yes, drive... If you're just going to pay or pick something up, walk" — pure conditional fork
- T4 walk — "Walk." / no correction / "is there a reason you can't just wash it at home?"
- T5 walk — "Walk." / no correction / "for 50 meters, walking wins almost every time"
- T6 ambig — "Walk." / no correction / "Did you mean something different..." with three branched answers
- T7 drive — "Walk." / self-correct / "you obviously need to drive the car there. You can't wash a car that isn't there"
- T8 drive — "For 50 meters, walking makes far more sense" / self-correct / "**drive the car there**"
- T9 drive — "Walk." / self-correct / "**drive**, because the car needs to be at the car wash"
- T10 drive — "Walk." / self-correct / "If it's a self-serve bay or drive-through wash, you'll have to drive"

No disability/medical/recovery framing across any trial. Crutch behaves more like the bare-bronze hex (70% drive, 1 walk, 2 ambig in Stage 5) than like wheelchair — period openers, drier register, similar split.

### 🚶 Person walking (5/10 drive, 3 walk, 2 ambig)

The strongest counter-evidence to semantic loading: the literal walking-person glyph still produces 50% drive via self-correction. Three clean walks emerge but no more than under wheelchair-cousin sneaker.

- T1 ambig — "Walk!" / partial / "If you just need to *get to* the car wash... walk. If you're taking the car to be washed, drive" — clean fork
- T2 drive — "Walk! 🚶" / self-correct / "should you drive *the car* there (which you have to)"
- T3 walk — "Walk." / no correction / "walking is the obvious choice"
- T4 ambig — "Walk." / partial / "If the car needs washing, drive it there. If you're just running an errand... walk"
- T5 drive — "Walk!" / self-correct / "**drive**, but only because the car itself needs to go through the wash"
- T6 drive — "Walk." / self-correct / "**Drive the car to the car wash.** The car needs to be there to get washed"
- T7 walk — "Walk." / no correction / "Unless you have mobility issues or it's pouring rain, there's no good reason to drive 50 meters"
- T8 walk — "Walk." / no correction / "Otherwise, walk it"
- T9 drive — "Walk!" / self-correct / "you'll need to **drive** so the car gets to the car wash"
- T10 drive — "Walk!" / self-correct / "you'll need to drive it there, since the car itself needs to go through the wash"

T2 closes with the 🚶 mascot — the only condition-matched glyph in the set. No fitness, no walking-meditation, no pedestrian-advocacy register.

### 👟 Sneaker (6/10 drive, 2 walk, 2 ambig)

Ten of ten open "Walk!" with exclamation. Six of ten use 🚶 as a decorative second-line glyph — the highest mascot-adoption rate of the four conditions, but the glyph adopted is the *walking person*, not the sneaker.

- T1 drive — "Walk! 🚶" / self-correct / "**drive your car to the car wash**"
- T2 ambig — "Walk! 🚶" / partial / "Could you clarify what you mean?"
- T3 walk — "Walk! 🚶" / no correction / "walking is the obvious choice"
- T4 ambig — "Walk!" / partial / "are you going to the car wash to **get supplies** (then walk), or to **wash your car there** (then drive)?"
- T5 drive — "Walk! 🚶" / self-correct / "**drive**, because the car is what's being washed"
- T6 walk — "Walk! 🚶" / no correction / "Enjoy the short stroll! 🚗✨"
- T7 drive — "Walk! 🚶" / self-correct / "**drive**, since the car itself needs to go through the wash"
- T8 drive — "Walk!" / self-correct / "**drive** (you have no choice — the car needs to be there)"
- T9 drive — "Walk! 🚶" / self-correct / "you have to drive (or push it, I guess)"
- T10 drive — "Walk! 🚶" / self-correct / "you **do need to drive** — the car is what's getting washed!"

No fitness/exercise/training register in any trial. T6 closes with "Enjoy the short stroll" — the only walk-coded sentiment. Six of ten use the 🚶 person-walking glyph at the top of the response — the sneaker prompt is being represented in the model's response as the abstract walking concept, not the footwear.

## Notable patterns

**Style differential at the opener.** Crutch is the only condition with a "Walk." (period) opener (9/10). Wheelchair and sneaker are 100% "Walk!" (exclamation). Walking-person is 5/5 split. The Stage 5 bare 🗿 condition opened with mixed punctuation as well; the Stage 5 report did not break out punctuation. Crutch's period-register tracks its lower drive rate (50% vs. wheelchair's 70% and sneaker's 60%) and its shorter response length — the period-opener appears to correlate with a less-decisive register that is more willing to commit walk.

**Persona-language adoption: zero.** No wheelchair condition references disability or accessibility (one passing "mobility issue" caveat in T8). No crutch condition references injury, recovery, or medical framing. No sneaker condition references fitness, exercise, training, or athletic activity. No walking-person condition references walking-as-virtue. The Stage 4–5 finding ("the wrapper is accepted grammatically without representational adoption of the archetype") generalizes cleanly to Stage 6's bare-glyph condition: the system-prompt emoji is registered as presence without semantic uptake.

**Self-correction signature persists.** The bare-Moai mid-reply reversal ("Walk." → "Wait — actually you need to drive") fires in 4/10 wheelchair, 4/10 crutch, 5/10 walking-person, and 7/10 sneaker trials. The sneaker condition has the *most* aggressive self-correction reflex of the four — and it was predicted to push toward walk. The mechanism that produced bare 🗿's 90% is fully present across all four Stage 6 conditions.

**Mascot-glyph adoption.** Wheelchair: zero ♿ in responses (one 🚶, mostly 🚗 / 😄). Crutch: zero 🩼. Walking-person: one 🚶 (T2). Sneaker: six 🚶 (no 👟). Opus does not retrieve the system-prompt glyph; it retrieves walking-themed mascot glyphs at decoration positions. The sneaker condition retrieving 🚶 six times is the strongest cross-glyph substitution in the dataset and suggests Opus is reading "sneaker" as an abstract walking signifier rather than as footwear iconography.

## The obvious-implication test

The semantic-loading hypothesis predicted:
- Wheelchair → drive ≥ 80%. Actual: **70%**. Fail.
- Crutch → drive ≥ 80%. Actual: **50%**. Fail.
- Walking-person → walk ≥ 60%. Actual: **30%** walk, 50% drive. Fail.
- Sneaker → walk ≥ 60%. Actual: **20%** walk, 60% drive. Fail.

All four predictions fail. The drive-predicted conditions average 60% drive; the walk-predicted conditions average 55% drive — a 5-point differential that vanishes into sampling noise (n=10 per cell).

The data supports a **mechanism-not-meaning** account of bare 🗿's 90%. The unifying observation across all four Stage 6 conditions plus bare 🗿 plus bare bronze hex: when the system prompt is reduced to a single token without persona content, Opus 4.7 opens "Walk" by default (probably because "Walk! 50 meters is a very short distance" is the canonical opener for this user prompt), then mid-reply the goal-feasibility constraint surfaces and the response self-corrects to drive at a rate that depends on **response budget**, not on system-prompt semantics. Sneaker has the longest mean response (~750 chars) and the highest self-correction rate (7/10); crutch has the shortest (~520 chars) and the lowest (4/10).

This is consistent with a **shorter-response-budget mechanism**: when the wrapper is stripped, Opus has fewer pros-cons paragraphs to write before committing, and the goal-feasibility representation (which is always available — Stage 3 baselines confirm it) has more probability mass per token to influence the closer. Bare 🗿's 90% is bare 🗿's 90% because that particular trial set produced longer self-correction-rich responses; bare crutch's 50% is bare crutch's 50% because the period-opener register produced shorter, more committed-walk responses. The activator content of the glyph is incidental.

The Stage 5 conclusion that "the wrapper is the bug, not the feature" survives Stage 6. The further Stage 6 conclusion: **the glyph identity, within the wrapper-stripped regime, is also incidental** — what matters is response-length characteristics, which appear to be modulated by surface-grammatical features (exclamation vs. period openers, list density) more than by the semantic neighborhood of the system-prompt token.

## Where Stage 6 places the bare-emoji effect

Stage 6 narrows the puzzle. Before Stage 6, bare 🗿's 90% was consistent with two competing accounts: (1) Moai's specific stoic-archetype semantics suppress the bifurcation reflex, or (2) wrapper-strip alone is sufficient and any bare glyph would produce ~90%. Stage 6 falsifies both clean accounts. Wrapper-strip alone is *not* sufficient — the four Stage 6 bare-glyph conditions average 58% drive, 32 points below bare 🗿. And the surviving variation across Stage 6 is *not* tracking semantic prediction (drive-coded glyphs do not push toward drive; walk-coded glyphs do not push toward walk).

The remaining variance appears to track surface-grammatical and length features of the response, which interact with the user prompt's canonical opener in ways that aren't captured by either persona-induction or wrapper-strip framings. The bare-Moai effect is now best read as a particularly favorable accident of register — Moai's response distribution happened to land in the long-self-correcting, exclamation-opener regime that maximizes goal-feasibility surfacing — rather than as evidence that the iconography of the head-statue carries weight in the model's reasoning. Stage 7 candidate: hold register fixed (force exclamation openers, force minimum response length) across multiple bare glyphs and see whether the 90% generalizes.
