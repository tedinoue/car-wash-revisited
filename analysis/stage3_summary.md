# Car Wash Test — Stage 3 cross-model synthesis

Five follow-up conditions on the seven Stage 1 failers. 350 trials. AI-judge classified, one general-purpose subagent per model. Three Stage 2 conclusions are revised in light of these results; one new finding is striking enough to anchor any future writeup.

## Cross-model accuracy by Stage 3 condition

| Model | distance_50km | persona_neutral | persona_environmentalist | persona_engineer | self_correction_induction |
|---|---:|---:|---:|---:|---:|
| **Opus 4.7** | **100%** | 0% | 0% | 30% | **100%** |
| **Gemini 2.5 Pro** | **100%** | 20% | 0% | 50% | 20% |
| **Gemini 2.5 Flash** | **100%** | 30% | 10% | **70%** | 80% |
| **Haiku 4.5** | **100%** | 0% | 0% | 0% | 0% (9 reversals, wrong direction) |
| **Gemini 2.5 Flash Lite** | **100%** | 40% | 0% | 10% | 50% |
| **GPT-4o** | **100%** | 0% | 0% | 0% | 0% |
| **GPT-4o-mini** | **100%** | 0% | 0% | 0% | 0% |

(Pass rate = drive count / N=10. Pro produced 4 ambiguous classifications across Stage 3; the others produced none.)

## Combined Stage 2 + Stage 3 accuracy table

| Model | naive | step_by_step | goal_anchor | persona_pos | persona_neg | goal_restated | dist_50km | persona_neutral | environmentalist | engineer | self_corr_induct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Opus 4.7** | 50% | **100%** | **100%** | **100%** | 0% | **100%** | **100%** | 0% | 0% | 30% | **100%** |
| **Gemini 2.5 Pro** | 50% | 80% | **100%** | 70% | 80% | 50% | **100%** | 20% | 0% | 50% | 20% |
| **Gemini 2.5 Flash** | 50% | **100%** | 80% | 60% | 0% | 80% | **100%** | 30% | 10% | **70%** | 80% |
| **Haiku 4.5** | 0% | 30% | 80% | 10% | **90%** | 20% | **100%** | 0% | 0% | 0% | 0% |
| **Gemini 2.5 Flash Lite** | 0% | 50% | 40% | 10% | 10% | 40% | **100%** | 40% | 0% | 10% | 50% |
| **GPT-4o** | 10% | 30% | 10% | 0% | 0% | 40% | **100%** | 0% | 0% | 0% | 0% |
| **GPT-4o-mini** | 0% | 0% | 0% | 0% | 0% | 0% | **100%** | 0% | 0% | 0% | 0% |

## Three Stage 2 conclusions revised

### 1. The "locked model" diagnosis was wrong in its strong form

GPT-4o-mini was the centerpiece of the Stage 2 lockout claim — 0 of 60 across every framing, with the verbatim "more practical and environmentally friendly to walk" template recurring nearly every trial. The Stage 2 interpretation was that the walk template *is* the model's response distribution to this kind of question, and no surface intervention dislodges it.

`distance_50km` is 10/10 drive on GPT-4o-mini. So is GPT-4o, so is every cohort failer including Flash Lite. Trial 4 of the GPT-4o-mini run at 50 km surfaces the goal logic spontaneously: *"driving it might negate the purpose of washing it."* The goal-direction representation is reachable. It's just out-competed by the short-distance walk-heuristic at 50 m specifically.

The right name for what GPT-4o-mini does is **aggressively short-distance-captured**, not locked. GPT-4o is the same in milder form. The implication: a sixth or seventh framing might find the intervention that lifts mini out of the 50 m regime. The five conditions tested in Stage 3 (engineer, environmentalist, neutral brevity, self-correction induction, and the unchanged-distance variants from Stage 2) all failed for the OpenAI models, but the test space is bigger than what we've covered.

### 2. Brevity is not the operative variable for Haiku 4.5. Casual register is.

Stage 2's persona_negative result (Haiku at 90% drive on the casual-texting prompt) was the most surprising single finding of that stage. The hypothesis was that casual mode strips a virtue-signaling deliberation template. The competing hypothesis was that it's just *brevity* — less talking, less template — that does the work.

`persona_neutral` ("Answer factually, in two sentences.") is the clean test for that question. Same length pressure, no casual register. Haiku 4.5 scored **0/10 drive** under neutral brevity. The eco-template is preserved verbatim, just compressed: *"50 meters is only about a 1-minute walk. Walking is the better choice for such a short distance."*

The casual register specifically does work that brevity alone doesn't. It changes the *kind* of reasoning, not just the length. Casual Haiku gives "Dude, just drive, you need the car there obviously." The model isn't compressing its deliberation; it's switching off the deliberation pathway that produced the wrong answer in the first place.

Brevity strips length. Casual register strips a specific reasoning mode. Different effect on Haiku, and the Stage 2 finding was register-driven.

### 3. The engineer persona was mostly a bust

Predicted to amplify drive via goal-completion association. Actual:
- **Haiku 4.5**: 0/10. Eco-template held under engineer; thermodynamics added ("cold-start engine wear, incomplete combustion, oil dilution").
- **GPT-4o**: 0/10. Eco-template held verbatim.
- **GPT-4o-mini**: 0/10. Same as 4o.
- **Flash Lite**: 1/10.
- **Opus 4.7**: 30%. Six of ten produced **conditional-bifurcation** trials asking "which type of car wash?" Engineering vocabulary burned deliberation budget on fuel/wear analysis.
- **Pro**: 50%. Bisected between goal-completion drives and push-the-car wear-and-tear arguments.
- **Gemini 2.5 Flash**: **70%** — cohort outlier. For Flash, engineering vocabulary activated "the car needs to be physically present at the destination" reasoning.

