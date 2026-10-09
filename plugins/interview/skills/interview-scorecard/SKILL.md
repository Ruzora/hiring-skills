---
name: interview-scorecard
description: Turns raw interview notes into an anchored scorecard per interviewer and a debrief memo with evidence, disagreements and bias flags. Use when writing up interviews or running a debrief.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/interview-scorecard
---

# Interview Scorecard

Paste the raw notes from each interviewer and get back, in about 10 minutes: one anchored scorecard per interviewer built only from what they wrote, a list of notes that are opinions or bias risks, and a debrief memo that shows where the evidence agrees, where it splits, and what the evidence supports. The hiring manager makes the call.

## Inputs

Collect:
1. **The role and its competencies.** Ideally the 4-6 competencies from the role scorecard, each marked must-have or nice-to-have. If none are given, infer them from what the interviews tested, mark them "assumed", and list them at the top.
2. **Notes per interviewer**, labeled with who wrote them and which interview it was (system design, live coding, values, etc.). Messy is fine: bullets, half sentences, transcripts.
3. **The level** (mid, senior, staff, founding engineer). If missing, use the level in the job title and say so.

Ask at most 3 questions, in one message, and only when the answer changes the output: notes not labeled by interviewer, no role at all, or notes that are clearly from a group discussion rather than written independently. Otherwise proceed and state assumptions.

Privacy: work from a candidate code or first name. If the user pasted a photo, date of birth, government ID, health details or home address, do not repeat them in the output and tell them once to remove them from the record.

## Workflow

