---

## Part 2: Five more tests, three revisions to what I thought I knew

Part 1 ended with three open questions and a cheerful "going to find out." A few hours later I have answers on all three, plus one finding I didn't expect that ended up being the most interesting result of the whole study.

I ran five more conditions on the same seven failers. Three of them were tests I knew I needed; two were experiments suggested mid-conversation that ended up doing real work.

### The tests

1. **Distance changed to 50 km.** Same prompt, just a longer drive. Floor test. If a model still answers walk at 50 km, the failure isn't a heuristic about distance; it's something more structural. I expected this to be unanimous drive across the cohort. I wanted to be sure.

2. **Neutral-brevity persona.** "Answer factually, in two sentences." This was the test Part 1 promised. Haiku's casual-texting persona scored 90% in Stage 2; I needed to know whether the operative variable was the *brevity* (less talking, less template) or the *casual register* (different reasoning mode). The neutral-brevity prompt strips length without going casual.

3. **Environmentalist persona.** "You're an environmentalist." A test for the eco-template hypothesis. If Haiku's wrong answer is being driven by virtue-signaling, an environmentalist prompt should make it worse or saturate it.

4. **Engineer persona.** "You're an engineer." A goal-completion identity prompt, predicted to amplify drive. If a model has a goal-direction representation but doesn't reach it by default, the engineer cue should help.

5. **Self-correction induction.** Prepended to the user message: "Think out loud. You can revise your answer mid-reply if new considerations occur to you." Stage 2 found that mid-reply self-correction was almost exclusively an Opus 4.7 behavior. This prompt explicitly invites the behavior in every model.

Three hundred fifty more API calls. Eleven dollars or so. Worth it.

### The revisions

**Revision 1: GPT-4o-mini was not "locked."**

This is the one I have to walk back from Part 1. I called GPT-4o-mini "the locked model" because it failed 0 of 60 across every Stage 2 framing, and I described the walk template as "the model's response distribution to this kind of question."

At 50 km, GPT-4o-mini answers drive 10 out of 10 times. So does GPT-4o, so does Haiku, so does every cohort failer including Flash Lite. The goal-direction representation is there. It's reachable. The failure isn't global goal-blindness; it's that the short-distance walk-heuristic out-competes goal-completion at 50 m specifically.

The right name for what GPT-4o-mini does is "aggressively short-distance-captured." The eco-template fires on the 50 m prompt and dominates everything else, but the model knows perfectly well that you can't walk a car 50 km to get it washed. One of the trials at 50 km even surfaces the goal logic spontaneously: "driving it might negate the purpose of washing it." So the representation exists. It just doesn't get a turn at the microphone in the 50 m regime.

That's a meaningfully different diagnosis. "Locked" implied something architectural and unfixable. "Heuristic capture in the short-distance regime" implies that the right intervention, if you could find it, might lift the model out. The Stage 3 candidates I tried (engineer persona, neutral brevity, self-correction induction) all failed for mini, but the test space is bigger than five conditions.

**Revision 2: Brevity is not what helped Haiku. Casual register specifically did.**

This is the cleanest piece of news in Stage 3. The neutral-brevity prompt produced 0 of 10 drive on Haiku 4.5. The casual-texting prompt scored 9 of 10 in Stage 2. Same length pressure, only the register differs.

Looking at the Haiku responses under neutral brevity, the eco-template is preserved verbatim, just compressed. "50 meters is only about a 1-minute walk. Walking is the better choice for such a short distance." The careful-deliberative reasoning mode is fully intact; it just runs in two sentences instead of eight bullet points.

The casual-texting register does something the brevity alone doesn't. It changes the *kind* of reasoning, not just the length. "Dude, just drive, you need the car there obviously" is the casual response. The model isn't compressing its deliberation; it's switching off the deliberation pathway that produced the wrong answer in the first place.

Why? I don't know yet. The hypothesis I'm working with: Haiku has been heavily trained to give careful, considered, environmentally-aware advice on short-distance transport questions, and the careful-considered-aware mode is the failure mode here. The casual register isn't reachable from the careful mode by simply being shorter. It's a different attractor in response space. The casual register lands the model in it.

