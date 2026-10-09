# Structured interview kit: Senior Backend Engineer, senior
Assumptions:
- Jordan (engineering manager) is the hiring manager and makes the decision.
- US-based employer, all interviews by video, candidates have 3+ years of backend experience (so mostly behavioral questions, with situational ones where noted).
- Dana runs the 30-minute screen for logistics only and does not score.
- Sam has not yet shadowed two loops, so he shadows Stages 2 and 3 and does not score. After two shadowed loops he can become a scoring interviewer.
- The CTO has 30 minutes per candidate in total, so the CTO scores in writing and does not attend the debrief.
- The work sample is unpaid with a hard 2-hour cap. If you want a longer exercise, pay for it.

## Competencies
| # | Competency (observable) | Must / Nice | Why it matters in this role |
|---|---|---|---|
| C1 | Designs an ingestion pipeline for messy carrier files (EDI, CSV) where every file is traceable, duplicates are harmless and bad rows can be quarantined and replayed | Must | Year 1 they own the ingestion pipeline that normalizes carrier files |
| C2 | Writes and reviews production Go and Postgres code that is correct, testable and safe to retry | Must | Daily work in Go and Postgres; matching errors become money errors for customers |
| C3 | Debugs production problems methodically (evidence before changes, root cause, prevention) and clears a failure backlog by cause, not one by one | Must | They must cut the failed-match backlog and carry on-call one week in five |
| C4 | Works async across US time zones: writes status and decisions down by default, and gives and takes direct feedback in writing | Must | Fully remote team; this replaces "culture fit" |
| C5 | Helps another engineer get measurably better (pairing, reviews, scoped tasks) | Nice | You named mentoring as a bonus |

"Culture fit" is replaced by C4. Undefined fit is where similar-to-me bias lives; C4 names the behaviors a remote team actually depends on.

## The loop
| Stage | Format | Owner | Length | Competencies assessed |
|---|---|---|---|---|
| 0. Screen | Video call, logistics only, not scored | Dana | 30 min | None |
| 1. Work sample + review | 2-hour take-home (hard cap), then live walkthrough and a seeded pull-request review | Priya | 60 min live | C2, C1 |
| 2. Pipeline design and incidents | Live design of carrier-file ingestion, a code question on the design, incident questions. Sam shadows | Marco | 75 min | C1, C2, C3 |
| 3. Ownership and mentoring | Behavioral interview. Sam shadows | Jordan | 60 min | C3, C4, C5 |
| 4. Remote work and feedback | Behavioral interview | CTO | 30 min | C4 |

Candidate time: 4 h 15 min live (including the screen) + 2 h work sample (hard cap)

What changed from your current loop:
- 7 steps become a screen plus 4 assessed stages. Stages 2-4 are booked as one block, which fixes the scheduling delay that lost your last two candidates.
- The "should take a weekend" take-home breaks the 2-3 hour limit. It is trimmed to a 2-hour scoped exercise with a starter repo.
- The take-home review and system design stay, with the same owners. "Design a URL shortener" is replaced by the carrier-file ingestion problem you actually have.
- Your 1-hour "get to know you" becomes Stage 3, with fixed questions.
- The culture fit lunch is removed. It produces no scoreable evidence and invites similar-to-me judgments. Candidates still meet Sam in Stages 2 and 3.
- The CTO chat stays at 30 minutes, with fixed questions on C4.

## Coverage check
| Competency | Stage A | Stage B | Assessors |
|---|---|---|---|
| C1 Ingestion pipeline design (Must) | 1. Work sample + review | 2. Pipeline design | Priya, Marco |
| C2 Go and Postgres code (Must) | 1. Work sample + review | 2. Pipeline design | Priya, Marco |
| C3 Debugging and on-call (Must) | 2. Pipeline design | 3. Ownership | Marco, Jordan |
| C4 Async and written feedback (Must) | 3. Ownership | 4. Remote work | Jordan, CTO |
| C5 Mentoring (Nice) | 3. Ownership | n/a | Jordan |

