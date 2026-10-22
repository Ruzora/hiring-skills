---
name: contractor-classification-check
description: Checks whether a contractor engineer looks like an employee under IRS, DOL and state tests, plus IP and account ownership, with questions for counsel. Use when hiring or reviewing a 1099 contractor.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/contractor-classification-check
---

# Contractor Classification Check

Describe how a contractor actually works with you. In about 10 minutes you get: a risk level for each test that applies (IRS, US Department of Labor, your state), the specific facts driving the risk, a rough idea of the money at stake, an IP and account-ownership check, and the questions to take to an employment lawyer. It is a risk read to prepare that conversation, never a legal verdict.

General information as of 2026-10, not legal or tax advice. Classification depends on facts and on the law where the person works; confirm with counsel.

## Inputs

For each contractor, collect the facts below. The label in the contract does not decide anything; how the work happens does.
1. **Where they work** (US state, or country) and how long the engagement has run and is expected to run.
2. **Control**: who sets hours, required meetings, how work is reviewed, whether they manage or are managed like staff.
3. **Money and independence**: how they are paid (hourly, monthly retainer, per milestone), their own business entity, other clients, own equipment, ability to hire helpers or subcontract, who pays their expenses.
4. **Integration**: is the work part of your core product, do they do the same work as employees, company email and title, benefits, were they ever your employee.
5. **Paper and access**: written agreement and whether it assigns IP, who owns the code repository, cloud, domain and other accounts they use.

Ask at most 3 questions, in one message, only if a missing fact would move a risk level (usually: where they work, whether they have other clients, whether a signed IP assignment exists). Otherwise proceed, and treat an unknown fact as unresolved: list it under "Facts that would change this" and do not assume the favorable answer.

## Workflow

1. **Pick the tests that apply** from the worker's location: IRS common-law rules (federal tax) always for US workers; DOL economic-reality analysis (federal wage and hour) for US workers; the state's test where they work. California uses the ABC test (AB5, Labor Code 2775); for New Jersey, New York, Massachusetts, Illinois, Washington, Oregon, Texas and Florida use the state table in [references/factors.md](references/factors.md). For any other state, say "check your state's test" rather than guessing. For a worker outside the US, US tests mostly decide US tax reporting, and the worker's country decides the labor-law question: flag it and add questions for local counsel.
2. **Score each factor** with the factor table in [references/factors.md](references/factors.md): Employee-like, Mixed, or Contractor-like, each with the fact from the user's description that drives it.
3. **Rate each test** Low / Medium / High risk with the 2-3 facts that matter most. Use the rules below; don't count factors as if they were votes.
4. **Estimate exposure** with the user's numbers. Compute an illustrative dollar total per worker per tax year with the 3509 formula and the 2026 rates in Rules, show the formula and each line next to it, and label it "illustrative, not a calculation of what you owe". If the user gave only an hourly rate, state the annual figure you assumed. Use the figures in Rules; never invent penalty amounts that aren't listed there.
5. **List fixes**, cheapest first, each with what it solves and what it doesn't: restructure the engagement, convert to employee, move to an employer of record or staffing firm, the IRS Voluntary Classification Settlement Program, or end the engagement.
6. **Check IP and accounts** with the checklists in [references/ip-and-accounts.md](references/ip-and-accounts.md). These risks exist even when classification is fine.
7. **Write the questions for counsel**, specific to these facts.

## Rules that matter

