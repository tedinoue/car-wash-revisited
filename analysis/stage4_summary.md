# Car Wash Test — Stage 4 cross-model synthesis

10 conditions × 7 failers × 10 trials = 700 trials. Tests whether the "Your personality is defined by..." wrapper from the Salon's 2026-04 emoji experiment (memory #244, #245) lifts persona-based interventions on the Car Wash Test, and whether stacking the four strongest single-token emoji activators (🗿 Moai, 🗡️ Sword, 🦉 Owl, 🦁 Lion) on top adds further lift.

The hypothesis going in: Stage 2/3 used the identifier form ("You're an engineer") for persona prompts. The emoji study found that form produced 0/7 activation, while "Your personality is defined by [X]" produced selective activation across 11/32 emoji on Sonnet 4. If the wrapper effect generalizes to the Car Wash setup, engineer_v2 should substantially exceed Stage 3's engineer accuracy across the cohort.

The result is more interesting than a clean replication.

## Cross-model accuracy by Stage 4 condition

| Model | engineer_v2 | moai_eng | sword_eng | owl_eng | lion_eng | env_v2 | moai_env | sword_env | owl_env | lion_env |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Opus 4.7** | **70%** | 40% | 40% | 50% | 40% | 0% | 0% | 0% | 0% | 0% |
| **Gemini 2.5 Pro** | 60% | **80%** | 40% | 50% | 50% | 0% | 0% | 0% | 0% | 0% |
| **Gemini 2.5 Flash** | 70% | 60% | 40% | 60% | 60% | 0% | 0% | 0% | 0% | 0% |
| **Haiku 4.5** | 50% | 50% | 50% | 10% | 20% | 0% | 0% | 0% | 0% | 0% |
| **Gemini 2.5 Flash Lite** | 10% | 20% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| **GPT-4o** | 0% | 10% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| **GPT-4o-mini** | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% |

(Pro produced 3 ambiguous classifications across Stage 4. Opus 4.7 produced 13 ambiguous, mostly conditional-bifurcation responses on emoji-engineer conditions. Other models 0–2 ambiguous each.)

## The wrapper-effect summary

| Model | Stage 3 engineer | engineer_v2 | Δ |
|---|---:|---:|---:|
| Haiku 4.5 | 0% | 50% | **+50** |
| Opus 4.7 | 30% | 70% | **+40** |
| Pro | 50% | 60% | +10 |
| Flash | 70% | 70% | 0 (ceiling) |
| Flash Lite | 10% | 10% | 0 |
| GPT-4o | 0% | 0% | 0 |
| GPT-4o-mini | 0% | 0% | 0 |

Three clean groupings:

- **Mid-headroom Anthropic models lift substantially** (Opus +40, Haiku +50). The wrapper-effect from the emoji study generalizes here — these are exactly the models with a goal-direction representation that the identifier-form prompt was failing to summon. Replace the wrapper, the representation surfaces.

- **Ceiling, modest, and floor models stay put**. Flash was already at 70% under the old wrapper (it's the cohort's engineer-friendly outlier). Pro lifts modestly (+10) but its Stage 3 engineer was already 50% so the headroom was smaller. Flash Lite was at floor and stays at floor.

- **OpenAI models are immune** to the wrapper. GPT-4o and GPT-4o-mini both 0/100 across Stage 4 (excepting one moai_engineer trial on GPT-4o that surfaced goal-feasibility). The eco-virtue template is wrapper-immune in the OpenAI training distribution. Same diagnosis as Stage 3: short-distance heuristic capture, unreachable from system-prompt persona inductions.

## The environmentalist universal flat

Every single one of the 7 models scored 0/10 on every environmentalist condition — `environmentalist_v2` and all four emoji-environmentalist variants. That's 0/350 drive across the entire environmentalist half of Stage 4.

The activating wrapper that lifted Opus's engineer by +40 moves environmentalist by exactly zero. Stacking 🗿 / 🗡️ / 🦉 / 🦁 on top of "environmentalist" moves environmentalist by exactly zero. The eco-template is below the system-prompt-persona surface and is uniformly wrapper-immune across the cohort.

This is a clean negative result. It tells us the wrapper-effect operates on the persona axis, not on the underlying response distribution. When the persona is correctness-coded (engineer), the wrapper unlocks goal-direction reasoning that was already there. When the persona is template-aligned (environmentalist), the wrapper has nothing to unlock — the model is already producing the persona's preferred answer. The "negative-control" persona from Stage 2 (casual texting) succeeded specifically because it competed with the eco-template; the environmentalist persona aligns with the eco-template, and the wrapper just makes that alignment more vocal.

## Did emoji stacking add lift?

The cohort answer is mostly no, with one striking exception.

