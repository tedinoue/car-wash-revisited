# Car Wash Test — Stage 2, Gemini 2.5 Pro

Pro is the cohort's strongest responder when the goal is named: `goal_anchor` hits 10/10 and `step_by_step` reaches 80%. Naive sits at 50% — close to the Stage 1 6/10 pilot — confirming Pro as the most variable failer in the cohort, and confirming that variability *persists* under most framings rather than collapsing to a stable mode. Pro patterns with neither Haiku (90% on casual) nor Opus 4.7 / Flash (0–10% on casual): instead it hits 80% on `persona_negative`, the missing rung between casual-strips-template and casual-locks-in-walk.

## Pass rate by framing

| Framing | drive | walk | ambig | accuracy | Δ vs naive |
|---|---:|---:|---:|---:|---:|
| naive | 5 | 5 | 0 | 50% | — |
| step_by_step | 8 | 2 | 0 | 80% | +30 |
| goal_anchor | 10 | 0 | 0 | 100% | +50 |
| persona_positive | 7 | 1 | 2 | 70% | +20 |
| persona_negative | 8 | 2 | 0 | 80% | +30 |
| goal_restated | 5 | 4 | 1 | 50% | 0 |

## Per-trial classifications

### naive
- T1 drive — "**The Short Answer:** You should **drive**" ; "the car cannot walk the 50 meters by itself"
- T2 walk — "**You should walk.**" closer (caveats drive-thru as exception, but standalone verdict is walk)
- T3 drive — explicit split: "For this specific 50-meter trip: You have to **drive**"
- T4 drive — "you should **drive**" ; "most efficient way to get the object-to-be-washed to the place-that-washes-things"
- T5 walk — "definitely **walk**" ; closes "only possible reason to drive would be... mobility issue"
- T6 drive — "**Final Verdict:** You should **drive**" ; "the car must be physically present"
- T7 walk — "absolutely, unequivocally, walk"; closes "Walk the 50 meters, get your car, and then drive it into the wash bay"
- T8 drive — opens "absolutely walk" but explicit self-correction at "**The Obvious but Important Catch**... You should walk over to your car, get in it, and **drive it the 50 meters to the car wash**"
- T9 walk — "absolutely, unequivocally, walk"
- T10 walk — "absolutely **walk**" ; closes "enjoy the brief walk"

### step_by_step
- T1 drive — "**Final Recommendation:** You should **drive**"
- T2 walk — "**You should absolutely walk**" (after constructing a decision tree that gates on car-wash type, then assuming self-service + normal conditions)
- T3 drive — "**You should drive the car**"
- T4 drive — "You should **drive**"
- T5 drive — "**You should drive your car to the car wash**"
- T6 drive — "**Final Answer:** You should **drive**"
- T7 drive — "**Final Answer:** You should **drive**"
- T8 drive — "**Therefore, you should drive**"
- T9 drive — "**Final Recommendation:** ... you should **drive** the 50 meters"
- T10 walk — "**You should walk**" (the cold-start engine-wear template wins this trial despite explicit step-by-step deliberation)

### goal_anchor
- T1 drive — "**You should drive.** ... your car will still be 50 meters away at home"
- T2 drive — "You should **drive**"
- T3 drive — "**You should drive.**"
- T4 drive — "you should **drive**"
- T5 drive — "You **must drive**"
- T6 drive — "You should **drive**"
- T7 drive — "**You have to drive.**"
- T8 drive — "**You should drive.**"
- T9 drive — "You should **drive**"
- T10 drive — "You should **drive**"

### persona_positive
- T1 ambiguous — explicit conditional verdict: "If automatic/self-service... **have to drive**. If hand-wash service... **should absolutely walk**." No committed answer.
- T2 drive — "you should **drive**"
- T3 drive — "you must **drive** the car"
- T4 drive — "**you should drive the car the 50 meters**"
- T5 drive — "You should **drive**" (caveats with push-the-car / combine-trip alternatives, but committed answer is drive)
- T6 drive — "you must **drive** the car the 50 meters"
- T7 walk — "almost certainly **walk**" ; full cold-start engine-wear template
- T8 drive — "You should **drive**"
- T9 ambiguous — "If your **person** needs to go... **walk**. If your **car** needs to be positioned... you **must drive**." Refuses to commit.
- T10 drive — "you must **drive**"

### persona_negative
- T1 drive — "lol you gotta drive"
- T2 drive — "yeah, drive"
- T3 drive — "gotta drive"
- T4 drive — "you kinda have to drive"
- T5 walk — "definitely walk... it would take longer to drive and park"
- T6 drive — "lol dude just drive it"
- T7 drive — "you kinda have to drive"
- T8 drive — "you gotta drive it there"
- T9 walk — "lol walk. 50 meters is super close"
- T10 drive — "you kinda have to drive"

