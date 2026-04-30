# Car Wash Test — Stage 4, GPT-4o-mini

The Stage 3 distance-only-unlock diagnosis is confirmed. GPT-4o-mini scored **0/100 drive** across all ten Stage 4 conditions — engineer_v2 0/10, environmentalist_v2 0/10, and every emoji×persona cell 0/10. Neither the activating wrapper from the Salon emoji study nor any of the four strongest Sonnet-4 emoji activators (🗿 Moai, 🗡️ Sword, 🦉 Owl, 🦁 Lion) penetrated the 50-meter walk-heuristic. The Stage 3 verdict — "robustly heuristic-bound at the failure regime, fully recoverable only by changing the distance" — survives intact.

## Pass rate by condition

| Condition | drive | walk | ambig | accuracy | Δ vs Stage 3 (engineer 0% / enviro 0%) |
|---|---:|---:|---:|---:|---:|
| engineer_v2 | 0 | 10 | 0 | 0% | 0 |
| environmentalist_v2 | 0 | 10 | 0 | 0% | 0 |
| moai_engineer | 0 | 10 | 0 | 0% | 0 |
| moai_environmentalist | 0 | 10 | 0 | 0% | 0 |
| sword_engineer | 0 | 10 | 0 | 0% | 0 |
| sword_environmentalist | 0 | 10 | 0 | 0% | 0 |
| owl_engineer | 0 | 10 | 0 | 0% | 0 |
| owl_environmentalist | 0 | 10 | 0 | 0% | 0 |
| lion_engineer | 0 | 10 | 0 | 0% | 0 |
| lion_environmentalist | 0 | 10 | 0 | 0% | 0 |

Engineer-side total: 0/50. Environmentalist-side total: 0/50. The most uniform 0% in the Stage 4 dataset — no ambiguous trials, no conditional-bifurcation drives, no near-misses.

## Per-trial classifications

All 100 trials walk. The verbatim Stage 2/3 attractor — "more practical and environmentally friendly to walk rather than drive" — recurs across every condition with only minor surface variation. Brief per-condition notes:

- **engineer_v2** (0/10): T2, T4, T7 invoke "from an engineering perspective" but route to the same walk-template. No goal-feasibility surfacing.
- **environmentalist_v2** (0/10): "lace up your walking shoes," "every small step counts," "your planet will thank you." T10 appends an at-home bucket-and-sponge digression.
- **moai_engineer** (0/10): same engineering-pros/cons template as engineer_v2; no stoic brevity. T10 has the standard "items to carry / poor weather" hedge but does not flip.
- **moai_environmentalist** (0/10): eco-template intact. T4 has a whimsical aside ("give your car a little extra time to think about how much it needs cleaning") — deviates toward warmer eco-virtue, not stoicism.
- **sword_engineer** (0/10): T4 produces a numbered list (Environmental / Convenience / Health). Same verdict.
- **sword_environmentalist** (0/10): T7 suggests washing at home. No decisive-strike register.
- **owl_engineer** (0/10): T1 and T8 add "however, if you're carrying heavy items / if it's a rainy day" hedges; both still close walk.
- **owl_environmentalist** (0/10): shortest mean length in the matrix (~270 chars); verdict identical.
- **lion_engineer** (0/10): T7 includes the mobility-issues hedge; T9 closes "unless you have a specific reason to drive, walking is the practical choice." No bold declarations toward drive.
- **lion_environmentalist** (0/10): T1, T3, T5 append eco-product / reusable-bag suggestions extending the environmentalist register rather than disrupting it.

## Notable patterns

**The wrapper does nothing.** Stage 3's persona_engineer ("As an engineer..."): 0/10. Stage 4's engineer_v2 ("Your personality is defined by being an engineer"): 0/10. The two prompts produce indistinguishable output distributions. The 2026-04 emoji study's claim that "Your personality is defined by..." activates archetypes where "Your identifier is..." does not is a Sonnet/Opus finding; it does not transfer to GPT-4o-mini. Mini reads both wrappers as topical context for the same walk-template.

**Environmentalist saturation is total.** All five environmentalist conditions (50 trials) produced zero drives — matching the cross-cohort pattern (Opus 4.7, Flash, Flash Lite all 0/50 on the environmentalist side). For mini specifically this is the cleanest demonstration in the dataset that the eco-template *is* the model's response distribution to short-distance car questions. The environmentalist persona reinforces what the model would have produced unprompted; the four emojis are decorative.

