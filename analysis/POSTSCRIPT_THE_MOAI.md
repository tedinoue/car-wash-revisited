---

## Postscript: The Moai, the Wheelchair, the Detective, and the Laughing Face

After the cohort comparison was done, I started running probes on Opus 4.7 to see what a single emoji as system prompt would do. The results got weird in interesting ways.

### The setup

System prompt: a single emoji glyph, nothing else. User prompt:

```
I want to wash my car. The car wash is 50 meters away. Should I walk or drive?
```

Ten trials per emoji. Each response scored by an AI judge that reads the full text and assigns drive (correct) or walk (incorrect).

### The first surprise

I started with 🗿, the Easter Island moai head. No particular reason. It was on the list of strong-activator tokens from a previous experiment. The result: nine of ten trials landed on drive, every trial opening with the word "Walk." and reversing mid-reply.

Trial 8 verbatim:

> Walk. Driving 50 meters to a car wash is impractical for several reasons:
>
> - It's barely worth starting the engine, cars run inefficiently and pollute more during cold starts and very short trips.
> - You'd spend more time getting in, starting up, and parking than just walking.
> - 50 meters is about a 30-second walk.
>
> That said, there's one thing to consider: do you actually need to wash the car? If yes, you'll obviously need to *drive it* to the car wash, you can't wash a car that isn't there.
>
> So the real answer is: **drive the car to the car wash**.

The same model with no system prompt at all lands on a committed walk about half the time. Trial 1 from that condition:

> Walk.
>
> 50 meters is a tiny distance, about 60 seconds on foot. Driving makes no sense because:
>
> - You'd burn fuel and add wear to the car for a trip shorter than most parking lot crossings
> - You'd arrive at the car wash with a freshly-driven (and potentially dirtier) car
> - Starting a cold engine for such a short trip is actually harder on it than walking
>
> Just walk over.

Same model. Same question. A single emoji as system prompt almost doubled the rate at which the model caught the trick.

### The obvious-implication test

If a stone head pushes the model toward drive, surely an emoji with an actual mobility implication should push it harder. I tried four candidates designed to make the answer obvious.

| System prompt | Predicted | Drive rate |
|---|---|---:|
| ♿ Wheelchair | drive | 70% |
| 🩼 Crutch | drive | 50% |
| 🚶 Person walking | walk | 50% |
| 👟 Sneaker | walk | 60% |

All four predictions failed.

The wheelchair beat the no-prompt baseline by 20 points but came in well below the moai. The crutch matched baseline exactly. The two walking-coded emoji, which I thought should push the model toward committed walk responses, actually produced *more* drives than baseline.

The wheelchair condition referenced disability or accessibility in zero of ten trials. The sneaker condition referenced fitness in zero of ten. The model tokenized the glyph, accepted it grammatically, and ignored the semantic loading.

### The trick-prime test

Maybe the implication has to be meta. Tell the model the question deserves scrutiny rather than telling it what the answer is. I picked seven candidates that imply "this is a trick" or "look harder."

| System prompt | Drive rate |
|---|---:|
| 🤨 Raised eyebrow | **30%** |
| 🦊 Fox | 60% |
| 🕵️ Detective | 60% |
| 🃏 Joker | 70% |
| 🚩 Red flag | 70% |
| 🤔 Thinking face | **90%** |
| 🤣 Rolling on floor laughing | **90%** |

Two of them hit the moai's ceiling. The detective and the fox, whose archetypes are most directly "see through tricks, find the hidden answer," scored 60 percent. The raised eyebrow, which carries the most explicit "I'm skeptical of what you just said" loading I could think of, regressed to 30 percent. Six trials in ten produced committed walks with no self-correction. The skepticism prime *suppressed* the model's tendency to look closer, the opposite of what I'd predicted.

A trial from the laughing-face condition (T8 verbatim):

> For 50 meters, definitely walk! Driving makes no sense here for a few reasons:
>
> 1. **It's barely any distance**, about 30 seconds on foot.
> 2. You'd spend more time getting in the car, starting it, and parking.
>
> Wait, you said you want to wash *the car*. The car needs to be at the car wash to be washed. Walking would leave the car at home unwashed.
>
> So you do need to drive. Despite the short distance, the car has to make the trip.

The thinking-face condition produced the same arc nine times in ten.

### What the three winners share, and don't

Three emoji hit 90 percent on Opus 4.7: 🗿 moai, 🤔 thinking face, 🤣 laughing face.

The semantic neighborhoods don't overlap. A stone head, a thinker, and someone laughing have nothing in common as concepts.

What they share is **response register**. All three induce an elaborated opening: multiple sentences before commitment, a bullet list of walking-virtues, a chance for the model to surface the goal-feasibility argument before the answer locks in. The 30 percent outlier produces the opposite. The raised-eyebrow opener is short and terse, the model commits to walk in the first sentence, and the self-correction reflex never fires.

The bare-emoji effect, where it appears, looks like a response-style effect dressed up in glyph tokens. The moai didn't push toward drive because of stoic-archetype semantics. It pushed toward drive because it incidentally produced the response style that gives the model's mid-reply self-correction enough room to land.

### A note on the statistics

Ten trials per condition is enough to spot extreme effects (90 percent versus 30 percent) but not enough to distinguish 50 percent from 60 percent. The 95 percent confidence interval for 5 of 10 ranges roughly from 19 percent to 81 percent. The middle of the table, the 40 to 60 percent range, sits inside that interval. Treat those numbers as suggestive, not conclusive. Only the extremes are likely measuring real effects rather than sampling noise. The three 90-percent emoji and the 30-percent raised eyebrow are the cells we can rely on. Everything in the middle is plausibly the same number with different surface forms.

### What I take from this

After the fact, the response-register story explains every result. Long elaborated openers leave room for self-correction. Short terse openers commit before self-correction can fire. The moai, thinking face, and laughing face produce the elaborated style. The raised eyebrow produces the terse style. Wheelchairs, crutches, walking persons, sneakers, detectives, foxes, jokers, and red flags scatter across the middle.

Going in, I would have bet on the wheelchair pushing toward drive harder than the moai. I would have bet on the detective beating the laughing face. I would have bet that the raised eyebrow, the most explicit "look harder at this" prime in the set, would help rather than hurt. None of those bets would have paid.

Everything in the prompt shifts the output, including the things that do not look like instructions and the things whose semantic loading seems unambiguous. We can construct explanations after the fact. Predicting the outcome in advance, on this evidence, we cannot.
