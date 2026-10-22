---
title: "Interview Kit Template for Engineering Roles (Free)"
description: "A free AI skill that builds a structured interview kit for an engineering role: lean loop, fixed questions, anchored 1-4 rubric and a legal lint."
target_query: interview kit template
category: interview
related_blog: structured-vs-unstructured-interviews
cta: /how-we-vet
author: Roberto Espinoza
updated: 2026-10-04
---

# Interview kit template for engineering roles, built for your loop

Structured Interview Kit is a free AI skill that turns one engineering role into a complete interview kit: at most four assessed stages with named owners, the same questions for every candidate, a 1-4 rubric with behavioral anchors, scoring and debrief rules, a candidate email and a legal lint. Built for small teams aiming to decide within 10 business days.

## What you get

- **Competencies** written as observable capabilities, marked must-have or nice-to-have.
- **The loop** (stages, owners, lengths, candidate time), a coverage check and a timeline to decision.
- **The rubric:** four anchored levels per competency plus "NE" for no evidence.
- **Interview guides** per stage: an opening script, 3-4 fixed questions and the only probes allowed.
- **Scoring form, debrief agenda, candidate email** and a **legal lint** of every question your team already likes.

## Sample output

From a run on a fictional Series A logistics company whose seven-stage loop was losing candidates, and whose team liked asking "What year did you start coding?" and "How do you handle on-call with family stuff?":

What changed from your current loop:
- 7 steps become a screen plus 4 assessed stages. Stages 2-4 are booked as one block, which fixes the scheduling delay that lost your last two candidates.
- The "should take a weekend" take-home breaks the 2-3 hour limit. It is trimmed to a 2-hour scoped exercise with a starter repo.
- The take-home review and system design stay, with the same owners. "Design a URL shortener" is replaced by the carrier-file ingestion problem you actually have.
- Your 1-hour "get to know you" becomes Stage 3, with fixed questions.
- The culture fit lunch is removed. It produces no scoreable evidence and invites similar-to-me judgments. Candidates still meet Sam in Stages 2 and 3.
- The CTO chat stays at 30 minutes, with fixed questions on C4.

**One competency from the rubric (C1, ingestion pipeline design for messy carrier files):**

| Score | Anchor (what you heard or saw) |
|---|---|
| 4 | Asks about carrier count, file volume and format variance before drawing anything. Keeps the raw file, makes processing idempotent (for example a file hash or carrier plus invoice number as the key) and names 2 or more trade-offs (strict vs lenient parsing, Kafka partition key, sync vs batch matching). When a carrier silently changes format, says how bad rows are quarantined, made visible and replayed after a fix, without being asked. |
| 3 | A workable end-to-end pipeline with raw file retention and a quarantine or dead-letter path. Names one trade-off. Handles the duplicate file or format change correctly after one probe. |
| 2 | Designs the happy path only. Duplicate files, a crash mid-file or a format change are missed until the probe, and the fix stays vague ("we'd validate it"). |
| 1 | No end-to-end flow, or bad rows are dropped or overwritten with no way to find or rerun them, and the candidate does not see the problem when probed. |
| NE | Not assessed in this stage, note why |

**From the debrief rules:**

3. (12 min) Competencies where the two assessors differ by 2 or more points go first. Each assessor reads their evidence. If neither wrote a quote or observed behavior, both scores are struck and the competency becomes NE. Never average a split.

## How it works

Structured interviews were the highest-ranked predictor of job performance in Sackett, Zhang, Berry and Lievens' 2022 re-analysis in the Journal of Applied Psychology, at a validity of about .42. The skill does the day of work that structure takes and applies these rules:

- **Four stages is enough.** Google's internal analysis, reported by CNBC in 2019, found four interviews predicted its hire decisions with 86% confidence, and each extra interview added less than 1%.
- **Two reads per must-have, never four.** Each must-have is assessed by two different people. A founder with no team gets a paid outside reviewer for the technical must-haves, or an honest note that coverage is weaker.
- **No evidence is not a 1.** If a stage didn't test something, the interviewer writes NE. And if two scores differ by 2+ points with no quote behind either, both are void, never averaged.
- **Score alone, then talk.** Written scores with quoted evidence are due within 24 hours, before any chat about the candidate. In the debrief, the least senior interviewer speaks first and the hiring manager last.
- **Speed is part of fairness.** Once a candidate passes the first stage, the rest are booked as one block.
- **The lint runs on your favorite questions too.** Graduation year, family plans, "where are you from" and salary history get flagged with a lawful rewrite.

The kit never outputs hire or reject. It organizes the evidence and leaves the decision to the hiring manager.

### How this compares

A downloaded interview kit template gives you generic questions and a 1-5 scale labeled "meets expectations". Asking a chatbot cold gets you a longer list of questions. Neither checks coverage, sets a time budget, or anchors each score in behavior two interviewers would agree on.

## How to install and use

**Claude.ai:** download the skill's .zip and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then paste your job description and list who can interview.

**Claude Code:** run `/plugin marketplace add Ruzora/hiring-skills`, then `/plugin install hire-interview@ruzora-hiring`, and ask for an interview kit for your role.

**Any other AI (ChatGPT, Gemini and others):** copy the prompt version of the skill from the repo, paste it as the first message, then describe the role.

It asks at most three questions or proceeds with stated assumptions.

## Frequently asked questions

### What should an interview kit include?

The competencies you're hiring for, the stages and who runs each, the exact questions per stage, a rubric with anchored score levels, a scoring form filled in before the debrief, and the debrief rules.

### How many interviews should a software engineer loop have?

For most startup roles, a short screen plus up to four assessed stages. More stages mostly add delay, and delay loses candidates.

### What is an anchored rating scale?

A scale where each score has a description of what the interviewer heard or saw at that level, such as "found the data-loss bug first and explained its customer impact". Two interviewers reading the same answer should land on the same score.

### Which interview questions are illegal?

In the US, questions about age or graduation year, national origin, citizenship beyond work authorization, family or pregnancy, religion, disability or health before an offer, and salary history where banned. General information, not legal advice; states and cities add more.

## Want engineers who already passed a structured loop?

Every Ruzora engineer goes through 5-stage vetting, including live coding, system design and AI-tool proficiency, and you get a vetted shortlist within 72 hours. See [how we vet](/how-we-vet) or [request a shortlist](/request-shortlist).

For the background on why structure matters, read [structured vs unstructured interviews](/blog/structured-vs-unstructured-interviews).
