---
name: new-hire-90-day-review
description: Turns notes on a new engineer into a fair, documented day 30/60/90 review separating ramp-up issues from capability gaps, with options and a script. Use when checking if a new hire is working out.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/new-hire-90-day-review
---

# New-Hire 90-Day Review

You walk away with an evidence-based review of one new engineer at day 30, 60 or 90: what was expected, what happened, which gaps are the company's to fix and which are the hire's, the options with their trade-offs, a script for the conversation and a written summary for the file. About 15 minutes. You decide; this review organizes the evidence.

## Inputs

Read what the user gave. Ask for what is missing, in ONE message, at most 3 questions:

1. **What was the hire expected to achieve, and was it written down before they started?** (Role scorecard, onboarding plan, offer letter, or a kickoff message. Paste it.)
2. **What actually happened, with examples and dates?** PRs, shipped work, missed commitments, review feedback, things others said. Facts, not impressions.
3. **What support did they get?** Buddy, docs, access, time with the manager, changes in priorities or team.

Also note (without asking, unless relevant to the input): employee or contractor, US state or country, day count. Never ask for or record health details, family situation, age, religion or similar. If the user mentions medical leave, a disability, pregnancy, an accommodation request, a complaint the hire made, or a similar protected matter, do not weigh it in the review; follow rule 9.

## Workflow

1. **Rebuild the expectations.** List the outcomes and when each was due. If nothing was written before the hire started, say so at the top: a fair review can't call something a capability gap if it was never asked for. In that case the main recommendation is to write expectations now and review again in 30 days.
2. **Fill the evidence table**, one row per expectation, using only the user's facts. Mark rows with no evidence as "No evidence", not as failures.
3. **Run the support check** (rule 2) before judging the person.
4. **Classify every gap** as Ramp-up, Capability, Conduct/reliability, or Role mismatch (rule 3).
5. **Lay out the options** (rule 6) with what each requires. Point to the one the evidence best supports and say how confident the evidence is. The human decides.
6. **Write the conversation script and the file summary.**
7. **If parting ways is an option on the table, add the part-ways checklist** (rule 10).
8. **Self-check** and return.

## Rules that matter

1. **Trajectory beats level until day 90.** At day 30 almost nobody is fully productive. Compare week 2 with week 8: PR size and review rounds, quality of questions, how often the same feedback repeats, whether they now catch problems on their own.
2. **Support check first.** Before any capability call, answer: Did they have working access and a dev environment in week 1? A buddy with real time? Clear written priorities that didn't change more than once? Docs, or someone who answered questions within hours? If two or more answers are "no", the gaps are presumed Ramp-up (the company's to fix) until support is fixed and given time to work, usually 30 days.
3. **Four kinds of gap, four different responses.**
   - **Ramp-up:** missing context, access, docs or clear priorities. Fix the environment.
   - **Capability:** the same gap shows up across different tasks after support was given and feedback was clear, and doesn't shrink. Coaching with a dated plan, then decide.
   - **Conduct/reliability:** missed commitments without warning, misrepresenting work, ignoring agreed process. Name it directly, one clear warning in writing; dishonesty about work is serious from the first instance.
   - **Role mismatch:** good engineer, wrong job (hired for backend, needed for frontend; hired to execute, needed to define). Consider reshaping the role before anything else.
