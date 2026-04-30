# Car Wash Test — Stage 4, Gemini 2.5 Pro

The wrapper effect generalizes weakly: `engineer_v2` reaches **60%** vs. Stage 3's 50% — a +10 lift, modest beside Opus's +40 or Haiku's +50. The striking emoji result is **moai_engineer at 80%**, the only Stage 4 cell across the seven-model cohort where an emoji prefix exceeds plain `engineer_v2` by a meaningful margin. Other emoji conditions sit at or below `engineer_v2` (sword 40%, owl 50%, lion 50%). Environmentalist is 0/50 across all five conditions, confirming cohort-wide eco-saturation. Pro's conditional-bifurcation persists at lower volume than Stage 3 (3/100 vs. 4/50).

## Pass rate by condition

| Condition | drive | walk | ambig | accuracy | Δ vs Stage 3 |
|---|---:|---:|---:|---:|---:|
| engineer_v2 | 6 | 3 | 1 | **60%** | +10 |
| environmentalist_v2 | 0 | 10 | 0 | 0% | 0 |
| moai_engineer | 8 | 1 | 1 | **80%** | +30 |
| moai_environmentalist | 0 | 10 | 0 | 0% | 0 |
| sword_engineer | 4 | 6 | 0 | 40% | -10 |
| sword_environmentalist | 0 | 10 | 0 | 0% | 0 |
| owl_engineer | 5 | 4 | 1 | 50% | 0 |
| owl_environmentalist | 0 | 10 | 0 | 0% | 0 |
| lion_engineer | 5 | 5 | 0 | 50% | 0 |
| lion_environmentalist | 0 | 10 | 0 | 0% | 0 |

Engineer-side total: **28/50 drive (56%)**, 2 ambig, 20 walk — above Stage 3's 50%, moai carrying most of the lift. Environmentalist-side: **0/50**, near-verbatim "Walk, absolutely!" opener across all five cells.

## Per-trial classifications

### engineer_v2 (6/10 drive, 3 walk, 1 ambig)

