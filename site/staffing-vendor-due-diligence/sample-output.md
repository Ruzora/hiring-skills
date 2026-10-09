# Vendor due diligence: staff augmentation (Vendor A) vs dev shop team (Vendor B), 2 senior React/Node engineers for about 12 months
Prepared 2026-10-04. This is evidence for your decision, not a recommendation, and it is not legal advice.

## Where the evidence leans today
**Biggest risk, whichever vendor you pick: no one at Quillstone can direct or review the engineers' work.** Your VP Eng has left. Vendor A supplies engineers, not technical leadership. Vendor B is a dev shop, but nothing it has said so far shows a tech lead or delivery manager in the price. Before you sign, decide who will set priorities and review pull requests. You have three options: an internal lead, a fractional technical advisor for a few hours a week, or a managed delivery model where the vendor contractually owns delivery. Ask Vendor B directly whether it offers the third. Without one of these, two strong seniors can still build the wrong thing, and you won't see it until late.

On the evidence, Vendor A leads today, **45/100 vs 37.5/100**. Three facts drive that:
- You have already interviewed two of Vendor A's engineers and rated them highly. Vendor B has shown no one and will "match the team after signing".
- Vendor B wants your staging and CI on its own AWS account. Your code and pipeline would then sit in an environment you don't control and would have to describe in your customers' security questionnaires.
- Vendor A costs $52,800 less over 12 months.

Vendor A's lead is fragile. Two of its contract terms are the two most common ways this goes wrong:
- It "may reassign personnel at its discretion". This means the engineers you interviewed may not be the ones who show up.
- IP transfers only "upon Vendor's receipt of full payment".

The lean changes if:
- Vendor A refuses to name your two engineers in the SOW or to switch to assignment on creation.
- Vendor B introduces named engineers you rate as highly, agrees to work in your AWS account, and sends security documents that Vendor A cannot match.

Neither vendor has yet answered anything on security, insurance or identity verification. That is 35% of the score, unknown for both.

## Knockout checks
| Check | Vendor A | Vendor B |
|---|---|---|
| Named engineer or key personnel, no swap without approval | **FAIL**: "may reassign personnel at its discretion" | **FAIL**: no one named; "match the team after signing" |
| IP assigned on creation, not on payment | **FAIL**: transfers "upon Vendor's receipt of full payment of all outstanding invoices" | pass: "hereby assigns". Check that "Deliverables" covers all code. |
| Identity verification described | ? | ? |
| Employer chain disclosed, no hidden subcontracting | ? | ? |
| You own repo, cloud and domains | ? | **FAIL**: wants staging and CI "on their own AWS account" |

A failed check does not rule a vendor out. It means this term needs to be fixed in negotiation before you sign.

## Scorecard
Default weights are kept. Security already carries 15. Speed is not a scored criterion, so it is covered under "Speed" below.

| Criterion (weight) | Vendor A score: evidence | Vendor B score: evidence |
|---|---|---|
| 1. Talent transparency and substitution (20) | 2: you saw 4 profiles and interviewed 2, but the MSA assigns "qualified resources" and lets the vendor "reassign personnel at its discretion" | 1: no one met; team matched "after signing" |
| 2. Vetting evidence (10) | 3: your own video interviews of both engineers count as buyer evidence. The vendor's own answer ("top 2% of applicants") is a percentage claim, which alone scores 1. | 1: no vetting description and no interviews |
| 3. Identity verification (10) | 1: not answered | 1: not answered |
| 4. Contract protections (20) | 2: IP conditional on payment; conversion fee "to be mutually agreed"; no remedy clause seen; account ownership unknown. 60 days' notice is clearly stated. | 2: present-tense IP assignment (good), but no chain-of-title warranty seen. Vendor-hosted staging and CI is proposed; if it goes into the contract, this drops to 1. Replacement clock runs from the "Effective Date", not the start date. 6-month minimum term with no stated commitment in return. |
| 5. Commercial clarity (10) | 3: $8,800/month per engineer, clear; inclusions (equipment, time off, holidays, increase cap) not stated | 3: $11,000/month per engineer, clear; inclusions not stated |
| 6. Delivery and retention record (10) | 1: no references yet | 2: 3 current-client references; no former client; no tenure or attrition data |
| 7. Working fit (5) | 1: no core hours in writing; no escalation contact | 1: no core hours in writing; no escalation contact |
| 8. Security, insurance and standing (15) | 1: nothing provided | 1: nothing provided |
| **Weighted total /100** | **45** | **37.5** |

**Unknowns, scored 1 until answered:** identity verification for both; security attestation, insurance and legal entity for both; overlap hours and escalation contact for both; Vendor A references; Vendor B vetting; employer chain and subcontracting for both; account ownership for Vendor A; Vendor A's remedy if an engineer doesn't work out.

**Money, outside the score:**

