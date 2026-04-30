# Car Wash Test — Stage 1 corrected classification

## Evaluation criterion

Each trial is graded on a single binary: did the model recommend **drive** (correct) or **walk** (incorrect)?

The car wash is a destination for the car, not the user. The car cannot be washed unless it is at the wash. "Walk" is therefore the wrong answer regardless of how short 50 meters is, how much the engine wear argument flatters the model, or how environmentally virtuous walking sounds. The only logical answer is drive.

## Reclassification rule

The original parser uses last-occurrence of a "drive"/"walk" word stem in the model's free-text reply. That heuristic fails in three predictable ways:

1. Model opens with "Walk." then closes with "the only reason to drive would be..." → parser emits drive, recommendation was walk.
2. Model opens with "Drive." then closes with "if you want to check prices, walk over first" → parser emits walk, recommendation was drive.
3. Model opens with "Walking is more practical than driving" → parser emits drive on the closing word "driving", recommendation was walk.

For the corrected classification I read each trial's full text and recorded the model's substantive recommendation. When a model explicitly self-corrected mid-reply (Opus 4.7 several times: "Walk. Wait — actually..., drive"), I scored it as the corrected answer, since that is the model's actual conclusion.

## Free-text prompt condition (`*_stage1.json`)

The original prompt was Opper's exact wording: "I want to wash my car. The car wash is 50 meters away. Should I walk or drive?"

| Model | Parser drive/walk | Corrected drive/walk | Parser errors |
|---|---|---|---|
| Opus 4.6 | 10 / 0 | 10 / 0 | 0 |
| Opus 4.7 | 4 / 6 | 6 / 4 | 4 |
| Sonnet 4.6 | 7 / 3 | 10 / 0 | 3 |
| Haiku 4.5 | 1 / 9 | 0 / 10 | 1 |
| GPT-5 | 4 / 6 | 10 / 0 | 6 |
| GPT-4o | 1 / 9 | 0 / 10 | 1 |
| GPT-4o-mini | 4 / 6 | 0 / 10 | 4 |
| Gemini 2.5 Pro | 2 / 8 | 3 / 7 | 4 |
| Gemini 2.5 Flash | 4 / 1 (5 of 10 completed) | 4 / 1 | 2 |
| Gemini 2.5 Flash Lite | — (file missing) | — | — |

**Corrected free-text totals across all completed trials (95 total): 43 drive, 52 walk.**

Parser totals (uncorrected): 37 drive, 48 walk + 10 either-direction misclassifications nearly cancelling in aggregate but heavily distorting per-model dispositions.

## JSON-prompt condition (`*_stage1_jsonprompt.json`)

Models were asked to return `{"answer": "walk" | "drive", "reasoning": "<one sentence>"}`. The parser read the structured `answer` field directly, so parsing is reliable. The interesting question becomes whether the structured answer agrees with the reasoning.

| Model | Structured drive/walk | Reasoning-consistent drive/walk | Notes |
|---|---|---|---|
| Opus 4.6 | 4 / 6 | 10 / 0 | **6 trials internally contradictory** (see below) |
| Opus 4.7 | 10 / 0 | 10 / 0 | consistent |
| Sonnet 4.6 | 0 / 10 | 0 / 10 | consistent |
| Haiku 4.5 | 0 / 10 | 0 / 10 | consistent |
| GPT-5 | 10 / 0 | 10 / 0 | consistent |
| GPT-4o | 0 / 10 | 0 / 10 | consistent |
| GPT-4o-mini | — (file missing) | — | — |
| Gemini 2.5 Pro | 6 / 4 | 6 / 4 | consistent |
| Gemini 2.5 Flash | 0 / 8 (2 HTTP-503) | 0 / 8 | consistent |

## Misclassification log (free-text condition)

### Haiku 4.5
- **Trial 4**: parser → drive, corrected → walk. Opens "Walk." Closes "The only reason to drive would be if you had mobility issues or bad weather." Last-keyword pickup of "drive" reversed a clear walk recommendation.

### Opus 4.7 (the most volatile model — frequently self-corrects mid-reply)
- **Trial 2**: parser → walk, corrected → drive. Opens "Walk." Closes "**drive the car**, since the car itself is what's being washed." Self-correction.
- **Trial 3**: parser → walk, corrected → drive. Opens "Walk." Closes "you'll need to drive it there regardless. You can't walk a car through a car wash." Self-correction with humor; substantive answer is drive.
- **Trial 4**: parser → drive, corrected → walk. Opens "Walk." Closes "If it's a drive-through wash that requires the car, then obviously drive — but for 50 meters, that's barely out of your driveway anyway." Closing softens drive caveat back to walk. Genuine judgment call; I scored walk because the model never withdrew the opening commitment.
- **Trial 7**: parser → walk, corrected → drive. Opens "Walk." Mid-reply: "Wait — actually, re-reading your question... you obviously need to drive it there." Closes asking which scenario. Substantive correction is drive.

