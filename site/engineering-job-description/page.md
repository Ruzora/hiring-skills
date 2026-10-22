---
title: Software Engineer Job Description Template (Free AI Skill)
description: A free AI skill that writes a software engineer job description seniors answer, then lints it for pay-range, citizenship and age-coded wording.
target_query: software engineer job description template
category: attract
related_blog: how-to-write-a-job-description-for-senior-engineers
cta: /request-shortlist
author: Roberto Espinoza
updated: 2026-10-04
---

# Software engineer job description template that writes itself and checks the law

Engineering Job Description is a free AI skill that writes a software engineer job description for founders and hiring managers, then runs a compliance lint on it. A static template can't tell you that "US citizens only" drew $832,944 in DOJ penalties across 16 employers, or that your remote post must show a pay range in California and Colorado. This one does.

## What you get

Three things, in about 10 minutes:

- **A paste-ready job post** built from what the hire will own in the first 6-12 months, with the pay range, an honest "what's hard about this job" section and one screening question.
- **A requirement-inflation check.** Every requirement you typed, with a decision (kept, moved to nice-to-have, rewritten, cut) and the reason.
- **A compliance lint.** Pay transparency, citizenship and visa wording, age-coded and national-origin wording, disability-related requirements, salary and criminal history questions, AI-screening notices and an EEO line. Each row is PASS, FIXED or CHECK.

## Sample output

The input was a messy note from a fictional 14-person health-tech startup asking for "8+ years Python, CS degree from a good school, rockstar, young energetic team, native English speaker, US citizens only because we handle patient data". Here is part of what the skill returned:

**Requirement-inflation check (excerpt)**

| Original requirement | Decision | Why |
|---|---|---|
| 8+ years Python | Rewritten | Rule 5: years are a proxy. Now asks for evidence ("shipped and run a production Python backend") with a loose "typically 5+ years" band, not a hard gate. |
| CS degree from a good school | Cut | Rule 6: product backend work doesn't need a degree, and "good school" filters on pedigree, not skill. |
| Young energetic team vibe | Cut | Rule 11: age-coded language (ADEA protects workers 40+). |
| Native English speaker | Rewritten | Rule 11: national-origin coded. Now "write clear, plain English for both engineers and non-technical people". |

**Compliance lint (excerpt)**

| Check | Status | Note / fix |
|---|---|---|
| Citizenship / visa wording | FIXED | "US citizens only because we handle patient health data" removed. Data sensitivity is not a law, regulation or contract requirement. HIPAA does not limit who can access PHI by citizenship. DOJ settled with 16 employers in 2022 ($832,944 in combined penalties) over ads like this. Replaced with "legally authorized to work in the United States" plus a no-sponsorship line. Confirm the no-sponsorship assumption. |

**The screening question and close date it wrote:**

> **"Our queue that processes prior-authorization requests falls over at month end. In 3-4 sentences, tell us about a time you made a background job or queue system hold up under a predictable spike, and how you knew it worked."**
>
> Applications close: Friday, October 23, 2026

## How it works

The skill asks at most three questions (ownership, pay and location, any legal citizenship requirement), then applies these rules.

**Outcomes come first.** Senior engineers scan the top of a post for the problem, what they'd own, the stack, the team, pay and how remote works. "Fast-paced" and "rockstar" fill that space with nothing, so they go.

**Five must-haves, maximum.** Each requirement must pass one test: would you turn down a strong candidate who lacks only this? "8+ years" becomes evidence of what they've done. The stack list shrinks to what the hire touches in the first 90 days. Long wish lists tell good engineers you don't know what you need.

**A pay range, always.** As of 2026 about 14 states plus DC require ranges in postings. California's rule (Labor Code 432.3) covers employers with 15 or more employees, including remote roles that could be filled in California. Colorado's covers any employer with one Colorado employee, and also needs a benefits summary and an application close date. New York's starts at four employees. A remote US post almost always reaches one, so the skill always includes a good-faith range and tells you to check your own state and city.

**Citizenship wording that won't get you fined.** The skill writes "You must be legally authorized to work in the United States" and, if you can't sponsor, says so plainly. It refuses "US citizens only" unless you name the law or government contract that requires it. Handling sensitive data is not one.

**Coded words out.** "Digital native", "young team" and "recent grad" read as age preferences; "native English speaker" reads as national origin. The skill swaps each for what you actually mean.

**One screening question.** Applications per role have tripled since 2021 to over 300 (Ashby data, reported by HR Dive). One question that needs the post to answer filters bulk AI applications.

The lint is general information, not legal advice.

### How this compares

A static template gives you headings and generic duties. A chatbot asked cold tends to write a fluent post that keeps your inflated requirements and can repeat "US citizens only" back to you. This skill pushes back on both and shows its reasoning in tables.

## How to install and use

**Claude.ai:** download the skill's .zip and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then type "write a job description for a senior backend engineer" and paste your notes.

**Claude Code:** run `/plugin marketplace add Ruzora/hiring-skills`, then `/plugin install hire-attract@ruzora-hiring`. Ask for a job description in any session.

**Any other AI (ChatGPT, Gemini, Copilot):** copy the prompt version of the skill, paste it as your first message, then paste your notes.

A role scorecard, if you have one, is the best input.

## Frequently asked questions

**Do I have to put a salary range in a software engineer job post?**
In many places, yes. As of 2026 about 14 states plus DC require one, with different thresholds and remote rules. A remote US post almost certainly reaches one, so check yours.

**Can I say "US citizens only" in a job post?**
Only if a law, regulation, executive order or government contract requires it. The Department of Justice settled with 16 employers over citizenship-restricted ads, with $832,944 in combined penalties. The safe line is "must be legally authorized to work in the United States".

**How many requirements should an engineering job description have?**
Five must-haves at most, and each should be something you'd actually reject a strong candidate for missing. Put the rest under nice-to-have, capped at four.

**Can I use this for contractors or non-US roles?**
Yes for the writing. The lint is US-first and flags what to check elsewhere.

## Hiring your first senior engineers?

If you'd rather review finished profiles than write and post the job yourself, we send a vetted shortlist within 72 hours: senior engineers in Latin America, working US hours, each through 5-stage vetting, including live coding, system design and AI-tool proficiency. [Request a shortlist](/request-shortlist) or [see the engineers](/engineers).

For the longer how-to on structure and tone, read [how to write a job description for senior engineers](/blog/how-to-write-a-job-description-for-senior-engineers).