Each must-have appears in exactly 2 stages with 2 different assessors. Load per interviewer: Priya 2, Marco 3, Jordan 3, CTO 1 (none above 3).

## Timeline (target: offer decision within 10 business days of first interview)
| Day | What happens | Who |
|---|---|---|
| 1 | Screen. If logistics fit, Dana sends the work sample the same day | Dana |
| 1-3 | Candidate does the 2-hour exercise whenever suits them, submits by end of Day 3 | Candidate |
| 4 | Stage 1: work sample review | Priya |
| 5 | Priya's score is in by morning. Jordan decides whether to continue on the evidence. Dana books Stages 2-4 as one block on Day 7 (or two adjacent half-days, Days 7-8) | Priya, Jordan, Dana |
| 7 | Stage 2 (75 min), Stage 3 (60 min), Stage 4 (30 min), with breaks between | Marco, Jordan, CTO, Sam shadowing |
| 8 | All scoring forms submitted (24 hours after each interview) | Marco, Jordan, CTO |
| 9 | Debrief (30 min) and decision | Priya, Marco, Jordan, Sam observing |
| 10 | Buffer day. Candidate hears the decision no later than today | Jordan |

## Rubric
### C1: Ingestion pipeline design for messy carrier files
| Score | Anchor (what you heard or saw) |
|---|---|
| 4 | Asks about carrier count, file volume and format variance before drawing anything. Keeps the raw file, makes processing idempotent (for example a file hash or carrier plus invoice number as the key) and names 2 or more trade-offs (strict vs lenient parsing, Kafka partition key, sync vs batch matching). When a carrier silently changes format, says how bad rows are quarantined, made visible and replayed after a fix, without being asked. |
| 3 | A workable end-to-end pipeline with raw file retention and a quarantine or dead-letter path. Names one trade-off. Handles the duplicate file or format change correctly after one probe. |
| 2 | Designs the happy path only. Duplicate files, a crash mid-file or a format change are missed until the probe, and the fix stays vague ("we'd validate it"). |
| 1 | No end-to-end flow, or bad rows are dropped or overwritten with no way to find or rerun them, and the candidate does not see the problem when probed. |
| NE | Not assessed in this stage, note why |

### C2: Production Go and Postgres code
| Score | Anchor (what you heard or saw) |
|---|---|
| 4 | Explains why the code is structured as it is (error handling, transactions, interfaces for testing). Names the limits of their own code before being asked. In the seeded pull request, flags the correctness issues (SQL built by string concatenation, missing transaction, swallowed error) before any style comment and writes or describes the concrete fix. Explains what makes a write safe to retry (unique constraint, upsert, idempotency key). |
| 3 | Correct, specific explanation of what they built and why. Finds 2 of the 3 seeded correctness issues. Gets to limits and retry safety after one probe. |
| 2 | Describes what the code does but not why. Comments mostly on naming and style and misses at least 2 seeded correctness issues. Retry-safety answer is vague or partly wrong. |
| 1 | Cannot explain their own submission, or explanations contradict the code. Misses all seeded correctness issues. |
| NE | Not assessed in this stage, note why |

### C3: Debugging and on-call ownership
| Score | Anchor (what you heard or saw) |
|---|---|
| 4 | Describes an order of work: check scope and customer impact, gather evidence (logs, metrics, consumer lag, recent deploys) before changing anything, tell affected people what is happening and when the next update comes, confirm root cause. Names both prevention and earlier detection (an alert, a dashboard, a test). For a backlog, groups failures by cause, fixes the largest cause first and shows how they measured that it shrank. |
| 3 | Sensible method and a confirmed root cause. Prevention ideas are generic ("more tests"). Mentions communicating with others only when probed. |
| 2 | Changes something (restart, rollback) before gathering evidence, reaches the cause with hints. Works a backlog item by item with no grouping by cause. |
| 1 | Describes random changes or blames others or external systems without evidence, or has no example of owning a production problem. |
| NE | Not assessed in this stage, note why |

