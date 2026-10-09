## Review: Dev S., Mid-level Backend Engineer (document ingestion), day 54 of 90
Prepared for you (Quillmark), with input from Carla (eng lead, Dev's manager). General information, not legal advice. The decision is yours.

## Assumptions and gaps in the evidence
- **Up front:** you asked for a paper trail to let Dev go. The evidence you gave doesn't support that decision yet. Three of the four support checks fail, his expectations had no due dates, and he hasn't had a documented performance conversation with examples. A file built now would show the company's gaps more clearly than his. This review sets up the fair version: dated expectations, fixed support and a day-90 checkpoint that can support whatever you decide.
- **Day count:** Dev started Mon Aug 11, 2026. Today (Sun Oct 4) is **day 54**, not 58. Day 60 is Sat Oct 10. Day 90 is **Mon Nov 9, 2026**. All proposed dates below fall before Nov 9.
- **Expectations were stated at the offer, but it's not clear they were written down.** You said "what we told him at the offer." Pull the offer letter or the kickoff message and check that the three outcomes are written there. **None of them had a due date.** Without one, "Behind" can only mean "not done yet," not "missed."
- **Employment context:** W-2 employee, remote, Ohio, at a 26-person company. Ohio is generally at-will, but see rule 9 below and the part-ways checklist.
- **Excluded protected matter:** the mid-September week off for a medical procedure is **left out of this review entirely**. It isn't used as evidence and isn't used to adjust or excuse any result. Remove it from any performance notes too. It sits about 2-3 weeks before the "went quiet" incident and about 3 weeks before you started leaning toward letting him go. **If an adverse decision is on the table, talk to an employment lawyer first.** Acting close to medical leave can look like retaliation or disability discrimination even when it isn't. At 26 employees and under 12 months of service, federal FMLA doesn't apply (it needs 50+ employees, plus 12 months and 1,250 hours of service). The relevant risks are the ADA, which covers 15+ employees, and Ohio's civil-rights law, which covers much smaller employers.
- **Impressions excluded from the evidence:** "just not senior enough," "not a culture fit," "too quiet in standup." None of these is an observable fact tied to a written expectation. Being talkative in standup was never a stated requirement for this role. "Culture fit" in a file invites the question "fit to what?", so leave it out. If something specific sits behind "not senior enough," write the examples down (task, date, what was expected).
- **Positive fact noted:** other engineers like working with him. It's an impression, recorded as context only.
- **No identity or security signals** were mentioned.
- **Missing evidence to collect before day 90:** PR list with review-round counts per PR (week 2 vs now); whether the testing expectation is written anywhere (CONTRIBUTING, PR template); the ingestion failure-rate baseline on the day he started ingestion work vs now; status of the parser bug queue handover; whether Carla has ever raised the missing-tests pattern with him directly, outside PR comments.

## Expectations used
| # | Expectation | Source (scorecard / plan / message) | Due by |
|---|---|---|---|
| 1 | Own the document-ingestion pipeline (PDF/DOCX parsing → clause extractor) | Stated at offer (confirm it's in writing) | Not set |
| 2 | Get ingestion failures under 2% (baseline ~7%) | Stated at offer (confirm it's in writing) | Not set |
| 3 | Take over the parser bug queue from Carla | Stated at offer (confirm it's in writing) | Not set |
| 4 | PRs include tests (inferred from Carla's repeated review comment) | **Not in the offer.** Appears only in review feedback. Check whether it's a written team standard applied to peers. | Not set |
| 5 | Raise blockers promptly (inferred from the Oct 1-2 incident) | **Not stated anywhere you mentioned.** A reasonable norm, but write it down now. | Not set |

## Evidence
| # | Expectation | What happened (facts, dates) | Status: Ahead / On track / Behind / No evidence |
|---|---|---|---|
| 1 | Own ingestion pipeline | First PR merged on about day 9 (around Aug 20) after broken local setup. Pulled to the billing migration for 3 weeks in September, then returned to ingestion. Shipped the scanned-PDF fix on Sep 30, which Carla called "solid." | On track (given ~5 weeks of actual ingestion time) |
| 2 | Failures < 2% | ~7% → ~5.5% (about 1/3 of the gap closed). Scanned-PDF fix shipped Sep 30. | Behind the end target. No due date was set, so no deadline was missed. |
| 3 | Take over parser bug queue | Nothing provided | No evidence |
| 4 | PRs include tests | Carla reports leaving the same missing-tests comment on "maybe 4-5" PRs. No PR numbers or dates given. | Behind (early-warning signal: same comment 3+ times) |
| 5 | Raise blockers promptly | Oct 1-2: no visible progress on a ticket for 2 days, then reported it had been blocked on a permissions issue he hadn't raised | Behind (single instance) |

## Support check
| Question | Answer from input | Note |
|---|---|---|
| Working access + environment in week 1 | **No** | Setup docs were outdated and docker compose was broken. He needed calls with Carla, and the first PR took 9 days. The Oct 1-2 blocker was also an access/permissions issue. |
| Buddy with real time | **No** | Buddy Anton left in week 3 and was never replaced |
| Written priorities, stable | **No** | Pulled off ingestion to billing for 3 weeks in September (about 40% of his tenure so far). No due dates on the original priorities. |
| Fast answers / docs | **Partial** | Carla made time for calls. The docs were out of date. |

**Result: 3 "No" + 1 "Partial."** Under rule 2, the gaps are **presumed Ramp-up (the company's to fix)** until support is fixed and has had time to work, usually 30 days. No gap can fairly be called Capability yet.

## Gap diagnosis
| Gap | Type: Ramp-up / Capability / Conduct / Role mismatch | Why | Company action | Hire action |
|---|---|---|---|---|
| Failure rate at 5.5% vs < 2% target | Ramp-up | No due date. Three weeks diverted to billing. Trending in the right direction, and the Sep 30 fix was rated solid. | Set a dated interim target with Dev, say ≤ 4% by Nov 6 (your call on the number). Protect him from re-assignment until Nov 9 unless leadership signs off. | Weekly failure-rate number in writing every Friday, with what changed |
| Missing tests on 4-5 PRs | Ramp-up (presumed). **Watch for Capability.** | Repeated 3+ times, which is a real warning signal. But no written test standard was cited, he had no buddy, and the feedback came only as PR comments. If it continues after it's written down and discussed directly, it moves to Capability. | Write the test expectation down (PR template checklist and what "tested" means for parser code). Carla raises it directly in the meeting, not only in PR comments. | Every PR from Oct 7 includes tests per the checklist. Target: zero "missing tests" comments by Nov 6. |
| Silent 2 days on a blocker (Oct 1-2) | Conduct/reliability (first instance, minor) | Not raising a blocker is a reliability issue. It isn't dishonesty, and it's a first instance. The blocker itself was an access gap, and he had no buddy to ask. | State the norm in writing: raise any blocker within half a working day in the team channel. Fix the permissions provisioning for his scope. | Follow the norm. Daily async status on tickets in progress. |
| Parser bug queue not taken over | No evidence yet | No information on handover status | Carla schedules a handover session and lists the queue by Oct 16 | Owns the queue from Oct 16. Triages new parser bugs within 2 working days. |
| "Not senior enough," "culture fit," "quiet in standup" | Not a gap (impression) | Not tied to any written expectation or example | If Carla has specific examples, document them with dates. Otherwise drop them. | None |

## Trajectory
Early weeks: about 9 days to a first merged PR on a broken environment with outdated docs, then losing his buddy in week 3, then three weeks on an unrelated billing fire. Recent weeks: back on ingestion, he shipped a scanned-PDF fix on Sep 30 that his lead called solid, and the failure rate moved from ~7% to ~5.5%. The concerning pattern is the missing-tests comment repeating on 4-5 PRs. We don't have the dates to say whether that is shrinking or holding steady. Pull the review-round counts for his earliest and latest PRs to see the direction. The single silent-blocker episode (Oct 1-2) is recent and worth a direct conversation, but one instance isn't a trend. Overall the output trend is upward, while the process gaps (tests, blocker escalation) need written expectations to be judged.

## Options
| Option | When it fits | What it requires next | Risk |
|---|---|---|---|
| On track | The evidence showed clear progress against dated targets | Confirm, set the next 90 days | Overlooks the repeated missing-tests pattern and the silent blocker |
| On track with focused support | Gaps are named and the hire can close them with support | 3 named gaps, company fixes, hire targets, check-in by Nov 6 | Low. Needs Carla to actually make the time. |
| **Reset (with focused support inside it)** | Expectations had no dates, priorities changed for 3 weeks, support failed | Rewrite expectations with dates now (this week), fix the environment/buddy/permissions by Oct 9, mid-point check Oct 23, decision review Mon Nov 9 (day 90) | Low. Costs about 5 weeks. If gaps persist, you'll then have a clean, fair record. |
| Part ways | Only if a Capability or Conduct gap persists after support was given, he was told clearly with examples, and it didn't change in a reasonable window | **None of these conditions are met today.** Would require the Reset period first, plus legal review given the timing near medical leave. | **High** now: failed support check, no dated expectations, no documented conversation, and adverse action ~3 weeks after medical leave (retaliation/ADA exposure). The record would undercut the reason. |

**What the evidence supports:** Reset, with a focused-support plan and a day-90 decision on Nov 9, 2026. Confidence is **medium-high** that parting ways isn't supported today: 3 of 4 support checks failed, no due dates existed, there's been no documented direct conversation, and the measurable trend (7% → 5.5%, the Sep 30 fix) is positive. Confidence about how Dev will perform once support is fixed is **low**, because there's no evidence yet under fair conditions. **What would change this:** dated PR evidence showing the missing-tests issue is not shrinking after the written standard and direct conversation on Oct 6. A second unraised blocker after the norm is written down. No movement on the failure rate or the bug queue by Nov 6 despite protected focus time. Any of these, documented, would make Capability or Conduct a fair call at day 90. Talk to counsel before acting on it.

## Conversation script (20-30 min)
1. Open: "We're at about day 55. I want to reset your goals with real dates, fix what we got wrong on our side, and be clear about two things I need from you."
2. Ask first: "How has the work on ingestion gone since you came back from billing, and what's slowed you down?" / "What support would make the biggest difference over the next five weeks?"
3. Share:
   - "Your scanned-PDF fix on Sep 30 was solid, and failures moved from about 7% to 5.5%. That's real progress."
   - "Tests: Carla has left the same missing-tests comment on 4-5 of your PRs. From now on every PR needs tests per the checklist we're adding to the PR template."
   - "On Oct 1-2 a ticket was blocked on permissions for two days before anyone knew. When you're blocked, flag it in the team channel within half a working day."
   - "On our side: the setup docs and docker compose were broken, your buddy left in week 3 and we didn't replace him, and we pulled you to billing for three weeks. We're fixing those."
4. Agree: Company by Fri Oct 9: fix setup docs and docker compose, assign a new buddy with 2 hrs/week, fix permissions for the ingestion scope, publish the PR test checklist. Ingestion stays protected through Nov 9. Dev: tests on every PR from Oct 7; blockers raised within half a day; parser bug queue handed over by Oct 16; a written failure-rate number every Friday; ≤ 4% failure rate by Nov 6 (or the number you set). Check-ins: Fri Oct 23 (mid-point) and Mon Nov 9 (day-90 review).
5. Close: "I'll send you a written summary of this today so we're both working from the same page. Reply if anything in it doesn't match your understanding."

## Written summary for the file (send to the hire after the meeting)
Date: [meeting date, e.g. Tue Oct 6, 2026]. Day-54/60 check-in, Dev S. and Carla [surname].

Role expectations (from offer): own the document-ingestion pipeline, reduce ingestion failures below 2% (baseline ~7%), take over the parser bug queue from Carla.

Current status: the failure rate is ~5.5%. The scanned-PDF fix shipped Sep 30. Dev worked on the billing migration for three weeks in September. The parser bug queue handover has not yet happened.

Discussed: the "missing tests" review comment appeared on 4-5 PRs. A ticket was blocked on permissions Oct 1-2 without the blocker being raised.

Company commitments by Oct 9: updated setup docs and docker compose, new onboarding buddy (2 hrs/week), ingestion-scope permissions, PR test checklist. Dev stays on ingestion through Nov 9.

Agreed next steps: tests on every PR from Oct 7; blockers raised in the team channel within half a working day; parser bug queue owned from Oct 16; weekly failure-rate update each Friday; failure rate at or below 4% by Nov 6.

Check-ins: Oct 23 and Nov 9, 2026.

## Part-ways checklist  (include only if Part ways is an option)
*Included because you raised it. On today's evidence it's not the supported option.* Check your local law and your contract; at-will rules vary.
- [ ] Reread offer letter / contract for probation, notice and severance terms
- [ ] Check your state's at-will and final-pay rules (Ohio); talk to counsel if any protected event in rule 9 applies. **It does here: the mid-September medical leave. Talk to an employment lawyer before any adverse decision.**
- [ ] Decision made before the meeting; script ready; meeting under 15 minutes
- [ ] Access revoked during or right after (use the access register); devices recovered; account ownership moved (ingestion pipeline, parser bug queue, any repos/services he owns)
- [ ] Written record of the reasons, matching what was told to the hire. Use only dated facts tied to the written expectations above, never "culture fit," "quiet," or "not senior enough."

---
Made with the free New-Hire 90-Day Review skill by Ruzora · ruzora.com/skills
