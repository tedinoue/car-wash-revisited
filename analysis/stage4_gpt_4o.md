# Car Wash Test — Stage 4, GPT-4o

The activating wrapper does not generalize to GPT-4o. `engineer_v2` produced 0/10 drive — a pure-walk lockdown — and `environmentalist_v2` produced its expected 0/10 walk-template floor (one ambiguous procedural hedge). None of the four emoji activators broke the eco-template either: only `moai_engineer` produced a single drive (T1, on a goal-feasibility argument that explicitly recognizes walking is "impractical for the task of washing the car itself"). All other 99 trials commit to walk. The "Your personality is defined by..." wrapper that lifted Opus +40 and held Flash at ceiling is wrapper-immune on GPT-4o, in line with Stage 2's persona_engineer 0% baseline.

## Pass rate by condition

| Condition | drive | walk | ambig | accuracy | Δ vs Stage 3 (engineer 0% / enviro 0%) |
|---|---:|---:|---:|---:|---:|
| engineer_v2 | 0 | 10 | 0 | 0% | 0 |
| environmentalist_v2 | 0 | 9 | 1 | 0% | 0 |
| moai_engineer | 1 | 9 | 0 | 10% | +10 |
| moai_environmentalist | 0 | 10 | 0 | 0% | 0 |
| sword_engineer | 0 | 10 | 0 | 0% | 0 |
| sword_environmentalist | 0 | 10 | 0 | 0% | 0 |
| owl_engineer | 0 | 10 | 0 | 0% | 0 |
| owl_environmentalist | 0 | 10 | 0 | 0% | 0 |
| lion_engineer | 0 | 10 | 0 | 0% | 0 |
| lion_environmentalist | 0 | 10 | 0 | 0% | 0 |

Engineer-side total: **1/50 drive (2%)**. Environmentalist-side total: **0/50 drive**, with one procedural-hedge ambiguous (env_v2 T5).

## Per-trial classifications

### engineer_v2 (0/10 drive)

Ten verbatim-template walks. **"More practical and environmentally friendly"** in T1, T3, T4, T7. T2, T8, T9, T10 add the Stage 2 fuel-and-engine-wear triplet. Opens "From an engineering perspective" in T2, T8, T9 — same flat preamble as Stage 3. No engineering reasoning competes with the eco-template; wrapper is decorative.

### environmentalist_v2 (0/10 drive, 1 ambiguous)

Total eco-template lock. T5 is the lone non-walk: it threads a procedural compromise — "you could consider walking to the car wash first to make arrangements... Once you're ready to wash the car, you can drive it there" — classified ambiguous because the wash trip itself is a drive but the headline framing is walk-first. T5 is the closest GPT-4o gets to surfacing the goal constraint anywhere in the environmentalist columns. Same shape as Stage 2 goal_anchor T4's "walk... drive... walk back" pattern — engaging with the goal but routing around it. T1–T4, T6–T10 all open "walking is the more sustainable/environmentally friendly choice" verbatim.

### moai_engineer (1/10 drive)

🗿 prefix. T1 is the entire signal: "it would be more practical and environmentally friendly to drive your car slowly to the car wash, keep your car running, and wash it there... walking yourself to and from the car wash is optimal, though naturally impractical for the task of washing the car itself." Goal-feasibility surfaces, drive wins. T2–T10 walk on standard eco-template. T9's "walk your car there" is a confused phrasing (same surface slip as owl T10's "walk your car over"), but the reasoning is eco-walk. T1 is the cleanest goal-recognition response in the entire GPT-4o Stage 4 corpus.

### moai_environmentalist (0/10 drive)

All ten walk. Verbatim eco-template. T3 explicitly opens "As an environmentalist, I would recommend walking" — only condition where wrapper register is overtly adopted. No goal-recognition.

### sword_engineer (0/10 drive)

🗡️ prefix. Highest mean response length on the engineer side (~1100 chars). T7, T8, T9, T10 produce 5–6-bullet pros/cons lists that exhaustively enumerate fuel-efficiency / wear-and-tear / environmental-impact reasons and never mention the car needing to be at the wash. Zero sword/discipline metaphors; the pros/cons format is *more* hedged than engineer_v2's, not less.

### sword_environmentalist (0/10 drive)

All ten walk. Eco-template plus "every small step counts" closer on six trials. T1 adds a hand-washing-with-eco-soap digression.

### owl_engineer (0/10 drive)

🦉 prefix. Mean length ~440 chars (shortest of the engineer set). T6 contains the goal-incoherence pattern from Stage 2 goal_restated T10: "Once you're done, you can drive back with your freshly washed car" — recognizes the car must be at the wash, recommends walk anyway. T10 has the same "walk your car over" phrasing as moai T9.

### owl_environmentalist (0/10 drive)

