# Anchors and flags

## The 1-4 scale (applies to every competency)

| Score | Label | Anchor (what the notes must show) |
|---|---|---|
| 4 | Strong yes | Clear evidence at or above the level, unprompted. Did the thing without hints, explained why, and handled a follow-up that pushed further. |
| 3 | Yes | Evidence at the level, with minor gaps or one hint needed. You would be comfortable if this were their weakest area. |
| 2 | Lean no | Partial evidence. Needed several hints, answered the "what" but not the "why", or the evidence is at the level below. |
| 1 | No | Evidence against: wrong or unsafe approach defended after a hint, or could not do a core part of the task. |
| NE | No evidence | The interview did not produce evidence on this competency. A gap, not a score. |

Rule: when the notes describe what the candidate actually did and you hesitate between two scores, pick the lower one and write what would have earned the higher one. That sentence is useful in the debrief. When the notes are interviewer shorthand with no behavior ("solid", "ok", "meh"), don't lower the score: score NE and ask the interviewer for the detail.

## Level adjustment

The same answer scores differently by level. A senior or staff candidate who needs a hint to consider failure modes (retries, timeouts, partial writes) scores a 2 on system design; a mid-level candidate with the same answer can score a 3. A founding engineer is scored on the senior bar plus ownership: they should raise the questions nobody asked (cost, on-call, what to cut).

## Anchors for common engineering competencies

**Problem solving / coding**
- 4: Clarified the problem before coding, chose an approach and said why, wrote working code, tested edge cases without being asked, explained the complexity.
- 3: Working solution with one hint; tested the main path; could explain choices when asked.
- 2: Partial solution; jumped into code without clarifying; could not explain why their approach worked.
- 1: No working path after hints, or could not explain code they had just written.

**System design**
- 4: Started from requirements and load, named the trade-offs, picked one and defended it, handled a failure-mode follow-up (what breaks at 10x, what if the queue is down).
- 3: Sound design for the stated scale; trade-offs named when asked.
- 2: Listed components without connecting them to the requirements; no trade-offs.
- 1: Design would not work for the stated requirements and the candidate did not see why after a hint.

**Code quality / review**
- 4: Found the important bugs first (correctness, security, data loss) before style; suggested a test for each.
- 3: Found most important issues; mixed them with style nits.
- 2: Mostly style comments; missed a correctness issue.
- 1: Missed or defended a clear bug.

**Ownership**
- 4: Specific story where they found a problem nobody assigned, fixed it, and followed through after shipping (metrics, docs, on-call). Uses "I" for their part and "we" for the team's.
- 3: Specific example of owning a project end to end.
- 2: Examples are about tasks they were given; vague on their own part.
- 1: Blames others for every failure, or no example.

**Communication (content, never accent or delivery)**
- 4: Explained a technical decision so a non-engineer could follow it, adjusted when asked, wrote or drew a clear summary.
- 3: Clear when asked to clarify.
- 2: Answers wander; the interviewer had to reconstruct the point.
- 1: Could not explain their own work after several attempts.

**Collaboration**
- 4: Specific example of disagreeing with a teammate, how it was resolved, and what they changed their mind about.
- 3: Specific example of working through a conflict.
- 2: Generic ("I get along with everyone").
- 1: Describes teammates with contempt, or no example.

**Working with AI tools (when the role expects it)**
- 4: Used the assistant for the right parts, caught its mistake, explained what they checked and why.
- 3: Used it productively and verified output when prompted.
- 2: Accepted output without checking; could not explain the generated code.
- 1: Could not proceed without the tool, or submitted code they could not explain.

## Flag phrases (strike from scoring, list in section 2)

| Written | Why it is a flag | What to ask or score instead |
|---|---|---|
| "young", "energetic", "hungry", "digital native", "overqualified", "set in their ways", graduation year | Age or age proxy (age 40+ is protected federally) | The specific behavior: pace, learning a new tool, with evidence |
| "accent", "English not great" (for a job where the interview went fine) | National origin proxy | Did they explain the trade-off clearly? Score the content |
| kids, spouse, pregnancy, "family commitments", "might need flexibility" | Sex / pregnancy / family status | Nothing. Availability is asked of every candidate the same way, as a job requirement |
| religion, holidays, church, prayer | Religion | Nothing |
| health, disability, "seemed nervous / anxious", medication | Disability; pre-offer disability inquiries are prohibited | Score the work evidence only |
| "culture fit", "not a fit", "vibe", "beer test", "reminded me of me", shared school or hobby as a positive | Vague similarity; a proxy risk and the similar-to-me bias | Name the needed behavior and score it with evidence |
| appearance, clothing, background in the video | Irrelevant; can proxy for religion, race or income | Nothing |
| where they are "really from", citizenship | National origin / citizenship status | The only lawful questions are whether they are authorized to work in the US and whether they will need sponsorship, asked the same way of everyone |

General information as of 2026-10, not legal advice. State and city laws add protected traits; check yours.
