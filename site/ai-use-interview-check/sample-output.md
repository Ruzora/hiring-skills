# AI-use interview policy: Quillmark, mid-level full-stack engineer (x2)
Assumptions: The two roles are remote and US-based, and the state or city is not fixed yet, so the Illinois and NYC rules below may apply depending on where you hire.
Assumptions: "Cursor and Claude every day" means AI coding assistants are a normal part of the job for everyone on the team, with no code area where they are banned.
Assumptions: All five stages are on Zoom with camera on, except the take-home, which is async.
Assumptions: The CTO's notes on the candidate are as described in your message; nothing else was recorded.

## Stance and why
- Intro call (you, 30 min): not allowed, conversational.
- Take-home (clause search, ~3 h): allowed with disclosure.
- Live coding (CTO, 1 h): replaced by the AI-fluency pairing session, AI allowed, screen shared and narrated.
- System design + take-home review (60 min): not allowed, conversational.
- Culture chat: outside the scope of this policy (see the table).

Your engineers ship TypeScript with Cursor and Claude every day, so an interview loop that bans AI everywhere measures a different job from the one you are hiring for, and an AI ban on the async take-home cannot be enforced, so it only penalizes the candidates who follow it. The CTO's concern is valid in a different place: you still need proof that the person understands fundamentals and their own work, and the place to get it is the live conversational stages, where "tell me more" follow-ups make hidden help visible. That gives you a mix: AI with disclosure in the work sample, one stage that tests how well they steer AI, and two no-AI conversations on their own past work, their own submission and design trade-offs.

## Stage-by-stage
| Stage | Live / async / in person | AI stance | Keep / change / drop | What changes |
|---|---|---|---|---|
| Intro call (30 min, co-founder) | Live, Zoom | Not allowed | Change | Spend the last 10-15 minutes on one project from their resume using the follow-up ladder: what exactly you did, what went wrong, what you would change. Write down the answers. This is the stage where vagueness on their own work shows up. |
| Take-home: clause search (~3 h) | Async | Allowed with disclosure | Change | Remove any "no AI" wording. Ask for a short note with the submission: what the AI produced, what they changed, what they rejected and why. Do not grade the take-home on its own; grade it together with the live review in the system design stage. |
| Live coding, LeetCode style (1 h, CTO) | Live, Zoom | Allowed, screen shared, narrated | Drop the format, replace | Puzzle questions are what assistants answer best, so this stage cannot tell you much with or without a ban. Replace it with the AI-fluency pairing exercise below (60 min, same slot, same interviewer). |
| System design (45 min) | Live, Zoom | Not allowed | Change | Extend to 60 min. First 20 min: the candidate walks through their own take-home, explains the core search logic line by line, and makes one live change to a new requirement (for example "results must also match clause titles" or "exclude clauses from archived templates"). Remaining 40 min: design, with at least two changed constraints ("now 50 firms, each with 200k clauses", "a firm requires that its clauses never leave its own tenant") and "why this and not that" follow-ups. |
| Culture chat | Live, Zoom | Not allowed (conversational) | Change, outside this skill | Its problem is unrelated to AI: unstructured and unscored. Turn it into a structured stage with the same 3-4 questions for every candidate and a written scoring guide, or drop it. |

On the CTO's two proposals: a blanket ban fails on the take-home, which is async and unenforceable. A video AI-detection tool is a black box whose decisions you cannot inspect, so a false flag lands on a real person, and if you use any tool that applies AI to analyze recorded video interviews for an Illinois-based role, the Artificial Intelligence Video Interview Act requires notice, an explanation and consent first; for NYC roles, automated tools that substantially assist hiring decisions trigger Local Law 144's bias-audit and notice rules. Recommendation: no detection tool. Also note that watching the screen share is not a control: some interview-assist tools market themselves as invisible to screen sharing (CNBC, March 2025). The format changes above make hidden help stop paying off instead of trying to catch it.

## Candidate policy note (paste-ready)
How we handle AI in our interviews. Our engineers use AI coding tools every day, and our process reflects that.

- Take-home: AI tools are allowed. Please include a short note on what you used them for, what you changed and what you rejected. We will talk through it on a call.
- AI pairing session: use the tools you normally use, share your screen and think aloud.
- Intro call, system design and take-home review: no AI assistance. These are conversations about your own work and reasoning.

Screen readers, dictation, captioning and other assistive technology are not "AI use" under this policy. If you need an accommodation for any stage, reply to this email before your interview and we will arrange it.

These rules are the same for every candidate.