| | Vendor A | Vendor B |
|---|---|---|
| 12 months, 2 engineers | **$211,200** | **$264,000** |
| Cost to exit | 60 days' notice = $35,200 at any point | Locked in for the first 6 months = $132,000 committed. After month 6, 30 days' notice = $22,000. |
| Conversion fee | "to be mutually agreed" (unpriced) | not stated |

Difference: Vendor B costs $52,800 more over the year.

**Speed (your 1-month target):**
- Vendor A can meet it if the two engineers you interviewed are contractually named and actually available.
- Vendor B still has to find people. Its 60-day replacement window runs from the Effective Date (signing), so if matching and onboarding take 3-4 weeks, roughly half the window is gone before anyone writes code.

## Contract and proposal read
| Clause | What it says | Risk | Ask for instead |
|---|---|---|---|
| A: Personnel | "Vendor shall assign qualified resources to the Services based on project needs and may reassign personnel at its discretion." | Bait-and-switch. The engineers you interviewed can be swapped at any time without your consent. | Name both engineers in the SOW. Substitution only with your written approval, after you interview the replacement. |
| A: IP | "All Work Product shall transfer to Client upon Vendor's receipt of full payment of all outstanding invoices." | Any invoice dispute means you don't own your own code. It also complicates your answers to customers about who owns the product. | "Vendor hereby assigns to Client all right, title and interest in all Work Product upon creation," plus a warranty that the vendor holds signed assignments from every person who touches the code. |
| A: Termination | "Either party may terminate this Agreement upon sixty (60) days written notice." | Clear and mutual, which is good. It costs about $35,200 to exit, and the vendor can also walk with 60 days' notice. | Keep it, and add termination for cause with shorter notice (e.g. 10 days) if an engineer underperforms or is swapped without approval. |
| A: Conversion | "to be mutually agreed" | Unpriced. You could face a large fee or a refusal later, when you have the weakest hand. | A stated fee that falls over time, reaching $0 after an agreed period (e.g. 12 months). |
| B: Term | "Initial term of six (6) months; thereafter month-to-month with thirty (30) days notice." | A $132,000 commitment before you have met anyone. A minimum term can be fair if the vendor commits something in return; so far it hasn't. | Shorter initial term, or termination for cause during it. Alternatively, keep 6 months only if you interview and approve named engineers before signing. |
| B: Replacement | "Vendor will replace any team member within 14 days of Client's request during the first 60 days following the Effective Date." | The clock starts at signature, not on the first working day. After day 60 there is no remedy at all. | 60 days from each engineer's first working day; replacements also need your approval; no extra charge; a fee credit for gap days. |
| B: Hosting (proposal) | Staging and CI on the vendor's "own AWS account 'for efficiency'" | You don't control the environment holding your code, secrets and possibly customer test data. Access depends on the vendor, and you must disclose this in security questionnaires. | All repos, cloud, CI and domains in Quillstone's accounts. Vendor engineers get individual users that you can revoke. |
| B: IP | "Vendor hereby assigns to Client all right, title and interest in the Deliverables." | Good present-tense wording. Risk: "Deliverables" may not cover all code, configs, CI pipelines and docs, and there is no warranty that each worker has assigned to the vendor. | Define "Deliverables" (or "Work Product") as everything created for you, and add a chain-of-title warranty. |
| Both: not seen | Subcontracting, data protection and subprocessors, confidentiality signed by each worker, liability caps, insurance, governing law, non-solicit | Unknown. These are what your customers' questionnaires and your lawyer will ask about. | Request the full MSA and SOW from both. Look for: subcontracting only with your consent; a breach notice period; each worker under NDA; liability for IP, data and confidentiality carved out of caps; E&amp;O and cyber insurance with limits; a non-solicit that includes a conversion path. |

## Email to send each vendor
Subject: A few questions before we decide

Hi [name], we're close to a decision on two senior React/Node engineers for about 12 months. Please answer in writing and attach documents where requested.

**People and direction**
1. Is each engineer your employee, your contractor, or a partner firm's contractor? In which country?
2. Will you subcontract any part of this work? If so, to whom?

**Vetting and identity**
3. Please send the technical assessment you use for senior React/Node engineers and a redacted scorecard from a recent hire. Who runs the technical interview: an engineer or a recruiter?
4. How do you verify that a candidate is who they claim to be, and when? Do you re-verify at the start of the engagement?
5. Where does equipment ship, and are engineers paid into an account in their own name?

**Security, insurance and standing**
6. Please send your SOC 2 or ISO 27001 report. If you don't have one, can you complete our security questionnaire?
7. Please send certificates of professional liability / E&amp;O and cyber insurance, with limits.
8. Which legal entity would sign, in which jurisdiction? How long have you operated, and what share of revenue does your largest client represent?

**Contract**
9. Please send your full MSA and SOW, including data protection, subprocessors, confidentiality (signed by each individual worker?), liability caps and governing law.
10. Do you hold signed IP assignments from every person who will work on our code, and will you warrant that in the contract?

**Money**
11. What does the monthly rate include (equipment, time off, holidays)? Do we pay while an engineer is on leave? How and when can the rate increase, and is there a cap?

