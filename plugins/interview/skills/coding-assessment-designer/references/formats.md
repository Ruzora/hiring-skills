# Assessment formats: how to build each one

## 1. Seeded-bug review

**Shape:** a pull request of 80-150 lines that adds or changes one feature in the user's domain, with a 3-5 line PR description written as if by a teammate. The candidate leaves review comments (async) or talks through them (live), then discusses.

**Seed exactly 5 issues, one from each category:**
| Category | Examples |
|---|---|
| Correctness / business rule | Rounding money with floats; off-by-one in pagination; a rule in the PR description that the code does not implement (this is the one that requires reading the brief) |
| Data safety / security | SQL built by string concatenation; missing authorization check on an endpoint; secrets in code; logging personal data |
| Failure handling | Swallowed exception; no retry or idempotency on a webhook or queue consumer; a partial write with no transaction |
| Performance at realistic scale | Query inside a loop (N+1); loading a full table into memory; missing index implied by a new filter |
| Maintainability / tests | Test that asserts nothing meaningful; duplicated logic; misleading name on a function that does something else |

Mark severity: at least one **high** (data loss, security, money wrong), two **medium**, two **low**. The answer key says what a strong reviewer says for each, including the fix.

**What strong looks like:** ranks the high-severity issue first; explains impact in business terms ("customers get charged twice when the webhook retries"); proposes a specific fix; asks about the ambiguous requirement; does not drown the real issues in style comments.

**Keep it fair:** use the user's real stack and plain domain language; no trick syntax; the code should look like normal team code, not a puzzle.

## 2. Extend an existing small codebase

**Shape:** a small working service or app (300-800 lines) in the user's stack, with a README, a few tests, and clear conventions (folder structure, error handling style, how tests are written).

**Task:** add one feature that touches 2-3 files, and fix one failing test whose cause is a real bug. Include one ambiguous requirement.

**Grader checks:** feature works for the main and one edge case; follows existing conventions instead of inventing new ones; tests added for the new behavior; the failing test fixed at the cause, not by changing the assertion; the ambiguity was asked about or the assumption written in the README or PR notes; a short note explaining choices and, under the disclosure policy, what AI was used for.

**Follow-up must include:** a live change to the feature ("now it also has to handle X"), done or talked through on screen.

## 3. Paid trial

Use [paid-trial-terms.md](paid-trial-terms.md). The work should be realistic but not on the critical path, with no production or customer-data access. Pair with a daily 15-minute check-in so you also see how they communicate and ask for help.

## Formats to avoid, and why

- **Greenfield "build X from scratch":** an AI assistant produces a complete solution; you learn little about the person.
- **Uncapped "weekend" take-homes:** you lose employed and caregiving candidates; seniors decline.
- **Algorithm puzzles for product roles:** test memorized patterns, not the work, and some AI overlay tools market themselves as invisible during screen-shared coding interviews (CNBC, March 2025).
- **Grading without a conversation:** you cannot tell who wrote the code.

## Follow-up question bank (pick and tailor)

- "Walk me through your submission as if I'm a new teammate. Where would you start reading?"
- "You chose [specific choice in their code]. What else did you consider, and why not that?"
- "What is the riskiest part of this code if it went to production tomorrow?"
- "If traffic was 100 times higher, what breaks first?"
- "Here's a new requirement: [change]. Show me or tell me what you'd change."
- (AI allowed with disclosure) "What did you use AI for? Show me one thing it gave you that you changed, and why."
- (AI not allowed) Same walkthrough questions; a candidate who wrote the code answers these easily.
- (Review format) "If you could only leave one comment on this PR, which one and why?"
