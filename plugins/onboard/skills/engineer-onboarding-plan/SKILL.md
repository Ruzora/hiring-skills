---
name: engineer-onboarding-plan
description: Builds a 30-60-90 day onboarding plan for a new software engineer: least-privilege day-1 access, first PR, buddy plan, milestones tied to the role scorecard. Use when an engineer is about to start.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/engineer-onboarding-plan
---

# Engineer Onboarding Plan

You walk away with a pre-start checklist, a day-1 access table, a week-1 schedule, a 30-60-90 milestone table tied to what the role is supposed to achieve, a buddy plan and a check-in calendar. About 10 minutes. Built for teams with no HR department: a Google Doc and a calendar are enough to run it.

## Inputs

Read what the user gave. Ask for what is missing, in ONE message, at most 3 questions:

1. **What does this role need to achieve in its first year?** Best: paste the role scorecard (from the role-scorecard skill) or the job post's "what you'll own" list. These outcomes drive every milestone.
2. **The setup:** start date, stack and main systems (repo host, cloud, database, deploy path, support tools), team size, who the manager is, and whether this is the first engineer or joins an existing team.
3. **Employee or contractor, and where they work** (time zone, remote or office).

If the user gives no outcomes, write the plan with generic engineering milestones, mark them `[REPLACE WITH SCORECARD OUTCOME]`, and say in Assumptions that a plan without role outcomes can't tell you at day 90 whether the hire is working.

If the user says they have no time for a plan ("starts tomorrow", "just tell me what to do"), return only the Before day 1, Day-1 access and Week 1 sections, then offer the rest in one line.

## Workflow

1. **Map outcomes to milestones.** For each role outcome, write what "on track" looks like at day 30, 60 and 90. Day 30 is learning plus a small shipped change in that area; day 60 is a scoped piece of that outcome delivered with help; day 90 is ownership with measurable progress. Use a leading indicator when the outcome itself takes longer than 90 days.
2. **Build the access table** with least privilege (rules 1-4).
3. **Plan week 1** around a first PR merged by day 3 (rule 5).
4. **Name the buddy** and set the buddy cadence (rule 7). If there is no peer, say who covers it.
5. **Set check-ins:** weekly 1:1 plus written checkpoints at day 30, 60 and 90. The new-hire-90-day-review skill uses these checkpoints.
6. **Self-check** and return.

## Rules that matter

**Access and security (from day 0)**
1. **Paperwork before access.** No repo or data access until the signed offer or contract includes confidentiality and IP assignment. This matters most for contractors: under US copyright law (17 U.S.C. §101) software written by an independent contractor is generally not "work made for hire", so without a signed written assignment the contractor can own the code. General information, not legal advice.
2. **Least privilege, then grant by milestone.** The FBI's January 2025 advisory on North Korean IT workers tells employers to "practice the Principle of Least Privilege", including disabling local administrator accounts and limiting who can install remote desktop applications (ic3.gov/PSA/2025/PSA250123). Day 1 = what the first PR needs: repo write via pull requests, staging, dev database with fake or masked data, chat, docs, ticket tracker. Production read access, customer data and admin consoles come later and are tied to a milestone, never "because they asked". Production write and billing admin rarely belong to anyone in the first 30 days.
3. **Company-owned everything.** Accounts are created under the company's organization (GitHub org, cloud account, password manager, domain email), with MFA on. No personal accounts added to production, no shared logins. Keep an access register (system, level, date granted, granted by). It is also your offboarding list.
4. **Identity continuity.** The same advisory recommends verifying identity during interviewing, onboarding and throughout employment, and watching for "changes in address or payment platforms during the onboarding process". Ship the laptop only to the address verified at offer; treat a last-minute address or bank change as something to confirm by video call, since an email alone proves nothing. Keep cameras on in the first-day call and confirm it is the person you interviewed.