### C4: Async remote work and written feedback
| Score | Anchor (what you heard or saw) |
|---|---|
| 4 | Gives concrete examples of written updates or design notes sent by default, with who read them. Asks for help early with a specific question when blocked. In a disagreement, argued with evidence, committed after the decision and credits the other side. Describes a specific change they made to their work after written feedback. |
| 3 | Describes these habits with at least one concrete example. Disagreement handled with evidence, but thin on what they learned or changed. |
| 2 | Relies on meetings or on others asking for status. Waited a day or more when blocked before asking. Disagreement story is one where they were simply right. Feedback example is vague. |
| 1 | No working method or example beyond "I just get it done", or speaks about colleagues or feedback with contempt. |
| NE | Not assessed in this stage, note why |

### C5: Mentoring
| Score | Anchor (what you heard or saw) |
|---|---|
| 4 | Names what a specific person could not do before and can do now. Describes the method (pairing, review comments, gradually larger tasks) and something they changed when their first approach did not work. |
| 3 | A specific example with a result for the other person. Thin on what they adjusted along the way. |
| 2 | Describes answering questions when asked. Names no change in the other person. |
| 1 | No example, or describes mentoring as doing the work for the other person. |
| NE | Not assessed in this stage, note why |

## Interview guides
### Stage 0: Screen, Dana, 30 min (not scored)
Opening (2 min, read aloud): "Thanks for making time. This call covers logistics and your questions about the role. Nothing here is scored. I'll ask the same questions I ask every candidate."
| # | Question (read as written) | Competency | Probes (use only these) |
|---|---|---|---|
| 1 | Are you legally authorized to work in the US? Will you now or in the future require sponsorship? | Logistics, not scored | None |
| 2 | This role is on call one week in five, including nights and weekends. Can you meet that schedule? | Logistics, not scored | None |
| 3 | What salary range are you looking for? | Logistics, not scored | None |
| 4 | In year 1 this role owns our carrier-file ingestion pipeline and works down a backlog of failed invoice matches. Which parts of that do you want to grow into, and where would you want support? | Logistics, not scored | "Tell me more." |
Closing (5 min): candidate questions, next steps exactly as in the timeline (work sample sent today if you continue, review on Day 4, decision within 10 business days).

### Stage 1: Work sample + review, Priya, 60 min
Work sample (sent Day 1, 2-hour hard cap): a starter Go repo with a Postgres schema and three sample carrier files (a CSV with mixed date formats and amounts in cents, a short EDI 210 excerpt, a file with duplicate rows). Task: normalize them into the canonical invoice table and match each invoice to a shipment. Stop at 2 hours and add a short README note on what you would do next. AI tools are allowed; note where you used them.

Opening (2 min, read aloud): "Thanks for doing the exercise. I'll ask four questions, the same ones every candidate gets, and I'll take notes as we go. We'll look at your code first, then a short change I'll share. Please think aloud."
| # | Question (read as written) | Competency | Probes (use only these) |
|---|---|---|---|
| 1 | Walk me through your code from the moment a file is read to the moment an invoice is matched. Why did you structure it this way? | C2 | "Where would this break first with a file 10 times larger?" / "What would you test first with another hour?" |
| 2 | Here is a 40-line change to a normalizer. Review it the way you would review a teammate's pull request. | C2 | "Which comment would you block the merge on?" / "How would you write that fix?" |
| 3 | A carrier starts sending files with a different column order and amounts in cents instead of dollars, without telling us. What happens in your solution, and what would you change? | C1 | "How would we find out?" / "What happens to files already processed?" |
| 4 | Your matcher cannot match 8% of invoices. How would you change the design so those invoices are visible and can be re-run, rather than lost? | C1 | "Where do the unmatched invoices live?" / "How does someone re-run them after a fix?" |
Closing (5 min): candidate questions, next steps exactly as in the timeline (Jordan decides by Day 5, and if you continue, Dana books the remaining interviews as one block on Day 7).

