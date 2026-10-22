---
title: Interview Scorecard Template, Filled From Your Notes
description: Free AI skill that turns raw interview notes into anchored 1-4 scorecards per interviewer and a debrief memo with evidence, disagreements and bias flags.
target_query: interview scorecard template
category: interview
related_blog: structured-vs-unstructured-interviews
cta: /how-we-vet
author: Roberto Espinoza
updated: 2026-10-04
---

# Interview scorecard template, filled from your interview notes

Interview Scorecard is a free AI skill that turns raw interview notes into an anchored 1-4 scorecard per interviewer and a debrief memo, for startups hiring engineers. A blank template still leaves you to score. This one scores from evidence only, strikes biased comments, and shows where interviewers disagree.

Structured interviews are the strongest single predictor of job performance in recent meta-analysis (about .42, Sackett, Zhang, Berry and Lievens, 2022, Journal of Applied Psychology). It only pays off if the scoring is structured too, the part small teams skip.

## What you get

Paste the notes each interviewer wrote (bullets, half sentences, a transcript) and the role's must-have competencies. In about 10 minutes you get:

- One scorecard per interviewer, each score backed by a quote from their own notes
- "NE" (no evidence) where a must-have was never tested, instead of a polite 3
- Opinions like "seemed sharp" turned into a question for the interviewer
- A "struck from the record" table for comments about age, accent, family or "culture fit"
- A debrief memo: evidence for and against, disagreements, gaps, a 90-day watch list, and what the evidence supports, with the decision left to the hiring manager
- A 20-minute debrief agenda

## Sample output

This is from a real run on a fictional startup's notes: three interviewers, a senior backend candidate, and the kind of messy comments real notes contain.

**Priya (Senior Eng), live coding**

| Competency | Score (1-4 / NE) | Evidence from the notes | Confidence |
|---|---|---|---|
| Coding quality | 3 | "took ~8 min asking clarifying qs (what counts as dupe, timezone)". Wrote it in Python and it "worked for main case". She "missed the case where amounts are strings with commas, found it herself when I said 'try the sample file'". "No tests until I asked, then wrote 2 pytest cases quickly." "Talked through complexity fine." That is a working solution after one hint, with explained choices, which matches the 3 anchor. A 4 would have needed the comma edge case and tests without prompting. | High |

**Their overall lean:** "lean no. not sure she's senior" · **Supported by their evidence?** Weaker than evidence. The written evidence supports a 3. The lean rests on speed compared with another candidate and on a comment that has been struck, not on a written coding gap.

**2. Struck from the record**

| Interviewer | What was written | Why it was struck | Suggested action |
|---|---|---|---|
| Marcus | "she's probably early 40s, wondering if she'd be ok with startup pace vs big bank" | Age guess and age-based doubt. Age 40+ is federally protected. | Remove from the doc. Have a private word with Marcus. If pace matters, define the behavior (for example "ships small PRs daily") and ask every candidate the same question. |
| Priya | "strong accent, communication might be an issue with the team?" | Accent is a national origin proxy. Her own notes say she "talked through complexity fine", so the content she communicated was clear. | Remove from the doc. Have a private word with Priya. Score communication on content only. |
| Jordan | "mentioned she has two kids so might need flexible hours, fine with us but flagging" | Family status, sex and pregnancy proxy. It is not job-related. | Remove from the doc. Have a private word with Jordan. Ask every candidate about availability the same way, as a job requirement. |

## How it works

The skill follows the rules an experienced engineering hiring manager uses in a debrief.

**Scores are written before anyone talks.** Otherwise they drift toward the most senior voice. If notes show interviewers already compared views, the skill marks those scores as possibly anchored.

**Every score needs evidence.** A quote, a behavior or a work product. "Great energy" is not evidence, and neither is "not senior enough". Only evidence reaches a score.

**Each interviewer scores their own area.** The coding interviewer's view on leadership is noted, not scored. That stops one strong impression from spreading everywhere (the halo effect).

**Averages hide vetoes.** The skill never decides on the mean. One evidence-backed 1 on a must-have blocks a hire unless someone rebuts it with evidence. A 1 backed only by opinion becomes a question instead.

**No champion, no hire.** A slate of 3s with no 4 usually means nobody would bet on this person. The skill asks the bet question explicitly.

**"Culture fit" is not a competency.** It usually means "like us". Name the behavior the team needs and score that. Comments touching protected traits (age, national origin, sex and pregnancy, religion, disability, or their proxies) are struck and listed.

**Fraud signals go to verification.** Camera refusal or a face that changes between rounds goes under "verify before any offer", never into a score.

**How this compares.** A static scorecard template gives you empty boxes and a 1-5 scale with a middle to hide in. A chatbot asked cold usually averages the opinions, repeats the biased comment and recommends a hire. This skill keeps opinions out of the score and leaves the decision with you.

## How to install and use

**Claude.ai:** download the skill's .zip and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then paste your notes.

**Claude Code:** run `/plugin marketplace add Ruzora/hiring-skills`, then `/plugin install hire-interview@ruzora-hiring`. Then paste your notes.

**Any other AI (ChatGPT, Gemini, Copilot):** copy the prompt version of the skill, paste it as the first message, then paste your notes.

Label each block of notes with the interviewer and the interview type. Remove anything you shouldn't be storing: photos, dates of birth, health details.

## Frequently asked questions

**What should an interview scorecard include?**
The role's competencies with must-haves marked, a scale with written anchors, an evidence column, and the interviewer's overall lean. This skill adds "NE" so untested skills don't get a guessed score.

**Why a 1-4 scale instead of 1-5?**
A 5-point scale lets interviewers park at 3. With four points everyone has to lean yes or lean no, and the anchors say what each score requires.

**Can AI make the hire or no-hire decision?**
It shouldn't, and this skill doesn't. It summarizes what the evidence supports and leaves the decision to the hiring manager. New York City and Illinois also regulate automated tools in hiring decisions.

## Want candidates who arrive pre-vetted?

The scorecard helps you judge the candidates you have. If you'd rather start from engineers who already passed 5-stage vetting, including live coding, system design and AI-tool proficiency, see [how we vet](/how-we-vet) or [request a vetted shortlist within 72 hours](/request-shortlist).

For the reasoning behind structured scoring, read [structured vs unstructured interviews](/blog/structured-vs-unstructured-interviews).