**Record and working fit**
12. How long do engineers stay on a client engagement on average, and how often does one leave mid-engagement? What happened the last time?
13. Please introduce us to two clients of our size engaged 12+ months and one client who ended the engagement.
14. What core hours will the engineers work in US Eastern time [adjust to your time zone], and will you put them in the SOW?
15. Who is our escalation contact if an engineer underperforms, and how fast do you remove access when someone rolls off?

**Vendor A only**

16. Will you name the two engineers we interviewed in the SOW, with no substitution without our written approval and a new interview? Can both start by early November?
17. Will you change the IP clause to "hereby assigns ... upon creation" rather than on payment?
18. What is the conversion fee to hire an engineer directly, and does it fall to zero over time?
19. Please confirm that all repositories, cloud accounts and domains stay in our accounts.
20. If an engineer doesn't work out, what is the remedy (replacement, fee credit or termination for cause), what triggers it, how fast is it, what does it cost, and when does any clock start?

**Vendor B only**

16. Can you introduce named engineers for us to interview before we sign? Can they start by early November?
17. Will your team work inside our AWS account, CI and repositories, with individual user access that we control and can revoke?
18. Will you define "Deliverables" to include all code, configuration, CI pipelines and documentation created for us?
19. Will the 60-day replacement window start on each engineer's first working day instead of the Effective Date, with replacements subject to our approval?
20. What does the 6-month minimum commit on your side? Does the rate include a tech lead or delivery manager who directs the work? What is the fee to hire an engineer directly?

## Reference call script
**Who to call:**
- Vendor A: ask for two current clients of similar size engaged 12+ months, plus one client who ended the engagement.
- Vendor B: you have three current clients. Ask for one who ended the engagement.

**Open with:** "Thanks for the time. I'm considering [vendor] for two senior React/Node engineers. Everything you say stays with me."

1. What did you hire them for, and how long have you worked with them?
2. Was the engineer you interviewed the one who started? Has anyone been swapped since?
3. How long until the engineers were shipping useful React/Node work without hand-holding? Who on your side directed them?
4. Tell me about the first time something went wrong. What did the vendor do, and how fast?
5. Did invoices ever surprise you?
6. When your own customers sent security questionnaires, did the vendor help answer them? Whose cloud and CI did they work in?
7. If you could change one thing in their contract, what would it be?
8. On a scale of 1-10, how likely are you to use them again for a critical role? What would make it a 10?
9. (For the client who left) Why did you end it, and how did the exit go: access removal, code handover, final invoice?

**Listen for:** hesitation on question 2, "they were great until...", and any replacement that took weeks.

**Verify the referee is real:** their name, title and company should match a public profile and a company email domain. A reference who gives only a personal email and a mobile number is weak evidence.

## Day-1 checks for whoever you pick
- **Identity:** the person on the first video call is the person you interviewed (Vendor A) or approved (Vendor B). Compare against the interview recording or notes.
- **Contract:** each engineer is named in the signed SOW before they get any access.
- **Access:** engineers get individual accounts in Quillstone's GitHub, AWS and CI, with MFA on and least privilege. No shared credentials, and nothing hosted in the vendor's accounts.
- **Equipment and pay:** equipment ships to the address the vendor verified. Treat any request to change address or payment details during onboarding as a red flag.
- **Paperwork:** collect signed confidentiality and IP assignment confirmations covering each individual engineer.
- **Working hours:** core hours and the escalation contact are written down and tested in week 1.
- **First week:** each engineer opens at least one reviewed pull request. Someone qualified on your side (your interim lead or advisor) reviews it.
- **Remedy clock:** note the date the replacement or remedy clock started and when it ends.

## Where this leaves you
- **Vendor A:**
  - Strong on: you have met and rated the actual engineers; lower cost ($211,200 per year); clear, mutual 60-day exit.
  - Open items: identity verification, security documents, insurance, references, account ownership, the remedy if an engineer fails, and the employer chain.
  - Negotiate: name both engineers in the SOW with an approval-only substitution clause; IP "hereby assigned" on creation; a stated conversion fee that falls to zero; termination for cause.
- **Vendor B:**
  - Strong on: clean present-tense IP wording; three references offered; a written replacement commitment; cheaper to exit after month 6 ($22,000).
  - Open items: no engineers shown yet; vetting, identity, security documents, insurance and retention data are all missing; vendor-hosted infrastructure; whether any technical leadership is included.
  - Negotiate: interview named engineers before signing; everything in your AWS account; replacement clock starts on day 1 of work; something committed in return for the 6-month minimum; justify the $52,800 premium (for example, an included tech lead).

**For both vendors:** security documents and insurance certificates are what you'll need for your customers' questionnaires, so get them before signing. Separately from the vendor choice, solve "who directs the work". Have a lawyer read the final contract, especially IP, liability and termination.

The decision is yours.

---
Made with the free Staffing Vendor Due Diligence skill by Ruzora · ruzora.com/skills
