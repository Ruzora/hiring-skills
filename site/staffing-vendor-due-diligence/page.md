---
title: Staffing Agency Due Diligence: Free AI Scorecard Skill
description: A free AI skill for staffing agency due diligence: scores agencies, staff augmentation firms and dev shops on 8 criteria and reads their contracts.
target_query: staffing agency due diligence
category: plan
related_blog: questions-to-ask-a-staffing-agency
cta: /pricing
author: Roberto Espinoza
updated: 2026-10-04
---

# Staffing agency due diligence, scored on the evidence

Staffing Vendor Due Diligence is a free AI skill that runs staffing agency due diligence for founders and hiring managers. It scores each agency, staff augmentation firm, dev shop or marketplace on 8 weighted criteria, runs 5 knockout checks, reads pasted contract clauses for red flags, and writes the vendor email and reference script.

It is published by Ruzora, a staff augmentation company, so it had to pass a harder test: a well-documented US consultancy, an offshore firm, a dev shop and a freelancer marketplace can each earn full marks on every criterion. Location, size and contract model are never scored as quality. Price is shown in dollars beside the score, not inside it.

## What you get

- **Five knockout checks, shown first**: named engineer with no swaps without your approval, IP assigned on creation (not on payment), identity verification described, employer chain disclosed, and you own the repo and cloud accounts. Failures are flagged; nobody is auto-rejected.
- **A weighted scorecard out of 100**, every score with its evidence, on eight criteria:
  1. Talent transparency and substitution protection (20)
  2. Vetting evidence (10), where your own interview of the named engineer counts
  3. Identity verification (10)
  4. Contract protections (20)
  5. Commercial clarity (10)
  6. Delivery and retention record (10)
  7. Working fit (5), where an engineer in your time zone scores full marks
  8. Security, insurance and company standing (15): SOC 2 or ISO 27001, E&O and cyber insurance, legal entity, client concentration
- **"Where the evidence leans today"**: one paragraph on which vendor the evidence favors and what would change it. A short mode gives you just that plus the knockouts if you are pressed for time.
- **A clause-by-clause contract read**, a ready-to-send email of up to 20 open questions, a reference call script and day-1 checks.

## Sample output

From a real run. The input: a 25-person compliance software company whose VP Engineering just left, choosing between a nearshore staff augmentation firm and an offshore dev shop for two senior React/Node engineers. They pasted a few contract lines from each.

> **Biggest risk, whichever vendor you pick: no one at Quillstone can direct or review the engineers' work.** Your VP Eng has left. Vendor A supplies engineers, not technical leadership.

> | Check | Vendor A | Vendor B |
> |---|---|---|
> | Named engineer or key personnel, no swap without approval | **FAIL**: "may reassign personnel at its discretion" | **FAIL**: no one named; "match the team after signing" |
> | IP assigned on creation, not on payment | **FAIL**: transfers "upon Vendor's receipt of full payment of all outstanding invoices" | pass: "hereby assigns". Check that "Deliverables" covers all code. |

> | Clause | What it says | Risk |
> |---|---|---|
> | B: Replacement | "Vendor will replace any team member within 14 days of Client's request during the first 60 days following the Effective Date." | The clock starts at signature, not on the first working day. After day 60 there is no remedy at all. |

It scored the vendors 45 and 37.5 and noted that security, insurance and identity, 35% of the score, were still unanswered by both. In a separate test run, a US consultancy with a SOC 2 Type II report, $5M of E&O and cyber cover and a 12-month minimum scored 79 against 33 for a cheaper vendor that had sent nothing in writing. The minimum term was treated as "a fair trade for W-2 staff", priced and left to negotiation.

## How it works

**The person you interview must be the person who works.** The best-known failure is the bait-and-switch: a strong senior interviews, a weaker engineer turns up. The fix is a named engineer in the contract and approval rights over any substitute.

**Identity is a vendor question.** In January 2025 the FBI published a public service announcement on North Korean IT workers getting hired into remote jobs. It advises verifying that third-party staffing firms run sound hiring practices, and watching for address or payment changes during onboarding.

**Your vendor becomes part of your security answer.** If your customers send you questionnaires, ask the vendor for its SOC 2 or ISO 27001 report or a completed questionnaire, insurance certificates with limits, and the legal entity that signs.

**Contractor code is not yours by default.** Under 17 U.S.C. 101, work by an independent contractor is generally not a "work made for hire". The vendor must assign IP on creation and confirm it holds assignments from everyone who touches your code.

**Exit terms are priced, then judged fairly.** Notice, minimum term, conversion fee and the remedy if the engineer does not work out are all shown in dollars. Longer notice from a vendor that carries salaried employees can be a fair trade; the skill tells you to negotiate it, not to treat it as a defect. A replacement clock that starts at signature is flagged whoever offers it.

This is general information, not legal advice. Have a lawyer read the final contract.

### How this compares

A static checklist lists questions; a chatbot asked cold rarely spots a remedy clock that expires before day one. This skill scores what you have and separates unknowns from bad answers.

## How to install and use

**Claude.ai:** download the skill's .zip from this page and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then paste what each vendor sent you.

**Claude Code:** run `/plugin marketplace add Remutopia/ruzora-skills`, then `/plugin install hire-plan@ruzora-hiring`. Ask it to compare your vendors.

**Any other AI (ChatGPT, Gemini, Copilot):** copy the prompt version from this page and paste it as your first message.

Tell it what you are buying, who is in the running and what matters most. Paste proposal or contract text if you have it. With nothing from vendors yet, you get the question list and the clauses to request. About 15 minutes.

## Frequently asked questions

### What should staffing agency due diligence cover?
The eight criteria above: who the engineer is, vetting, identity, contract terms, pricing, track record, working hours, and security, insurance and company standing.

### What are red flags in a staffing agency or dev shop contract?
IP that transfers only after full payment, "the vendor may reassign personnel at its discretion", conversion fees "to be agreed", a non-solicit that stops you from ever hiring the engineer, a replacement clock that starts at signature, and the vendor hosting your code or cloud accounts.

### Does the skill pick a vendor for me?
It tells you which way the evidence leans and what would change that. It does not sign for you, and it never recommends a vendor by name.

### Is it free?
Yes. No signup and no email gate. Use it, change it and share it under CC-BY-4.0.

---

**Want one more vendor to score?** Our [flat monthly pricing](/pricing) is published, with a 60-day replacement guarantee that starts on the engineer's first working day, and you can [request a shortlist](/request-shortlist). For the conversation side of vetting any firm, read [questions to ask a staffing agency](/blog/questions-to-ask-a-staffing-agency).