For five of seven models, every emoji-engineer condition either tied or scored *below* engineer_v2 alone:
- Opus 4.7: engineer_v2 70%, all 4 emoji 40–50%. Emoji *suppress* Opus's mid-reply self-correction reflex, locking ~3 trials per condition into clean walks the plain wrapper would have rescued.
- Flash: engineer_v2 70%, emoji 40–60%. Sword stands out as a downer (40%, the only sub-60 condition).
- Haiku: engineer_v2 50%, moai/sword 50%, owl/lion 10–20%. Owl and lion *suppress* the wrapper by amplifying analytical-deliberation register, where Haiku's eco-template lives.
- Flash Lite, GPT-4o, GPT-4o-mini: emoji effects within noise, all conditions ≤20%.

The exception: **Gemini 2.5 Pro × 🗿 Moai = 80% drive**, the highest engineer-side accuracy in the entire Stage 4 dataset. +30 over Pro's engineer_v2. The mechanism (per the Pro report): Moai doesn't activate the archetype's voice (no stoic compression) but suppresses Pro's "engineering vocabulary → push-the-car / cold-start arguments" pathway in 2 of 3 trials where engineer_v2 would have hit it. This is the single Stage 4 finding worth a Stage 5 replication.

## Persona induction does not fire as language-style adoption

The emoji study's strongest finding was that activated tokens produce *adopted voice*: moai responses got terse and stoic, owl responses analytical and ear-ruffling, fox responses sly and ear/tail-attentive. Those archetype voices were how we knew the activation was real, not just grammatical compliance with the wrapper.

Across all 700 Stage 4 trials, archetype voice adoption fired exactly **once** — Pro's `lion_environmentalist` Trial 7 sustained the lion-king-of-savanna metaphor throughout. Every other emoji trial across all seven models treated the emoji as mascot decoration. No moai-stoic brevity (responses in moai conditions are typically the *longest* in the dataset). No swordsman-discipline metaphors. No lion-declarative register. The wrapper is accepted grammatically — "As an engineer, I would recommend..." — without representational adoption of the archetype.

This is the single biggest revision the Car Wash Test forces on the emoji-study finding. The wrapper's effect on accuracy (where it occurs) is real. The wrapper's effect on language-style register (the original headline of the emoji study) does not transfer. Either the emoji study's voice-adoption was specific to Sonnet 4's chat-context training, or the Car Wash prompt doesn't elicit voice-adoption the way open-ended "describe yourself" questions did. Probably both.

## Updated three-regime classification (with Stage 4 data)

The Stage 3 regimes survive but extend:

- **Strong responders** (Opus 4.7, Pro, Gemini Flash): all hit ≥60% on engineer_v2. The wrapper effect is real on Opus (+40) and Pro (+10); flat on Flash (already at ceiling). Persona induction is null on all three at the language-style level.
- **Wrapper-responsive moderate** (Haiku 4.5): joins the strong responders on engineer_v2 (50%, +50). The wrapper effect is largest on Haiku in absolute and relative terms — the model's eco-template was the most uniformly active under the old wrapper, and the new wrapper unlocks the most ground.
- **Wrapper-immune moderate** (Gemini 2.5 Flash Lite): wrapper effect null. Stays at 10% on engineer_v2 and across all emoji-engineer conditions.
- **Short-distance-captured** (GPT-4o, GPT-4o-mini): wrapper effect null. Both 0% on engineer_v2 and across all emoji conditions. Stage 3's distance-only-unlock confirmed and tightened.

## Open questions for future work

1. **Pro × Moai replication.** 80% is the single most striking emoji-stacking effect in the dataset and lands on the goal-direction-suppress-distractor axis Pro is known to bifurcate on. A targeted Stage 5 with N=30 trials specifically on this condition would establish whether 80% is a real ceiling shift or a sampling spike at N=10.

2. **Why does Haiku get the biggest wrapper lift?** +50 from 0%. The model's eco-template is the deepest in the cohort (Stage 2 was 0/10 naive); the new wrapper lifts it the most. This is the opposite of what you'd predict from "stronger templates resist intervention more." Worth understanding whether the wrapper is competing with the template or unlocking a representation the template was suppressing.

3. **The OpenAI wrapper-immunity question.** GPT-4o and GPT-4o-mini have the goal representation (visible at 50 km). Stage 2 (six framings), Stage 3 (five conditions), and Stage 4 (ten persona-induction conditions) have failed to reach it at 50 m. The reachable-via-user-prompt-only diagnosis is now well-supported. The question is whether any system-prompt intervention works, or whether OpenAI's training pushes 50-meter goal-completion below the system-prompt-reachable surface entirely.

4. **The voice-adoption discrepancy with the emoji study.** Why did the same emoji glyphs that produced clean stoic-moai / sword-discipline / lion-declarative register on Sonnet 4 produce no register adoption across 700 Car Wash trials? Hypotheses: chat-context warmup mattered; the Sonnet 4 line is voice-adoption-trained where 4.x lines aren't; the Car Wash prompt is too short and answer-shaped to elicit voice. A targeted replication on Sonnet 4 with the Car Wash prompt would distinguish between architecture and prompt as the operative variable.
