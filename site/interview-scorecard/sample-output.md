# Interview scorecard: Dana, Senior Backend Engineer (Python/Postgres), Senior

**Assumptions:** Level is Senior, taken from the job title. The notes did not name the hiring manager, so the decision line is left open for whoever makes the call. "Coding quality" is scored against the problem solving / coding anchors, plus the code quality anchors for testing. Each competency has one signal owner: Marcus owns design, Priya owns coding quality, and Jordan owns ownership and mentoring. Jordan's notes say "Marcus and I already chatted and we agree", so Jordan's scores are marked possibly anchored. Marcus may be too, and he should confirm whether he wrote his notes before or after that chat. Nobody asked about mentoring in a structured way.
**Competencies:** Backend design for money-moving systems (must-have) · Coding quality (must-have) · Ownership (must-have) · Mentoring (nice-to-have)

## 1. Scorecards by interviewer

### Marcus (CTO), system design
| Competency | Score (1-4 / NE) | Evidence from the notes | Confidence |
|---|---|---|---|
| Backend design for money-moving systems | 4 | "Started by asking volumes, how many customers, cutoff times for ACH." Proposed a jobs table and worker pool with an "idempotency key per payout = (invoice_id, attempt_group)" and "explained why a retry must not double pay". When asked what happens if a worker dies mid-batch, she proposed "in_flight" rows with a lease timeout and a reconciler job: "didn't need a hint". One gap: she "didn't bring up observability until I asked", then proposed alerts on rows stuck in_flight past the lease. | High |

**Their overall lean:** "strong yes" · **Supported by their evidence?** Yes. She started from the requirements, used idempotency correctly and gave a failure-mode answer without a hint, which meets the 4 anchor at senior level. Raising observability unprompted would have made it a clear 4.
**Opinions to turn into evidence:** "best design interview this quarter" -> ask: "Against the senior bar, not other candidates, which part of her design went beyond what you expect from a senior?"
**Other observations (not scored):** None.
**Bias check:** Contrast. "best design interview this quarter" ranks her against other candidates instead of the bar. Her score rests on the written evidence, not on this line. Possible anchoring: Jordan wrote that they "already chatted and we agree". Marcus should confirm his notes were written before that conversation.

### Priya (Senior Eng), live coding
| Competency | Score (1-4 / NE) | Evidence from the notes | Confidence |
|---|---|---|---|
| Coding quality | 3 | "took ~8 min asking clarifying qs (what counts as dupe, timezone)". Wrote it in Python and it "worked for main case". She "missed the case where amounts are strings with commas, found it herself when I said 'try the sample file'". "No tests until I asked, then wrote 2 pytest cases quickly." "Talked through complexity fine." That is a working solution after one hint, with explained choices, which matches the 3 anchor. A 4 would have needed the comma edge case and tests without prompting. | High |

**Their overall lean:** "lean no. not sure she's senior" · **Supported by their evidence?** Weaker than evidence. The written evidence supports a 3. The lean rests on speed compared with another candidate and on a comment that has been struck, not on a written coding gap.
**Opinions to turn into evidence:**
- "took ~8 min asking clarifying qs... which I thought was a lot" -> ask: "Did any of those questions change the solution (dupe rule, timezone)? Under our anchors, clarifying before coding is positive evidence."
- "not sure she's senior" -> ask: "What did she say or do that was below the senior bar, apart from needing a prompt for tests?"
- "solution was ok" -> ask: "What specifically was missing from the solution?"
**Other observations (not scored):** None that are usable. The communication comment is struck (see section 2).
**Bias check:** Contrast. "honestly the last candidate (Ken) was faster" compares her with another candidate instead of the bar. Speed is not in the competency list.

### Jordan (CEO/founder), values + ownership
| Competency | Score (1-4 / NE) | Evidence from the notes | Confidence |
|---|---|---|---|
| Ownership | 4 | Reconciliation bug at her last job: she "noticed mismatch in nightly report nobody was assigned to, traced to a rounding issue in FX conversion, fixed it, then wrote the runbook and set up an alert. said 'I' for the fix and 'we' for the rollout". She also "asked good questions about our runway and on-call". The story matches the 4 anchor point for point. | Med (self-reported story; interviewer possibly anchored) |
| Mentoring (nice-to-have) | NE | "said she ran the intern program at the bank for 2 years but didn't go into details." This is a claim without any described behavior. | Low |

**Their overall lean:** "strong yes, I'd hire her tomorrow" · **Supported by their evidence?** Yes for ownership. Part of the stated reasoning is "great culture fit" and "reminded me of me", which are struck and carry no weight.
**Opinions to turn into evidence:**
- "super easy to talk to" -> ask: "What did she explain or ask that showed clear communication?"
- Mentoring claim -> ask: "What did she do in the intern program: selection, code review, a curriculum? Did any intern go on to a full-time role?"
**Other observations (not scored):** None.
**Bias check:**
- Similar-to-me: "reminded me of me at my first startup".
- Halo risk: "great culture fit!!" appears before any evidence and may lift the overall lean.
- Possibly anchored: "Marcus and I already chatted and we agree". Give Jordan's view less weight in any disagreement.

