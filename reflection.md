# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, the hints were consistently wrong — guessing a
number higher than the secret still showed "Go HIGHER!" instead of "Go LOWER!".
The score also went negative (-25, -35) even during normal gameplay, which made
no sense for a guessing game. The game also felt like it ran out of attempts
faster than expected, and the difficulty settings did not seem to affect the
secret number range at all.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of 85, secret was 73 | "Go LOWER" hint | "Go HIGHER!" shown | none |
| Any even-numbered attempt | Normal number comparison | Secret converts to string, breaks comparison | none |
| Wrong guess on even attempt | Score decreases | Score increases by +5 for wrong guess | none |
| First game load | 8 attempts available | Starts at attempt 2 (attempts init = 1) | none |
| New Game clicked on Easy | New secret between 1-20 | New secret always from 1-100 | none |
| Playing on Easy difficulty | Banner says "1 to 20" | Banner hardcoded to "1 to 100" | none |

---

## 2. How did you use AI as a teammate?

I used Claude as my AI coding assistant throughout this project. One example
of a correct AI suggestion was when I asked it to explain why the hints were
backwards — it correctly identified that the messages "Go HIGHER!" and
"Go LOWER!" were swapped inside check_guess() in logic_utils.py, and I
verified this by reading the if/else logic myself and confirming that
guess > secret should always direct the player lower, not higher.
One example of a misleading suggestion was when the AI initially explained
the string conversion bug as just a type mismatch, but did not immediately
flag that it was intentionally placed on even attempts — I had to read the
code myself to see the `if attempts % 2 == 0` pattern causing it.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed when the game behavior matched what I expected
after playing it again manually and running pytest. For the inverted hint bug,
I tested by guessing a number I knew was higher than the secret and confirming
the hint now said "Go LOWER!" correctly. I also wrote a pytest case that
verified check_guess(85, 73) returns "Too High" and check_guess(30, 73)
returns "Too Low". The AI helped me structure the test by suggesting clear
input/output pairs to cover win, too high, and too low cases.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the entire Python script from top to bottom every time the
user interacts with the app, like clicking a button or typing in a field.
Session state is how Streamlit remembers values between those reruns — without
it, variables like the secret number or attempt count would reset to their
starting values on every interaction. I explained it to myself like this: 
imagine refreshing a webpage but the page remembers your progress because it
saved it in a notepad before refreshing. The bug where attempts started at 1
instead of 0 was a direct result of not understanding how session state
initializes on the very first run.
---

## 5. Looking ahead: your developer habits

One habit I want to reuse is adding FIXME comments directly in the code
before touching anything, so I have a clear map of where the problems are
before I start fixing. Next time I work with AI on a coding task, I would
give it more specific context upfront — like pasting the exact function and
describing the exact wrong behavior — instead of describing it vaguely. This
project changed how I think about AI-generated code because I realized the AI
can produce code that looks completely correct and runs without errors but
still has subtle logic bugs that only show up during actual use.
