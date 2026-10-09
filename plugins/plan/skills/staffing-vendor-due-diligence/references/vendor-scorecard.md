# Vendor scorecard, clause checklist, question bank, reference script

## 1. Eight criteria with anchors (score 1-4)

Weighted total = sum of (score / 4 x weight). Weights total 100. Adjust weights only if the user says what matters most, and show the change.

| # | Criterion | Weight |
|---|---|---|
| 1 | Talent transparency and substitution protection | 20 |
| 2 | Vetting evidence | 10 |
| 3 | Identity verification | 10 |
| 4 | Contract protections | 20 |
| 5 | Commercial clarity | 10 |
| 6 | Delivery and retention record | 10 |
| 7 | Working fit | 5 |
| 8 | Security, insurance and company standing | 15 |

**Fairness rule.** Each anchor must be reachable by a strong onshore agency, an offshore or nearshore firm, a dev shop and a marketplace alike. If a criterion cannot apply to the engagement type, mark it N/A and rescale. Never score location, company size or employment model as quality.

### 1. Talent transparency and substitution protection (20)
- **4:** Named engineer(s) or, for a dev shop, named key personnel in the SOW. Substitution only with your written approval after you meet the replacement. You meet or interview before committing.
- **3:** Named people; substitution needs notice but not approval.
- **2:** You see profiles but the contract assigns "a resource" of a level.
- **1:** No chance to meet anyone, or no answer.
- *Adapt:* recruiting agency = presents real, consenting candidates it has spoken to, no unsolicited CV dumps. Marketplace = you contract the named person directly, so this is usually a 4.

### 2. Vetting evidence (10)
- **4:** Shares the actual assessment used for your stack, a redacted scorecard, and who runs each stage (engineers, not only recruiters), including a live technical conversation.
- **3:** Describes the stages specifically but shares no artifact, **or** you have already run your own technical interview of the named engineer (note it as buyer evidence).
- **2:** Generic description ("rigorous multi-step process").
- **1:** Percent-rejected claims only, or no answer.
- Your own interview is evidence about that engineer, not about the vendor's process; if you will replace or add engineers later, the vendor's process matters again.

### 3. Identity verification (10)
- **4:** A documented identity check tied to the person you will meet (for example a government ID matched to a live video, or the identity and work-authorization checks the vendor completes as the legal employer), re-verification at start, equipment shipped only to a verified address, pay to an account in the worker's own name.
- **3:** Most of the above, one gap.
- **2:** "We do background checks" with no detail on identity.
- **1:** Nothing, or no answer.

### 4. Contract protections (20)
- **4:** Present-tense IP assignment on creation plus a warranty of chain of title from every worker; you own all accounts; notice, minimum term and any conversion fee stated in writing and proportionate to what the vendor commits; a written remedy if the engineer does not work out (replacement, fee credit or termination for cause) with its trigger and timing.
- **3:** One of those is weaker but disclosed in writing.
- **2:** Two or more weaker, or IP conditional on payment.
- **1:** Vendor-owned IP or accounts, or no contract shared.
- Longer notice or a minimum term from a vendor that employs its engineers on salary is a negotiating point, not an automatic downgrade. Downgrade only when exit terms are open-ended ("to be agreed") or out of proportion to the engagement.

### 5. Commercial clarity (10)
- **4:** One all-in rate (or, for recruiting agencies, one fee basis) in writing; inclusions listed (equipment, time-off coverage, holidays); increase cap; no hidden setup or placement fee.
- **3:** Clear rate, inclusions partly listed.
- **2:** Rate depends on items to be "scoped later".
- **1:** No written rate.
- Price level is not scored here. Report dollars beside the score.

### 6. Delivery and retention record (10)
- **4:** References including one client who left; states average engagement length and how often engineers leave mid-engagement, and what happened.
- **3:** Current-client references only, answers tenure questions.
- **2:** References but no retention data.
- **1:** No references.
- Single-person dependency (one engineer, no backup or handover plan) caps this criterion at 2 and goes in the risk list, whatever the references say.

### 7. Working fit (5)
- **4:** The engineer works in your time zone (this alone earns a 4), **or** a remote engineer has contracted core hours with at least 4 hours of overlap AND a named escalation contact.
- **3:** A remote engineer with overlap in writing but no named escalation contact, or overlap promised but not in writing.
- **2:** Overlap "flexible".
- **1:** No overlap commitment for a remote engineer.
- If the engineer is in your time zone, score 4 on location alone and note it; the escalation contact is what lifts a remote engineer from 3 to 4.

### 8. Security, insurance and company standing (15)
- **4:** A current SOC 2 Type II or ISO 27001 report (or a completed security questionnaire if you accept that), certificates of professional liability / E&O and cyber insurance with limits, a named legal entity and jurisdiction as the contracting party, and a straight answer on years operating and client concentration.
- **3:** Insurance certificates and a completed security questionnaire, but no third-party attestation.
- **2:** Says it is insured or secure but provides no documents.
- **1:** No answer.
- *Adapt:* marketplace freelancer = score the platform's terms and any insurance the freelancer holds; mark N/A if neither applies and say so.

