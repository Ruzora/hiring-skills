---
title: Contractor vs Employee Checklist for Engineering Hires
description: Free AI skill that checks a contractor engineer against IRS, DOL and state tests, plus IP and account ownership, and writes your questions for counsel.
target_query: contractor vs employee checklist
category: close
related_blog: staff-augmentation-vs-independent-contractor
cta: /why-latam
author: Roberto Espinoza
updated: 2026-10-04
---

# Contractor vs employee checklist for engineering hires

Contractor Classification Check is a free AI skill that runs a contractor vs employee checklist on how your contract engineers actually work, against IRS, Department of Labor and state tests. It gives a risk level per test with the facts behind it, checks code ownership and account control, and lists questions for your lawyer.

If the IRS reclassifies a worker, IRC 3509 makes the employer owe 1.5% of wages plus 20% of the employee's FICA share on top of its own full FICA share, and more if 1099s weren't filed. The skill computes that with your numbers. It gives no legal verdict; it gets you to the lawyer with the right facts.

## What you get

Describe each contractor in plain words: where they live, hours, meetings, how they're paid, other clients, equipment, contract. In about 10 minutes you get:

- **A summary table:** IRS, DOL and state risk (Low, Medium, High), plus IP and account status, per worker
- **The facts driving each rating**, quoted from your description, and the unknowns that would move it
- **The state test prong by prong** where an ABC test applies, such as California's
- **Money at stake**, as an illustrative formula with your numbers
- **Fix options, cheapest first:** restructure, convert, employer of record or staffing firm, the IRS voluntary settlement program, or end the engagement
- **An IP checklist and an account-ownership checklist** (code host, cloud, domain, app stores)
- **Questions for your lawyer and accountant**, specific to your facts
- **What to do this week** without waiting for anyone

## Sample output

From a real run on a fictional 9-person health-tech startup in California with three contractors: a full-time developer, a design agency, and a QA engineer moved from W-2 to contractor to save on benefits. This is the money section for the developer.

**3. Money at stake (illustrative)**

This uses the federal IRC 3509 reduced rates with 1099s filed (as of 2026-10, IRS Topics 751 and 759):

**Formula:** 1.5% × wages + 20% × (employee Social Security 6.2% + Medicare 1.45%) + 100% × (employer Social Security 6.2% + Medicare 1.45%) + FUTA (6.0% on the first $7,000, or 0.6% after the full state credit)

**Marco, tax year 2025 (wages $176,000, under the 2025 Social Security wage base of $176,100; 1099 filed):**

| Line | Calculation | Amount |
|---|---|---|
| Income-tax withholding | 1.5% × $176,000 | $2,640.00 |
| Employee FICA share | 20% × ($10,912 SS + $2,552 Medicare) = 20% × $13,464 | $2,692.80 |
| Employer FICA | $10,912 + $2,552 | $13,464.00 |
| FUTA | 0.6% × $7,000 (6.0% would be $420) | $42.00 |
| **Total** | | **$18,838.80** (or $19,216.80 with no FUTA credit) |

## How it works

**The label doesn't decide it.** The IRS looks at behavioral control, financial control and the relationship of the parties. What the contract is called doesn't change the facts.

**In California, prong B usually decides it.** Under the ABC test (Labor Code 2775, from AB5), a worker is presumed an employee unless the work is outside the usual course of your business, among other conditions. A developer building your core product at a software company rarely meets that. Willful misclassification can cost $5,000 to $15,000 per violation, or $10,000 to $25,000 for a pattern (Labor Code 226.8).

**The federal DOL test is in transition.** Since Field Assistance Bulletin 2025-1 (May 2025), the Department of Labor no longer enforces its 2024 contractor rule and uses older guidance; the 2024 rule still applies in private lawsuits. A replacement rule was proposed in February 2026 and is not final as of October 2026.

**Other states are named, not guessed.** The skill carries the main test and statute for New Jersey, New York, Massachusetts, Illinois, Washington, Oregon, Texas and Florida, and says "check your state's test" for the rest.

**Some facts outweigh the rest.** Converting an employee to a contractor for the same job, full-time single-client work with no end date, required standups and a fixed monthly payment. The skill doesn't count factors like votes.

**Exposure is computed, not hand-waved.** Under IRC 3509, the employer owes 1.5% of wages and 20% of the employee's FICA share (3% and 40% if 1099s weren't filed), plus the full employer FICA and FUTA. The skill runs that with 2026 rates (Social Security 6.2% each side up to $184,500, Medicare 1.45% each side, FUTA on the first $7,000) and shows every line. The reduced rates disappear if the IRS finds intentional disregard. From 2026, a 1099-NEC is required at $2,000 a year, up from $600.

**There's a voluntary fix.** Eligible employers can use the IRS Voluntary Classification Settlement Program (Form 8952) and pay 10% of one year's reduced-rate liability, with no interest or penalties. It covers federal employment tax only.

**IP and accounts are separate risks.** Contractor code is generally not a "work made for hire" under 17 U.S.C. 101, so without a signed written assignment the contractor can own it. Investors' lawyers check this. And if the GitHub organization is in a contractor's personal account, they control your product.

General information as of 2026-10, not legal or tax advice.

**How this compares.** A generic checklist lists the IRS factors and stops. A chatbot asked cold often returns a confident "this person is a contractor" and skips IP and accounts.

## How to install and use

**Claude.ai:** download the skill's .zip and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then describe your contractors.

**Claude Code:** run `/plugin marketplace add Ruzora/hiring-skills`, then `/plugin install hire-close@ruzora-hiring`, and ask for a contractor classification check.

**Any other AI (ChatGPT, Gemini, Copilot):** copy the prompt version of the skill, paste it as the first message, then describe the engagements.

Include each person's state or country. It decides which tests apply.

## Frequently asked questions

**How do I know if a developer should be a contractor or an employee?**
Look at control (who sets hours and methods), money (fixed price, own tools, other clients, chance of loss) and the relationship (open-ended, core work, benefits). In ABC-test states such as California, the work must also be outside your usual business.

**What happens if I misclassify a contractor?**
Federal back taxes under IRC 3509 at minimum, plus employer FICA and FUTA, interest and penalties, and state penalties that in California run $5,000 to $25,000 per violation. Back wages and benefits claims can follow.

**Can I fix misclassification without an audit?**
Options include restructuring the engagement, converting to employee, moving to an employer of record or staffing firm, and the IRS Voluntary Classification Settlement Program for eligible employers.

## Engineers without the classification question

If you want senior engineers in Latin America, working US hours, without carrying contractor classification risk yourself, see [why Latin America](/why-latam) and our [flat monthly pricing](/pricing).

For a side-by-side of the models, read [staff augmentation vs independent contractor](/blog/staff-augmentation-vs-independent-contractor).
