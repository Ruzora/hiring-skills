---
title: Software Engineer Leveling Guide, Applied by AI
description: Free AI skill that sets the level a role needs and estimates a candidate's real level by scope, with confidence, evidence and 3 questions to settle it.
target_query: software engineer leveling guide
category: interview
related_blog: mid-level-to-senior-developer-what-us-companies-expect
cta: /how-we-vet
author: Roberto Espinoza
updated: 2026-10-04
---

# A software engineer leveling guide that levels your actual role and candidate

Calibrate Seniority is a free AI skill that applies a software engineer leveling guide to your real situation: the level the work needs, and the level a candidate's evidence supports. It levels five dimensions by scope, not years. A CV alone never gets more than Low confidence, and you get three questions that settle the call.

Most leveling guides are a table you read once. This one argues with your plan: describe a "mid-level" hire who will own payments with nobody reviewing them, and it tells you that is senior scope.

## What you get

Paste a role description, a CV, interview notes, or all three. In about 10 minutes:

- **The level the work needs**, per dimension (scope, ambiguity, autonomy, ownership, technical depth), with mismatch flags when the planned level, title or budget does not fit.
- **The level the evidence supports**, with a quote and source per dimension, "NE" (no evidence) where nothing was tested, and a capped confidence rating.
- **A title check** that treats "Senior" as a claim about scope at that company.
- **The gap**, and the one dimension that puts the role's outcomes at risk.
- **Three questions that separate the two adjacent levels**, with what each level's answer sounds like.
- **Options with conditions.** The decision line stays blank for you.

It also accepts a role scorecard or interview scorecard you already made.

## Sample output

From a real run. The input: an 11-person freight software startup planning a "mid-level backend engineer, 3-5 years max" at $125-140k to own carrier payouts alone once the CTO moves to sales. The candidate's CV says "Senior Software Engineer" at a 6-person agency, after five years in carrier settlements on the operations side.

The level the work needs:

> **Needed level:** Senior, set by Autonomy and Impact and ownership. Scope and Ambiguity agree. **Reviewer test:** Fail. Once the CTO steps back nobody can review payout design decisions, so the role needs Senior at minimum.
> **Mismatch flags:** The role was planned as mid-level with a "3-5 years max" ceiling and a $125-140k budget. But this person owns payments alone with no reviewer, and that is senior scope. Either the level and budget move up, or the role is re-scoped, or a reviewer is added (see section 5). Staff is not needed: there is one payments system and three engineers, so the cross-team scope does not exist yet.

The level the evidence supports:

> **Estimate:** Mid · **Confidence:** Low. The sources are a CV and one 30-minute screen call. The CV alone caps confidence at Low, and a short screen does not raise it.
> | Dimension | Evidence (quote or close paraphrase, with source) | Points to | Strength |
> |---|---|---|---|
> | Autonomy | Stripe idempotency fix: "we added an idempotency check with the lead dev from the client", and the spec was not hers (screen). "Led a team of 2 junior devs on a hotel booking app" (CV), with no statement of what she decided. | Mid | Weak |


Her school's country, her graduation year and the year ceiling went into a "Not used" list. One of the three separating questions:

> | # | Question | A Mid answer sounds like | A Senior answer sounds like | Tests |
> |---|---|---|---|---|
> | 3 | "From January nobody here will review your payouts design or code. How would you know your design is right before it moves real money?" | Unsure, or "I'd check with the CTO", or "I'd test it well" with no detail. | Gives specifics: a written design doc, tests for duplicates and failed returns, a small first release (for example quick-pay for a few carriers), metrics and alerts on failed or duplicate payouts, and an outside reviewer for the parts that cannot be undone. | Autonomy (binding gap) |

It ended with three options (hire at Mid only with a senior reviewer for 6 months, re-level the role to Senior, or split the role) and a blank decision line for the CTO.

## How it works

The skill follows the rules an experienced engineering manager uses when a founder asks "is this person senior?"

**Level is scope.** Junior does tasks others defined. Mid delivers features end to end once someone framed the problem. Senior owns a system: designs it, builds it, runs it, fixes it, and turns a vague goal into a plan. Staff sets direction across several systems. Years are a weak proxy, and never a maximum: a year ceiling screens out older applicants, and the ADEA protects workers 40 and over.

**The reviewer test sets the floor.** At a startup where nobody can review the hire's design, mistakes surface in production. That role needs senior scope whatever the budget hoped.

**Built is not ran.** The senior signal is the second year: on call, the incident they owned, the migration off something they built. A CV where every story ends at launch is feature-level evidence, however big the feature.

**Titles depend on the company.** "Senior" after two years at a six-person agency often means trusted client delivery, not running production systems. A big-company senior may have owned a narrow slice while platform teams ran deploys and on-call. Each becomes a question, not an automatic up- or down-level. CV verbs get the same treatment: "worked on" is participant evidence, "owned" and "on call for" are system evidence.

**Confidence has caps.** CV only is Low, always. One structured interview with quotes reaches Medium. High needs two independent sources that agree.

**The floor rule.** The estimate is the lowest level among the dimensions the role depends on. Great technical depth with mid-level autonomy is a mid-level hire for a job that runs alone.

**Proxies stay out.** School prestige, graduation year, accent, nationality and gaps are never used; if your notes mention them, they are listed as struck. General information, not legal advice.

### How this compares

A static leveling guide or competency matrix gives you the ladder but leaves you to place the person, usually by title and years. A chatbot asked cold tends to accept the CV's title and answer "should we move her forward?" with a yes or no. This skill separates what was claimed from what was shown and hands you the questions that would change the answer.

## How to install and use

**Claude.ai:** download the skill's .zip and upload it under Customize > Skills (any plan, including Free; code execution must be on in Settings > Capabilities). Then paste the role, the CV or your notes.

**Claude Code:** run `/plugin marketplace add Remutopia/ruzora-skills`, then `/plugin install hire-interview@ruzora-hiring`. Ask "what level is this candidate?" and the skill loads.

**Any other AI (ChatGPT, Gemini, Copilot):** copy the prompt version of the skill, paste it as your first message, then paste your input.

Use a first name or a candidate code. Leave out photos, dates of birth and anything about health or family.

## Frequently asked questions

### How do you tell if a developer is really senior?
Look for ownership after launch: a system they designed and then ran, an incident they led, a decision they would now reverse. Titles and years vary too much between companies to settle it.

### What is the difference between a mid-level and a senior software engineer?
A mid-level engineer delivers features once someone else has framed the problem and reviews the design. A senior engineer takes a vague goal, writes the plan, builds and runs the system, and needs nobody for their area.

### Can I level a candidate from a CV alone?
Only as a starting estimate. The skill caps CV-only reads at Low confidence and tells you what evidence would raise it.

### Should a startup's first engineers be senior?
If nobody on the team can review their design decisions, usually yes. Hiring one level below works only when someone at the needed level reviews their work for the first months.

---

**Want candidates whose level is already checked?** See [how we vet](/how-we-vet): 5-stage vetting, including live coding, system design and AI-tool proficiency, for senior engineers in Latin America, working US hours. Or [request a vetted shortlist within 72 hours](/request-shortlist). For what US companies expect at each step, read [mid-level to senior developer: what US companies expect](/blog/mid-level-to-senior-developer-what-us-companies-expect).
