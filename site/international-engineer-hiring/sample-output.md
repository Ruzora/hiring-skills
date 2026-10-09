# International engagement plan: Senior data engineer in Brazil (São Paulo)
Prepared 2026-10-04. General information, not legal or tax advice. Confirm with local counsel and your tax advisor.

**Short answer:** don't send the offer yet. The setup you describe is a full-time employee with a contractor label. An online template probably won't hold up in a reclassification claim, and it won't cover what your hospital BAAs require. Two decisions come first: which model you use, and whether your customer contracts allow her to access patient data from Brazil.

## Situation and assumptions
- **Who:** Tidewater Analytics (12 people, Delaware C-corp, Austin HQ, no entities outside the US) wants to engage a senior data engineer. She is a Brazilian national, lives and works in São Paulo, and is not a US citizen or green-card holder.
- **Shape of the work:** full time, no end date, daily standup, roughly 9:00–18:00 São Paulo time, a company MacBook and an @tidewater email. You planned to pay her a flat $7,000/month through an international transfer service. She would need access to a Snowflake warehouse that holds patient-level data from hospital customers, two of which have BAAs with you. She may travel to Austin for a one-week offsite in March.
- **Assumption:** she would have no other clients while working for you. You didn't say. Confirm it with her.
- **Assumption:** your product (analytics dashboards) uses only standard commercial encryption and isn't export-controlled. Confirm with whoever owns your security stack.
- **Assumption:** she won't sign, negotiate or sell anything for Tidewater. Her role is technical only.

## Classification check
5 of 6 employment-like signals are confirmed, and the 6th is probably true:
- full-time hours you set (9–18 plus daily standup)
- open-ended term
- your equipment and email
- part of your team rituals and structure
- fixed monthly pay regardless of deliverables
- only client: not yet confirmed

Risk: **high**. This is the pattern that leads to reclassification claims in many countries. Whether that applies in Brazil, and what it would cost you, is the first question for a Brazilian employment lawyer. Calling her a contractor in the template doesn't decide it.

## Models compared for you
| Model | Fit for you | Main risk for you | What to get a quote for |
|---|---|---|---|
| Direct contractor | Poor as planned. Your setup has all the signs of employment. | Reclassification (back benefits, termination costs) plus weak IP and data-protection terms from an online template | A Brazilian employment lawyer's fee for a classification opinion and contract review |
| EOR | Strong. One long-term, full-time person you manage like staff, and no Brazilian entity | Total cost is higher than $7,000. Ending her employment has a local cost. The IP chain and BAA terms must also run through the EOR. | Monthly EOR fee, all mandatory employer costs on top of her gross pay, the exact cost to end the employment at month 6, and their HIPAA/BAA position |
| Staffing vendor | Weak. You've already found and vetted her, so the vendor's main value (sourcing and replacement) is wasted | Paying a margin for sourcing you didn't need. A vendor may not take on a candidate you bring. | Monthly rate for a named, pre-selected candidate, the conversion fee, and whether they'll sign a BAA |
| Own entity | Poor. It's one person, and you have no other plans in Brazil | Setup and ongoing compliance cost and effort for a single hire | Your accountant's setup and annual-cost estimate, if you plan several Brazil hires |

**Starting model:** EOR. Everything about the role (full time, open-ended, managed like staff, on your tools) fits an employee. An EOR gives you that without a Brazilian entity, and its employment paperwork is generally easier to line up with your BAA obligations than a template contractor agreement.

**Runner-up:** direct contractor. Switch only if both of these happen:
- You restructure the work into a genuine project engagement: defined deliverables, paid per deliverable or milestone, she sets her own hours, she uses her own equipment, and she's free to take other clients.
- A Brazilian employment lawyer confirms in writing that the restructured arrangement is safe.

If you want her working exactly as you described, the contractor route doesn't fit.

The decision is yours.

