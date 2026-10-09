# Seniority calibration: Backend Engineer, Carrier Payouts / Camila
**Mode:** Both · **Inputs used:** role description (Haulwise, 11 people, seed), Camila's CV (pasted text), CTO's 30-minute screen call notes · **Date:** 2026-10-04
**Assumptions:**
- Nobody at Haulwise except the CTO can review a payments design. The frontend engineer and the load-board full-stack engineer have not owned money movement.
- From January the CTO is not available to review the payouts design or code.
- The must-have outcomes are to rebuild payouts so they do not fail or pay twice, to run payouts alone in production, and to add broker invoicing within 6 months. Helping interview engineer #4 is a nice-to-have.
- The screen call was unstructured and did not cover every dimension.

**Not used:**
- Her university and the country it is in. School prestige and national origin are not evidence of level.
- Her graduation year and the guess about her age. Both are age proxies.
- The "3-5 years max" limit and "too senior, gets bored or costs too much". A year ceiling screens out workers 40 and over, who are protected under the US ADEA. If boredom or cost is the worry, ask about scope and pay expectations directly.
- "Good energy, seemed senior to me". These are opinions, not evidence.

(This is general information, not legal advice. State and local rules add more.)

## 1. Level the work needs
| Dimension | What the work requires (from the input) | Level |
|---|---|---|
| Scope | Owns carrier payouts as a system: quick-pay and standard 30-day payouts, the bank ACH integration, failure handling and reconciliation, then broker invoicing. Replaces a cron job plus manual spreadsheet fixes. | Senior |
| Ambiguity | "Rebuild payouts properly" is a goal, not a spec. Even the CTO did not know offhand how the bank handles a failed ACH return. Someone has to find out, choose a design and decide the order. | Senior |
| Autonomy | "They'll work pretty much alone" from January. The CTO will be on sales calls and fundraising. No other engineer has payments experience. | Senior |
| Impact and ownership | Has to run the system in production as well as build it. Carriers were paid twice, twice this year. Failed and duplicate payouts land on this person, with real money at stake. | Senior |
| Technical depth | Idempotency, retries, ACH returns, partial failures, and reconciliation against bank records and deliveries. Mistakes cost money and carrier trust. | Senior |

**Needed level:** Senior, set by Autonomy and Impact and ownership. Scope and Ambiguity agree. **Reviewer test:** Fail. Once the CTO steps back nobody can review payout design decisions, so the role needs Senior at minimum.
**Mismatch flags:** The role was planned as mid-level with a "3-5 years max" ceiling and a $125-140k budget. But this person owns payments alone with no reviewer, and that is senior scope. Either the level and budget move up, or the role is re-scoped, or a reviewer is added (see section 5). Staff is not needed: there is one payments system and three engineers, so the cross-team scope does not exist yet.

## 2. Level the evidence supports
**Estimate:** Mid · **Confidence:** Low. The sources are a CV and one 30-minute screen call. The CV alone caps confidence at Low, and a short screen does not raise it.
| Dimension | Evidence (quote or close paraphrase, with source) | Points to | Strength |
|---|---|---|---|
| Scope | "Built and deployed REST APIs in Node.js / TypeScript (Postgres, Redis)" and "Lead developer on e-commerce and booking projects for 8+ clients" (CV). Neither bullet names a system, a scale or a result. The screen did not show any system she owned over time. | Mid | Unverified |
| Ambiguity | Asked how she would rebuild payouts, she "talked about a payouts table with statuses and retries, then asked me what our bank does on a failed ACH return" (screen). She went straight to the right failure mode before designing, which is a Senior-flavored signal. On the Stripe work, "the client's lead dev wrote the spec, she implemented" (screen). | Mid, with one Senior signal | Weak |
| Autonomy | Stripe idempotency fix: "we added an idempotency check with the lead dev from the client", and the spec was not hers (screen). "Led a team of 2 junior devs on a hotel booking app" (CV), with no statement of what she decided. | Mid | Weak |
| Impact and ownership | "On call for the first 2 weeks" on the booking app, and "after launch most agency projects are handed to the client's team" (screen). Separate from engineering: "Managed carrier settlements and payment exceptions for 300+ trucking partners" and "Built Excel/VBA tools to reconcile carrier invoices against delivery records, cut monthly close from 6 days to 2" (CV, Operations Analyst). That shows real, long-running ownership of a payments process with scale and a result, but it is not ownership of a production software system. | Mid (engineering); strong domain ownership | Weak (engineering) / Strong for domain, CV only |
| Technical depth | Payouts table with statuses and retries, and the ACH-return question (screen). Implemented an idempotency check to someone else's spec (screen). "Really knows freight payments from the ops side, explained quick-pay vs standard terms" (screen). Nobody tested trade-offs under pushback or asked "what did you reject". | Mid | Weak |

