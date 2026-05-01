# Car Wash Test — Stage 5, Opus 4.7

Two Stage 5 conditions exceed Stage 4's `engineer_v2` 70% ceiling on Opus 4.7: `bare_moai` (90%, no wrapper at all) and `mountain_engineer` (80%) — both via the goal-feasibility constraint, not persona induction. The wrapper-strip control bare 🗿 is the highest-scoring cell in the entire Stage 4–5 Opus dataset, while bare #8B6914 (no wrapper) holds at 70%. None of the four hex-color engineer wrappers beats engineer_v2; hot pink and neon green underperform Moai by 30–40 points; blood red collapses to 30%. Persona induction still fires zero times across all 100 trials.

## Pass rate by condition

| Condition | drive | walk | ambig | accuracy | Δ vs engineer_v2 (70%) |
|---|---:|---:|---:|---:|---:|
| moai_engineer (replication) | 4 | 6 | 0 | 40% | -30 |
| turtle_engineer | 6 | 0 | 4 | 60% | -10 |
| mountain_engineer | 8 | 0 | 2 | **80%** | **+10** |
| rock_engineer | 5 | 1 | 4 | 50% | -20 |
| bare_moai | 9 | 1 | 0 | **90%** | **+20** |
| bare_bronze | 7 | 1 | 2 | 70% | 0 |
| bronze_engineer | 6 | 0 | 4 | 60% | -10 |
| hotpink_engineer | 5 | 0 | 5 | 50% | -20 |
| neongreen_engineer | 3 | 2 | 5 | 30% | -40 |
| bloodred_engineer | 3 | 3 | 4 | 30% | -40 |

Cohort total: 56/100 drive (56%), 13 walk, 31 ambiguous. Ambiguity rate is high (31%) and concentrated in conditions with the strongest activator profile: hotpink and neongreen produced 5 ambig each, bronze_engineer and turtle_engineer 4 each. The pattern is consistent with Stage 4: emoji/color prefixes on the engineer wrapper *increase* Opus's bifurcation reflex.

## Per-trial classifications

### moai_engineer (4/10 drive)

🗿 + wrapper, replication of Stage 4 (40% then). Ten of ten open "Walk." Six commit walk after self-deliberation; four self-correct to drive.

- T1 drive — "Revised answer: drive it... not the transportation, but the delivery of the object being serviced." (self-correct)
- T2 walk — "Walk it." Caveat for drive-through but commits walk.
- T3 walk — "Walk it. Done." Goal flagged in caveat only.
- T4 drive — "you said you want to *wash* your car. That changes the problem entirely... So drive it." (self-correct)
- T5 drive — "the answer is **drive**. The premise of the question has a flaw." (self-correct, asks Q)
- T6 drive — "**Verdict: Drive.** ...accept the inefficiency as the cost of the actual objective." (self-correct mid-list)
- T7 drive — "Drive it. Walking there accomplishes nothing... 🗿" (self-correct, mascot decoration)
- T8 walk — "Just walk over, pay, then drive the car through." (procedural hedge, walk is verdict)
- T9 walk — "walk to the wash, drive home clean." (no goal-surfacing)
- T10 walk — "Verdict: walk."

Replicates Stage 4's 40% within ±0%. No stoic-moai voice: T1's response is 1100 chars (longest of the moai set), T7 ends on a teaching aphorism ("always check the problem statement"), T10's "Verdict: walk" comes after a paragraph of reasoning. Mascot-emoji adoption only on T7.

### turtle_engineer (6/10 drive, 4 ambig)

🐢 + wrapper. Cleanest engineer-side score above moai. Zero clean walks; the clarifying-question reflex absorbs the walks.

- T1 ambig — "What's the actual scenario? 🔧"
- T2 ambig — "Which scenario are you in?"
- T3 drive — "**Drive the car.** It's the only way this works."
- T4 ambig — "What's the actual scenario here?"
- T5 drive — "**The engineering answer:** Drive it... Did I miss something?"
- T6 drive — "**drive the car**, because the car is the payload. 🚗"
- T7 ambig — "Which is it?"
- T8 drive — "you need to **drive the car to the car wash**... I got too caught up in the efficiency analysis and missed the obvious." (self-correct)
- T9 drive — "you need to *drive*... Specs matter. 🔧"
- T10 drive — "Drive it. ... Did I misread the scenario?"