## 2. Clause checklist (read pasted contracts against this)

| Clause | Good looks like | Red flag |
|---|---|---|
| Personnel | Named engineer or key personnel; swaps need your written approval | "Vendor may assign qualified personnel at its discretion" |
| IP assignment | "hereby assigns" all work product on creation; vendor warrants it holds assignments from all personnel | "upon receipt of full payment"; license instead of assignment; "pre-existing tools" your product depends on without a perpetual license |
| Accounts | Client owns repos, cloud, domains, third-party services | Vendor hosts or holds admin access you cannot revoke |
| Subcontracting | Only with your written consent | Silent, or "affiliates and subcontractors" allowed freely |
| Term and termination | Notice and minimum term stated and proportionate to what the vendor commits; termination for cause available | Open-ended lock-in, or early-termination fees with no matching commitment from the vendor |
| Conversion / buyout | Stated fee, ideally falling over time | Not mentioned (ask), or "to be agreed" |
| Non-solicit | Mutual, limited in time, with a conversion path | Bars you from ever hiring the engineer |
| Remedy if it does not work out | Replacement, fee credit or termination right; trigger and timing stated; any clock starts on the first working day | Clock starts at signature; remedy billed; vague trigger |
| Rate | All-in, inclusions listed, increase cap | Rate "subject to change"; billable "resource management" hours |
| Insurance | Professional liability / E&O and cyber, with limits; certificates on request; you named where appropriate | No insurance clause, or limits far below the harm a breach could cause |
| Data protection and subprocessors | Data handling terms, list of subprocessors, breach notice period, return or deletion on exit | Silent on data, or vendor may use any subprocessor without notice |
| Confidentiality | Each worker signs; survives termination | Covers the vendor company only, not individuals |
| Liability | Mutual caps; IP infringement, confidentiality and data breach carved out | Vendor liability capped at one month of fees for everything |
| Governing law and disputes | Your state or a neutral venue | Vendor's foreign jurisdiction only |

## 3. Question bank (pick what is still unknown, max 20)

**People and direction**
1. Will the engineer I interview be named in the contract, and can anyone else be substituted without my written approval?
2. Is the engineer your employee, your contractor, or a partner firm's contractor? In which country?
3. Will you subcontract any part of the work?

**Vetting and identity**
4. Please send the assessment your engineer would take for this stack and a redacted scorecard from a recent hire.
5. Who runs the technical interview: an engineer, or a recruiter?
6. How do you verify a candidate's identity, and when? Do you re-verify at start?
7. Where does equipment ship, and to whose account is the engineer paid?

**Security, insurance and standing**
8. Please send your SOC 2 or ISO 27001 report, or complete our security questionnaire.
9. Please send certificates of professional liability / E&O and cyber insurance, with limits.
10. Which legal entity would sign, in which jurisdiction? How long have you operated, and what share of revenue does your largest client represent?

**Contract**
11. Please send your standard MSA and SOW, including data protection and subprocessors.
12. When does IP transfer to us? Do you hold signed IP assignments from every person who will work on our code?
13. What is the notice period and minimum term, and what do you commit in return?
14. If we want to hire the engineer directly, what is the fee and does it change over time?
15. What happens if the engineer does not work out: trigger, timing, cost, and when does any clock start?

**Money**
16. What is the all-in rate, what does it include (equipment, time off, holidays), and how can it increase?

**Record and working fit**
17. How long do your engineers stay on a client engagement on average, and how often does one leave mid-engagement?
18. Please introduce us to two clients of our size engaged 12+ months and one who ended the engagement.
19. What core hours will the engineer work in our time zone?
20. How fast do you remove access when someone rolls off, and who handles it if the engineer underperforms?

## 4. Reference call script (15 minutes)

Open: "Thanks for the time. I'm considering <vendor> for a <role>. Everything you say stays with me."

1. What did you hire them for, and how long have you worked with them?
2. Was the engineer you interviewed the one who started? Has anyone been swapped since?
3. How long until the engineer was doing useful work without hand-holding?
4. Tell me about the first time something went wrong. What did the vendor do, and how fast?
5. Did invoices ever surprise you?
6. Did they help when your own customers asked security questions about them?
7. If you could change one thing in their contract, what would it be?
8. On a scale of 1-10, how likely are you to use them again for a critical role? What would make it a 10?
9. (For the client who left) Why did you end it, and how did the exit go: access, code handover, final invoice?

Listen for: hesitation on question 2, "they were great until...", and any mention of a replacement that took weeks.

Verify the referee is real: their name, title and company should match a public profile and a company email domain. A reference who only gives a personal email and a mobile number is weak evidence.
