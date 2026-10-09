## Assumptions
- The user wanted a draft right away with no follow-up questions, so I wrote the post from the message as given.
- Sponsorship was not answered. I assumed you **cannot** sponsor a visa for this role. If you can, replace that line before posting.
- The application close date is **Friday, October 23, 2026**: you post this week and want to move within 3 weeks. Change it if your timeline moves.
- Time-zone overlap: most of the team is in Colorado and Texas, so I asked for 4 hours of overlap with US Mountain/Central business hours. Adjust or remove it.
- Kubernetes, Kafka, Terraform, React and ML are not part of the first 90 days. The work you described is Django, Postgres, AWS, payer scrapers/APIs and the auth-request queue, so I left the others out of the must-haves. If you already run Kubernetes or Kafka in production, tell me and I'll add them.
- Equity is described as "0.25%-0.5%, 4-year vest, 1-year cliff". The type (options or RSUs) and strike details are left as `[FILL]`.
- Paid time off, health premium coverage and the take-home time cap were not given, so they are `[FILL]` placeholders.
- Applications come in through the LinkedIn and Wellfound postings.

## Job post (paste-ready)

# Senior Backend Engineer (Python/Django), remote US

Pinecrest Health automates prior authorization for small physical therapy clinics, so their staff spend less time on insurance paperwork and more time with patients. We are 14 people and raised a $6M seed round in March. Our CTO, Maya, wrote most of the backend herself. We are hiring you to take it over so it can keep up with our growth.

### What you'll own
- **The backend itself.** Within your first 3 months you will be the day-to-day owner of our Python/Django backend and Postgres database on AWS, taking over from Maya.
- **Payer integrations that don't break silently.** We connect to insurance payer portals through scrapers and a few real APIs. They break often. You will make breakage visible before a clinic notices, and make fixes fast and routine. `[FILL: a target, e.g. "integration incidents found by monitoring, not by customers"]`
- **A queue that survives month end.** Our auth-request queue falls over during the month-end volume spike. You will make it handle that peak without anyone stepping in by hand.
- **A calmer on-call.** You will share on-call with Maya and cut down the pages that wake either of you up.

### What you'll work on day to day
In your first 90 days you will work in Python, Django and Postgres on AWS. Most of your time goes to the payer scrapers and API clients and to the background queue that processes authorization requests. You report to Maya, and you will work directly with her and with our CEO. Now and then you will talk to clinic staff to understand a failed request. `[FILL: other engineers on the team, if any]`

