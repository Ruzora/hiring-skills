---
name: international-engineer-hiring
description: Builds an engagement plan for hiring an engineer in another country: contractor vs EOR vs vendor, risk register, setup checklist, questions for counsel. Use when hiring international contractors.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/international-engineer-hiring
---

# International Engineer Hiring Plan

You walk away with an engagement plan for one engineer outside the US: which model fits your situation and why, what can go wrong for you specifically, the setup checklist (contract, tax form, payment, access), and the exact questions to put to a local lawyer, your accountant and any employer of record. About 15 minutes.

General information, not legal or tax advice. Employment and tax law differs by country and changes; this skill states no country-specific rule as fact. It turns country law into questions for counsel.

## Inputs

Read what the user gave. If missing AND it would change the plan, ask in ONE message, max 3 questions:

1. **Who and where:** the country the engineer lives and works in, and whether they are a US citizen or green-card holder (that changes the tax form and rules).
2. **The shape of the work:** full-time or part-time, expected length, and how you will manage it (daily direction like staff, or a defined project with deliverables).
3. **Your setup:** do you have a legal entity in that country, does the engineer need access to customer or production data, and is your product in a regulated or export-controlled area (defense, advanced encryption, government customers)?

If the user says "just draft it", proceed and list the assumptions at the top.

## The four models

| Model | Legal employer | You handle | Best when |
|---|---|---|---|
| **Direct contractor** | Nobody; the engineer is self-employed | Contract, invoices, payment, IP assignment | Defined project, part-time, or under ~6 months |
| **Employer of record (EOR)** | A company in the engineer's country employs them for you | Daily direction; the EOR runs payroll, local benefits and local employment paperwork | One long-term, full-time person you manage like staff, no entity there |
| **Staffing / staff augmentation vendor** | The vendor | Daily direction; the vendor sources, vets, employs and replaces | You want someone else to find, vet and replace the engineer |
| **Your own entity** | You | Everything locally: payroll, benefits, filings | A team of several people in one country; your accountant runs the break-even |

## Workflow

1. **Restate the situation** in three lines: who, where, the shape of the work, and the assumptions you made.

2. **Run the classification check.** Count how many of these are true: works full-time hours you set; open-ended term; you are their only client; uses your equipment and email; sits in your org chart and team rituals; paid a fixed monthly amount regardless of deliverables. Three or more means a "contractor" relationship looks like employment, which is the pattern that leads to reclassification claims in many countries (back benefits, severance). Do not give a verdict. Mark it high and make it the first question for local counsel; compare the EOR or vendor model.

3. **Pick a starting model** using the "Best when" column and the check above. Name the runner-up and the conditions that would switch to it. The user decides.

4. **Build the risk register**: each risk that applies to THIS situation, why it applies, a likelihood (high, medium, low) with the reason, the mitigation, and who owns it. Use the rules below as the candidate list. Skip risks that do not apply and say why in one line.

5. **Write the setup checklist** for the chosen model: contract terms, tax documentation, payment set-up, identity verification, access and security, working hours.

6. **Write the questions for counsel**, split by who answers them: local employment lawyer, US tax advisor, an immigration lawyer if the engineer will travel to the US, the EOR or vendor. Make every question specific to the user's facts.
   - If the user quoted a single monthly figure, ask whether it is the person's gross pay or the user's total budget. Under an EOR, mandatory employer costs come on top of gross pay, so the same budget buys a lower gross salary. When comparing EOR quotes, make every quote state the same basis (gross pay plus fee plus employer costs = total), or the comparison breaks.

7. **Lay out a 30-day timeline** from today to the engineer's first productive week.

## Rules that matter