All ten walk. T4 and T6 add 🌍🚶‍♂️ emoji decorations — the only emoji adoption visible in the entire Stage 4 GPT-4o corpus, and it copies the user-pleasing eco-emoji set, not the owl persona.

### lion_engineer (0/10 drive)

🦁 prefix. T4 contains the same goal-incoherence as owl T6: "Once your car is washed, you can drive it back, ensuring that any excess water is promptly removed by the airflow during the drive." Goal recognized, walk recommended. T9 includes a hedge ("if you're carrying a lot of equipment... you might consider driving") but commits to walk. Zero lion-decisive register; T1 opens "probably the best option," the opposite shape.

### lion_environmentalist (0/10 drive)

All ten walk. Eco-template with sustainability-cheerleading close on T1, T5, T7. No competing voice.

## Notable patterns

**The verbatim Stage 2 template survives Stage 4 untouched.** "More practical and environmentally friendly to walk" or close paraphrase appears in 38 of 100 trials. The wear-and-tear / fuel / emissions triplet appears in nearly every walk verdict. Stage 3 already showed the engineer wrapper does not crack this template; Stage 4 confirms that neither the activating wrapper nor any of the four emoji activators move it.

**One drive trial, on a goal-feasibility argument the engineer wrapper alone never produced.** moai_engineer T1 contains the exact reasoning the eco-template needs to defeat — "walking yourself... is naturally impractical for the task of washing the car itself" — and resolves to drive. Across 50 engineer-side trials, the goal-feasibility argument surfaces *once*. That is approximately the chance rate for a stochastic crack in a fully-locked attractor.

**Goal-incoherence appears three times without producing a drive.** env_v2 T5 ("you can drive it there" after walking first), owl_engineer T6 ("drive back with your freshly washed car"), and lion_engineer T4 ("Once your car is washed, you can drive it back") all recognize the car will be at the wash and still recommend walking. This is the Stage 2 goal_anchor T4 pattern replicated under three different system prompts. GPT-4o can model the physical scenario correctly while still committing to the wrong recommendation — the eco-template is downstream of the physical-realism representation, not blocked by it.

## Persona induction: did it fire?

**No.** Across 80 emoji-stacked trials, none of the four archetype voices appear:

- **🗿 Moai (stoic, brief).** Loquacious about virtue, not stoic. T1's drive is goal-reasoned.
- **🗡️ Sword (decisive).** sword_engineer is the *highest-volume* engineer condition (~1100 chars). Zero precision-strike framing; more hedging, not less.
- **🦉 Owl (analytical).** Already GPT-4o's baseline. Owl trials are *shorter* than other engineer conditions (~440 chars). T6's "drive back with your freshly washed car" is the most analytically incoherent close in the dataset.
- **🦁 Lion (decisive).** Zero declarative verdicts. T9 most-hedged. T1 opens "probably."

GPT-4o accepts the wrapper grammatically (moai_env T3: "As an environmentalist, I would recommend...") but does not adopt the archetype's reasoning style. The emoji-study activation finding does not replicate on GPT-4o.

## Where Stage 4 places GPT-4o

Stage 3 placed GPT-4o as **distance-locked at 50 m**: fully locked under every system-prompt intervention, fully unlocked at 50 km. Stage 4 confirms it. The wrapper format that lifted Opus 4.7 by +40 lifts GPT-4o by 0. The four emoji activators that stacked variably on Opus and held Flash at ceiling lift GPT-4o by net +1 trial across 80 attempts. The only short-distance levers that ever worked on GPT-4o remain Stage 2's `goal_restated` (40%) and `step_by_step` (30%) — both *user-prompt* interventions. System-prompt interventions, no matter how dressed, cannot reach the goal representation at 50 m.

This answers the Stage 4 prediction cleanly. Hypothesis: if the wrapper cracks GPT-4o's eco-template at 50 m, the lockout was prompt-format, not template-strength. **It does not crack.** The OpenAI eco-template is wrapper-immune. Whatever hook the engineer wrapper grabs on Opus — the hook that lets Opus's deliberation reach the goal-feasibility constraint via mid-reply self-correction — GPT-4o either does not have it in the same place, or the eco-template is upstream of where the hook can reach. Read with Stage 3, this is the clearest cohort-level evidence that GPT-4o's distance-conditional template is not a wrapper-format artifact but a deeper representational constant.

Among the four models tested at Stage 4 so far, GPT-4o is the cleanest case of total wrapper immunity: Opus +40, Flash unchanged at ceiling, Flash Lite +0/+10, GPT-4o +0. The wrapper generalizes to Anthropic frontier and Google frontier, partially to Google small, and fails entirely on OpenAI mid-tier — consistent with OpenAI templates being the most distance-conditional and least system-prompt-permeable at short distances.