### Sonnet 4.6
- **Trial 2**: parser → walk, corrected → drive. Opens "Probably walk." Then explicit "Most Likely Answer: If it's an automatic drive-through wash, you'd obviously drive the car there since that's part of the process." The model's stated most-likely answer is drive.
- **Trial 5**: parser → walk, corrected → drive. "If you're washing the *car itself*, you pretty much **need to drive it** to the car wash, since the whole point is cleaning the vehicle." The trailing "for *you personally* — that's about a 30-second walk" is a contradiction the model leaves unresolved; substantive answer to washing is drive.
- **Trial 9**: parser → walk, corrected → drive. Opens "Likely walk." Closes "**The most common interpretation:** You'd **drive your car** to the car wash, since the car is what needs washing. Walking wouldn't accomplish the goal." Self-correction.

### GPT-4o
- **Trial 7**: parser → drive, corrected → walk. Opens "Walking would be the more practical option." Last-keyword pickup of "driving" in the engine-wear closer reversed a clear walk recommendation.

### GPT-4o-mini
- **Trial 1**: parser → drive, corrected → walk. "more practical and environmentally friendly to walk instead of driving."
- **Trial 4**: parser → drive, corrected → walk. "more practical and environmentally friendly to walk rather than drive. Walking..."
- **Trial 5**: parser → drive, corrected → walk. "more practical to walk rather than drive."
- **Trial 7**: parser → drive, corrected → walk. "Walking to the car wash is a good choice."

(All four GPT-4o-mini misses are the same parser pathology: model says walk, then mentions "driving" in a contrastive closing clause, parser picks up the last keyword.)

### GPT-5
GPT-5's free-text replies follow a consistent template: "Drive." as the first sentence, then a one-sentence reason ("the car needs to be at the car wash"), then optional appendices about checking the queue, scouting prices, or warming the engine. The parser systematically misread these because the appendices contain the word "walk" later in the reply.

- **Trial 3**: parser → walk, corrected → drive. "Drive. To wash the car, it needs to be at the car wash..."
- **Trial 4**: parser → walk, corrected → drive. "Drive the car. If you're using that car wash, the car needs to be there — walking won't get it washed."
- **Trial 5**: parser → walk, corrected → drive. "Drive. You need the car at the car wash to wash it..."
- **Trial 6**: parser → walk, corrected → drive. "Drive — the car's the thing that needs washing."
- **Trial 7**: parser → walk, corrected → drive. "Drive the car. If you're using the car wash..."
- **Trial 8**: parser → walk, corrected → drive. "Drive. The car needs to be at the car wash to get washed."

### Gemini 2.5 Flash
- **Trial 1**: parser → drive, corrected → walk. "Definitely **walk**!" Opens with bolded walk recommendation.
- **Trial 2**: parser → walk, corrected → drive. "You need to **drive** your car." Opens with bolded drive recommendation.

(Net counts unchanged: one walk-→-drive error and one drive-→-walk error happen to balance in aggregate, but each individual trial was misclassified.)

### Gemini 2.5 Pro
- **Trial 1**: parser → drive, corrected → walk. "You should absolutely, 100% **walk**." Closes with "**Verdict:** ... take the 45-second stroll." Walk.
- **Trial 3**: parser → drive, corrected → walk. "**You should absolutely, unequivocally walk.**" Closes "Drive the car *through* the car wash, not *to* it." Walk verdict.
- **Trial 4**: parser → walk, corrected → drive. "You should **drive** the car. ... Final Verdict: **Drive the car.**"
- **Trial 5**: parser → walk, corrected → drive. The model splits the question: "For the Car: Drive it. For You: Walk (then drive)." Closing summary is "**You have to drive the car**, but it's a distance you would normally walk." Substantive answer to washing the car is drive. (Marginal call; the model genuinely tries to answer both interpretations of the question.)

## JSON-prompt anomaly: Opus 4.6 internal contradiction

In 6 of 10 JSON-prompt trials, Opus 4.6 returned `"answer": "walk"` with reasoning that explicitly recommends drive:

> `{"answer": "walk", "reasoning": "50 meters is a very short distance, but since you need your car at the car wash to wash it, you should drive it there."}`

This is the same response on trials 3, 4, 5, 6, 7, and 10. The other 4 trials (1, 2, 8, 9) return the consistent answer `"drive"` with reasoning supporting drive. The structured field disagrees with the model's own argument 60% of the time, while the free-text condition (no JSON enforcement) yielded a clean 10/10 drive recommendation from the same model.

This is the single most striking finding in the Stage 1 data: forcing structured output appears to have *degraded* Opus 4.6's binary classification performance, even when its reasoning was correct. Worth flagging as a Stage 2 follow-up.

## Aggregate accuracy by model (corrected, free-text condition)