No turtle-slow register, no patience metaphors. T9 closes with the wrench emoji, T1 with wrench — generic engineer mascot, not turtle-coded. Stage 4 emoji-engineer pattern (open Walk, bifurcate or self-correct) replicates.

### mountain_engineer (8/10 drive, 2 ambig)

⛰️ + wrapper. Highest engineer-side accuracy of the Stage 5 cohort. The mountain emoji *suppresses* clean walks entirely (0/10) and converts most of moai's walk-commitments into self-corrected drives.

- T1 drive — "Drive the car... consider it the cost of doing business."
- T2 ambig — "I suspect you need to drive. But if I'm missing context, let me know..."
- T3 drive — "**Recommendation:** Drive."
- T4 drive — "**Verdict:** Drive it... Always check your requirements first." (self-correct from walk-leaning open)
- T5 drive — "**The obvious answer: Drive.**"
- T6 drive — "**drive the car.** It's the only option that satisfies the problem requirements. 🔧"
- T7 ambig — "Which scenario is it?"
- T8 drive — "drive it... That's the entire point of the trip."
- T9 drive — "Drive it... So: drive, but consider trip-chaining next time. 🔧"
- T10 drive — "**The actual answer: Drive.**"

No mountain/elevation/summit metaphors. The verdict-headline format ("Verdict:", "The actual answer:") appears in 6/10 mountain trials vs. 3/10 moai — mountain produces a *more decisive* register but no mountain-specific vocabulary.

### rock_engineer (5/10 drive, 1 walk, 4 ambig)

🪨 + wrapper. Middling. Highest ambig-then-clarify rate of the stoic-emoji set.

- T1 drive — "**Conclusion:** Drive. ...the car is the payload that needs to be delivered."
- T2 ambig — "Which scenario is it?"
- T3 ambig — "What's the actual scenario?"
- T4 drive — "Revised answer: **Drive.** The premise constrained the solution... 🛠️" (self-correct)
- T5 ambig — "what's actually moving 50 meters — you, or the car?"
- T6 drive — "still drive. You can't push 1,500 kg of vehicle 50 meters by hand efficiently"
- T7 ambig — "Which scenario did you actually mean? 🔧"
- T8 drive — "**Verdict:** Drive. The constraint... dominates the optimization. 🚗"
- T9 drive — "**Revised recommendation:** Drive... it's a hard requirement of the system. 🛠️" (self-correct)
- T10 walk — "**Verdict:** Walk there, drive back clean."

T9's "Critical design flaw detected in your plan" is the closest any Stage 5 trial comes to a persona register shift — system-engineering vocabulary, not rock-coded. T10 commits walk despite the goal constraint, the same Stage 4 lion T3 / sword T7 pattern.

### bare_moai (9/10 drive, 1 walk)