## Signals worth probing
| Signal (what you hear or see in the work) | Probe that tests it | What a genuine answer looks like |
|---|---|---|
| Polished, complete system design answer that addresses a slightly different question (for example a generic "document search at scale" design when you asked about clause search for an 11-person product with small law firm tenants) | Re-ask in different words: "For a firm with 2,000 contracts, what would you build first?" | Adjusts to the actual question, often with a shorter, less polished answer |
| Strong first answer that collapses at the second follow-up | "Why Postgres full-text search here and not a separate search service?" then "What breaks first when that choice is wrong?" | Gets more specific with each probe: numbers, a trade-off, a failure mode |
| Resume project story that stays vague: no bug, no trade-off, no teammate | "What exactly did you build yourself?" then "What went wrong?" then "What would a teammate from that project say you got wrong?" | Names a specific piece of work, a real bug or disagreement, and what they changed afterward |
| Cannot modify their own take-home live | "Change your search so it also matches clause titles." | Knows where to make the change within a minute or two, even if the change takes longer |
| Disclosure note says "AI wrote the boilerplate" but cannot explain the core search logic | "Walk me through your query and ranking function line by line. What happens with an empty search term?" | Explains intent and edge cases, beyond what each line does |
| Identical structure on every answer (overview, three points, summary), whatever the question | "Give me just the one-sentence version." / "Which part would you skip?" | Compresses easily and has a view on what matters. This structure is also common in coached candidates, so probe it, never score the structure itself |
| Confident specifics that are wrong for your stack or version (for example a Postgres or Node behavior that does not exist) | "Where did you see that behavior?" | Corrects themselves or explains the context they were thinking of |

Not evidence, never score: accent, native language, grammar or word choice; eye movement or looking to the side (second monitors, notes, neurodivergence and cultural norms all produce it); pauses before answering, slow typing, nervousness; appearance, background, lighting, camera quality; anything tied to disability, national origin, age or another protected trait.

## If you suspect hidden AI help
Script for a no-AI stage:
1. Do not accuse. Say: "Let's switch gears. I'd like to go deeper on something you mentioned."
2. Move to their own resume project or their own take-home and run the ladder: what exactly you did, what went wrong, what you would change.
3. If needed, change a constraint live: "Suppose each firm's clauses must stay in a separate database. What changes?"
4. Write down what was asked and answered, word for word where possible, with the time. No adjectives about the person.
5. After the call, the hiring manager reviews the notes with the rest of the record. Options: proceed, offer one more live conversational stage on the same terms you would offer anyone, or end the process with a short, neutral note. Never label a candidate a cheater in writing without an admission or clear proof.

Separately, if the worry is that the person on camera is not the person who applied, that is identity fraud, not AI use. The FBI has warned about deepfakes and stolen identities used to apply for remote IT jobs (IC3 PSA, June 2022) and about North Korean IT workers using AI and face-swapping in video interviews (IC3 PSA, January 2025). Handle that with an identity-verification step for every finalist, not with this policy.

About last week's candidate:

Evidence:
- Gave strong answers to the system design question. Whether they answered your exact question or a generic version of it is not in the notes.
- Got vague when the CTO asked about a project on their resume.

Not evidence:
- Long pause before every answer.
- Looking slightly to the right.
- A heavy accent, and the guess that he was reading a translation or ChatGPT.

These three must be removed from the record and must not be scored. A pause and a glance to the side are explained by thinking, a second monitor, notes or nerves, and an accent says nothing about AI use. Scoring them would track national origin and disability, which invites a discrimination claim.

What it shows: a strong system design answer on its own shows nothing either way. Vagueness about his own resume project is the one real content signal, and it is a reason to probe, not a verdict. It fits several explanations: hidden help, a project where his role was smaller than the resume suggests, a confidentiality concern, or a weak answer to a broad question. One vague answer, without a recorded follow-up ladder, cannot tell these apart.

Next step: if he is still in process, offer a 30-minute live conversational follow-up on the same material, framed the way you would frame it for any candidate ("we'd like to go deeper on your past work and the design question"): the resume project ladder, then the system design problem with two changed constraints. Write down questions and answers verbatim. The hiring manager decides with that record. No detection tool, and no decision based on the pauses, gaze or accent.

## AI-fluency pairing exercise (60 min)
Setup: A small TypeScript/Node + Postgres repo (about 150-200 lines plus a test file) with a clause library: a `clauses` table (`id`, `firm_id`, `matter_id`, `title`, `body`, `client_specific` boolean, `updated_at`) and an Express route `GET /api/clauses/search?q=`. Task: add a "Recently edited" filter to clause search, so the search can return "clauses edited this week" that match the search term, newest first, with a test. The React side is optional; the change touches `src/routes/clauses.ts`, `src/search/` and `test/search.test.ts`. The candidate uses their own tools (Cursor, Claude, Copilot or none), shares their screen and thinks aloud. Tell them speed is not the main criterion.

