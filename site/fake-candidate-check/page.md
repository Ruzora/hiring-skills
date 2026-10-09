---
title: "Fake Candidate Detection: Free AI Skill for Remote Hires"
description: A free AI skill that turns FBI guidance into an identity-check protocol for remote engineering hires and a fair red-flag log for any candidate you doubt.
target_query: fake candidate detection
category: screen
related_blog: how-to-identify-fake-candidates
cta: /how-we-vet
author: Roberto Espinoza
updated: 2026-10-04
---

# Fake candidate detection for remote engineering hires

Fake Candidate Check is a free AI skill that builds an identity-verification protocol for remote engineering hires, from application to day 30. Describe the role and what you noticed about a candidate; it writes a dated red-flag log with a verification step for each flag, a neutral message for every finalist, and what to do if a check fails.

The threat is documented. In June 2025 the US Department of Justice announced actions against North Korean remote IT worker schemes that had placed workers at more than 100 US companies, with searches of suspected laptop farms in 16 states.

## What you get

- **A risk tier** based on what the hire touches in week one.
- **The money rules**, including why paying a sanctioned worker is a legal risk.
- **A stage-by-stage protocol** (application to day 30) with who does each check and when, the same for every finalist.
- **A red-flag log:** each observation as a dated fact, rated Strong, Moderate or not a signal, with the step that would clear or confirm it.
- **A "dropped from the log" list** for worries that are not evidence, such as an accent.
- **A next step for you to decide**, never a verdict.
- **A finalist message** and a failure script.

## Sample output

From a real run. The input: a 14-person startup about to offer a remote contractor week-one access to its only AWS account and customer data. The top candidate asked for $38/hr against a $75-95 range, shared a phone number with another applicant, looked different in round two, gave Gmail references, then asked to ship the laptop to a cousin and to pay a company instead of him. The cofounder wanted to drop him over his accent.

> | Date | What happened (fact) | Signal | Why it matters | Verification step that resolves it |
> |---|---|---|---|---|
> | Sep 29 | Asked to ship the work laptop to "his cousin's place in Dallas" rather than his stated Tulsa address, because he will be traveling | Strong | Laptops sent to other addresses are how laptop farms operate (FBI and 2026 alert) | Ship only to the address verified at offer, or have him collect it in person; any other address waits for a live video call with ID |
> | Sep 29 | Asked to be paid to "Brightlane Services LLC" instead of to him directly | Strong | Payment to a third party or a name other than the worker's is a listed money signal | Paying his own company is fine. Ask for the company's registration; check the state business registry shows him as owner or member, and that the bank account is in that company's name. If not, pay only to an account in his own legal name |

> **Dropped from the log (not a signal):**
> - Accent you could not place: an accent is never evidence and using it is national-origin discrimination.
> - Slack English more polished than spoken English: many people write better than they speak in a second language, and many use grammar tools.

> 1. Hold the offer for a few days for all three finalists and send every one of them the message below. Run the same offer-stage checks for the other 2 finalists in parallel, so nobody is treated differently.

It also caught that one shared AWS account gives a new hire production access.

## How it works

**The signal is inconsistency, not origin.** Identity fraud shows up as mismatches: the face on video against the ID, contact details shared with other applicants, a laptop address that differs from the one on file, a payout account in someone else's name. Accent, nationality, a foreign degree and non-native English are never evidence.

**Fraud moves to the handoffs.** The FBI's January 2025 warning describes workers who stole code and data, then held it for ransom once discovered. It recommends checking identity through interviewing, onboarding and employment, cross-checking applicants for reused phone numbers and emails, and watching for address or payment changes. So most of the protocol sits between the last interview and first payroll.

**Verify references yourself.** Call the referee's employer on its main line, never the number the candidate supplied.

**Identity checks are not work-authorization checks.** For US employees, Form I-9 happens after hire, the employee chooses the documents, and E-Verify cannot prescreen. A live ID check, viewed on camera and not copied, goes to every finalist at the same stage.

**Already hired and suspicious? Cut access first.** Reduce access to code, cloud and data quietly, then verify. If you suspect a North Korean IT worker or identity theft, report it at ic3.gov.

General information, not legal advice; rules vary by state.

### How this compares

A static fake-candidate checklist lists warning signs, often mixing in "unusual accent" or "foreign education". Asking a chatbot cold tends to give generic advice or agree with your hunch. This skill turns each observation into a fact and a verification step, drops the signals that invite a discrimination claim, and covers the laptop and payment steps where the fraud happens.

## How to install and use

**Claude.ai:** download the skill's .zip from this page and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then describe the role and what you have noticed, with dates.

**Claude Code:** run `/plugin marketplace add Remutopia/ruzora-skills`, then `/plugin install hire-screen@ruzora-hiring`. Describe the hire and the skill loads on its own.

**Any other AI (ChatGPT, Gemini, Copilot):** copy the prompt version from this page, paste it as your first message, then describe the situation.

Never paste ID photos, ID numbers or bank details. Describe them.

## Frequently asked questions

### What counts as evidence that a candidate is fake?
Look for identity and money mismatches: a phone number shared with another applicant, a different face in a later round, a laptop shipped elsewhere, pay to a third party or in crypto. Each leads to a verification step, not a conclusion.

### What are the red flags for North Korean IT workers?
FBI and allied-government guidance lists reused contact details, refusing video, below-market rates, laptops shipped to other addresses, payment to third parties or in crypto, and accounts that change behavior by time of day. Each maps to a check.

### Can I ask a candidate for ID before making an offer?
A live identity check is generally fine if you apply it to every finalist at the same stage, ideally after a conditional offer, and do not keep copies. It is separate from Form I-9, which comes after hire and lets the employee choose the documents. Check your state's rules.

### Is it free?
Yes. No signup and no email gate. Use it, change it and share it under CC-BY-4.0.

---

**Rather have identity checked before anyone reaches your inbox?** See [how we vet engineers](/how-we-vet): 5-stage vetting, including live coding, system design and AI-tool proficiency. Or [request a shortlist](/request-shortlist) and get a vetted shortlist within 72 hours. For the background on the threat, read [how to identify fake candidates](/blog/how-to-identify-fake-candidates).