### Stage 2: Pipeline design and incidents, Marco, 75 min (Sam shadows)
Opening (2 min, read aloud): "Thanks for joining. Sam is here to learn our process and won't be asking questions. I'll ask four questions, the same ones every candidate gets. The first is a design problem we really have, so ask me anything you'd want to know before designing."
| # | Question (read as written) | Competency | Probes (use only these) |
|---|---|---|---|
| 1 | Design the ingestion pipeline for carrier invoice files: about 200 carriers, EDI and CSV, arriving by SFTP and email, ending in Postgres for matching. Kafka is available. Start wherever you'd start. (25 min) | C1 | "The same file arrives twice. What happens?" / "One carrier sends a 2 GB file at month end. What changes?" |
| 2 | In your design, write or describe the Go code and SQL for the step that saves a normalized invoice and its line items. What makes it safe to retry? | C2 | "What happens if the process dies between the two writes?" / "What index does this need, and why?" |
| 3 | Tell me about the worst production incident you handled in the last two years. | C3 | "What did you check first, and why?" / "What did you change so it would not happen again, or be caught sooner?" |
| 4 | It's your on-call week. Kafka consumer lag on the ingestion topic has climbed for 40 minutes and new matches have stopped. Walk me through your first 15 minutes. | C3 | "What do you tell the support team, and when?" / "When do you wake someone else up?" |
Closing (5 min): candidate questions, next steps exactly as in the timeline (decision no later than Day 10).

### Stage 3: Ownership and mentoring, Jordan, 60 min (Sam shadows)
Opening (2 min, read aloud): "Thanks for your time. Sam is here to learn our process and won't be asking questions. I'll ask three questions about past work, the same ones every candidate gets. Specific examples help me most, and I'll ask what you personally did."
| # | Question (read as written) | Competency | Probes (use only these) |
|---|---|---|---|
| 1 | Tell me about a backlog of failed records, jobs or tickets you were asked to clear. How did you decide what to fix first? | C3 | "How did you know the fixes worked?" / "What did you change so the backlog would not grow back?" |
| 2 | Tell me about a time you were blocked for a day or more while working with people in other time zones. | C4 | "What did you write, to whom, and when?" / "What would you do differently now?" |
| 3 | Tell me about someone you helped get better at engineering work. | C5 | "What could they do afterward that they couldn't before?" / If no example: "Tell me about a time you helped a teammate learn a codebase or system." |
Closing (5 min): candidate questions, next steps exactly as in the timeline (decision no later than Day 10).

### Stage 4: Remote work and feedback, CTO, 30 min
Opening (2 min, read aloud): "Thanks for meeting me. I'll ask three questions about how you work with a distributed team, the same ones every candidate gets, then leave time for yours."
| # | Question (read as written) | Competency | Probes (use only these) |
|---|---|---|---|
| 1 | Tell me about a time you disagreed with a teammate or manager on a technical decision. | C4 | "How did you make your case, and in what format?" / "What did you do after the decision was made?" |
| 2 | Tell me about the most useful written feedback you received on your work, and what you did with it. | C4 | "What did you change?" / "How did you reply to the person?" |
| 3 | At your last job, how did you keep others aware of your progress when they were not online at the same time as you? | C4 | "What did a typical update contain?" / "Who read it?" |
Closing (5 min): candidate questions, next steps exactly as in the timeline (decision no later than Day 10).

## Scoring form (one per interviewer, submit before the debrief)
| Competency | Score 1-4 or NE | Evidence: quote or observed behavior |
|---|---|---|
| (only the competencies your stage assesses) | | |
Submitted within 24 hours. Do not discuss the candidate before submitting.