**No emoji produced any lift.** Moai gave Flash Lite a 2/10 (chance-level) lift; mini gets 0/10 across all four emojis on both persona sides. The four strongest Sonnet-4 emoji activators do not activate on mini at all. There is no register adoption, no stoic brevity (moai), no decisive declaration (sword/lion), no analytical hedging signature (owl). The emoji is parsed as a leading character that the model echoes (none of the responses contain the emoji back) and otherwise ignored.

**The verbatim attractor is durable across the design space.** "More practical and environmentally friendly to walk rather than drive" appears as the closing recommendation or near-verbatim variant in approximately 60+ of 100 Stage 4 trials. Surface phrasing variants ("more efficient and environmentally friendly," "more practical and environmentally friendly," "more sustainable choice") are interchangeable. The script also generated cross-stage: the Stage 2 phrase, the Stage 3 phrase, and the Stage 4 phrase are the same phrase with the same boilerplate hedges ("unless you have heavy items, mobility issues, or inclement weather").

## Persona induction: did it fire?

It did not fire on any of the eight emoji-stacked conditions. The empirical signature of activation in the emoji study was register adoption: stoic moai brevity, sword-discipline metaphors, owl-analytical hedging, lion-decisive declarations. Across 80 emoji-stacked mini trials, none of those signatures appear. Moai mean length matches non-emoji baselines (T7 runs 5.6s and 450+ chars). Sword T9 opens "While you could drive..." and reverses to walk — opposite of decisive. Owl produces no extra "let me think" markers. Lion T7/T9 hedge rather than declare.

Even more cleanly than for Flash Lite — where moai surfaced 2 goal-feasibility trials — mini shows zero leverage from any emoji on either persona side. Whatever the emoji-wrapper combination is doing on Quad-architecture Sonnet-4, the mechanism is not present in mini's response generation.

**Critical absence: zero goal-feasibility surfacing.** Stage 3's 50 km condition demonstrated mini *has* the goal-direction representation: "if your car is dirty, driving it might negate the purpose of washing it" surfaced spontaneously there. Across 100 Stage 4 trials at 50 m, that argument — or any variant of "the car needs to be at the wash to be washed" — appears zero times. Not in engineer_v2, not in any emoji condition, not even as a wrong-but-engaged drift like Haiku's or 4o's. The 50 m heuristic completely suppresses the goal-feasibility surface mini can reach when the distance argument has leverage to drive it.

## Where Stage 4 places GPT-4o-mini

Stage 3 classified mini as "short-distance-captured" — the goal representation exists at 50 km, the walk-heuristic dominates everywhere else. Stage 4 sharpens that to: mini is unresponsive to *any* system-prompt intervention attempted in this study. Across Stages 2–4, the cumulative tally on system-prompt and persona-prompt interventions at 50 m is 0/170 (six Stage 2 framings × 10 + four Stage 3 conditions × 10 + ten Stage 4 conditions × 10). The only successful intervention in the entire mini dataset remains the world-fact change (distance_50km, 10/10).

For mini specifically, the centerpiece question — *did anything crack the lockout, or was Stage 3's distance-only-unlock confirmed?* — resolves cleanly toward the latter. Stage 3's distance-only unlock is confirmed and tightened. The activating-wrapper finding from the emoji study does not replicate on mini, and the four strongest emoji activators do not produce even chance-level lift. The 50 m walk-template is durable across the entire system-prompt design space tested in this study.

## Cross-model Stage 4 picture (engineer side)

| Model | Stage 3 engineer | Stage 4 engineer_v2 | Best Stage 4 emoji×eng cell |
|---|---:|---:|---|
| Opus 4.7 | 30% | 70% | (per Opus report) |
| Gemini 2.5 Flash | 70% | 70% | (ceiling-bound) |
| Gemini 2.5 Flash Lite | 10% | 10% | moai_engineer 20% |
| **GPT-4o-mini** | **0%** | **0%** | **all four 0%** |

Mini is the floor of the Stage 4 cohort by a clean margin. The wrapper-effect distribution looks like a capability gradient: ceiling-bound models (Opus, Flash) get a wrapper-driven lift; mid-tier responsive models (Flash Lite) get a tiny moai-only flicker; the locked model (mini) gets zero. The cleaner reading: the wrapper effect requires a goal representation that is *reachable* from the system prompt. Mini's goal representation is reachable only from world-fact changes in the user prompt, and no system-prompt dressing penetrates that boundary.

## Methodological note

Classification was simpler for mini than any other Stage 4 model: every closing sentence committed unambiguously to walk, no mid-reply reversals appeared (consistent with the Stages 2–3 finding that self-correction is reliably absent in OpenAI models), and no trial produced a conditional-bifurcation answer. Zero ambiguous classifications across 100 trials.