## Risk register
| Risk | Why it applies to you | Likelihood (why) | Mitigation | Owner |
|---|---|---|---|---|
| Worker reclassification | 5–6 of 6 employment signals | High (the setup is built like employment) | Use an EOR, or restructure into a real project and get a written opinion from a Brazilian lawyer | You + Brazilian employment lawyer |
| Breach of a BAA or customer contract by offshore PHI access | Snowflake holds patient-level data covered by two BAAs. BAAs often restrict subcontractors, data location or where data can be accessed from. | High until you've read them (unknown terms, and you'd be relying on them) | Read both BAAs, your MSAs and any security questionnaires you've answered before granting access. Give notice or get consent where required, and sign a downstream BAA or equivalent with her or the EOR. | You + your US healthcare/privacy counsel |
| Too much PHI access | A data engineer may not need identifiable patient data | Medium (the default is often broad warehouse access) | Least-privilege Snowflake roles, de-identified or masked views where possible, access logging, MFA, no local data extracts | You (engineering lead) |
| Brazilian data-protection obligations | She'd be processing personal health data from Brazil | Medium (whether local law applies to US patient data processed in Brazil is unclear) | Ask local counsel. Include data-protection clauses in her contract or the EOR's. | Brazilian employment lawyer |
| IP not assigned | An online template may not use present-tense assignment, may not survive local formalities, and with an EOR the chain has to run through them | Medium (templates often get this wrong) | Present-tense "hereby assigns" wording. Confirm with local counsel that it's enforceable in Brazil (including moral rights). With an EOR, get a written chain from her to the EOR to you. | You + Brazilian employment lawyer |
| Tax and immigration exposure from the Austin offsite | US work days can change tax treatment and immigration status | Medium (one week, but it's planned work in the US) | Ask your tax advisor and an immigration advisor before booking. Decide whether the week is attendance only or productive work. | You + US tax advisor (+ immigration advisor) |
| Permanent establishment | A full-time person working in Brazil for a US company | Low (she's an engineer who doesn't sign or negotiate deals) | No title like "country manager", no authority to sign or negotiate. Confirm with your tax advisor. | You + US tax advisor |
| Payment fraud or redirection | Monthly international transfers | Low (personal referral, though referrals don't verify identity) | Pay only an account in her legal name in Brazil. No crypto, no third-party accounts. Video confirmation before any change to bank details or address. | You (finance) |
| Hardware shipping and customs | You'd ship a MacBook to Brazil | Medium (import duties and delays are unknown) | Ask local counsel or the EOR how to provide equipment. Some EORs handle it, or she buys locally and is reimbursed. Ship only to her verified address. | You / EOR |
| Exit cost unknown | An open-ended term with no defined exit | Medium (you haven't priced it) | EOR: get the exact month-6 termination cost in writing. Contractor: a notice clause reviewed by counsel. | You |

**Not applicable here:**
- *Sanctions:* Brazil isn't expected to be under a comprehensive embargo, but still screen her name in OFAC's Sanctions List Search on signing day, plus any EOR or intermediary company, and check ofac.treasury.gov for the current country list.
- *Export controls:* low risk, on the assumption that your dashboards use only standard commercial encryption and aren't defense or government products. Ask counsel before granting repo access if that's wrong.
- *Overlap hours:* not a risk. 9–18 São Paulo time gives roughly 6–7 hours of overlap with an Austin workday, depending on the time of year. Confirm the current offsets and put core hours in the contract.

## Setup checklist
### Contract
- [ ] Don't send an offer on the online template. Choose the model first.
- [ ] If you use an EOR: the employment contract comes from the EOR. Agree with her whether $7,000 is her gross salary or your total cost, because mandatory employer costs come on top.
- [ ] If you use a contractor: have a Brazilian lawyer draft or review the agreement. Write in deliverables, no fixed hours, her own equipment, and freedom to take other clients.
- [ ] IP: present-tense assignment ("hereby assigns"), moral-rights handling checked by local counsel, and a written chain from her to the EOR to Tidewater if you use an EOR.
- [ ] Confidentiality and data-protection clauses that match your BAA obligations (no local copies, breach notification, return or destruction of data on exit).
- [ ] No title or authority to sign or negotiate on Tidewater's behalf.
- [ ] Exit terms written down: notice period, and with an EOR, the month-6 termination cost.

### Tax and payment
- [ ] Contractor route: collect Form W-8BEN (she's a non-US person). Confirm with your accountant. With an EOR, you pay the EOR and the EOR pays her.
- [ ] Pay only an account in her legal name, in Brazil, matching her verified identity. No crypto, no third-party accounts.
- [ ] Any change to bank details or address requires a live video confirmation first.
- [ ] Get US tax and immigration advice on the March offsite before booking travel.

### Identity, access and security
- [ ] Live video call with a government ID matched to her face, before signing.
- [ ] OFAC Sanctions List Search on her name and any EOR or intermediary company, on signing day.
- [ ] Read both BAAs, your MSAs and any security questionnaires you've answered. Complete any required notice, consent or downstream BAA before giving her PHI access.
- [ ] Ship the MacBook only to her verified address, after the customs question is answered.
- [ ] On day 1, not before: SSO and MFA, least-privilege Snowflake role, masked or de-identified views where possible, access logging, and disk encryption and MDM on the laptop.
- [ ] Off-boarding plan: same-day access revocation and laptop return.

### Working arrangement
- [ ] Core hours in the contract, e.g. 10:00–16:00 São Paulo time for overlap with Austin. Re-check the time offsets when US daylight saving changes.
- [ ] Standup and team rituals are fine under an EOR. Under a contractor model they add to the classification risk.
- [ ] Decide whether the March offsite is attendance only or productive work, based on the advice you get.

## Questions for counsel and providers
### Local employment lawyer (Brazil)
1. She'd work full time (9–18), open-ended, joining our daily standup, on our MacBook and email, for a fixed $7,000/month, probably for us only. Would Brazilian authorities or courts treat that as employment despite a contractor agreement? What exposure would Tidewater have if they did?
2. Is there any version of a direct contractor arrangement for a full-time senior data engineer that you'd consider safe? What would have to change in practice?
3. Is a present-tense IP assignment from her (or from an EOR) to a Delaware C-corp enforceable in Brazil? How are moral rights and any formal requirements handled?
4. She'd access identifiable US patient data in our Snowflake warehouse from São Paulo. Does Brazilian data-protection law impose obligations on her, on Tidewater or on an EOR for that processing?
5. What's the cleanest way to provide her a company MacBook: ship from the US, buy locally and reimburse, or have the EOR provide one? What import costs or formalities apply?

### US tax advisor
1. She's a Brazilian non-US person working entirely in Brazil, paid $7,000/month. On the contractor route, is a W-8BEN the right documentation, and do we have any US withholding or reporting obligations?
2. Could a full-time engineer working in São Paulo (no sales role, no signing authority, technical title only) create a permanent establishment for Tidewater in Brazil, either directly or through an EOR?
3. If she comes to the Austin offsite for one week in March and does some work, does that change the tax treatment of her pay for that week, or our reporting? What should we do before she travels?
4. Under an EOR, how do we treat the EOR invoices for tax purposes, and is there anything we need to collect from the EOR?

### EOR or vendor (if used)
1. What's the total monthly cost to Tidewater if her gross salary is the equivalent of $7,000/month, broken down into your fee and every mandatory employer cost?
2. What's the exact cost to Tidewater of ending her employment at month 6, including notice and any mandatory payments?
3. Will you sign a BAA or BAA-equivalent terms with us, since she'll access PHI from two hospital customers? Do your employment contract and policies support our BAA obligations (confidentiality, breach notification, data return)?
4. Does your contract assign all IP she creates to you and then to Tidewater, in present-tense wording, and have you checked it's enforceable in Brazil?
5. Can you provide or import her laptop and enforce our security requirements (MDM, encryption), and how do you handle the business trip to Austin?

## 30-day timeline
| Week | Step | Owner |
|---|---|---|
| 1 (Oct 5–11) | Hold the offer and tell her you're finalizing the structure. Read both BAAs, your MSAs and security questionnaires. Request quotes from 2–3 EORs. Book the Brazilian employment lawyer and your US tax advisor. Confirm with her that she'd have no other clients. | You |
| 2 (Oct 12–18) | Get answers from counsel and the tax advisor. Compare EOR quotes, including the month-6 exit cost. Choose the model. Send any customer notices or consent requests your BAAs require. Live video ID check and OFAC screening. | You + counsel + tax advisor |
| 3 (Oct 19–25) | Sign: the EOR agreement plus her employment contract, or the counsel-approved contractor agreement with W-8BEN. Put the IP chain and BAA-aligned data terms in place. Ship the laptop to her verified address, or set up local purchase. Build least-privilege Snowflake roles and masked views. | You / EOR |
| 4 (Oct 26–Nov 1) | Day 1: grant SSO, email and scoped Snowflake access, with logging on. Onboarding and first productive week. Book the March offsite travel only after the tax and immigration answers come back. | You (engineering lead) |

---
Made with the free International Engineer Hiring Plan skill by Ruzora · ruzora.com/skills