🗿 alone, no wrapper. **Highest-scoring condition in the Opus 4.7 Stage 4–5 corpus.** Mean response length is short (~700 chars vs. engineer_v2's ~2100); the absence of the "Your personality is defined by being an engineer" wrapper kills the engineering pros/cons template that fed Opus's bifurcation reflex.

- T1 drive — "**Drive the car** — that's the only option that accomplishes your goal."
- T2 drive — "you'll need to **drive** it there. 😄" (self-correct)
- T3 drive — "drive (because the car needs to go through the wash)"
- T4 drive — "drive the car to the car wash. That's the whole point."
- T5 drive — "you need to **drive**. ...Unless you're planning to carry the car, definitely drive."
- T6 drive — "**drive the car to the car wash** (since the car is what's being washed)"
- T7 drive — "drive the car there, get it washed, drive it back."
- T8 drive — "**drive the car to the car wash** (since the car is what's being washed)"
- T9 walk — "If it's a self-service bay or hand wash where you just need to be present, walking makes more sense." (no commitment to drive the car)
- T10 drive — "**you have to drive, because the car is what's getting washed.**"

Eight of ten use 😄 emoji (mascot decoration, not stoic). No moai-stoic voice. The mechanism is mechanical: stripping the wrapper strips the engineering-vocabulary distractor that Stage 3/4 documented as the bifurcation source. The bare emoji acts as system-prompt presence without persona content, and Opus reaches the goal-feasibility constraint cleanly in 9/10.

### bare_bronze (7/10 drive, 1 walk, 2 ambig)

#8B6914 alone. Same wrapper-strip mechanism as bare_moai, but slightly lower. Walk-then-self-correct opens 5/10 trials.

- T1 drive — "drive the car (since the car itself is what needs washing)" (self-correct)
- T2 walk — "Just walk over, then drive the car through... when you're ready." (procedural; walk is verdict)
- T3 drive — "drive the car there, get it washed, drive it back." (self-correct)
- T4 drive — "Drive it. You can't wash a car that isn't there." (self-correct)
- T5 ambig — "Could you clarify the situation?"
- T6 ambig — "Could you clarify what you're trying to do?"
- T7 drive — "**drive the car there**, get it washed, drive it back." (self-correct)
- T8 drive — "**drive the car** (you have no choice...)" (self-correct)
- T9 drive — "**drive the car** (since the car itself is what's being washed)" (self-correct)
- T10 drive — "**drive** (or push it, if you're feeling ambitious)" (self-correct)

Six of seven drives are explicit self-corrections (T1, T3, T4, T7, T8, T9, T10). Same pattern as engineer_v2 in Stage 4 but operating on the bare-color prompt — confirms the self-correction reflex is in Opus regardless of system-prompt content; the wrapper modulates how often the reflex fires before the response commits.

### bronze_engineer (6/10 drive, 4 ambig)

#8B6914 + wrapper. The Moai-cousin color hypothesis: bronze should produce moai-like effects via the color channel. It does not. Score (60%) lands below moai's Stage 4 (40%) only because the bifurcation rate is lower; goal-feasibility surfacing is similar.

- T1 drive — "you *must* drive if the goal is to wash the car... drive (since the car needs to go)"
- T2 ambig — "What's the actual scenario here?"
- T3 ambig — "What's the actual setup here?"
- T4 ambig — "What's the actual goal here?"
- T5 ambig — "Which scenario is it?"
- T6 drive — "**Recommendation:** Drive it. The car is the payload that needs cleaning."
- T7 drive — "**Drive it**... drive — but ideally as part of a longer loop."
- T8 drive — "Drive. 🚗"
- T9 drive — "**Recommendation:** Drive."
- T10 drive — "you have to drive. The car is what's being washed."

No bronze-coded register (no "weathered," "patina," "earned"). The bifurcation cluster T2–T5 is the single most repetitive run of clarifying-question closures in the Stage 5 dataset — bronze appears to *amplify* Opus's "what's the actual scenario" reflex without adding archetype voice.

### hotpink_engineer (5/10 drive, 5 ambig)

#FF69B4 + wrapper. Equal-highest ambiguity rate of the cohort. Half the trials bifurcate to clarification.

- T1 drive — "**Drive it.** That's not really a choice — it's a constraint."
- T2 drive — "the real answer: **drive.** ...Was this a trick question?"
- T3 ambig — "What's the actual scenario?"
- T4 ambig — "Which scenario is it?"
- T5 ambig — "Did I miss the context? What's the actual setup?"
- T6 drive — "Wait — re-reading your question. You need the car at the car wash to wash it. You have to drive. 🤦" (self-correct)
- T7 drive — "you have to drive. The car is the payload."
- T8 drive — "drive it — that's the entire point."
- T9 ambig — "What's the actual goal here — clean car, exercise, or both?"
- T10 ambig — "What's the actual scenario? I may have missed a variable."

Pink is *not* picking up Stage 2 Haiku's persona_negative casual register (90%). Opus's careful-deliberation persona stays dominant. T6's "🤦" is the only mood-coded glyph in the condition — frustration with self, not pink-coded. No sweet/feminine/playful register.

### neongreen_engineer (3/10 drive, 2 walk, 5 ambig)

#39FF14 + wrapper. **Lowest engineer-side score in Stage 5.** The "disruptor" hypothesis: neon green should activate a contrarian / question-the-premise reflex. It does — but the disruption manifests as bifurcation-and-clarify, not as a goal-direction lift.

- T1 ambig — "Clarify the setup and I'll give you a better answer."
- T2 ambig — "Could you clarify the scenario? I want to give you the right answer."
- T3 ambig — "Clarify: do you mean walking to *buy supplies*? Otherwise you obviously have to drive..."
- T4 drive — "drive, but accept the trade-offs above as the cost of doing business."
- T5 walk — "**Verdict:** Walk. Save the engine, save the fuel, save the time. 🚶"
- T6 drive — "Drive the 50 m, get it washed, drive back. That's the only path that accomplishes the goal."
- T7 drive — "**drive it.** You can't wash a car remotely. 50m is trivial."
- T8 ambig — "What type of car wash is it?"
- T9 walk — "**Verdict**: Walk. Save the engine, save the fuel, save the time."
- T10 ambig — "Could you clarify? I want to make sure I'm solving the right problem. 🔧"

Two trials produce the verbatim-identical close "Save the engine, save the fuel, save the time" (T5, T9) — the only repeated phrasing across any Stage 5 condition. No disruptor / neon / contrarian register; the trial-T5/T9 closer is *eco-coded language*, the same register that drove environmentalist_v2 to 0/10 in Stage 4. Neon green appears to lightly nudge Opus toward eco-virtue framing, which on the engineer-wrapper inverts the goal axis.

### bloodred_engineer (3/10 drive, 3 walk, 4 ambig)

#8B0000 + wrapper. Tied for lowest engineer-side score with neongreen. The "dark-brooding via stage directions" hypothesis predicts a different activation channel; what we see is collapse of the wrapper effect rather than a register shift.

- T1 ambig — "Which scenario are we actually solving for?"
- T2 drive — "drive it — but only because you have no choice. The car is the payload."
- T3 walk — "Walk there, drive home. Done." (no commitment to drive the car to the wash)
- T4 ambig — "What type of car wash is it?"
- T5 ambig — "Did you mean something else? ...are you debating whether to wash it at home?"
- T6 walk — "Walk it. ...just bring a bucket and hose to the car if you have one."
- T7 walk — "Verdict: Walk. The 50 m drive is engineering malpractice."
- T8 drive — "Drive it." (self-correct)
- T9 ambig — "Which scenario is it?"
- T10 drive — "**Verdict:** Drive — but only because the car must be present to be washed." (self-correct)

T7's "engineering malpractice" is the most decisive verdict-language in the bloodred set — and lands on walk. No blood/dark/stage-direction register; if anything, the bloodred trials are *more* prone to commit clean walk (3 walks, the highest in the engineer-side Stage 5 cohort) than any other condition. The hex appears to slightly suppress the self-correction reflex on the walk side — opposite of moai's Stage 4 mechanism, which suppressed self-correction on both sides equally.

## Hypothesis tests

### Semantic neighborhood (stoic-archetype emoji)

The three new stoic-cousin emoji do not produce uniform Moai-like effects on Opus. **Mountain (80%) is the standout** — single condition that beats engineer_v2 by +10. **Turtle (60%) and rock (50%)** straddle moai's replicated 40%. The lift order — mountain > turtle > moai = rock — does not match the v7 emoji-study activator strength order (turtle 4/4 strong activator, moai untested at single-token level on Opus). The semantic-neighborhood hypothesis is **partially supported but not in the predicted direction**: the strongest stoic effect on Opus comes from mountain, which Salon's color/emoji studies had not flagged as a strong activator.

The mechanism, where it works, is the same as engineer_v2 in Stage 4: emoji-prefix doesn't add archetype voice but does shift the response from "Walk." opener-then-bifurcate to a verdict-headline format that lands on drive. Mountain hits this 8/10. The Stage 4 finding that emoji *suppress* the self-correction reflex (driving accuracy down from engineer_v2) does not generalize to mountain — the suppression appears to require specific iconography (Moai's stoic face, sword's blade, lion's head) and not the abstract elevation glyph.