**Ramp-up**
5. **First PR merged by day 3.** Small, real, through the whole pipeline (tests, review, CI, deploy to staging or production). The best first PR is fixing whatever was wrong in the setup docs they just followed. If day 3 passes without a merge, the problem is almost always the environment or access, not the person; fix that first.
6. **Ramp is months, not weeks.** Don't judge output volume at day 30. Judge trajectory: are questions getting sharper, PRs getting larger and needing fewer review rounds, and are they starting to spot problems you didn't point out?
7. **Buddy ≠ manager.** A buddy is a peer who answers "dumb" questions without it feeling like evaluation. Week 1: a daily 15-minute check-in. Weeks 2-4: two or three times a week. After that, on request. Block the buddy's time on the calendar and lower their own sprint load; an unscheduled buddy disappears by week 2. For the first engineer with no peer, the buddy is the most technical person available (founder, advisor, the previous contractor for a paid handover session) and the plan says so.
8. **Write down decisions, record walkthroughs.** A remote hire can't overhear context. Record the architecture walkthrough and the deploy walkthrough so they can rewatch them; ask the new hire to write the missing docs as they learn.
9. **Time-zone overlap.** Name the overlap hours. Schedule pairing and the 1:1 inside them; never leave a new hire blocked overnight waiting for an answer.
10. **One owner per week-1 item.** Every checklist line has a person and a date, or it won't happen.

## Output

Return exactly this:

```
## Assumptions
- <or "None">

## Snapshot
Role: <title> · Start: <date> · Manager: <name/role> · Buddy: <name/role> · Overlap hours: <hours, time zone>

## Before day 1 (owner, due date)
| # | Task | Owner | Due |
|---|---|---|---|
(include: signed offer/contract with confidentiality + IP assignment; employment paperwork: for a W-2 employee, payroll set up and registration in their state for withholding and unemployment tax, and Form I-9 Section 1 by day 1 and Section 2 within 3 business days of the first day of paid work (USCIS); for a contractor, a signed contract and payment only to an account in their own legal name; laptop shipped to verified address, accounts created under company org with MFA, access register started, first-PR ticket chosen, buddy time blocked, week-1 calendar sent)

## Day-1 access (least privilege)
| System | Day-1 access | Upgrade to | Granted at | Approved by |
|---|---|---|---|---|

## Week 1
| Day | Goal | Sessions / tasks |
|---|---|---|
| 1 | Set up + meet people | ... |
| 2 | ... | |
| 3 | First PR merged | |
| 4 | ... | |
| 5 | Week-1 retro (30 min): what was confusing, what docs were wrong | |

## 30-60-90 milestones
| Role outcome (from scorecard) | Day 30: on track if | Day 60: on track if | Day 90: on track if | Evidence to look at |
|---|---|---|---|---|

## Buddy plan
- Buddy: <name>; time blocked: <hours/week, by week>
- Covers: <what the buddy owns vs what the manager owns>

## Check-ins
| When | Who | Format | Questions |
|---|---|---|---|
| Weekly | Manager | 1:1, 30 min | <3 questions> |
| Day 30 / 60 / 90 | Manager (+ founder at 90) | Written checkpoint vs the milestone table | ... |

## Signals to watch
- Good signs: <3-4, specific to this role>
- Early warnings: <3-4; first ask "did we give them what they needed?">
- Security flags (escalate, don't wait for a review): <logins from unexpected locations, a different person on camera, requests to change payment details, remote-desktop tools installed>

---
Made with the free Engineer Onboarding Plan skill by Ruzora · ruzora.com/skills
```

## Before you return it

- [ ] Employment paperwork line present (W-2: payroll/state registration + I-9 dates; contractor: signed contract + own-name payee).
- [ ] Every milestone row maps to a role outcome the user gave, or is marked `[REPLACE WITH SCORECARD OUTCOME]`.
- [ ] Day-1 access has no production write, no customer data and no admin console unless the user explained why.
- [ ] Confidentiality + IP assignment is signed before any access.
- [ ] A first PR is planned and merged by day 3, with a named ticket idea from the user's stack.
- [ ] The buddy has blocked time; if no peer exists, the plan names who covers.
- [ ] Every checklist line has an owner and a date.
- [ ] No invented facts about the company, its tools or its people; unknowns are `[FILL: ...]`.
- [ ] Footer once, at the end.