### You'll do well here if you
- Have shipped and run a production Python backend that real customers depended on, ideally in Django (typically 5+ years of backend work, but we care about what you've run, not the count).
- Know Postgres well enough to find and fix a slow query or a risky migration in production.
- Have built or maintained integrations with unreliable third-party systems (scraping, flaky APIs) and made them dependable with retries, idempotency and monitoring.
- Have made a background job or queue system hold up under predictable load spikes.
- Write clear, plain English for both engineers and non-technical people, and are comfortable sharing on-call.

### Nice to have
- Experience with healthcare data and HIPAA safeguards.
- Experience with insurance payers, prior authorization or healthcare EDI.
- Infrastructure as code on AWS (for example Terraform).
- Experience at an early-stage company where you owned a system end to end.

### What's hard about this job
- The integrations break constantly. Payer portals change without warning, and a lot of this work is repair before it is improvement.
- You will be on-call every other week, alternating with Maya, and month end is the hardest stretch until the queue is fixed.
- Most of the code was written by one person under time pressure. Expect gaps in tests and documentation.
- We are a small team and our CEO is non-technical. You and Maya are the backend engineering team, and you will make a lot of calls without a big group to check with.

### Pay and benefits
- Base salary: $165,000-$200,000 per year, plus 0.25%-0.5% equity `[FILL: stock options or RSUs]`, vesting over 4 years with a 1-year cliff
- Health and dental insurance `[FILL: share of premiums the company pays]`
- 401(k) (no employer match)
- $1,500 home office stipend
- `[FILL: paid time off / holidays]`
- Fully remote within the US, with at least 4 hours of overlap with US Mountain/Central business hours

### How we hire
1. A call with our CEO.
2. A technical interview with Maya.
3. A take-home exercise `[FILL: time cap, e.g. no more than 3 hours]`.
4. References.

We aim to make a decision within 3 weeks of your first call.

### To apply
Apply through this LinkedIn or Wellfound posting and answer one question:
**"Our queue that processes prior-authorization requests falls over at month end. In 3-4 sentences, tell us about a time you made a background job or queue system hold up under a predictable spike, and how you knew it worked."**

Applications close: Friday, October 23, 2026

You must be legally authorized to work in the United States. We are unable to sponsor or take over sponsorship of an employment visa for this role. Pinecrest Health is an equal opportunity employer. We do not discriminate on the basis of race, color, religion, sex, sexual orientation, gender identity, national origin, age, disability, veteran status or any other protected characteristic. We may use an automated tool to help review applications. A person reviews every application before any decision, and you can ask for an alternative review process by writing to `[FILL: contact email]`.

## Requirement-inflation check
| Original requirement | Decision | Why |
|---|---|---|
| 8+ years Python | Rewritten | Rule 5: years are a proxy. Now asks for evidence ("shipped and run a production Python backend") with a loose "typically 5+ years" band, not a hard gate. |
| CS degree from a good school | Cut | Rule 6: product backend work doesn't need a degree, and "good school" filters on pedigree, not skill. |
| Django | Kept as must-have | It's the system they take over on day one (folded into the Python must-have). |
| Postgres | Kept as must-have | Day-one stack. The queue and integrations both depend on it. |
| AWS | Kept (in day-to-day stack) | Day-one stack. Infrastructure as code moved to nice-to-have. |
| Kubernetes | Cut | Rule 7: not mentioned as part of the first 90 days. Add it back only if you run it in production today. |
| Kafka | Cut | Rule 7: the queue problem is a must-have, but naming one tool would turn away people who solved it with something else. |
| Terraform | Moved to nice-to-have | Rule 7: useful on AWS, but not a reason to reject an otherwise strong candidate. |
| React | Cut | Rule 7: this is a backend role, and nothing in the first 90 days touches the frontend. |
| ML experience | Cut | Rule 7: no ML work in the outcomes. |
| Healthcare experience (HIPAA) | Moved to nice-to-have | Rule 4: you wouldn't turn down a strong backend engineer who lacks only this. HIPAA safeguards can be learned. |
| Startup experience | Moved to nice-to-have | Rule 4. Rewritten as "owned a system end to end". |
| Rockstar who can wear many hats | Cut / Rewritten | Rule 1: hype words. The actual hats (integrations, queue, on-call, talking to clinic staff) are now spelled out in the post. |
| Young energetic team vibe | Cut | Rule 11: age-coded language (ADEA protects workers 40+). |
| Native English speaker | Rewritten | Rule 11: national-origin coded. Now "write clear, plain English for both engineers and non-technical people". |
| US citizens only (patient health data) | Rewritten | Rule 10: handling health data is not a legal citizenship requirement. Replaced with work-authorization and no-sponsorship wording. |
| (new) Integrations with unreliable third-party systems | Kept as must-have | Comes straight from your #1 pain point (payer portals break constantly). |
| (new) Queue reliability under spikes | Kept as must-have | Comes straight from your month-end outage. |

## Compliance lint
General information as of October 2026, not legal advice. Confirm with counsel for your locations.
| Check | Status | Note / fix |
|---|---|---|
| Pay range present and good-faith | PASS | $165k-$200k base. The top is about 1.21x the bottom, which is well within one level. Equity is stated plainly. |
| Your state/city pay-transparency rule (range, benefits, close date) | CHECK | A remote US post reaches every covered state. **Colorado** (you have employees there, so you're covered): range, benefits description and close date are all required and all in the post. Fill PTO before posting. **New York** (4+ employees): range required if the role could be done in NY. Included. **California** (15+ employees): at 14 people you may be just under the threshold, but your next hire puts you over it. The range is included either way. **WA, IL, MD, MN, HI, VT, MA, NJ, DC** have their own thresholds and remote-coverage rules. The range covers the main requirement, but check each state where you would accept a hire. **Texas and Delaware** have no state posting-pay law. |
| Citizenship / visa wording | FIXED | "US citizens only because we handle patient health data" removed. Data sensitivity is not a law, regulation or contract requirement. HIPAA does not limit who can access PHI by citizenship. DOJ settled with 16 employers in 2022 ($832,944 in combined penalties) over ads like this. Replaced with "legally authorized to work in the United States" plus a no-sponsorship line. Confirm the no-sponsorship assumption. |
| Age-coded wording | FIXED | "Young energetic team vibe" cut. "8+ years" rewritten as evidence plus a loose band with no maximum. |
| National-origin / language wording | FIXED | "Native English speaker" replaced with "write clear, plain English for both engineers and non-technical people". |
| Disability-related requirements | PASS | No physical requirements on a desk job. |
| Salary history / criminal history asked | PASS | The post asks neither. Make sure your LinkedIn/Wellfound application forms don't ask for current or past salary either (Colorado, California, New York and others ban it). |
| AI screening notice (NYC, IL) | CHECK | You plan to pre-screen with an AI tool, so a notice line is added. **NYC Local Law 144:** if the role can be filled by someone in NYC, the tool needs an independent bias audit within the past year, a published summary and 10 business days' notice before use. **Illinois (HB 3773, effective January 1, 2026):** notice is required when AI is used in hiring decisions. **Colorado** has its own AI Act covering high-risk AI in employment decisions, and its effective date has been pushed back more than once. Check its status with counsel, since your team is mostly in Colorado. Simplest path: have a person read the screening-question answers instead. |
| EEO statement | FIXED | Added a short, plain EEO line. No demographic questions on the application. |

## Before you post
- **Confirm sponsorship.** The post says you can't sponsor. If you can, swap that line, because it changes who applies.
- **Decide on the AI pre-screen now.** Either confirm your vendor has a current bias audit and do the NYC/IL/CO notice steps, or skip the tool. One screening question and a person reading the answers will get through 400 applications faster than you expect, since most bulk applicants won't answer it.
- **Fill the placeholders:** PTO, health premium share, equity type, take-home time cap and the contact email in the AI notice. Then check that the LinkedIn and Wellfound forms don't ask about salary history.
- **Agree with Maya on who reads applications and by when.** For a 3-week close, plan to screen daily in week 1 and schedule her technical interviews by week 2.

---
Made with the free Engineering Job Description skill by Ruzora · ruzora.com/skills