- **The contract label does not decide classification.** Most countries, like the US, look at how the relationship works in practice. A full-time, open-ended, exclusive, managed-like-staff "contractor" is the classic risk. The fix is either to make it a genuine project engagement or to use an EOR or vendor; local counsel decides which is safe.
- **An EOR handles employment, not every tax question.** Permanent establishment (a taxable presence for your company in their country) is a separate question. Under the OECD Model Tax Convention, Article 5, a person who habitually concludes contracts on behalf of a foreign company can create one, and tax treaties and local law vary. An engineer who writes code and never signs or negotiates deals is generally a lower concern than a salesperson, but ask your tax advisor. Do not give the engineer a title like "country manager" or authority to sign anything.
- **Get the IP in writing, through the whole chain.** Under US copyright law (17 U.S.C. 101), work by an independent contractor is generally not a "work made for hire", so you need a signed written assignment with present-tense wording ("hereby assigns"). Local law may handle moral rights and assignment formalities differently; ask local counsel whether your assignment is enforceable there. With an EOR or vendor, the chain must run engineer to EOR or vendor to you, in writing.
- **US tax paperwork depends on the person, not the country.** According to the IRS, pay to a nonresident alien for services performed outside the United States is foreign-source income and not subject to US withholding or reporting. Many companies collect Form W-8BEN to document foreign status; confirm with your accountant. A US citizen or green-card holder living abroad is a US person: collect a W-9 instead, and different rules apply. If the engineer will work while physically in the US, even briefly, that changes both tax and immigration: ask before any trip.
- **A work trip to the US is an immigration question.** USCIS lists consulting with business associates and attending conferences among the activities allowed for B-1 business visitors, and says visitors who go beyond their status, such as working for an employer in the United States, violate it. If the engineer will come to the US for an offsite or a sprint, ask an immigration lawyer what they may do there, which visa or travel authorization applies to their nationality, and whether the trip changes their tax position, before anyone books travel.
- **Check sanctions before you sign.** OFAC says all US persons, including US companies, must comply with US sanctions. Search the engineer's and any intermediary company's name in OFAC's Sanctions List Search, and confirm the country is not under a comprehensive embargo (North Korea is the obvious one; the list changes, so check ofac.treasury.gov on the day).
- **Repo access can be an export.** If your product touches export-controlled technology (some encryption, defense, certain advanced computing), sharing controlled technology or source code with a foreign person can require a license. The US Commerce Department's BIS calls the inside-the-US version a "deemed export". Ask counsel before granting repository access if any of this could apply.
- **Read your own customer contracts first.** Enterprise and government customers sometimes restrict where their data can be accessed from, or require notice of subcontractors. Check your customer agreements, security questionnaires you have answered, and your privacy policy before giving production-data access to someone abroad.
- **Payment hygiene is fraud prevention.** Pay only into an account in the engineer's legal name, in the country where you verified they live. Refuse crypto and third-party accounts. Any change to payment details or shipping address gets a live video confirmation first. These are the red flags US and allied agencies list for North Korean IT worker schemes (joint alert, July 2026).
- **Verify identity before access.** A live video with an ID document matched to the face, equipment shipped only to the verified address, and access granted on day 1, not before.
- **Overlap hours are a contract term.** For an engineer who collaborates daily, in our experience 4 hours of overlap with the team's working day is the workable minimum. Write the core hours into the contract.
- **Know the exit cost before entry.** Contractor: the notice clause. EOR: ask for the exact cost of ending the employment at month 6, because local termination rules apply. Vendor: notice period and any conversion fee.

## Output

Use this template exactly.

```
# International engagement plan: <role> in <country>
Prepared <date>. General information, not legal or tax advice. Confirm with local counsel and your tax advisor.

## Situation and assumptions
- ...

## Classification check
<n> of 6 employment-like signals: <list>. Risk: high / medium / low.

## Models compared for you
| Model | Fit for you | Main risk for you | What it costs you to get a quote for |
|---|---|---|---|
| Direct contractor | | | |
| EOR | | | |
| Staffing vendor | | | |
| Own entity | | | |

Starting model: <model>, because <reasons tied to the facts>.
Runner-up: <model>. Switch if: <conditions>.
The decision is yours.

## Risk register
| Risk | Why it applies to you | Likelihood (why) | Mitigation | Owner |
|---|---|---|---|---|

Not applicable here: <risk: one-line reason>

## Setup checklist
### Contract
- [ ] ...
### Tax and payment
- [ ] ...
### Identity, access and security
- [ ] ...
### Working arrangement
- [ ] ...

## Questions for counsel and providers
### Local employment lawyer (<country>)
1. ...
### US tax advisor
1. ...
### EOR or vendor (if used)
1. ...

## 30-day timeline
| Week | Step | Owner |
|---|---|---|
```

Then end with:

```
---
Made with the free International Engineer Hiring Plan skill by Ruzora · ruzora.com/skills
```

## Before you return it

- No country-specific legal rule stated as fact (notice periods, severance amounts, mandatory bonuses, contractor tests). Each one is a question for counsel.
- The "not legal or tax advice" line appears once at the top.
- The classification check counts the user's actual facts, with no verdict.
- Tax form matches the person: W-8BEN for a non-US person, W-9 for a US citizen or green-card holder abroad.
- If the engineer will travel to the US, the visa question is in the risk register and in the questions for counsel.
- A single monthly figure is labeled gross pay or total budget, never left ambiguous.
- Sanctions, export, customer-contract and payment checks appear in the risk register or the checklist, or are marked not applicable with a reason.
- Every question for counsel uses the user's facts.
- No provider, EOR or vendor is named or recommended.
- Footer appears once, at the end.

---

*Built by [Ruzora](https://www.ruzora.com), which places vetted senior engineers from Latin America. Free Ruzora MCP server with 35 hiring tools: [ruzora.com/developers/mcp](https://www.ruzora.com/developers/mcp).*