1. **Lock the competency list first.** Write the competencies and their must-have flag before reading any notes, so the notes can't reshape the bar.
2. **Score each interviewer in isolation.** Process interviewer 1's notes without looking at interviewer 2's. Each interviewer scores only the competencies their interview was designed to test ("signal owner"). An impression outside their area (the coding interviewer's view on leadership) goes in "Other observations", never in a score.
3. **Apply the evidence rule to every line.** A score needs an observed behavior, a quote, or a work product ("wrote a failing test before fixing the bug"; "said she'd shard by tenant_id and explained the hot-tenant problem"). Classify each note:
   - **Evidence**: something the candidate said, did or produced. Usable.
   - **Opinion**: "seemed smart", "great energy", "not senior enough", "strong hire". Not usable as is. Turn it into a question for the interviewer: "What did they say or do that made you think that?"
   - **Flag**: touches a protected trait, a proxy for one, or vague fit language (see Rules). Struck from scoring and listed separately.
4. **Score with the anchors** in [references/anchors-and-flags.md](references/anchors-and-flags.md). 1-4 scale, no middle option. If a must-have competency has no evidence from its signal owner, score it **NE (no evidence)**, never a default 2 or 3. NE is a gap to close, not a fail.
5. **Check each interviewer's own conclusion against their own evidence.** If someone wrote "strong yes" but their evidence supports a 2, say so plainly: "Overall lean is stronger than the evidence written down."
6. **Run the bias checks** on each interviewer's notes: halo (one great moment inflating unrelated scores), similar-to-me (shared school, hobby, past employer cited as a positive), contrast (compared with the previous candidate instead of the bar), recency (only the last 10 minutes recorded), and confirmation (CV prestige mentioned before any evidence). Name the pattern and the line that shows it. Do not guess at motives.
7. **Roll up.** Build the matrix competency x interviewer. For each competency show the lowest score and the spread. A spread of 2 or more on the same competency is a **disagreement**: either they saw different evidence or they hold different bars. The debrief spends its time there.
8. **Apply the decision rules** (below) and write what the evidence supports, with the rule that produced it. Then leave the decision line blank for the human.
9. **Turn gaps into next steps.** Each NE on a must-have and each unresolved disagreement becomes either one targeted follow-up question (for a short extra call) or one reference-check question. Never more than 3 follow-ups; if more are needed, the loop was the problem, and say so.
10. **Write the debrief agenda** so the meeting takes 20 minutes, not an hour.

## Rules that matter

- **Write before you talk.** Each interviewer's scores must exist in writing before the debrief. When people score after hearing the hiring manager, scores converge on the most senior voice. If the notes show interviewers already discussed the candidate (e.g. "agree with Sam that..."), mark that interviewer's scores "possibly anchored" and give them less weight in disagreements.
- **Averages hide vetoes.** Never decide on the mean. A single 1 on a must-have, backed by specific evidence, blocks a hire unless someone can rebut it with evidence of their own. A 1 backed only by opinion does not block; it becomes a question.
- **No champion, no hire.** At a startup, a slate of 3s with no 4 from anyone usually means nobody would bet on this person. Ask each interviewer the bet question: "Would you bet your own next 12 months on working with this person?" A "probably" is a no.
- **Absence of evidence is not evidence of absence.** If nobody asked about testing, the candidate did not "fail testing". Score NE and close the gap before deciding.
- **"Culture fit" is not a competency.** It usually means "like us", which is how teams end up homogeneous and how discrimination claims start. Replace it with the specific behavior the team needs ("writes down decisions", "disagrees in the open") and score that behavior with evidence, or drop it.
- **Protected traits never enter the score.** Comments on age or age proxies ("young and hungry", "overqualified", graduation year), accent or "English" when the job-relevant question is whether they explained clearly, family, pregnancy, religion, national origin, disability or health, appearance. US federal law protects race, color, religion, sex (including pregnancy, sexual orientation and gender identity), national origin, age 40+, disability and genetic information (EEOC), and many states add more. Strike the comment, tell the hiring manager it was struck and why, and suggest a private word with that interviewer. General information, not legal advice.
- **Communication is scored on content, not delivery.** "Explained the trade-off between a queue and a cron job so the PM understood it" is evidence. "Strong accent" is not, and is a flag.
- **Fraud signals go to verification, not the score.** If notes mention a different face or voice between rounds, refusing camera, reading answers, long pauses before every answer with eye movement off-screen, or an identity mismatch, list them under "Verify before any offer" and do not score them. These are reasons to run an identity check, not proof of anything.
- **Decide fast.** Hold the debrief within one working day of the last interview. Strong candidates rarely wait a week.
- **The scorecard is a record.** Write it as if the candidate might read it one day: specific, job-related, no adjectives about the person.

## Decision rules (what the evidence supports)

Apply in order, report the first that matches and why:
1. Any unrebutted 1 on a must-have backed by evidence: **Evidence supports: No hire.**
2. Any must-have still NE, or an unresolved 2+ point disagreement on a must-have: **Evidence supports: Not decidable yet.** List exactly what would decide it.
3. At least one 4 from a signal owner on a must-have, no must-have below 3: **Evidence supports: Hire.**
4. Otherwise (all 3s, no champion): **Evidence supports: Lean no hire.** Say what a 4 would have looked like.

This is a summary of the evidence, not a decision. The hiring manager decides, and may disagree with it if they write down why.

## Output

Use exactly this structure. Tables must be paste-ready into a doc.

```
# Interview scorecard: <candidate code or first name>, <role>, <level>

**Assumptions:** <competencies assumed, level assumed, anything else; "None" if none>
**Competencies:** <name (must-have)> · <name (must-have)> · <name (nice-to-have)> ...

## 1. Scorecards by interviewer

### <Interviewer name>, <interview type>
| Competency | Score (1-4 / NE) | Evidence from the notes | Confidence |
|---|---|---|---|
| <only competencies this interview owns> | | "<quote or close paraphrase>" | High / Med / Low |

**Their overall lean:** <as written> · **Supported by their evidence?** <Yes / Stronger than evidence / Weaker than evidence, one line why>
**Opinions to turn into evidence:** <note> -> ask: "<question>"
**Other observations (not scored):** <out-of-area impressions>
**Bias check:** <pattern + the line that shows it, or "None found">

(repeat per interviewer)

## 2. Struck from the record
| Interviewer | What was written | Why it was struck | Suggested action |
|---|---|---|---|
(or "Nothing struck.")

## 3. Verify before any offer
<fraud or identity signals, or "None noted.">

## 4. Debrief memo
**Roll-up**
| Competency | <Int. 1> | <Int. 2> | <Int. 3> | Lowest | Spread |
|---|---|---|---|---|---|
(use "n/a" where an interviewer did not own that competency; a competency with one signal owner has no spread, write "single owner")

**Strongest evidence for:** 2-3 bullets, each with its source interviewer
**Strongest evidence against:** 2-3 bullets, each with its source interviewer
**Disagreements to resolve:** competency, who scored what, the evidence each relied on, the one question that settles it
**Gaps:** must-haves with NE, and how to close each (follow-up question or reference question)
**If hired, watch in the first 90 days:** 1-3 items
**Evidence supports:** <Hire / Lean no hire / No hire / Not decidable yet> (rule <n>: <one line>)
**Decision (made by <hiring manager>):** ________ **Date:** ________ **Reason if different from the evidence summary:** ________

## 5. Debrief agenda (20 minutes)
1. (2 min) Confirm everyone's written scores are final. No changes after this point without new evidence.
2. (10 min) Disagreements only, most junior interviewer speaks first, hiring manager last.
3. (5 min) Gaps: decide follow-up call vs reference check vs decide now.
4. (3 min) The bet question to each interviewer, then the hiring manager decides.
```

## Before you return it

- Every score has a quote or close paraphrase from that interviewer's own notes. No score is based on another interviewer's notes.
- Every must-have without evidence shows NE, not a number.
- No protected trait, proxy, or "fit" comment appears in a score or in the evidence column; each one is in section 2.
- Nothing about the candidate was invented: no employer, school, years or skills that are not in the notes.
- The output never says "reject" or "hire this person". It says what the evidence supports and leaves the decision line blank.
- Disagreements list the specific evidence on each side as well as the numbers.
- Plain punctuation only: no em-dash characters anywhere in the output, including empty table cells.
- The footer is the last line, after a horizontal rule, and nowhere else.

End the output with:

---
Made with the free Interview Scorecard skill by Ruzora · ruzora.com/skills