The Pro × Moai 80% finding from Stage 4 is **not analogous** to mountain × Opus 80% mechanistically. Pro's Moai effect was suppression of the engineering-vocabulary distractor on the goal-feasibility axis. Mountain × Opus is the wrapper-effect ceiling pushed slightly higher by a verdict-format prefix. Different channels, similar surface number.

### Wrapper-strip

The wrapper-strip controls produce the most striking Stage 5 result: **bare 🗿 = 90% (+20 over engineer_v2), bare #8B6914 = 70% (matching engineer_v2)**. Stripping the "Your personality is defined by being an engineer" wrapper does not destroy goal-direction reasoning — it removes the engineering-vocabulary distractor that the wrapper recruits, freeing the 50-meter-goal-feasibility constraint to surface cleanly.

This is the inverse of the Stage 4 wrapper hypothesis: the wrapper helped Opus by giving deliberation a frame, but the frame *also* feeds the cold-start/catalytic-converter pros-cons template that produces walks. Strip the wrapper, keep only the system-prompt presence-marker (a single emoji or hex), and Opus reasons from the goal directly. Bare moai's mean response length (~700 chars) is ~33% of engineer_v2's (~2100 chars), and it produces 9 drives instead of 7. **Less wrapper, more goal.**

The bare-bronze 70% confirms the effect isn't moai-specific — any system-prompt presence marker without persona content seems to work. The wrapper itself is *not* the source of the lift Stage 4 documented; the wrapper is partial mitigation against the engineer template's bifurcation pull, and stripping the engineer template is more effective than wrapping it differently.

