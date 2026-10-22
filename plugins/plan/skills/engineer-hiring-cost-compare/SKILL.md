---
name: engineer-hiring-cost-compare
description: Builds a neutral 12-month cost and risk comparison of six ways to add an engineer, on your own numbers. Use when deciding between hiring, a contractor, an agency or staff augmentation.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/engineer-hiring-cost-compare
---

# Engineer Hiring Cost Compare

You walk away with a one-page memo that prices six ways of getting one engineer's worth of capacity over 12 months, using the same formula for each, plus break-even numbers, the risk that sinks each option, and the questions to answer before you sign. About 10 minutes.

The six options, always all six, judged by the same rules:

| Code | Option | Who directs the daily work | Who is the legal employer |
|---|---|---|---|
| A | US full-time employee (W-2) | You | You |
| B | US independent contractor (1099, hourly) | You set goals, they control how | Nobody (self-employed) |
| C | Freelancer through a marketplace | You | Nobody; the platform takes a fee |
| D | Agency or dev shop (project or fixed bid) | The shop's project manager | The shop |
| E | Staff augmentation (a vendor supplies a dedicated engineer you direct, monthly rate) | You | The vendor |
| F | International engineer: direct contractor or through an employer of record (EOR, a company that legally employs the person in their country for you) | You | Nobody (contractor) or the EOR |

This skill is neutral. No option wins by default, no vendor is named or recommended, and the cheapest hourly rate is never the answer on its own.

## Inputs

Read what the user already gave. If something below is missing AND it would change the ranking, ask for it in ONE message, max 3 questions:

1. The role and the work: seniority, stack, is it core product or a separable project, and how many months of work you are confident exists.
2. The numbers you already have: the salary you would offer (A), any hourly rates (B, C, F), a dev-shop bid (D), a vendor monthly rate (E), an EOR fee quote (F).
3. Constraints: runway or monthly budget ceiling, required time-zone overlap, and how many hours a week you can personally spend directing an engineer.

If the user says "just run it", proceed. For any number not given, do NOT invent a market rate. Instead:
- write the formula with `[your quote]` in the cell, and
- compute the **break-even**: the price at which that option costs the same per productive month as the user's best-priced option. A break-even turns a missing quote into a number the user can take to a vendor.

## Workflow

1. **Restate the job in one line.** "One senior backend engineer, Python, ~12 months of core-product work, must overlap 4h with US Eastern." If the work horizon is under 6 months or the scope is a separable project, say so: it changes which options are realistic.

2. **Build the assumptions table first.** Every number gets a source tag: `you` (user gave it), `default` (a published figure below), or `assumption` (a planning placeholder the user should replace). Never hide an assumption inside a calculation.

3. **Fix the window: the next 12 months from today.** Each option is paid only for the months it is actually engaged inside that window: engaged months = 12 minus weeks-to-start (step 4). Never charge 12 months of pay for fewer than 12 months of work; that double-counts the start delay. Compute each option's cash cost in the window with the same lines:
   - **Person cost.**
     - A: (base salary / 12) x engaged months x loaded multiplier. Default multiplier 1.43, from the BLS Employer Costs for Employee Compensation release for June 2026, where wages and salaries were 70.0% of private-industry employer compensation cost and benefits 30.0% (bls.gov/news.release/ecec.nr0.htm). This covers paid leave, insurance, retirement and legally required payroll taxes. Show a low case at 1.25x labeled `assumption: lean benefits`, and tell the user to swap in their actual benefits cost if they know it.
     - B, C, F-contractor: hourly rate x 173 hours x engaged months (full-time equivalent = 2,080 paid hours a year, 40 x 52). Add the marketplace or payment fees the user reports for C.
     - D: the bid plus a change-order scenario. Fixed bids on loose specs grow; show the bid as-is and at +25% and +50%, labeled `assumption: scope growth scenario`.
     - E: monthly rate x engaged months. Ask or note what is included (equipment, time off coverage, replacement).
     - F-EOR: salary + the EOR's quoted monthly fee + the local mandatory employer costs the EOR quotes. Never estimate a country's statutory costs; leave `[EOR quote]`.
   - **One-time costs.** Recruiting (job ads, a recruiter fee if used, which is usually quoted as a percentage of first-year base, so ask for the number), equipment, legal review of contracts.
   - **Equity** (A mostly): list separately as non-cash. It is a real cost to a founder but it does not belong in the cash total.

