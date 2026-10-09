# Stage-by-stage identity protocol

Run the same checks for every candidate who reaches a stage. "All roles" = every remote hire. "High" = add for High-risk roles (production, code, customer data, credentials or money in the first 30 days).

## 1. Application (all roles, 5 minutes per shortlist)

| Check | How | What a mismatch looks like |
|---|---|---|
| Duplicate contact details | Search your inbox or applicant sheet for each shortlisted phone number and email | Same phone or email on two applicants with different names. Fraud operations reuse VoIP numbers and emails across many profiles (FBI, Jan 2025). |
| Profile consistency | Compare the CV with the LinkedIn or GitHub the candidate links | Different employers, dates or titles across the two; a GitHub account whose commit email or name belongs to someone else |
| Rate sanity | Compare the requested rate to your posted range | Far below market for the seniority claimed; the 2026 allied-government alert lists below-market rates as a red flag |

## 2. Interviews (all roles)

| Check | How |
|---|---|
| Camera on, every interview | State it in the invite for everyone. If a candidate cannot use a camera for a disability-related reason, offer an alternative verification step (see section 5) instead of dropping the call. |
| Same person every round | The first interviewer notes 2-3 neutral visual details (glasses, hairline, a distinctive item in the room). Later interviewers confirm it is the same person. |
| Liveness at the start of one call | Ask everyone: turn off filters and virtual backgrounds for a moment, turn your head side to side, pass a hand in front of your face. Real-time face swaps tend to break on these. |
| Claim consistency | Ask about details of the candidate's own CV and stated location, the way a curious colleague would: "What was the team like at <their company>?" "You said you're in <their city>; is that where you'd work from?" Never ask where they are "really" from. |

## 3. References (High; all roles if you call references at all)

| Check | How |
|---|---|
| Find the referee yourself | Look up the referee's company website and main phone number; ask to be put through, or email the company domain. Do not rely on the number the candidate gave. |
| Confirm the relationship | "In what role did you work with <candidate>, and when?" Compare dates with the CV. |
| Personal email referees | A former manager reachable only on a free email address and a mobile number is a Moderate signal; ask for a second referee from the same employer. |

## 4. Offer (all roles; do these for every finalist at the same point)

| Check | How |
|---|---|
| Live ID check | On a video call, the candidate holds a government photo ID next to their face; compare face and name; do not record or keep a copy unless you have consent and a reason. Or use an identity-verification service for every finalist (Illinois: BIPA written notice and release first). |
| Legal name match | The name on the contract, the ID, the payout account and the background check (if any) is the same person. |
| Background check (if used) | A third-party background check is a consumer report under the FCRA: standalone written disclosure, written authorization before ordering, and pre-adverse-action notice with a copy of the report before acting on it. |
| US employees | Form I-9 Section 2 within three business days of the start date. The employee picks the documents from the official lists. Never demand a specific document. No E-Verify before hire. |

## 5. Alternatives when a step is not possible

Offer, in this order: an in-person meeting (the FBI recommends doing as much of hiring and onboarding in person as possible), a verified-video call with a second interviewer, or a notary or identity-verification service. Use the same alternatives for anyone who asks.

## 6. Onboarding and first 30 days (High; laptop and payment rules for all roles)

| Check | How |
|---|---|
| Laptop shipping | Ship only to the address verified at offer. Any request to ship elsewhere (a "relative", a forwarding service, a new address) pauses shipping until a live video re-verification. Laptop farms receive company laptops at one US address and let workers abroad log in remotely. |
| Remote-access tools | Block unapproved remote-desktop and remote-control software on company machines. |
| Payment | Pay only to an account in the worker's legal name or their own company. No crypto. A change request in the first 90 days needs live video re-verification. |
| Least privilege | Week 1: a test environment with no production access, and only the repos they need. Production, customer data and admin rights only when the work needs them. If production and test share one cloud account, give the new hire a role limited to the test resources. |
| Login signals | Watch for logins from unexpected countries or many IP addresses, and accounts logged in around the clock. The 2026 alert notes the person behind an account "may change depending on the time of day". |
| Day 1 face check | The first video call on day 1 is with someone who interviewed the candidate. Same person? |
| Camera-on standups | For the first 2 weeks, cameras on in standup for the whole team, new hire included. |

## Sources (for the user who wants to read further)

- FBI PSA, Jan 23, 2025, North Korean IT workers and data extortion: https://www.ic3.gov/PSA/2025/PSA250123
- Joint alert on North Korean IT workers, Jul 31, 2026 (US, Japan, ROK, Australia, Canada, France, Germany, Italy, Netherlands, NZ, UK): https://www.ic3.gov/CSA/2026/260731.pdf
- State/Treasury/FBI advisory on DPRK IT workers and sanctions risk, May 16, 2022: https://ofac.treasury.gov/media/923126/download?inline=
- USCIS Handbook for Employers M-274, Section 2 timing and document choice: https://www.uscis.gov/i-9-central/form-i-9-resources/handbook-for-employers-m-274/40-completing-section-2-of-form-i-9
- E-Verify rules (no prescreening): https://www.e-verify.gov/e-verify-user-manual-10-introduction/15-user-rules-and-responsibilities
- Illinois BIPA, 740 ILCS 14/15: https://www.ilga.gov/documents/legislation/ilcs/documents/074000140K15.htm