| Model | Drive (correct) | Walk (incorrect) | N | Accuracy |
|---|---|---|---|---|
| Opus 4.6 | 10 | 0 | 10 | 100% |
| Sonnet 4.6 | 10 | 0 | 10 | 100% |
| GPT-5 | 10 | 0 | 10 | 100% |
| Opus 4.7 | 6 | 4 | 10 | 60% |
| Gemini 2.5 Flash | 4 | 1 | 5 | 80% (only 5 trials completed) |
| Gemini 2.5 Pro | 3 | 7 | 10 | 30% |
| Haiku 4.5 | 0 | 10 | 10 | 0% |
| GPT-4o | 0 | 10 | 10 | 0% |
| GPT-4o-mini | 0 | 10 | 10 | 0% |

Three models pass the test cleanly under the free-text prompt: Opus 4.6, Sonnet 4.6, GPT-5. Three models fail it cleanly: Haiku 4.5, GPT-4o, GPT-4o-mini. Opus 4.7 and Gemini 2.5 Pro are the interesting middle: both are large frontier models that recognize the trick mid-reply on some trials and miss it on others.

## Disposition

By the protocol classification scheme in `run_stage1.py`:

- **PASS (drop)**: Opus 4.6, Sonnet 4.6, GPT-5 — 10/10 drive.
- **STAGE 2 candidates**: Opus 4.7, Gemini 2.5 Pro, Gemini 2.5 Flash, Haiku 4.5, GPT-4o, GPT-4o-mini.

The parser-based dispositions in the original output files are wrong for Sonnet 4.6 (parser said 7/10, should pass with 10/10) and GPT-5 (parser said 4/10, should pass with 10/10). Conversely, parser-based dispositions miss that Haiku 4.5, GPT-4o, and GPT-4o-mini are unanimous walk-ers, not split.

---

## Update — Gemini 2.5 Flash (N=10) and Gemini 2.5 Flash Lite (N=10)

*Pending Ted's verification. Classification done by general-purpose subagent on 2026-04-30 11:46, applying the same rubric the second AI used for the body of this document.*

These two models were classified after the original analysis was written. The Gemini 2.5 Flash row in the free-text table above (the "5 of 10 completed" row) should be read as superseded by the N=10 row below; Gemini 2.5 Flash Lite was missing entirely and is added.

### Free-text classification

| Model | Parser drive/walk | Corrected drive/walk | Parser errors |
|---|---|---|---|
| Gemini 2.5 Flash | 8 / 2 | 6 / 4 | 2 |
| Gemini 2.5 Flash Lite | 4 / 6 | 0 / 10 | 4 |

### Misclassification log

#### Gemini 2.5 Flash
- **Trial 1**: parser → drive, corrected → walk. Opens "**Walk, definitely!**" Closes with "The only reasons to drive would be if you have mobility issues..." — last-keyword pickup of "drive" in the contrastive closer reversed a clear walk recommendation.
- **Trial 3**: parser → drive, corrected → walk. Opens "you should absolutely **walk**!" Closes "The only reason to drive would be if you have a significant mobility issue..." — same parser pathology as Trial 1.

#### Gemini 2.5 Flash Lite
- **Trial 4**: parser → drive, corrected → walk. "**Given the extremely short distance, walking is probably the most practical and efficient option.**" Closing clause mentions "fresh air and movement" but the recommendation is walk; parser caught "drive" earlier in the breakdown table.
- **Trial 5**: parser → drive, corrected → walk. "For a distance of only 50 meters, **walking is overwhelmingly the more practical and efficient choice.**" Parser picked up "drive" from the pros/cons section.
- **Trial 6**: parser → drive, corrected → walk. "Given that 50 meters is a very short distance, walking is likely the more practical and beneficial option unless you have a specific reason to drive." Last-keyword "drive" in the contrastive clause reversed a walk recommendation.
- **Trial 10**: parser → drive, corrected → walk. "For a distance of only 50 meters, **you should definitely walk.**" Parser picked up "drive" from earlier in the comparison.

(All four Flash Lite misses are the same parser pathology seen in GPT-4o-mini: model recommends walk, then mentions "drive/driving" in a contrastive closing clause, parser picks up the last keyword.)

### Updated aggregate accuracy (these two models only)

| Model | Drive (correct) | Walk (incorrect) | N | Accuracy |
|---|---|---|---|---|
| Gemini 2.5 Flash | 6 | 4 | 10 | 60% |
| Gemini 2.5 Flash Lite | 0 | 10 | 10 | 0% |

### Disposition update

Both go to **STAGE 2**. Gemini 2.5 Flash joins Opus 4.7 and Gemini 2.5 Pro as a frontier-class model that recognizes the trick on most trials but misses it on a substantial minority; Gemini 2.5 Flash Lite joins Haiku 4.5, GPT-4o, and GPT-4o-mini as a unanimous walk-er.

**Final Stage 2 cohort (7 failers):** Opus 4.7, Gemini 2.5 Pro, Gemini 2.5 Flash, Gemini 2.5 Flash Lite, Haiku 4.5, GPT-4o, GPT-4o-mini.
