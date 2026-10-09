# Leveling rubric

Use per dimension. A signal is something you can see in a CV line, a work sample or an interview answer. An anti-signal is what looks like the level but is not. Level each dimension on its own; then apply the floor rule from SKILL.md.

## 1. Scope (what they own)

| Level | Signals | Anti-signals |
|---|---|---|
| Junior | Tickets and bug fixes inside an existing codebase; one component or screen at a time. | "Built the app" when the story shows someone else designed it and they filled in parts. |
| Mid | A feature end to end: API, data, UI or job, tests, release. Can name the feature's users and what changed for them. | A long list of technologies or projects with no single thing they carried from start to release. |
| Senior | A system or service: its design, its data, its on-call, its roadmap. Others ask them before changing it. | A big system they "worked on" with 40 other engineers, where their slice was one endpoint. |
| Staff | Several systems or a cross-team concern (data platform, reliability, the payments domain). Their decisions show up in other teams' code. | Title "Lead" or "Head of Engineering" at a 3-person company: real breadth, but one system and no other teams to shape. |

## 2. Ambiguity (how unclear the problem can be)

| Level | Signals | Anti-signals |
|---|---|---|
| Junior | Works from a clear ticket; asks good clarifying questions. | Silent assumptions instead of questions. |
| Mid | Takes a product spec and fills the technical gaps; asks the lead when the spec is wrong. | Every story starts with "the tech lead told us to". |
| Senior | Takes a goal ("payouts keep failing", "the chain wants an integration") and writes the plan: options, what to cut, the order. Pushes back on the goal when it is wrong. | Restates the problem in more detail but never chooses; or chooses with no alternatives considered. |
| Staff | Finds the problem nobody has named yet (the architecture that will not survive next year's plan) and gets agreement to fix it. | Big vision talk with no shipped result. |

## 3. Autonomy (direction and review needed)

| Level | Signals | Anti-signals |
|---|---|---|
| Junior | Needs review on most work and a daily check-in. | Ships alone because nobody reviewed, not because it was safe. |
| Mid | Delivers a feature without help; design decisions go to someone more senior for review. | Describes being "the only dev" on client projects that were small, handed over at launch, and never run. |
| Senior | Needs nobody for their area. Asks for review as a choice, on the risky parts. Unblocks others. | Works alone but cannot say how they knew their design was right (no tests, no metrics, no second opinion). |
| Staff | Sets direction others follow without needing authority over them. | Authority by title only. |

## 4. Impact and ownership (built it, or built it and ran it)

| Level | Signals | Anti-signals |
|---|---|---|
| Junior | Finished tasks; fixed bugs others found. | Results claimed for the whole team. |
| Mid | Shipped features with a measured result; fixed bugs in their own features. | Percent improvements with no baseline or no "how" ("improved performance 40%"). |
| Senior | Ran what they built: on call, a postmortem they wrote, a migration they led, an alert they added after an incident, something they deprecated. Has "second year" stories. Uses "I" for their part and "we" for the team's. | Every story ends at launch. Every story is "we". |
| Staff | Changed how several teams work: a standard, a platform, a migration across services, hiring bar. | Wrote a doc nobody adopted. |

## 5. Technical depth (judgment in their area)

| Level | Signals | Anti-signals |
|---|---|---|
| Junior | Correct code for the main path; learning failure modes. | Copies patterns without knowing why; cannot explain code they just wrote (with or without AI). |
| Mid | Handles edge cases and tests unprompted; explains their choices when asked. | Knows the framework, not the problem: can't say what breaks under load or partial failure. |
| Senior | Names trade-offs before being asked, picks one and says what they gave up; handles failure-mode follow-ups (retries, idempotency, partial writes, what happens at 10x). Changes their mind when the pushback is right. | Recites best practices with no link to this problem; defends a bad choice after a clear hint. |
| Staff | Sees second-order effects across systems (cost, team load, migration paths) and makes them explicit. | Depth in one area presented as judgment in all areas. |

## CV verb ladder

| Verb in the bullet | Evidence of | Ask to confirm |
|---|---|---|
| worked on, helped, contributed to, was part of, assisted, exposure to | Participant (Junior evidence at most) | "What part was yours? Show me a decision you made." |
| built, implemented, developed, delivered, integrated | Feature (Mid evidence) | "Who designed it? Who ran it after launch?" |
| designed and ran, owned, on call for, migrated, rewrote, deprecated, led the incident | System (Senior evidence) | "What broke, and what did you change afterward?" |
| set direction, defined the standard, adopted by N teams, drove across teams | Cross-system (Staff evidence) | "Which teams changed what because of it?" |
| led a team of N | Coordination; level depends on what was led | "What did you decide that they would not have decided without you?" |

A bullet is only evidence if it has three parts: the system, the scale, and what changed because of this person. Missing two of three = "unverified".

## Title normalization

A title is a claim about scope at that company. Turn each case into a question, never an automatic up- or down-level.

| Situation | What the title often meant there | Question that settles it |
|---|---|---|
| "Senior" or "Lead" after about 2-3 years total, small agency or consultancy | Trusted with client delivery: many short projects, often handed over at launch, rarely run in production. | "Which project did you run in production for more than 6 months? What broke?" |
| Senior at a large company with platform teams | Owned a narrow slice deeply; deploys, infra, observability and on-call tooling were someone else's job. | "At a company with no platform team, what would you have to set up yourself in month 1?" |
| "Senior", "Lead" or "CTO" at an early startup | Owned everything, at small scale and with nobody reviewing. Breadth is real; depth and judgment are unproven. | "What decision from back then would you reverse now, and why?" |
| Mid-level or "Engineer II" at a large company | Can be senior-scope work under a conservative ladder. | "Walk me through the system you know best: who else could change it without asking you?" |
| Freelancer or contractor | Varies most. Delivery autonomy is real; long-term ownership often is not. | "Which client system are you still responsible for, or were for over a year?" |
| Company you do not know, or outside the US | Says nothing about scope either way. | "How many users, transactions or engineers? What were you on call for?" |

Never translate one company's level codes into another's from memory, and never state facts about a named company that the user did not give you.

## Confidence

| Evidence available | Highest confidence |
|---|---|
| CV, profile or portfolio only | Low |
| One screen call that asked scope questions | Low (screens are short and rehearsable) |
| One structured interview or assessment that probed the dimension, with quotes | Medium |
| Two or more independent sources that agree (work sample or code walkthrough plus a design or incident interview, or a reference confirming scope) | High |

## Question bank by adjacent pair

Pick 3 for the pair in play. Adapt the wording to the role's real system. Each has the answer you would hear at each level.

### Junior vs Mid
1. **"Walk me through a feature you shipped from the ticket to production."** Junior: describes their tasks inside it; someone else split the work. Mid: describes the whole feature, the data change, the tests, the release, and one thing they fixed after launch.
2. **"What did you do the last time the spec was wrong?"** Junior: built what was written, or waited. Mid: noticed, asked the right person a specific question, adjusted.
3. **"How did you test it?"** Junior: manual checks. Mid: names the edge cases they covered and why.

### Mid vs Senior
1. **"Tell me about a goal that arrived vague. What did you write or decide before any code?"** Mid: asked the lead or PM to clarify, then built. Senior: wrote a short plan with 2-3 options, picked one, named what was cut, got agreement.
2. **"Tell me about something you built that broke in production after launch."** Mid: fixed the bug when it was assigned. Senior: was on call or chose to own it, found the root cause, changed the design or added the alert, wrote it up.
3. **"Who reviewed your design decisions in your last role, and what did they catch?"** Mid: a lead reviewed every design; examples of corrections. Senior: asked for review on the risky parts by choice; can say what the reviewer caught and what they would have caught themselves.
4. **"What did you reject, and why?"** (follow-up to any design story). Mid: "it was the standard way". Senior: names the alternative and the cost of each.
5. **"If you joined and nobody reviewed your work, how would you know your design was right?"** Mid: unsure, or "I'd ask the CTO". Senior: tests, metrics, a written design doc, a small first release, an outside reviewer for the irreversible parts.

### Senior vs Staff
1. **"Tell me about a technical decision that changed how other teams work."** Senior: changed their own system's interface. Staff: proposed a standard or platform, got several teams to adopt it, ran the migration.
2. **"What problem did you find that nobody had asked you to fix?"** Senior: within their system. Staff: across systems, with the case they made to leadership.
3. **"How did you handle two teams needing incompatible things from your system?"** Senior: negotiated a compromise for their service. Staff: changed the architecture or ownership so the conflict stopped recurring.
4. **"Which engineers grew because of you, and how?"** Senior: mentored one or two. Staff: changed how a group makes decisions (review practice, design docs, hiring bar).

Follow-ups that expose a rehearsed answer: "What did you reject?", "What would you change now?", "What did your manager disagree with?", "Show me the code or the doc."