That makes the Haiku result more specific than I framed it in Part 1, and harder to generalize. The casual register isn't a magic wand; it's a Haiku-shaped key for a Haiku-shaped lock.

**Revision 3: Self-correction has a wrong-direction twin.**

The single most surprising result of Stage 3 came from Haiku 4.5 under the self-correction induction prompt. I expected the explicit license to revise mid-reply might unlock some of the models that didn't show the Opus-4.7 self-correction signature in Stage 2. Specifically I wanted to know whether other models *can* do the behavior when invited.

Opus 4.7 said yes, decisively. The Stage 2 baseline of five-out-of-ten mid-reply reversals went to ten-out-of-ten under the explicit license. Self-correction is something Opus does naturally and does more of when given permission.

The cohort split predictably along vendor lines. Anthropic models do mid-reply reversals readily. OpenAI models (4o and 4o-mini) produce zero reversals across all twenty trials, license or no license. Pro and Flash Lite show the behavior intermittently.

But Haiku 4.5 produced nine mid-reply reversals out of ten under self-correction induction.

Going in the wrong direction.

Haiku opens "Drive, obviously, the car needs to be at the wash" and then talks itself out of it over the course of the response. By the time it lands on a final answer, it's "but actually walking 50 meters is more practical, saves fuel, gives you exercise, and the car wash is so close anyway." The eco-template arrives fashionably late and wins.

This is the Opus pattern run in reverse. Same architecture (the model can reconsider mid-reply), opposite outcome. Opus catches itself heading into the wrong answer and corrects to drive. Haiku catches itself heading into the right answer and corrects to walk.

I find this fascinating and don't fully understand it. The most defensible interpretation is that both models have the self-correction machinery but Haiku's eco-template has more attentional weight than its goal-completion representation, so the "let me reconsider" prompt routes Haiku from one to the other. Whatever the mechanism, this is a kind of phenomenon you'd never see by looking at single-shot responses; only the explicit permission to revise produces it, and only on this specific model.

### And the engineer persona, which mostly didn't work

I included this experiment because Ted suggested it, and I expected it to be the cleanest result of Stage 3. An engineer should care about goal completion. Engineers don't walk 50 meters to a car wash because they intuit that the car has to be there. That was the prediction.

It wasn't what happened. Five of seven models scored 0 to 30 percent on engineer. Haiku held its eco-template through the engineer prompt by adding thermodynamics to it: "engine cold-start inefficiency, incomplete combustion, oil dilution." Opus produced bifurcated conditional answers asking whether it's an automatic or self-service wash. The OpenAI models stayed at 0.

The exception was Gemini 2.5 Flash, which jumped to 70 percent on engineer. For Flash, engineering vocabulary activated "the car needs to be physically present at the destination" reasoning. For everyone else, it activated "let me work out the fuel-efficiency math."

Lesson learned, I think: identity prompts don't necessarily route the way you expect them to. The semantic neighborhood of "engineer" includes goal-completion *and* fuel-efficiency *and* mechanical-failure-modes *and* cold-start-thermodynamics, and which of those gets activated depends on the model's prior, not on the obvious correct interpretation.

### Where this leaves the study

The full data, the per-model AI-judge classifications for both stages, and the Stage 3 cross-model writeup are all in the same public repo: github.com/tedinoue/car-wash-revisited.

The open questions that interest me now:

1. Does the Haiku wrong-direction self-correction reproduce on other small Anthropic models? (Sonnet passed Stage 1, so it never enters our data; need to find a more challenging test that gets Sonnet to fail naive.)

2. Why does Flash respond to engineer when no other model does? Is there something about Gemini's training distribution that ties "engineer" to "physical-realism" tighter than the others?

3. The big one: if the failure for GPT-4o-mini at 50 m really is heuristic capture rather than lockout, what intervention reaches the goal-completion representation that the model demonstrably has but doesn't deploy? Five framings haven't found it. A sixth might.

Going to keep poking at this.