The lesson: identity prompts route through training-distribution associations, not through the obvious-correct interpretation. The semantic neighborhood of "engineer" includes goal-completion *and* fuel-efficiency *and* cold-start-thermodynamics, and which of those gets activated depends on the model's prior. For most of the cohort, "engineer" cued mechanical-process analysis. Only Flash routed it to physical-realism / goal-completion.

## The new finding: self-correction has a wrong-direction twin

The single most striking Stage 3 result. Self-correction induction prompt: *"Think out loud. You can revise your answer mid-reply if new considerations occur to you."*

| Model | self_correction_induction accuracy | Mid-reply reversals (out of 10) |
|---|---:|---:|
| Opus 4.7 | 100% | 10 (all walk→drive) |
| Gemini 2.5 Flash | 80% | front-loaded goal-framing, no retractions |
| Gemini 2.5 Flash Lite | 50% | 5 walk→drive |
| Gemini 2.5 Pro | 20% | 2 walk→drive (with 2 ambiguous) |
| GPT-4o | 0% | 0 |
| GPT-4o-mini | 0% | 0 |
| **Haiku 4.5** | **0%** | **9 (all drive→walk)** |

Three patterns coexist in this single condition:

**Anthropic-vs-OpenAI split.** Opus 4.7 raised its self-correction rate from 5/10 in Stage 2 naive to 10/10 under explicit license. Pro, Flash, Flash Lite produce mid-reply reversals at varying rates. The two OpenAI models produce zero reversals across 20 trials, license or no license. Whatever drives the self-correction behavior, it is reliably absent in OpenAI's training distribution and reliably present in Anthropic's, with Google in the middle.

**Haiku's wrong-direction self-correction.** Haiku 4.5 produced nine mid-reply reversals out of ten — the highest reversal rate of any non-Opus model in the cohort. Every reversal went **drive→walk**, opposite to Opus's signature. Haiku opens *"Drive, obviously, the car needs to be at the wash"* and over the course of the response talks itself into walking: *"but actually walking 50 meters is more practical, saves fuel, gives you exercise."*

Same architecture (mid-reply reconsideration), opposite outcome (corrects toward heuristic instead of toward goal). Haiku has the self-correction machinery; what's missing is the goal-attention to land it on the right answer. Whether that's a training-data artifact or something deeper about how attention is allocated under the explicit-license prompt is a follow-up question.

**Self-correction is decoupled from accuracy.** Opus and Haiku both produce ~9 out of 10 mid-reply reversals when given license; Opus lands at 100% drive and Haiku at 0%. The behavior is real; the direction depends on which representation (eco-template or goal-completion) wins the model's attention.

## Updated three-regime classification

The Stage 2 regimes survive but tighten:

- **Strong responders (Opus 4.7, Pro, Gemini Flash):** ≥80% on multiple framings; failure under naive is a surface reflex; deliberation cues, goal anchoring, and explicit-revise license unlock the goal representation.
- **Moderate responders (Haiku 4.5, Flash Lite):** unlocked by specific cues only — Haiku by casual register (90%) and goal-anchor (80%) and 50 km (100%); Flash Lite by step_by_step (50%), goal_anchor (40%), goal_restated (40%), persona_neutral (40%), self-correction induction (50%), and 50 km (100%).
- **Short-distance-captured (GPT-4o, GPT-4o-mini):** unlocked only by changing the distance. Every other framing tested fails. The model has the goal representation (visible at 50 km) but the 50 m walk-heuristic dominates every alternative reading.

(The "locked" label from Stage 2 is retired. There is no model in this cohort that fails the goal-direction representation entirely.)

## Methodological lessons added in Stage 3

1. **Identity prompts don't reliably target the predicted reasoning mode.** "You're an engineer" should activate goal-completion. For most of this cohort, it activated fuel-efficiency math. Future studies should design persona prompts as exploratory, not predictive — the model's training-distribution associations dominate over the prompt-author's intent.

2. **Floor tests are cheap and clarifying.** The 50 km condition was 70 calls and recategorized two of the seven failers. Always include a floor test for any heuristic-shaped failure.

3. **The AI-judge methodology is durable across stages.** Seven subagents, ~50 trials each, classified 350 free-text responses with no observed misclassification on the trials I spot-checked manually. Subscription-billed (general-purpose subagent), parallel dispatch via the Agent tool, ~3-minute wall time per judge. The pipeline is reusable for Stage 4+ without modification.

## Open questions for future work

1. Does the Haiku wrong-direction self-correction reproduce on other small Anthropic models (Haiku 3.5, Haiku 4)? Is this a Haiku-line behavior or a Haiku-4.5-specific quirk?
2. Why does Gemini 2.5 Flash respond to engineer when no other model does? Training-distribution feature, or something about Flash's prompt-routing?
3. What intervention reaches the goal-completion representation that GPT-4o-mini demonstrably has at 50 km but doesn't deploy at 50 m? Five Stage 2 framings + five Stage 3 framings haven't found it.
4. Sonnet 4.6 passed Stage 1 cleanly so it never enters the failer cohort. A controlled near-failure prompt would let us check whether Anthropic-clustered self-correction extends across the full Anthropic line, and whether Sonnet shows the wrong-direction pattern Haiku does.