## 2. Struck from the record
| Interviewer | What was written | Why it was struck | Suggested action |
|---|---|---|---|
| Marcus | "she's probably early 40s, wondering if she'd be ok with startup pace vs big bank" | Age guess and age-based doubt. Age 40+ is federally protected. | Remove from the doc. Have a private word with Marcus. If pace matters, define the behavior (for example "ships small PRs daily") and ask every candidate the same question. |
| Priya | "strong accent, communication might be an issue with the team?" | Accent is a national origin proxy. Her own notes say she "talked through complexity fine", so the content she communicated was clear. | Remove from the doc. Have a private word with Priya. Score communication on content only. |
| Jordan | "great culture fit!!" / "reminded me of me at my first startup" | Vague fit language and similar-to-me bias | Replace with a named behavior the team needs and score it with evidence, or drop it. |
| Jordan | "mentioned she has two kids so might need flexible hours, fine with us but flagging" | Family status, sex and pregnancy proxy. It is not job-related. | Remove from the doc. Have a private word with Jordan. Ask every candidate about availability the same way, as a job requirement. |

General information, not legal advice. State laws may add protected traits.

## 3. Verify before any offer
None noted.

## 4. Debrief memo
**Roll-up**
| Competency | Marcus | Priya | Jordan | Lowest | Spread |
|---|---|---|---|---|---|
| Backend design for money-moving systems (must) | 4 | n/a | n/a | 4 | single owner |
| Coding quality (must) | n/a | 3 | n/a | 3 | single owner |
| Ownership (must) | n/a | n/a | 4 | 4 | single owner |
| Mentoring (nice) | n/a | n/a | NE | NE | single owner |

**Strongest evidence for:**
- She designed idempotent payouts with the key (invoice_id, attempt_group) and explained why a retry must not double pay. She handled a worker dying mid-batch with a lease and a reconciler, without a hint. (Marcus)
- Unassigned reconciliation mismatch: she traced it to an FX rounding issue, fixed it, then wrote the runbook and set up the alert. (Jordan)
- She asked clarifying questions before coding, found the comma-amount bug herself once pointed to the sample file, and explained the complexity. (Priya)

**Strongest evidence against:**
- She wrote no tests until asked, at the senior level. (Priya)
- She missed string amounts with commas until prompted to run the sample file. In AP automation, parsing money is the core of the job. (Priya)
- She did not raise observability on the payment scheduler until asked. (Marcus)

**Disagreements to resolve:** No score spread of 2 or more, because each competency has a single owner. There is a split in overall lean: Priya leans no while Marcus and Jordan say strong yes. Priya's written evidence supports a 3. Her lean rests on speed compared with Ken and on the struck accent comment. The question that settles it, for Priya: "Is there a line in your notes showing coding below the senior bar, other than needing a prompt for tests?" If needing a prompt for tests is the gap, the team should agree whether writing tests unprompted is a hard senior requirement. If it is, apply it to every candidate.

**Gaps:**
- No must-have is NE.
- Mentoring (nice-to-have) is NE. Close it with a reference question: "Describe what Dana did in the intern program, and one intern she developed."
- Ownership rests on a self-reported story, and the interviewer is possibly anchored. Close it with a reference question: "Tell me about the FX rounding reconciliation fix. Who found it, and who wrote the runbook and the alert?"

**If hired, watch in the first 90 days:**
1. Does she write tests unprompted in her first PRs, especially for money parsing and edge cases?
2. Does she add monitoring and alerts to payment paths she builds, without being asked?
3. Does mentoring show up in practice, for example in her code review comments for junior engineers?

**Evidence supports:** Hire (rule 3: Marcus scored 4 on backend design and Jordan scored 4 on ownership, and no must-have is below 3; Jordan's score is possibly anchored, but Marcus's 4 alone meets the rule).
**Decision (made by hiring manager, not named in notes):** ________ **Date:** ________ **Reason if different from the evidence summary:** ________

## 5. Debrief agenda (20 minutes)
1. (2 min) Confirm everyone's written scores are final. No changes after this point without new evidence. Marcus confirms his notes were written before he spoke with Jordan.
2. (10 min) Disagreements only, most junior interviewer speaks first, hiring manager last. Priya's lean no against her written 3 on coding quality. Agree whether writing tests unprompted is a hard senior requirement for every candidate.
3. (5 min) Gaps: decide follow-up call vs reference check vs decide now. Recommended: reference checks on the reconciliation story and the intern program.
4. (3 min) The bet question to each interviewer: "Would you bet your own next 12 months on working with Dana?" A "probably" is a no. Then the hiring manager decides.

---
Made with the free Interview Scorecard skill by Ruzora · ruzora.com/skills
