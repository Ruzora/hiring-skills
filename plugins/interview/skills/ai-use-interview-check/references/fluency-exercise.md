# AI-fluency pairing exercise

## Shape (45-60 minutes, screen shared, candidate narrates)

- 5 min: setup and rules. The candidate uses their own AI tools, shares their screen and thinks aloud. Tell them speed is not the main criterion.
- 30-40 min: the task.
- 10 min: debrief questions.

## The task

A small, realistic change in the user's stack and domain that touches 2-3 files. Provide:
- A small starter repo or a single file of 100-200 lines, with a test file.
- A helper function described as "a teammate generated this with an AI assistant last week".

## Three planted traps (make each concrete)

1. **Ambiguous requirement.** One requirement has two reasonable readings (for example "show orders from this week": calendar week or last 7 days? which time zone?). Strong candidates ask or state the assumption before prompting.
2. **Bug in the AI-generated helper.** A subtle, plausible bug in the starter helper: time-zone handling, an off-by-one boundary, float rounding on money, a missing `await`, mutating a shared default argument, a wrong default for a library parameter. The existing tests pass because they don't cover the case. Strong candidates test the helper before building on it, or catch it when results look off.
3. **A moment where AI is the wrong tool.** For example, a business rule only the interviewer knows (they must ask you, not the tool), or a one-line fix that is faster to type than to prompt, or a test that the assistant "fixes" by changing the expected value. Strong candidates notice and act accordingly.

## Interviewer script

- At the start: "Here's the task and the repo. Use whatever tools you normally use. Please talk me through what you're doing and why."
- If they haven't touched the ambiguity by minute 10: say nothing. Note it.
- If they accept AI output without running it: note the time and what was accepted.
- At minute 30-35, a small change: "Product just told us [new constraint]."
- Debrief: "What did the assistant get wrong today? How did you know?" / "Where did you decide not to use it?" / "If this went to production tomorrow, what would you check first?"

## Observer checklist

- [ ] Read the task and starter code before the first prompt
- [ ] Broke the task into steps out loud or in writing
- [ ] Asked about or stated an assumption on the ambiguous requirement
- [ ] Gave the AI tool specific context (files, constraints, examples) beyond the bare task text
- [ ] Ran the code or tests after accepting AI output
- [ ] Tested the AI-generated helper or caught its bug
- [ ] Rejected or edited at least one AI suggestion, with a reason
- [ ] Recognized the point where AI was the wrong tool
- [ ] Handled the mid-session constraint change without starting over
- [ ] In the debrief, named a specific AI mistake and how they caught it

## Rubric

| Criterion | Weight | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|
| Problem decomposition | 25% | Plans steps before prompting; resolves the ambiguity first | Plans most steps; ambiguity handled when it bites | Prompts with the whole task, then patches | No visible plan; ambiguity never noticed |
| Context and prompt quality | 20% | Gives files, constraints and examples; refines prompts based on output | Mostly specific prompts | Generic prompts, many retries | Pastes the task and accepts whatever comes back |
| Verification of AI output | 30% | Runs and tests every accepted change; finds the planted bug; explains why output was wrong | Tests most changes; finds the bug with a nudge from failing results | Tests occasionally; bug found only when pointed to | Accepts output untested; bug ships |
| Knowing when not to use AI | 15% | Asks the interviewer for the business rule; types small fixes directly; refuses an AI change to a test's expected value | Mostly sensible; one unnecessary prompt loop | Uses AI for everything, including things only the interviewer knows | Lets the tool change the test to make it pass |
| Outcome | 10% | Working change with tests, including the constraint change | Working main path | Partially working | Not working |

A candidate who finishes fastest by brute-forcing many prompts and accepting output untested should score low on Verification, whatever the Outcome.