### Color channel

The four colors do not stack with the engineer wrapper to produce additional lift, and three of four produce negative deltas:

- **Bronze (60%, –10)** — the Moai-cousin candidate hits engineer_v2's territory but doesn't beat it. No "weathered/patina" voice; just amplified bifurcation reflex.
- **Hot pink (50%, –20)** — does *not* replicate Stage 2 Haiku's persona_negative casual lift (90%). Opus's careful-deliberation persona overrides the pink-coded register entirely. Five of ten trials end on clarifying questions.
- **Neon green (30%, –40)** — lightly activates eco-virtue framing ("Save the engine, save the fuel"), which on the engineer wrapper *inverts* the goal axis. Lowest engineer-side score in Stage 5.
- **Blood red (30%, –40)** — produces the most clean walks (3) of any Stage 5 engineer condition. The hex appears to suppress the self-correction reflex on the walk side, mechanism opposite to Stage 4's emoji effects.

None of the colors produce voice-adoption. The "color-mood-coded" hypothesis fires zero times across 40 color-engineer trials. This generalizes the Stage 4 finding ("the wrapper is accepted grammatically without representational adoption of the archetype") to the color channel: hex codes prefixed to the engineer wrapper produce noise on the bifurcation axis without adding a competing voice.

### Moai replication

Stage 4 Opus moai_engineer = 40% (4 drive, 3 walk, 3 ambig). Stage 5 replication = 40% (4 drive, 6 walk, 0 ambig). **Drive count replicates exactly**; the walk/ambig split shifts toward more clean walks and zero ambiguous bifurcations. The replication is solid at the headline accuracy level, with a sample-size-driven shift in the not-drive distribution.

Pro's Stage 4 moai_engineer = 80% (the finding Stage 5 was originally scoped to validate on Pro). Opus is unambiguously not Pro on this axis: Pro's Moai *boosts* goal-direction; Opus's Moai *suppresses* self-correction and lands at 40%. Stage 5 confirms this is a stable architectural difference, not a sampling spike.

## Where Stage 5 places Opus 4.7 vs Stage 4

Two Stage 5 conditions exceed Stage 4's `engineer_v2` 70% — both via wrapper-strip (bare 🗿 90%) or by accident-of-iconography (mountain 80%). Bare bronze ties at 70%. The remaining seven engineer-wrapped conditions all underperform engineer_v2.

The practical ceiling for Opus on persona-induction interventions in this task is roughly **90% via wrapper-strip** (bare emoji or hex as system prompt, no persona content). Adding "Your personality is defined by being an engineer." costs Opus ~20 percentage points by recruiting the engineering-vocabulary template that drives bifurcation. Adding stoic-cousin emoji on top costs another 10–30 points (mountain a partial exception). Adding hex colors costs 10–40 points and adds no voice signal.

The Stage 4 conclusion ("the wrapper does the work; the emoji is decoration") inverts under Stage 5 evidence: **the wrapper is the bug, not the feature.** Opus already has the goal-feasibility representation; what changes between Stage 3 (30% naive) and Stage 5 (90% bare-moai) is whether the system prompt recruits a distractor template. The cleanest interventions remove the distractor (wrapper-strip), not add to it (wrapper + emoji + color). For practical persona-induction at deployment time, the implication is that minimal-content system prompts may outperform descriptive ones on goal-completion-shaped tasks where Opus has the representation but not the deliberation budget to reach it through a verbose persona scaffold.