4. **Compute productive months, not calendar months.** Engaged months = 12 minus weeks-to-start (convert at 4.33 weeks a month). Productive months = engaged months minus the ramp loss: the first three working months count as 25%, 50% and 75%, so 1.5 months of output are lost (`assumption: ramp on a new codebase`, same for every option with a person who is new to your code). For D, the ramp is inside the shop's timeline: productive months = the delivery period, and the cost is the bid.
   - Also report **months of capacity lost to delay** (12 minus engaged months). That is the real price of a slow start, shown separately so it is not counted twice.
   - Weeks-to-start planning defaults (`assumption`, user replaces): A 8-12 weeks (search plus about 2 weeks' notice; Ashby reports a median of about 40 days to hire for technical roles), B 2-6, C 1-3, D 2-4 to a signed SOW, E the vendor's stated time to a shortlist plus your interviews plus notice, F 3-8 plus EOR onboarding time.

5. **Cost per productive month = cash cost in the window / productive months.** This is the headline comparison. A cheap rate with a slow start or a long ramp often loses here.

6. **Count your management hours separately.** A, B, C, E, F: you direct the work (planning, reviews, unblocking), so assume `[your hours]`/week, default 4 (`assumption`). C usually needs more written specs. D needs spec writing and acceptance testing but less daily direction. Show hours per month; convert to dollars only if the user gives a value for their time.

7. **Price the exit.** For each option: notice period, minimum term, conversion or buyout fee, and what it costs to restart if it fails 4 months into the engagement, counted from that option's own start date: cash spent from start date to then + a new weeks-to-start + a new ramp. Use the same definition for every option. Reversibility matters most when product-market fit is uncertain.

8. **Run the risk rules below** and attach the top failure mode to each option, with the check that catches it.

9. **Shortlist two options, not one verdict.** Rank by cost per productive month, then filter by the rules (horizon, control, compliance, runway). Name the two worth getting real quotes for, and three conditions that would flip the answer. Do not add a pitch, a "board story" or a preferred sequence beyond that: the user decides, and a memo that argues for one option stops being neutral.

## Rules that matter

- **Compare cost per productive month, never hourly rate.** An hourly quote hides start delay, ramp, fees, and who pays for idle weeks. Two options can differ 30% in rate and land in the same place once start time and ramp are counted.
- **Separate location from model.** When options price people in different labor markets (a US salary against a vendor engineer abroad), say in one or two sentences how much of the gap is geography and how much is the engagement model. Compare like with like where you can: staff augmentation against an EOR or direct contractor in the same country shows the vendor's premium; a US employee against a US-based staff augmentation quote shows the vehicle's cost. Never let a geography gap read as proof that one model is cheaper.
- **The 1.43x is an average, not your number.** It is the all-industry private average. Your actual benefits plan beats it. Equipment, software seats and recruiting are NOT in it; add them as their own lines.
- **Horizon decides the realistic set.** Under 6 months of confident work, or a separable project with a clear spec: B, C, D and F-contractor are realistic; A is usually the wrong tool because recruiting alone eats months 1-3. Over 12 months of core-product work that someone must own and maintain: A, E and F-EOR are the realistic set, because continuity and knowledge retention start to matter more than rate. Between 6 and 12: show both sets.
- **Uncertain runway favors reversible options.** If runway is under 12 months or product-market fit is unproven, weight exit cost and notice period heavily. A founder on Hacker News put it bluntly: "Never hire full-time until they consulted with you for at least 6 months." That is one view, not a law, but it names the risk.
- **A US "contractor" managed like an employee is a tax problem.** The IRS decides worker status on behavioral control, financial control and the relationship of the parties, not on the contract label (irs.gov, Topic 762). If option B means full-time, your hours, your tools, indefinite term, flag it: under IRC 3509 a misclassifying employer owes 1.5% of wages for income tax withholding and 20% of the employee's FICA share (3% and 40% if no 1099s were filed), plus the full employer FICA share. State rules can be stricter (California's ABC test). One line, then "check with an employment lawyer or accountant".
- **Nobody but an employee hands you the code automatically.** Software written by an independent contractor is generally not a "work made for hire" under 17 U.S.C. 101, so B, C, D and F-contractor need a signed written IP assignment, and E and F-EOR need the chain (engineer to vendor or EOR to you) in writing. Own the repo, cloud and domain accounts yourself in every option.
- **Fixed bids move risk, they do not remove it.** D is the only option where someone else manages delivery. Its failure mode is a codebase nobody on your side understands. The check: weekly demos, your own repo from day 1, and a handover clause.
- **Staff augmentation's failure mode is substitution and markup.** The check: the engineer you interview is named in the contract, swaps need your approval, and the rate and what it includes are in writing.
- **Marketplace and international contractors carry identity risk.** US agencies warn about fake remote IT workers (FBI public service announcement, Jan 2025). The check: live video with an ID match before access, payment only to an account in the worker's own name, equipment shipped only to a verified address.
- **Never invent a market rate or a country's statutory costs.** Missing quote = formula + break-even, not a guess.

