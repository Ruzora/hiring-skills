---
title: Reference Check Questions for Engineers, With a Script
description: Free AI skill that writes reference check questions aimed at your candidate's real risks, verifies referees are genuine, and removes illegal questions.
target_query: reference check questions
category: close
related_blog: how-to-check-a-developers-references
cta: /how-we-vet
author: Roberto Espinoza
updated: 2026-10-04
---

# Reference check questions aimed at your candidate's real risks

Reference Check is a free AI skill that writes reference check questions for an engineering finalist, aimed at the doubts your interviews left open. It also checks that each referee is a real person who worked with the candidate, and removes questions you shouldn't ask.

In a 2025 Checkr survey of 3,000 US managers, 31% said they had interviewed someone later found to be using a fake identity. Generic reference questions get generic praise, because candidates choose referees who like them. A useful reference call tests two or three specific risks, asks for a ranking, and listens for hesitation.

## What you get

Give the skill your debrief worries and the referees the candidate named. In about 10 minutes you get:

- 2-4 named risks a referee can confirm or refute
- A verification route for every referee that doesn't rely on contact details from the candidate
- A 15-minute call script: five core questions for everyone, plus targeted questions per risk
- A "do not ask" box for the call
- A risk register to fill in as you call
- The legal steps that match who is calling
- Two short emails: to the candidate and to each referee

## Sample output

From a real run on a fictional startup's request. The founder wanted to ask about sick days and past pay; the skill removed both and explained why.

**1. Risks to test**

| # | Risk (confirmable or refutable) | Source (which interview / note) | Best referee |
|---|---|---|---|
| 1 | May not have *led* the move from Expo managed to bare workflow or the Stripe payments rewrite at Kindlewise. He may have been a team member, and the backend payment pieces (webhooks, retries) may have been someone else's. | System design interview (strong on mobile, fuzzy on payments backend); CTO's read | Sandra (manager): who led and who made the design decisions. Leo (peer): who built what, especially the server side |
| 2 | Waits for others to define a vague brief instead of driving it himself. | Product interview (PM) | Sandra first, Leo second. Ideally a Kindlewise PM (see missing referee types) |
| 3 | The 8-month Arcwell Labs contract in 2024 may not have happened as described (company, role, length). | CV / debrief; website down | Raj, once verified. Otherwise a different Arcwell contact |

Sick-day question removed: protected territory. Use the reliability question about dates held instead. Salary question removed: salary-history bans cover asking through others. Price the role from your own band and ask Theo for his expectations.

## How it works

**Start from the risks.** Each worry from the interviews becomes one sentence a referee can confirm or refute ("may have been on the payments migration team, not its lead"). More than four open risks means the interview loop didn't do its job.

**Verify before you dial.** Fake references are part of the fake-candidate kit, and the FBI's January 2025 advisory on North Korean IT workers tells employers to verify identity throughout hiring. The skill has you find each referee yourself, reach them through the company's main line or a company email address, and confirm when and how they worked with the candidate. A personal Gmail and a mobile number from the candidate are not enough on their own.

**Ask the questions that produce signal.** Ranking ("top 5%, 10%, 25% or 50% of engineers at their level?"), what they coached the candidate on, who actually led the named project, and the rehire question. Referees rarely say bad things, so the signal is in how enthusiastic they are. "Absolutely, tomorrow" and "yes, in the right role" are very different answers.

**Treat a factual mismatch as a stop sign.** A different title, different dates, or "I led that, he worked on part of it" means you pause and ask the candidate neutrally before the offer.

**Stay on the job.** Never ask about health, sick days, family, age, religion, national origin, arrest records or pay. California's salary-history ban, for example, covers seeking pay history "personally or through an agent", which includes asking a former manager.

**Know when federal law kicks in.** If a background-check company runs the reference calls for you, it is a consumer report under the Fair Credit Reporting Act, and interviews about character or work make it an "investigative consumer report". That means a standalone disclosure, written consent, a notice within 3 days of ordering, and adverse-action steps before any rejection based on it. General information as of 2026-10, not legal advice.

**How this compares.** A list of "25 reference check questions" gives you the same generic questions for every candidate and nothing on fraud. A chatbot asked cold usually adds the questions you asked for, illegal ones included. This skill ties every question to a named risk and verifies the referee.

## How to install and use

**Claude.ai:** download the skill's .zip and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then paste your debrief notes and the referee list.

**Claude Code:** run `/plugin marketplace add Ruzora/hiring-skills`, then `/plugin install hire-close@ruzora-hiring`, and ask for a reference check plan.

**Any other AI (ChatGPT, Gemini, Copilot):** copy the prompt version of the skill, paste it as the first message, then add your notes.

Keep referee details to name, company, title and work contact. Don't paste ID documents or health information.

## Frequently asked questions

**What are good reference check questions for a software engineer?**
Ask how they worked together and for how long, what the candidate personally owned on a named project, where they rank among engineers at their level, what they were coached on, and whether the referee would hire them again and for what role.

**How do I know a reference is real?**
Find the referee yourself, call through the company's main line or email their company address, and confirm overlapping dates and the working relationship early in the call. Unverifiable referees are replaced, not accused.

**Can I ask a reference about sick days or salary?**
No. Absences can touch disability and medical-leave protections, and many states and cities ban seeking pay history, including through a third party. Ask about reliability of delivery instead.

**Do I need the candidate's consent for reference checks?**
Ask for it anyway, and never call a current employer without it. If an outside company runs the checks, FCRA written authorization and disclosure are required.

## Hiring engineers without the guesswork

Reference checks are the last layer of vetting. If you'd rather start from engineers who already passed 5-stage vetting, including live coding, system design and AI-tool proficiency, see [how we vet](/how-we-vet) or [request a vetted shortlist within 72 hours](/request-shortlist).

For the full how-to, read [how to check a developer's references](/blog/how-to-check-a-developers-references).