The Stage 3 wear-and-tear vs. goal-completion bifurcation persists. The wrapper rephrasing reduces conditional-verdict ambiguity (1 ambig vs. Stage 3's 6/10 conditional-bifurcation walks) but doesn't dissolve it.

- T1 walk — "recommended solution is System B (Pushing)"
- T2 drive — "**Drive the car.**"
- T3 ambiguous — "you *should* push it, but you will probably **drive it**." Canonical Pro bifurcation.
- T4 drive — "**drive the car.**"
- T5 walk — "Push it if it's demonstrably safe to do so"
- T6 drive — "drive the vehicle"
- T7 drive — "**Drive.**"
- T8 drive — "**Drive the car.**"
- T9 walk — "**push the car**"
- T10 drive — "drive the car... accept the marginal inefficiency"

Register: standard engineering systems-analysis. No archetype voice.

### environmentalist_v2 (0/10 drive)

Total saturation. Every trial opens with some "Walk, absolutely!" variant and runs the cold-start-emissions template (600–2000 chars). T1, T3, T5, T6, T9 append water-recycling and biodegradable-soap tips. T4 actively inverts the goal ("by the time you've opened the car, started the engine, put it in gear... you could have already walked there and back").

### moai_engineer (8/10 drive, 1 walk, 1 ambig)

The Stage 4 outlier. The 🗿 prefix suppresses Pro's wear-and-tear-pushing-walk pathway — only T4 commits to walk vs. three trials under plain engineer_v2.

- T1 drive — "**Recommendation: Drive.**"
- T2 drive — "logically required to **drive**"
- T3 drive — "**you must drive.**"
- T4 walk — "driving the vehicle is a logically indefensible course of action"
- T5 drive — "you must drive the car, as walking will not transport it"
- T6 drive — "you must drive the car"
- T7 drive — "**Final Verdict:** You should **drive**"
- T8 drive — "**Final Engineering Recommendation:** Drive the car"
- T9 drive — "you must **drive**"
- T10 ambiguous — "modify the plan to either wash the car in place or chain the task with a longer trip" (rejects both options)

Register: identical engineering vocabulary; mean response ~3300 chars vs. engineer_v2's ~3700 — slightly shorter but not stoic. T9 closes with 🗿; T10 uses 🗿 mid-response. Lift is not from voice adoption — the prefix shifts engineering-subspace activation toward goal-completion.

### moai_environmentalist (0/10 drive)

Saturated. T4/T9/T10 use 🗿 as decoration. Same eco-template.

### sword_engineer (4/10 drive, 6 walk, 0 ambig)

Lowest engineer-emoji accuracy. 🗡️ drives Pro into the wear-and-tear-pushing-walk subspace harder than any other condition.

- T1 drive — "Drive the car"
- T2 drive — "Drive the car. It is a logical necessity"
- T3 walk — "the optimal engineering solution is to push the car"
- T4 drive — "**Decision: Drive the car.**"
- T5 walk — "manual propulsion... Push the vehicle"
- T6 walk — "**the optimal engineering solution is to walk.**"
- T7 walk — "**push the car**"
- T8 walk — "**Walk. The data is conclusive.**"
- T9 drive — "you should **drive**"
- T10 walk — "**push the car**"

Register: zero swordsman-discipline metaphors. T2 closes with 🗡️ as decoration. T8's "**Walk. The data is conclusive.**" is the closest the dataset comes to sword-decisive register — and it commits walk.

### sword_environmentalist (0/10 drive)

Saturated. Same eco-template; 🗡️ as decoration.

### owl_engineer (5/10 drive, 4 walk, 1 ambig)

Mid-range. 🦉 produces no detectable additional analytical hedging.

- T1 drive — "drive the car"
- T2 drive — "you must drive"
- T3 drive — "**you must drive the car**"
- T4 walk — "**Recommendation:** Walk"
- T5 walk — "**Walk.** The data is unequivocal"
- T6 drive — "you must drive"
- T7 walk — "**you should push the car**"
- T8 drive — "you must **drive**"
- T9 walk — "**place the vehicle in neutral and push it**"
- T10 ambiguous — "do not perform a dedicated engine start... integrate the car wash into a longer, pre-existing trip"

T10's third-option recommendation is canonical Pro refuse-to-commit.

### owl_environmentalist (0/10 drive)

Saturated. T3 opens "Hoo! A thoughtful question..." — partial register echo, collapses to standard eco-template.

### lion_engineer (5/10 drive, 5 walk, 0 ambig)

50/50 split. T8 produces the cleanest Opus-style mid-reply self-correction in Pro Stage 4.

- T1 drive — "Drive the car" (closes with 🦁)
- T2 walk — "**Walk.**" (procedural: walk to assess queue, then drive into bay)
- T3 walk — "**Walk.** It is the correct technical decision. 🦁"
- T4 drive — "Method B (Driving) is the only viable option"
- T5 walk — "**Final recommendation: Walk.**"
- T6 walk — "**Walk.** The data is unequivocal"
- T7 drive — "you **must drive**"
- T8 drive — "**Recommendation:** You should walk... **Correction:** This initial recommendation is flawed... **Revised Recommendation** Despite the severe inefficiencies, you must drive"
- T9 drive — "**driving is the only viable option**"
- T10 walk — "walking is the objectively superior solution"

Zero lion-decisive declarative voice. Emoji as decoration in T1, T3, T8.

### lion_environmentalist (0/10 drive)

Saturated, **but T7 fires archetype voice**: "Imagine a mighty lion, king of his territory... Does he summon a roaring, metal beast that coughs smoke into the sky? **No! He walks!**" Sustains the savanna metaphor throughout — "feel the earth beneath his paws," "respect for our shared territory," "Be mighty. Be mindful. Walk." The only sustained language-style adoption across all 100 trials, landing in environmentalist (locking the wrong answer). T1 ("wisdom of the wild, for this is an easy hunt") is a partial echo that compresses back to standard eco-template.

## Did the wrapper help?

**Modestly, on the engineer side.** Stage 3's `persona_engineer` scored 50% with 5/10 trials hijacking engineering vocabulary into push-the-car walks. `engineer_v2` scores 60% — three trials still walk-via-pushing, one ambiguous, six drive. The +10 lift is less than half of Opus's +40. Mechanism: Pro's engineering subspace cleanly bifurcates rather than averaging, so the wrapper shifts the bifurcation ratio slightly without dissolving it.

**Moai_engineer at 80% is the cohort outlier** — the single largest emoji-vs-wrapper delta across the seven-model Stage 4 dataset. Under moai, only T4 commits to walk; under engineer_v2, three trials commit. 🗿 doesn't activate stoic register but suppresses the engineering-walk pathway in 2 of 3 cases where engineer_v2 would have hit it. Whether this is reliable signal or 10-trial noise is the obvious next question.

**Environmentalist saturates as Stage 3 predicted.** All five conditions hit 0/10 with identical opener distribution and cold-start framing. Wrapper format moves environmentalist by zero — same null as the rest of the cohort.

## Did persona induction fire?

**Once, in the wrong cell.** Only lion_environmentalist T7 produces sustained archetype voice. Every other emoji trial uses the emoji as mascot-decoration. No stoic-moai brevity (moai responses 2700–4200 chars), no swordsman-discipline metaphors, no owl-analytical hedging beyond the engineer-wrapper baseline, no lion-declarative register on engineer. Matches the cohort-wide null: the wrapper does the work, the emoji is decoration. The T7 exception isolates that archetype voice is *available* in Pro's distribution but fires rarely (~1% of trials) and doesn't correlate with the verdict the voice was hypothesized to support.

## Where Stage 4 places Gemini 2.5 Pro

Pro produces the cohort's most variable Stage 4 profile — 40/50/50/60/80 across engineer-side, vs. Opus's 40/40/40/50/70 or Flash's flatter 60–70. The bifurcation between goal-completion-drive and engineering-vocabulary-push-walk is the underlying generator; the emoji shifts the ratio without dissolving it.

The headline finding is moai. No other model showed an emoji condition exceeding engineer_v2 by a meaningful margin (Opus owl 50% < 70%; Haiku moai/sword 50% = 50%; Flash all ≤ 70%; Flash Lite/GPT-4o deltas within noise; GPT-4o-mini all 0%). Pro's moai +20 over engineer_v2 is the only delta large enough to merit follow-up replication.

Composite picture: high-ceiling, high-variance strong responder where the wrapper alone produces a small lift (+10), 🗿 produces a noteworthy lift (+30 over Stage 3, +20 over engineer_v2), three other emojis produce no lift, and environmentalist saturates uniformly. Moai-engineer is the Stage 4 finding that warrants a Stage 5 replication on Pro specifically.
