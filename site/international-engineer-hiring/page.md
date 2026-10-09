---
title: Hire International Contractors: Free AI Planning Skill
description: A free AI skill that plans how to hire international contractors and engineers: contractor vs EOR vs vendor, a risk register and questions for counsel.
target_query: hire international contractors
category: plan
related_blog: contractor-vs-employer-of-record-remote-engineers
cta: /why-latam
author: Roberto Espinoza
updated: 2026-10-04
---

# Hire international contractors without the classic mistakes

International Engineer Hiring Plan is a free AI skill that helps founders hire international contractors and engineers safely. It returns an engagement plan comparing 4 models (direct contractor, employer of record, staffing vendor, own entity), a risk register, a setup checklist, and the exact questions to ask a local lawyer and your tax advisor.

It is general information, not legal or tax advice. That is deliberate: country law changes, so the skill states no country-specific rule as fact. It turns each one into a precise question for counsel, written around your facts.

## What you get

- **A six-signal classification check.** It counts how many signs of employment your plan has: full-time hours you set, open-ended term, only client, your equipment and email, part of your team rituals, fixed monthly pay. Three or more and your "contractor" looks like an employee.
- **The four models compared for your case**, with a starting model, a runner-up and the conditions that would switch them. You decide.
- **A risk register**: reclassification, IP, permanent establishment, customer-contract and data-access limits, sanctions, export controls, a US work trip (visa), payment fraud, exit cost. Each with why it applies to you, a likelihood and a mitigation. Risks that do not apply get a one-line reason.
- **A setup checklist, questions for counsel** (local lawyer, US tax advisor, EOR or vendor) and **a 30-day timeline**.

## Sample output

From a real run. The input: a 12-person US analytics company planning to engage a senior data engineer in São Paulo as a full-time contractor with no end date, a company laptop and email, a flat monthly payment, and access to a warehouse holding hospital patient data under two business associate agreements.

> **Short answer:** don't send the offer yet. The setup you describe is a full-time employee with a contractor label. An online template probably won't hold up in a reclassification claim, and it won't cover what your hospital BAAs require.

> | Risk | Why it applies to you | Likelihood (why) | Mitigation | Owner |
> |---|---|---|---|---|
> | Breach of a BAA or customer contract by offshore PHI access | Snowflake holds patient-level data covered by two BAAs. BAAs often restrict subcontractors, data location or where data can be accessed from. | High until you've read them (unknown terms, and you'd be relying on them) | Read both BAAs, your MSAs and any security questionnaires you've answered before granting access. Give notice or get consent where required, and sign a downstream BAA or equivalent with her or the EOR. | You + your US healthcare/privacy counsel |

The full output also flagged the one-week trip to Austin as a tax and immigration question to settle before booking travel.

## How it works

**The contract label does not decide classification.** In the US the IRS looks at behavioral control, financial control and the relationship of the parties, and many countries also look at how the work runs in practice. A full-time, open-ended, managed-like-staff "contractor" is the classic pattern behind reclassification claims. The skill counts your signals and sends the question to local counsel instead of guessing.

**An EOR solves employment, not every tax question.** An employer of record legally employs the person in their country for you. Permanent establishment, a taxable presence for your company abroad, is a separate question. Under Article 5 of the OECD Model Tax Convention, someone who habitually concludes contracts on your behalf can create one. An engineer who writes code and signs nothing is generally a lower concern, but your tax advisor confirms it.

**IP needs a written chain.** Under 17 U.S.C. 101, contractor work is generally not a "work made for hire", so you need a signed, present-tense assignment. Through an EOR or vendor, the chain runs engineer to provider to you. Local counsel confirms it holds up locally.

**US tax paperwork follows the person.** According to the IRS, pay to a nonresident alien for services performed outside the United States is foreign-source income, not subject to US withholding or reporting. Many companies collect Form W-8BEN to document that; a US citizen abroad gives a W-9 instead.

**Check sanctions, exports and your own contracts.** OFAC says all US persons, companies included, must comply with US sanctions, so screen names in its Sanctions List Search. Sharing controlled technology or source code with a foreign person can be an export (the Commerce Department calls the inside-the-US case a "deemed export"). And your enterprise customers' contracts may limit where their data can be accessed from.

**Payment hygiene stops fraud.** Pay only into an account in the engineer's own name in the country where you verified they live. No crypto, no third-party accounts, and a live video check before any change to bank details or shipping address. US and allied agencies list exactly these red flags in their July 2026 alert on North Korean IT workers.

### How this compares

A generic guide explains the models and stops; a chatbot asked cold often states country rules you cannot check. This skill works from your setup, refuses to state foreign law as fact, and hands you the questions for counsel.

## How to install and use

**Claude.ai:** download the skill's .zip from this page and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then describe the hire.

**Claude Code:** run `/plugin marketplace add Remutopia/ruzora-skills`, then `/plugin install hire-plan@ruzora-hiring`. Ask for an international hiring plan.

**Any other AI (ChatGPT, Gemini, Copilot):** copy the prompt version from this page and paste it as your first message.

Include the country, the person's US status, hours, length, how you will manage them, and whether they will touch customer data. About 15 minutes.

## Frequently asked questions

### Can I hire an international contractor full time with no end date?
You can sign that contract, but a full-time, open-ended, exclusive arrangement that you manage like staff is the pattern most likely to be treated as employment in many countries. The skill flags it and gives you the questions to put to a local employment lawyer before you commit.

### What is the difference between a contractor and an employer of record?
A contractor is self-employed and invoices you. An employer of record is a company that legally employs the person in their country on your behalf and runs local payroll and benefits, while you direct the daily work.

### Does the skill give country-specific legal answers?
No. It turns country law into specific questions for counsel, built from your facts, and states only US rules it can cite.

### Is it free?
Yes. No signup and no email gate. Use it, change it and share it under CC-BY-4.0.

---

**Weighing a hire in Latin America?** See [why teams hire senior engineers in Latin America, working US hours](/why-latam), or compare our [flat monthly pricing](/pricing). For a deeper look at the two most common models, read [contractor vs employer of record for remote engineers](/blog/contractor-vs-employer-of-record-remote-engineers).