**Title check:** "Senior Software Engineer" at a 6-person digital agency. She has been at that agency since Jan 2024 and has held the senior title since Mar 2025. This is the agency pattern: "Senior" there likely meant being trusted with client delivery across many short projects that were handed over at launch. To verify, ask: "Which project did you run in production for more than 6 months? What broke?"
**Unverified claims:**
- "Lead developer on e-commerce and booking projects for 8+ clients" (no system, scale or result)
- "Built and deployed REST APIs" (which system, for how many users, and what changed?)
- "Led a team of 2 junior devs" (what did she decide that they would not have?)
- "Improved page load times by 40%" (no baseline and no how)
- "Contributed to CI/CD setup with GitHub Actions" (participant verb: what part was hers?)
- "Worked on Stripe payment integration" (the screen showed she implemented it to the client lead's spec)

**What would raise confidence:**
1. A structured interview built on the three questions below, with her answers written down as quotes.
2. A work sample: a short written payouts design for Haulwise's case (quick-pay vs standard, ACH returns, duplicate prevention), followed by a walkthrough where you push back on it.
3. A reference from the client's lead dev or her agency lead that confirms what she designed vs implemented.

## 3. Gap
| Dimension | Needed | Estimated | Gap |
|---|---|---|---|
| Scope | Senior | Mid | One level |
| Ambiguity | Senior | Mid (one Senior signal) | Up to one level; the ACH-return question is a promising signal |
| Autonomy | Senior | Mid | One level |
| Impact and ownership | Senior | Mid (engineering) | One level; her domain ownership is a real asset |
| Technical depth | Senior | Mid | Up to one level; untested under pushback |

**Binding gap:** Autonomy. From January she would design and run carrier payouts with nobody reviewing her decisions. A shortfall here directly risks the must-have outcome: payouts that never fail silently and never pay a carrier twice.

## 4. Three questions that separate Mid from Senior
| # | Question | A Mid answer sounds like | A Senior answer sounds like | Tests |
|---|---|---|---|---|
| 1 | "On day one you get: 'payouts fail or double up, fix it.' Today it's a cron job calling the bank's ACH API plus spreadsheet fixes. What do you write or decide before any code? If the bank call times out after sending, what happens?" | Describes the table and statuses, then says she would ask the CTO how it should work. The timeout case gets a retry. | Writes a short plan with 2-3 options (for example a stop-the-bleeding fix first, then the rebuild), says what she would cut and in what order. Makes payouts idempotent with a key per payout so a retried call cannot pay twice, finds out the bank's return and status behavior before choosing, and plans daily reconciliation against bank records. | Ambiguity, Technical depth |
| 2 | "Tell me about something you built that broke in production after launch, on the booking app, the Stripe work or anything else. What did you change afterward?" | She fixed the bug when it was reported or assigned, and the story ends there. Or every story ends at handover. | She owned the problem by choice, found the root cause and changed the design or added an alert. She uses "I" for her part and "we" for the team's, and can say what she would do differently now. | Impact and ownership |
| 3 | "From January nobody here will review your payouts design or code. How would you know your design is right before it moves real money?" | Unsure, or "I'd check with the CTO", or "I'd test it well" with no detail. | Gives specifics: a written design doc, tests for duplicates and failed returns, a small first release (for example quick-pay for a few carriers), metrics and alerts on failed or duplicate payouts, and an outside reviewer for the parts that cannot be undone. | Autonomy (binding gap) |

Listen for: after each answer, ask "What did you reject, and why?" and "What would you change now?". A rehearsed answer has no rejected alternative and no regret.

## 5. Implication
- **Option A:** Move Camila forward and hire at Mid with a path, but only if someone at Senior level reviews the payouts design and code for the first 6 months. That could be a contracted or fractional senior payments engineer, or the CTO protecting fixed review time. Without that reviewer the path is a risk, because the role fails the reviewer test from January. Her settlements and reconciliation background is a real asset for this path.
- **Option B:** Re-level the role to Senior, revisit the budget and the "3-5 years max" ceiling, and keep looking at Senior. The current evidence on Autonomy and Impact and ownership points to Mid, with Low confidence. Camila can still be assessed as a Senior candidate through the questions above.
- **Option C:** Re-scope so a Mid hire owns broker invoicing and payout features, while a Senior (hired or contracted) owns the payouts design and its production running. This matches what the current evidence supports.
- **What would change this read:** Senior-level answers to questions 2 and 3, confirmed by the work-sample walkthrough, would move the estimate toward Senior with Medium to High confidence. Mid-level answers would confirm Option A or C.

**Decision (made by the CTO):** ________ **Date:** ________

---
Made with the free Calibrate Seniority skill by Ruzora · ruzora.com/skills