Scores stay hidden until every form is in. If you saw another stage's scores before your own interview, score that competency NE. Do not record anything about accent, age, looks, family, health, religion or origin, and do not use "overqualified".

## Debrief (30 minutes)
1. (2 min) Jordan confirms every form is in, then reveals all scores at once. The CTO and Sam do not score aloud; the CTO's written form stands as submitted.
2. (3 min) Read the bias traps aloud: halo (one strong answer lifting every score), similar-to-me (same school, same former employer, same hobbies), contrast effect (scoring against the previous candidate instead of the anchors), and presentation polish standing in for skill.
3. (12 min) Competencies where the two assessors differ by 2 or more points go first. Each assessor reads their evidence. If neither wrote a quote or observed behavior, both scores are struck and the competency becomes NE. Never average a split.
4. (8 min) Remaining competencies, in this speaking order: Priya, then Marco, then Marco reads the CTO's written evidence, then Jordan last. A score without a quote or observed behavior is not discussed.
5. (3 min) Must-have rule: if C1, C2, C3 or C4 was scored 1 by both assessors, name it as a serious gap and record in writing whether anything outweighs it. List any NE gaps and whether they block a decision.
6. (2 min) Questions that did not work are replaced for all later candidates, with the date noted.

Decision: made by Jordan, recorded with the evidence that drove it.

## Candidate email: what to expect
Subject: Your interview process at Tallyrun

Hi <Name>,

Thanks for your interest in the Senior Backend Engineer role. Here is the whole process, all by video:

1. A 30-minute call with Dana, our recruiter.
2. A coding exercise with a hard 2-hour cap, then a 60-minute review with Priya, Staff Engineer.
3. If we both want to continue, one interview block a few days later: system design with Marco, Principal Engineer (75 minutes), a conversation with me (60 minutes) and 30 minutes with our CTO.

AI tools are allowed on the exercise. Tell us where you used them and be ready to explain every line.

You will hear our decision within 10 business days of your first call.

If you need an accommodation, such as extra time or captioning, just reply to this email.

Jordan

## Legal lint
| Question | Issue | Rewrite |
|---|---|---|
| "Where do you see yourself in 5 years?" | Not tied to any competency, so it can't be scored. Answers often reveal family plans or age, which can then color the score (Title VII, ADEA risk). | Screen only, not scored: "In year 1 this role owns our carrier-file ingestion pipeline and works down a backlog of failed invoice matches. Which parts of that do you want to grow into, and where would you want support?" |
| "What year did you start coding?" | Age proxy (ADEA, protects 40+). Lets the interviewer estimate age. | Ask about the skill directly: "Walk me through your code from the moment a file is read to the moment an invoice is matched." (Stage 1, C2) |
| "How do you handle on-call with family stuff?" | Asks about family status (Title VII; EEOC warns that questions about marital status or children may violate it). Only some candidates tend to get asked it. | Ask every candidate in the screen: "This role is on call one week in five, including nights and weekends. Can you meet that schedule?" |
| "Tell me about a time you disagreed with a teammate" | No legal issue. Kept and tied to C4 with fixed probes. | "Tell me about a time you disagreed with a teammate or manager on a technical decision." (Stage 4, C4) |
| "Design a URL shortener" | No legal issue. Not tied to this job and widely rehearsed, so it tests preparation more than the work. | "Design the ingestion pipeline for carrier invoice files: about 200 carriers, EDI and CSV, arriving by SFTP and email, ending in Postgres for matching." (Stage 2, C1) |
| Culture fit lunch (unstructured) | Not illegal by itself, but unscored social judgment is a common route to proxy bias (age, family, background). | Removed. Its intent is assessed as C4 with fixed questions in Stages 3 and 4. |
| All other questions in this kit | No issues found in the questions reviewed. | n/a |
General information, not legal advice. US federal rules as of 2026; states and cities add more.

---
Made with the free Structured Interview Kit skill by Ruzora · ruzora.com/skills