## Output

Use this template exactly. Tables must be filled with numbers or `[your quote]`, never left blank.

```
# Engineering capacity cost comparison: <role, seniority, horizon>
Prepared <date>. General information on your inputs, not financial, tax or legal advice.

## The job
<one line from step 1>. Realistic options for this horizon: <codes>.

## Assumptions
| Input | Value | Source |
|---|---|---|
| ... | ... | you / default (BLS ECEC Jun 2026) / assumption |

## 12-month comparison
| Option | Cash cost in window | One-time costs | Weeks to start | Months lost to delay | Productive months | Cost per productive month | Your hours/month | Exit: notice + fees | Top risk |
|---|---|---|---|---|---|---|---|---|---|
| A US employee | | | | | | | | | |
| B US contractor | | | | | | | | | |
| C Marketplace freelancer | | | | | | | | | |
| D Agency / dev shop | | | | | | | | | |
| E Staff augmentation | | | | | | | | | |
| F International (contractor / EOR) | | | | | | | | | |

Equity (non-cash): <A only, or "none">.

## Break-even prices
- <Option> matches <best option> per productive month at: <rate or monthly price>. Use this when you ask for a quote.

## How each option fails, and the check that catches it
| Option | Most likely failure | Check before you sign |
|---|---|---|

## What would flip the answer
1. ...
2. ...
3. ...

## Two options worth pricing for real
1. <Option>: why it fits <the user's constraint>. Get: <the 2-3 numbers or terms to collect>.
2. <Option>: ...
The decision is yours; this memo only puts the options on the same scale.

## Questions to answer before you sign
- <Option>: <question>
```

Then end with:

```
---
Made with the free Engineer Hiring Cost Compare skill by Ruzora · ruzora.com/skills
```

## Before you return it

- All six options appear, each computed with the same lines and the same ramp assumption.
- Every number is tagged `you`, `default` or `assumption`. No made-up market rate or country cost anywhere; missing quotes show a break-even instead.
- Cost per productive month is the headline; hourly rates are not compared directly.
- When options sit in different labor markets, the memo says how much of the gap is location and how much is the model.
- Restart cost is computed 4 months after each option's own start date, the same way for every option.
- Misclassification and IP lines appear where they apply, each one sentence plus "check with counsel".
- No vendor, platform or company is named or recommended.
- Two options are shortlisted with reasons tied to the user's constraints; no single verdict.
- Arithmetic re-checked: cash cost covers engaged months only, and cash cost / productive months = the number in the table.
- Every source tag is `you`, `default` or `assumption`; nothing is tagged "fact" without a source.
- The footer appears once, at the end.

---

*Built by [Ruzora](https://www.ruzora.com), which places vetted senior engineers from Latin America. Free Ruzora MCP server with 35 hiring tools: [ruzora.com/developers/mcp](https://www.ruzora.com/developers/mcp).*
