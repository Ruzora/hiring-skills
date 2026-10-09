---
title: Role Scorecard Template for Engineers (Free AI Skill)
description: A free AI skill that turns a vague engineering hire into a role scorecard with 12-month outcomes, must-haves, competencies and an interview map.
target_query: role scorecard template
category: plan
related_blog: hiring-manager-intake-form-template
cta: /pricing
author: Roberto Espinoza
updated: 2026-10-04
---

# Role scorecard template for engineering hires, filled in by AI

Role Scorecard is a free AI skill that turns a vague engineering hire into a one-page role scorecard for founders and hiring managers. You describe the problem; it writes the mission, 3-5 measurable 12-month outcomes, at most 4 must-haves, competencies with evidence anchors and an interview map. It also strips the wording that shrinks your pool or creates legal risk.

A blank template asks you to fill in boxes. This skill argues with you first. Paste "rockstar full-stack dev, 5+ years, ML a plus" and it asks what is actually broken, then builds the role around that.

## What you get

- **A mission in one sentence**, in business terms ("make sync reliable enough that clinics stop calling support"), not a list of technologies.
- **3-5 outcomes for month 12 plus one for day 90**, each with a measure, a date and the evidence that would prove it. Missing numbers stay as `[target]` placeholders; it never invents your metrics.
- **A unicorn check.** If the outcomes need more than two specialties at senior depth, it tells you the job is two jobs and offers a split or a sequence.
- **A level set by scope, not years**, flagged when budget and level do not match.
- **Must-haves capped at 4**, each tied to an outcome and to the interview stage that tests it.
- **Language fixes** for proxies like "5+ years", "young, energetic team" and "native English speaker".

## Sample output

From a real run. The input: a 14-person company selling scheduling software to physical therapy clinics, a non-technical CEO, a job post that read "Rockstar Full Stack Developer. 5+ years React and Node, AWS, CS degree required, ML experience a plus. Must be a culture fit with our young, energetic team. Native English speaker." The real problems were a calendar sync that broke weekly, a stale mobile app, and a 30-clinic customer demanding an EHR integration by Q2.

> **Unicorn check:** The real problems need three specialties: backend integrations (sync and EHR), mobile (React Native) and ML. Nothing in your problems needs ML, so it is dropped. Mobile is a separate specialty at senior depth. **Sequence it:** this hire covers outcomes 1-4. Fix the mobile app with a React Native contractor on a fixed scope now, or make it the next hire.

> | Must-have | Tied to outcome | Tested at |
> |---|---|---|
> | Has owned a production service that syncs with third-party APIs (OAuth, webhooks, retries, idempotency, rate limits), including being on call for it | 1, 2 | Technical interview |
> | Can find the cause of an intermittent data-sync failure from logs and data, and propose a fix with its trade-offs | 90d, 1 | Work sample |

> | Found | Replace with | Why |
> |---|---|---|
> | culture fit | "Raises bad news early with options" and "writes things down so others can run them" | Can't be scored and invites bias |
> | young, energetic team | Remove | Age proxy (the ADEA protects workers 40 and over) |
> | Native English speaker | "Clear written and spoken English for daily async work" | National-origin proxy |

The "Rockstar Full Stack Developer" became "Senior Software Engineer, Integrations".

## How it works

The skill follows the rules a seasoned engineering manager uses when a founder says "we need an engineer".

**Outcomes come before skills.** A technology list tells you who to source. Outcomes tell you who to hire. Each outcome must pass one test: could two people disagree about whether it happened? If yes, it gets rewritten. "Write clean code" is an activity. "Ship the billing rewrite to every customer by month 6 with zero lost invoices" is an outcome.

**Five outcomes and four must-haves are ceilings.** More outcomes means you are describing a department. More must-haves shrinks the pool for little gain, because most "requirements" are learnable in a quarter by a strong engineer. The skill asks of every requirement: would you turn away an excellent person who lacks this but could learn it in 90 days? If not, it moves to nice-to-have.

**Senior is a scope.** The level ladder is about what the person owns without help. If you have no other senior engineer, your hire works without a spec and without a reviewer, so the scorecard says Senior whatever the budget hoped for, and tests judgment directly.

**Every requirement gets exactly one interview stage.** That map becomes your interview plan.

**Proxies and protected traits come out.** Year ceilings screen out older applicants, and the ADEA protects workers 40 and over. "Native English speaker" is a national-origin proxy. "US citizens only" has led to U.S. Department of Justice settlements when no law or government contract required it. The skill replaces each with the job-related version. This is general information, not legal advice.

### How this compares

A static template leaves the judgment to you. A general chatbot asked cold usually polishes the wish list you typed, "5+ years" and "culture fit" intact. This skill pushes back, caps the list and ties every line to a test.

## How to install and use

**Claude.ai:** download the skill's .zip from this page and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then start a chat and describe the role, or paste your draft job post.

**Claude Code:** run `/plugin marketplace add Remutopia/ruzora-skills`, then `/plugin install hire-plan@ruzora-hiring`. Ask for a role scorecard and the skill loads on its own.

**Any other AI (ChatGPT, Gemini, Copilot):** copy the prompt version from this page, paste it as your first message, then describe the role.

Give it the problem, your team setup and hard constraints. It asks at most three questions, or drafts with stated assumptions. About 10 minutes.

## Frequently asked questions

### What should a role scorecard include?
A one-sentence mission, 3-5 measurable outcomes for the first year, a level, at most four must-haves tied to those outcomes, competencies with observable signals, deal-breakers, and which interview stage tests each item. This skill produces all of them on one page.

### What is the difference between a role scorecard and a job description?
The scorecard is the internal definition of success that your interviewers score against. The job description is the public ad written from it. Write the scorecard first; the job post gets shorter and sharper as a result.

### Can a non-technical founder use this?
Yes. It is built for that case. You describe what is broken in plain words, and it translates that into outcomes, a level and the technical must-haves, then flags the questions to run past a technical advisor.

### Is it free?
Yes. No signup and no email gate. Use it, change it and share it under CC-BY-4.0.

---

**Scoped the role and now weighing the cost of filling it?** See [flat monthly pricing](/pricing) for senior engineers in Latin America, working US hours, or [request a shortlist](/request-shortlist) and get a vetted shortlist within 72 hours. For the intake conversation that comes before the scorecard, read our [hiring manager intake form template](/blog/hiring-manager-intake-form-template).