- **The label and the contract title don't decide it.** The IRS looks at behavioral control, financial control and the relationship of the parties. The facts of the working relationship override what the agreement calls it.
- **In California, prong B usually decides it for engineers.** Under the ABC test a worker is presumed an employee unless all three hold: (A) free from your control in doing the work, (B) the work is outside the usual course of your business, and (C) they are customarily engaged in an independent trade or business of that kind. A developer writing your core product at a software company is doing work in the usual course of your business, so B is very hard to meet. AB5 has exemptions (for example business-to-business) with strict conditions; whether one applies is a question for counsel, not an assumption.
- **The federal DOL test is in transition.** Since Field Assistance Bulletin 2025-1 (May 1, 2025), Wage and Hour enforcement no longer applies the 2024 independent-contractor rule and uses the older guidance (Fact Sheet #13 and Opinion Letter FLSA2019-6). The 2024 rule still applies in private lawsuits. A replacement rule was proposed on February 27, 2026; as of 2026-10 it is not final. The core question across versions: is the worker economically dependent on you, or in business for themselves?
- **The strongest employee signals**: they used to be your employee doing the same job; they work full time only for you with no end date; you set their hours and require standups as a condition; they're paid a fixed monthly amount like a salary; you supply the laptop, email and title; they appear on the team page or org chart. Any two of these together put the federal tests at Medium or worse.
- **The strongest contractor signals**: their own registered business with other current clients, a defined deliverable or statement of work with a price, their own tools, the right to send someone else or hire help, invoices they issue, and the risk of losing money on a fixed-price job.
- **Converting an employee to a contractor for the same job is the classic mistake.** Benefits savings are the motive regulators look for. Treat it as High risk unless the job truly changed.
- **Never end an engagement because the worker asked about classification.** It can look like retaliation; take it to counsel first.
- **Federal tax exposure has a formula.** If the IRS reclassifies and the reduced rates of IRC 3509 apply, the employer owes 1.5% of wages for income-tax withholding plus 20% of the employee's share of FICA, rising to 3% and 40% if required 1099s were not filed, plus the full employer share of FICA and FUTA, plus interest and penalties. Rates to compute it (as of 2026-10, IRS Topics 751 and 759): Social Security 6.2% employee share and 6.2% employer share, on wages up to $184,500 for 2026 ($176,100 for 2025); Medicare 1.45% each, no wage cap; FUTA 6.0% on the first $7,000 per worker, 0.6% after the full state credit; that credit assumes state unemployment tax was paid on time, which is often not true for a misclassified worker, so show $420 per worker per year as the upper bound. So for one year with 1099s filed: 1.5% x wages + 20% x (employee Social Security + Medicare) + 100% x (employer Social Security + Medicare) + FUTA. The reduced rates are not available when the IRS finds intentional disregard. In California, willful misclassification adds civil penalties of $5,000 to $15,000 per violation, or $10,000 to $25,000 for a pattern or practice (Labor Code 226.8). Back overtime, benefits eligibility, state unemployment insurance and workers' compensation can add more; name them without inventing amounts.
- **1099 threshold changed in 2026.** For payments made after December 31, 2025, Form 1099-NEC is required when you pay a US non-employee $2,000 or more in a year (it was $600). Foreign contractors working outside the US usually give you a Form W-8BEN instead of receiving a 1099; confirm with your accountant.
- **There is a voluntary fix.** The IRS Voluntary Classification Settlement Program (Form 8952, filed at least 120 days before the date you want to start treating workers as employees) lets eligible employers pay 10% of the employment tax that would have been due for the most recent tax year at the reduced 3509 rates, with no interest or penalties. Eligibility needs consistent contractor treatment, 1099s filed for the previous 3 years, and no current employment tax audit or DOL or state classification audit. It covers federal employment tax only, not state law or wage claims.
- **IP is a separate risk, and it bites at fundraising.** Software written by an independent contractor is generally not a "work made for hire" under 17 U.S.C. 101, because software is not one of the listed categories for commissioned works. Without a signed written assignment, the contractor owns the copyright in the code. The fix is a written assignment in present tense ("hereby assigns"), ideally signed before work starts; for past work, a confirmatory assignment with consideration, drafted by counsel. Investors' lawyers check this in due diligence.
- **Account ownership is an operational risk that becomes a legal one.** If the GitHub organization, cloud root account, domain registrar or app store account is in the contractor's name, they control your product. The company should own every account, with the contractor added as a member through company login, and 2FA recovery on company devices.
- **Output a risk level, never a verdict.** Use "High risk of being treated as an employee under <test>", never "this person is an employee".

## Output

Use exactly this structure.

```
# Contractor classification check: <company or engagement>, <date>
General information as of 2026-10, not legal or tax advice. Confirm with an employment lawyer where the worker is based.

**Assumptions and unknowns:** <...>

## 1. Summary
| Worker (role, location) | IRS | DOL | State (<name>, test) | IP | Accounts | Overall |
|---|---|---|---|---|---|---|
| | Low/Med/High | | | OK / Gap | OK / Gap | |

## 2. Per worker: <role, location>
**What drives the risk:** 2-4 bullets, each a fact from your description
| Factor | Your facts | Leans |
|---|---|---|
**State test:** <prong by prong if ABC; or "check your state's test" with what to ask>
**Facts that would change this:** <unknowns and which way each would move it>

(repeat per worker)

## 3. Money at stake (illustrative)
<formula with the user's numbers; what's excluded; "illustrative, not a calculation of what you owe">

## 4. Options, cheapest first
| Option | What it fixes | What it doesn't | Rough effort |
|---|---|---|---|

## 5. IP checklist
| Item | Status from your description | Action |
|---|---|---|

## 6. Account ownership checklist
| Account | Owner today | Action |
|---|---|---|

## 7. Questions for your lawyer (or accountant)
1. ...

## 8. Do this week
<3-5 actions that don't need a lawyer, e.g. move the GitHub org, stop adding new contractor work until counsel answers>
```

## Before you return it

- No sentence says a worker "is" an employee or contractor; every result is a risk level with reasons.
- Every risk level cites facts from the user's description; unknowns are listed, not assumed in the user's favor.
- Every law, rate and penalty in the output appears in this skill's Rules or references, with "as of 2026-10". No invented penalty amounts.
- Non-US workers are flagged for local counsel; US tests are not applied to their labor-law status as if they were decisive.
- The IP and account sections appear even when classification risk is low.
- The footer is the last line, after a horizontal rule.

End the output with:

---
Made with the free Contractor Classification Check skill by Ruzora · ruzora.com/skills

---

*Built by [Ruzora](https://www.ruzora.com), which places vetted senior engineers from Latin America. Free Ruzora MCP server with 35 hiring tools: [ruzora.com/developers/mcp](https://www.ruzora.com/developers/mcp).*