4. **Early-warning signals worth a conversation:** the same review comment needed three or more times; PRs that sit for days without a question asked; status that is "almost done" for over a week; blockers hidden until the deadline; needing step-by-step instructions after day 60 for work at the level they were hired for. Each one is a question to ask, not a verdict.
5. **Integrity and security signals go to a different track.** A different person on camera than the one interviewed, logins from unexpected countries, refusing video, requests to send pay to a third party: these are identity questions (the FBI's January 2025 advisory and the July 2026 multi-country alert on North Korean IT workers list them), not performance questions. Escalate to an identity check now; don't fold them into a review.
6. **Options, from least to most drastic:**
   - **On track:** confirm, set the next 90 days.
   - **On track with focused support:** name 1-3 gaps, what the company will change, what the hire will show, by a date (usually 30 days).
   - **Reset:** expectations were unclear or the role changed. Rewrite expectations in writing, restart the clock.
   - **Part ways:** only when the gap is Capability or Conduct, support was given (rule 2), the hire was told clearly with examples, and it didn't change in a reasonable window. Serious misconduct is the exception to the window.
   State which option the evidence supports and what would change the call. Never write "fire" or "terminate" as the conclusion; write the options and let the user decide.
7. **Write it like a stranger will read it.** Observable facts with dates and examples ("PR #212 merged after 4 review rounds on 10/14, same null-handling issue as #198") beat adjectives ("sloppy", "not senior", "bad attitude", "not a culture fit"). If the user only has impressions, say the review can't support a decision yet and list what evidence to collect.
8. **Same bar for everyone.** Check that the standard applied is the one written in the scorecard and the one applied to peers at the same level. Flag any expectation that appeared only after problems started.
9. **Protected matters stay out, and timing matters.** Never cite or weigh medical leave, disability, pregnancy, age, religion, national origin, caregiving, an accommodation request, or a complaint the hire made (about pay, safety, harassment or discrimination). If any of these happened recently and an adverse decision is on the table, tell the user to talk to an employment lawyer first, because acting close to a protected event can look like retaliation even when it isn't. Name the right frame for the company's size: federal FMLA (and "leave interference") applies only to employers with 50+ employees and employees with 12+ months and 1,250 hours of service (US DOL), so for most early-stage hires the relevant risks are retaliation and discrimination under the ADA (15+ employees), pregnancy laws and state law, which often covers smaller employers. General information, not legal advice.
10. **Part-ways path (general information, not legal advice).** Check your local law and your contract; at-will rules vary. Montana, for example, requires good cause to discharge an employee who has finished the probationary period (Mont. Code Ann. §39-2-904). Final-pay timing also varies by state (California makes wages due immediately on discharge, Cal. Labor Code §201). Offer letters that promise a "probation period" or "permanent" role can change the picture; reread them. Contractors end under their contract's notice terms. Mechanics either way: decide before the meeting, keep it short, revoke access during or right after the meeting, recover devices, move account ownership, and write it down.

## Output

Return exactly this:

```
## Review: <name or initials>, <role>, day <N> of 90
Prepared for <manager>. General information, not legal advice. The decision is yours.

## Assumptions and gaps in the evidence
- <including "expectations were / were not written before start">

## Expectations used
| # | Expectation | Source (scorecard / plan / message) | Due by |
|---|---|---|---|

## Evidence
| # | Expectation | What happened (facts, dates) | Status: Ahead / On track / Behind / No evidence |
|---|---|---|---|

## Support check
| Question | Answer from input | Note |
|---|---|---|
| Working access + environment in week 1 | | |
| Buddy with real time | | |
| Written priorities, stable | | |
| Fast answers / docs | | |

## Gap diagnosis
| Gap | Type: Ramp-up / Capability / Conduct / Role mismatch | Why | Company action | Hire action |
|---|---|---|---|---|

## Trajectory
<3-5 sentences comparing early weeks with recent weeks.>

## Options
| Option | When it fits | What it requires next | Risk |
|---|---|---|---|
**What the evidence supports:** <option> (confidence: low / medium / high, and why). **What would change this:** <specific evidence>.

## Conversation script (20-30 min)
1. Open: <one line, purpose of the meeting>
2. Ask first: <2 questions for their view>
3. Share: <the 2-3 key facts, neutral wording>
4. Agree: <next steps, dates, what support changes>
5. Close: <confirm you'll send a written summary today>

## Written summary for the file (send to the hire after the meeting)
<120-200 words: date, expectations, evidence, agreed next steps and dates. Facts only.>

## Part-ways checklist  (include only if Part ways is an option)
- [ ] Reread offer letter / contract for probation, notice and severance terms
- [ ] Check your state's at-will and final-pay rules; talk to counsel if any protected event in rule 9 applies
- [ ] Decision made before the meeting; script ready; meeting under 15 minutes
- [ ] Access revoked during or right after (use the access register); devices recovered; account ownership moved
- [ ] Written record of the reasons, matching what was told to the hire

---
Made with the free New-Hire 90-Day Review skill by Ruzora · ruzora.com/skills
```

## Before you return it

- [ ] Every fact came from the user; impressions are labeled as impressions or left out.
- [ ] The support check ran before any gap was called Capability.
- [ ] No protected matter (rule 9) is used as evidence; if one was mentioned, the review says to leave it out and, if an adverse decision is possible, to talk to counsel first.
- [ ] Identity or security signals, if any, are routed to an identity check, not scored.
- [ ] The output presents options and states what the evidence supports; it never states a firing decision as made.
- [ ] The file summary contains no adjectives about character, only observable facts and agreed dates.
- [ ] Part-ways section includes "check your local law and your contract; at-will rules vary".
- [ ] Day counts and dates are computed from the start date (day 90 = start date + 90 days), and every proposed date falls before the next checkpoint.
- [ ] The review is addressed to the person who asked for it.
- [ ] Footer once, at the end, never inside the summary sent to the hire.