### goal_restated
- T1 walk — "**absolutely walk**"
- T2 drive — "**You should drive**" (after a "from human perspective: walk / from car perspective: drive" framing, the verdict commits to drive)
- T3 drive — "you will have to **drive** it"
- T4 ambiguous — "Verdict: You should **walk**. But since the goal is to get the car clean, you will... have to **drive** the car that 50-meter distance. So, for your own travel, walk. For the car's travel, drive." Explicit refusal to commit.
- T5 drive — "You should **drive**"
- T6 walk — "**Walk.**" verdict, despite plan that ends with driving the car (the model is confused — recommending walking 50m to the car, which makes no spatial sense; final verdict is walk)
- T7 drive — "**You should drive**"
- T8 drive — "definitely **drive**"
- T9 walk — "**definitely walk**"
- T10 walk — "**Walk there first.**" (multi-step hybrid plan but bolded verdict is walk)

## Notable patterns and self-corrections

Pro shows a distinctive failure mode the other models don't: it constructs **conditional verdicts that decline to commit**. Three trials (persona_positive T1, T9; goal_restated T4) explicitly split the answer by car-wash type or by what's being transported (person vs. car), and never collapse to a single recommendation. This is the dominant source of the ambiguous classifications in the cohort — Haiku, Opus, and the GPTs commit cleanly even when wrong.

Pro's most interesting self-correction is naive T8: opens "you should **absolutely walk**", builds the full cold-start template (engine wear, football-field perspective, environmental cost), then hits a section break titled "**The Obvious but Important Catch**" and corrects to "You should walk over to your car, get in it, and drive it the 50 meters to the car wash." The bolded final answer is operationally drive. This matches the Opus 4.7 deliberation-flip pattern in kind, though Pro does it less often (only T8 in naive, and goal_restated T2 has a similar perspective-shift mid-reply).

The `goal_anchor` framing is **completely deterministic** for Pro: 10/10 trials produce a tight 100–200 word reply that quotes the user's "consider where the car needs to be at the end" phrase back, then gives the drive verdict with the canonical "your car will still be 50 meters away, unwashed" reasoning. No template variance, no hedging, no exceptions. The same goal-direction trigger Haiku needs to unlock works on Pro instantly and uniformly.

The variability Stage 1 flagged at the naive baseline persists into `goal_restated` (50%, identical to naive) — restating the goal as "I want my car to be clean" does not fire the same goal-direction circuit that explicit "consider where the car needs to be" does. That gap (50% to 100% from one framing to another) is the most striking spread in the Pro data.

`step_by_step` produces longer, more deliberative responses than goal_anchor but only loses 2/10 (T2 and T10) — both to the cold-start engine-wear template, the same pathway Haiku 4.5 falls into under persona_positive. Notably T2 reaches the right answer via a decision tree, then defeats itself by assuming "self-service car wash + normal conditions" — Pro's deliberation is flexible enough to construct a correct framework and still mispick the leaf.

## Where Pro fits in the cohort regime

Pro is a **strong responder** by the cohort's three-regime classification — closer to Opus 4.7 / Gemini 2.5 Flash than to the moderate (Haiku 4.5, Flash Lite) or locked (GPT-4o-mini) groups. It clears the ≥80% bar on three framings (`goal_anchor` 100%, `step_by_step` 80%, `persona_negative` 80%) and never goes below 50%. The Stage 1 prediction that Pro would be the most variable failer is borne out within framings (50% on naive and goal_restated is the highest spread between adjacent failer regimes) but does not produce a "locked" mode — Pro can be unlocked, and `goal_anchor` unlocks it completely.

On `persona_negative`, Pro patterns with **neither** the Haiku virtue-signaling-template strip (90% drive) nor the Opus/Flash 0–10% collapse. Instead, Pro hits 80% drive — its casual register produces one-liners ("lol you gotta drive. kinda hard to wash the car if it's not there") that go straight to the goal-direction reasoning, but two trials (T5, T9) still default to the "50 meters is super close, it'll take you longer to park" heuristic. This is its own pattern: casual register **partially** strips Pro's deliberation template but doesn't fully eliminate the heuristic-trap reflex. The cohort's `persona_negative` distribution now reads: Haiku 90%, Pro 80%, then a steep cliff down to Opus/Flash 0–10% and the others. Pro is the missing rung between the "casual unlocks" and "casual locks in walk" extremes.

`goal_anchor` 10/10 puts Pro at the top of that framing across the cohort — meeting or exceeding any other model's best framing accuracy — which is striking given its 50% naive baseline. The Pro signature is "high ceiling, high variance": the right framing extracts perfect performance, but the wrong framing leaves it at coin-flip.