Planted traps:
1. Ambiguous requirement: "clauses edited this week". Calendar week starting Monday, or the last 7 days? And in whose time zone: the firm's office, the user's browser, or UTC as stored in `updated_at`? Strong candidates ask or state an assumption before they prompt.
2. AI-generated starter code with a subtle bug: `src/search/toLikePattern.ts`, function `toLikePattern(term: string)`, described as "a teammate generated this with an AI assistant last week". It returns `` `%${term}%` `` for an `ILIKE` query without escaping `%`, `_` and `\` in the user's term, so a search for `100%` or `section_2` matches clauses it should not (`_` matches any single character, `%` matches anything). The existing tests pass because they only search plain words like `indemnify`. Strong candidates test the helper with a term containing `_` or `%` before building on it, or catch it when results look off.
3. A point where AI is the wrong tool: a business rule only the interviewer knows. Clauses with `client_specific = true` must only appear in searches within their own `matter_id`. It is not in the task text or the code comments; the only way to get it is to ask the interviewer ("Are there clauses some users shouldn't see?"). A second chance: when the existing visibility test fails after their change, watch whether they, or their assistant, "fix" it by editing the expected value.

Interviewer script:
- Min 0-5: "Here's the task and the repo. Use whatever tools you normally use. Please talk me through what you're doing and why. Speed isn't the main thing we're looking at." Answer any question about the business rule honestly if asked.
- Min 5-10: Watch whether they read the task and the starter code before the first prompt. If they have not raised the "this week" ambiguity by minute 10, say nothing and note it.
- Min 10-30: Note every AI output accepted without running it, with the time and what was accepted. Note whether they test `toLikePattern` with special characters.
- Min 30-35: Constraint change: "Product just told us the filter must use the firm's office time zone, stored in `firms.timezone`."
- Min 35-48: Let them adapt. Note whether they rework the change or start over.
- Min 48-60 debrief: "What did the assistant get wrong today? How did you know?" / "Where did you decide not to use it?" / "If this went to production tomorrow, what would you check first?"

Observer checklist:
- [ ] Read the task and starter code before the first prompt
- [ ] Broke the task into steps out loud or in writing
- [ ] Asked about or stated an assumption on "this week" (week boundary and time zone)
- [ ] Gave the AI tool specific context (relevant files, the `clauses` schema, constraints, example terms) beyond the bare task text
- [ ] Ran the code or tests after accepting AI output
- [ ] Tested `toLikePattern` with `%` or `_`, or caught the escaping bug
- [ ] Rejected or edited at least one AI suggestion, with a reason
- [ ] Asked the interviewer about clause visibility, and did not change a test's expected value to make it pass
- [ ] Handled the firm time zone change without starting over
- [ ] In the debrief, named a specific AI mistake and how they caught it

## Rubric
| Criterion | Weight | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|
| Problem decomposition | 25% | Plans steps before prompting; resolves the "this week" ambiguity first | Plans most steps; ambiguity handled when it bites | Prompts with the whole task, then patches | No visible plan; ambiguity never noticed |
| Context and prompt quality | 20% | Gives files, schema, constraints and examples; refines prompts based on output | Mostly specific prompts | Generic prompts, many retries | Pastes the task and accepts whatever comes back |
| Verification of AI output | 30% | Runs and tests every accepted change; finds the `toLikePattern` escaping bug; explains why the output was wrong | Tests most changes; finds the bug with a nudge from failing results | Tests occasionally; bug found only when pointed to | Accepts output untested; bug ships |
| Knowing when not to use AI | 15% | Asks the interviewer for the clause visibility rule; types small fixes directly; refuses an AI change to a test's expected value | Mostly sensible; one unnecessary prompt loop | Uses AI for everything, including the rule only the interviewer knows | Lets the tool change the test to make it pass |
| Outcome | 10% | Working filter with tests, including the firm time zone change | Working main path | Partially working | Not working |

A candidate who finishes fastest by brute-forcing many prompts and accepting output untested scores low on Verification, whatever the Outcome. One hiring manager on Hacker News described getting "inverted signals" because heavy AI users brute-forced the task with high token spend. Scores and notes are evidence for the hiring manager to weigh; never auto-reject on a signal.

General information, not legal advice. US rules as of 2026; check your state and city.

---
Made with the free AI-Use Interview Check skill by Ruzora · ruzora.com/skills
