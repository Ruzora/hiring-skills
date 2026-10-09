## Assumptions
- **Your two questions first.**
  - **Admin on Render and Stripe on day one: no.** Day 1 gets what her first PR needs and nothing more. For Stripe, that means test-mode/sandbox keys. She can see Render through GitHub-triggered staging deploys. She still gets to look around soon, with each grant tied to a milestone (see the access table). Live Stripe view-only comes in week 2. Render production logs come in week 3. Deploy and rollback rights come at day 60, when she takes on-call. Render workspace admin waits until day 90. Stripe Owner/Admin, bank and payout settings stay with you. Telling her this isn't distrust. It's the standard least-privilege practice; the FBI's January 2025 advisory on remote IT workers says to "practice the Principle of Least Privilege". Say it to her plainly. A senior engineer will usually respect it.
  - **Laptop to her parents' place in Ohio: not as asked.** Ship it to the Raleigh address you verified at offer. A last-minute change of shipping address during onboarding is one of the patterns that same advisory tells employers to watch for. It is very likely innocent here. Still, an email request proves nothing either way. Options, best first: (a) ship to Raleigh now, so it arrives before she leaves; (b) if it truly must go to Ohio, you start a camera-on video call with her, using contact details from her application rather than the email asking for the change. Confirm on that call that she's the person you interviewed and get the address from her there. Ship signature-required and write the address change in the access register.
- Nov 3, 2026 is a **Tuesday**, not a Monday. I used Tue Nov 3 as day 1, which puts the day-5 retro on Mon Nov 9. If you meant Mon Nov 2, move every date one day earlier.
- Time zones: Priya is in Raleigh (ET, UTC-5 after Nov 1), you're in Denver (MT, UTC-7) and the contractor is in Portugal (WET, UTC+0). I assumed the contractor works roughly 9:00-18:00 Lisbon time. **Three-way overlap: 11:00-13:00 ET (9:00-11:00 MT, 16:00-18:00 Lisbon).** You and Priya overlap 11:00-17:00 ET.
- Buddy: there's no full-time peer. The buddy is your Portugal contractor (`[FILL: contractor name]`), paid for his onboarding hours out of or on top of his ~10h/week. He leaves at the end of December, so every walkthrough he gives gets recorded, and you take over as buddy from January. You're also her manager, which is why the January handoff needs extra care (see Buddy plan).
- First, check the contractor's own contract. If it has no signed IP assignment, he may own much of the code Priya is about to inherit (17 U.S.C. §101: contractor work is generally not "work made for hire"). Fix that before he leaves. General information, not legal advice.
- These tools aren't named in your message, so they're `[FILL]`: domain email provider, password manager, support inbox tool, payroll provider, whether a separate staging environment exists on Render, whether CI runs on PRs today, and whether written notes from the August outages exist.
- Two outcome targets are mine and are marked `[FILL]`: the failed-payment ticket target and the deploy frequency. Change them to whatever you'd call success.

## Snapshot
Role: Senior Full-Stack Engineer (first full-time engineer) · Start: Tue Nov 3, 2026 · Manager: You (CEO) · Buddy: `[FILL: contractor name]` (Portugal contractor) through Dec 31, then you · Overlap hours: 11:00-13:00 ET three-way; 11:00-17:00 ET with you (9:00-15:00 MT)

## Before day 1 (owner, due date)
| # | Task | Owner | Due |
|---|---|---|---|
| 1 | Signed offer letter plus a confidentiality and invention/IP assignment agreement. No GitHub, Render, Stripe or data access until this is signed | You | Fri Oct 16 |
| 2 | Confirm the contractor's existing contract has confidentiality and IP assignment. If it doesn't, get a signed assignment covering past and future work | You | Fri Oct 16 |
| 3 | W-2 payroll set up for Priya in `[FILL: payroll provider]`. If she's your first North Carolina employee, register with the NC Department of Revenue (withholding) and NC Division of Employment Security (unemployment tax), and file NC new-hire reporting | You | Fri Oct 23 |
| 4 | Form I-9: Priya completes Section 1 by day 1 (Tue Nov 3). You complete Section 2 within 3 business days of her first day of paid work (by **Fri Nov 6**). She's remote, so either use an authorized representative near Raleigh or, if you're enrolled in E-Verify, the DHS remote document-review procedure | You + Priya | Sec 1: Nov 3 · Sec 2: Nov 6 |
| 5 | Ship laptop to the **Raleigh address verified at offer**, signature required (see Assumptions about Ohio). Set it up with a standard user account, local admin disabled or held by you, and no remote-desktop tools installed | You | Ships by Tue Oct 27 |
| 6 | Create her accounts under company orgs, with MFA enforced: domain email `[FILL]`, password manager `[FILL]`, GitHub org, Slack, Notion, Linear. No personal accounts, no shared logins | You | Fri Oct 30 |
| 7 | Start the access register (Notion page with columns: system, level, date granted, granted by). It's also your offboarding list. Add the contractor's current access while you're in there | You | Fri Oct 30 |
| 8 | Turn on GitHub branch protection for `main`: PR required, 1 review, CI must pass (if CI exists `[FILL]`) | Contractor | Fri Oct 30 |
| 9 | Dev database seed with fake teachers, students, lessons and invoices, so she never needs production data to run the app locally (skip if a seed already exists) | Contractor | Fri Oct 30 |
| 10 | Record two walkthroughs (Loom or similar, 30-45 min each) and save them in Notion: (a) architecture covering Next.js, the Express API, Postgres, Stripe webhooks and Sentry; (b) deploy path, i.e. how code gets from GitHub to Render and how to roll back | Contractor (you join for the "why" behind decisions) | Fri Oct 30 |
| 11 | Pick the first-PR ticket and put it in Linear. Default: "Fix whatever was wrong in the setup README while following it." Backup: a small, real fix from the Sentry backlog on the scheduling side, so it's off the payments path | You + contractor | Wed Oct 28 |
| 12 | Book the contractor's onboarding hours: daily 15-min buddy check-in in week 1 plus 3 pairing blocks (see Buddy plan). Agree on pay for any hours beyond his 10h/week | You | Fri Oct 23 |
| 13 | Export a redacted sample of ~10 recent failed-payment support tickets with teacher names and emails removed, for her day-2 reading | You | Fri Oct 30 |
| 14 | Send the week-1 calendar: day-1 call, team intros, buddy check-ins, walkthroughs, retro, and the weekly 1:1 (Tuesdays 11:00 ET / 9:00 MT) | You | Wed Oct 28 |
| 15 | Tell the team (Slack post) who Priya is, what she'll own and when to say hello. Ask 2-3 people who handle support to give her 15 minutes in week 1 | You | Fri Oct 30 |

## Day-1 access (least privilege)
| System | Day-1 access | Upgrade to | Granted at | Approved by |
|---|---|---|---|---|
| Domain email `[FILL]`, Slack, Notion, Linear | Member (normal user) | Unchanged | Day 1 | You |
| Password manager `[FILL]` | Her own vault plus a shared "Engineering – dev/test" vault (Stripe test keys, dev env vars) | Production secrets vault | Day 60, when she becomes on-call primary | You |
| GitHub org | Member, write through PRs only; `main` protected | Maintainer on the main repos (branch protection still on) | Day 90 | You |
| Laptop | Standard user; no local admin; no remote-desktop tools | Unchanged. Tool installs go through you or MDM `[FILL]` | n/a | You |
| Postgres | Local/dev database with fake seed data only | Read-only role on production (read replica if you have one), for invoicing analysis and incident debugging. **No production write**: schema and data changes go through migrations in the deploy pipeline | Day ~30 (Dec 3), after the day-30 checkpoint | You |
| Render | No direct login if staging auto-deploys from GitHub; otherwise the lowest role on the staging service only `[FILL: confirm Render role names on your plan]` | (1) Read production logs and metrics → (2) deploy and roll back production → (3) workspace admin | (1) Day ~14 (Nov 16), on-call shadowing starts · (2) Day 60 (Jan 4), on-call primary · (3) Day 90 (Feb 1). **Billing stays with you** | You |
| Stripe | **Test mode / sandbox only** (test API keys in the dev vault). No live dashboard | (1) Live dashboard **View only** → (2) Developer role (webhooks, API keys) for the retry work. Owner/Administrator, bank accounts and payouts stay with you | (1) Day ~8 (Nov 12), after the invoicing walkthrough · (2) Day ~45 (Dec 18), when the first retry slice is ready to ship | You |
| Sentry | Member on the staging/dev environment (if errors are split by environment; otherwise wait) | Production project, alerts routed to her | Day ~14 (Nov 16), on-call shadowing | You |
| Support inbox `[FILL]` | None. She gets the redacted ticket sample instead | Read access, so she can tag failed-payment tickets and measure the baseline | Day ~14 (Nov 16) | You |

## Week 1
| Day | Goal | Sessions / tasks |
|---|---|---|
| 1 · Tue Nov 3 | Set up + meet people | 11:00 ET welcome call with you, **cameras on**: confirm she's the person you interviewed, go over the 30-60-90 plan and the access timeline, and explain why access is staged · Laptop and account setup · Follow the setup README and keep a list of everything that's wrong or missing (that becomes her first PR) · 12:30 ET 15-min buddy check-in with the contractor · 2-3 short team intros |
| 2 · Wed Nov 4 | Local env running; understand the product as a teacher | Watch the recorded architecture walkthrough · On staging, act as a teacher: create a schedule, book lessons, send an invoice, pay with a Stripe test card, fail a payment with a decline test card · Read the 10 redacted failed-payment tickets · Open the first PR · Buddy check-in · 15 min with whoever handles support |
| 3 · Thu Nov 5 | **First PR merged** | First PR (README/setup fixes) reviewed by the contractor, CI green, merged and deployed through the normal Render path. Watch the recorded deploy walkthrough first · 11:00 ET pairing with the contractor (60 min) on the deploy and rollback path · Buddy check-in · If it hasn't merged by end of day, fix the environment or access problem before anything else |
| 4 · Fri Nov 6 | Map the invoicing + payments core | I-9 Section 2 completed (deadline today) · 11:00 ET pairing with the contractor (90 min, recorded): the invoicing flow and Stripe webhook handling in test mode · Read whatever notes exist on the 3 August outages `[FILL]`, or get the story from you in 20 min · Pick up a second small Linear ticket · Buddy check-in |
| 5 · Mon Nov 9 | Week-1 retro (30 min): what was confusing, what docs were wrong | 11:00 ET retro with you + contractor · She writes up a one-page "what I learned / what's missing in our docs" in Notion · Agree on weeks 2-4: Stripe live view-only (Nov 12), Render production logs + Sentry production + on-call shadowing (Nov 16), first test PR on the payments core · Buddy check-in |

## 30-60-90 milestones
| Role outcome (from scorecard) | Day 30 (Dec 3): on track if | Day 60 (Jan 4): on track if | Day 90 (Feb 1): on track if | Evidence to look at |
|---|---|---|---|---|
| 1. Rebuild invoicing so failed Stripe payments get retried and the ~40 support tickets/month stop | She has mapped every failed-payment path in the code and in Stripe (webhooks handled and missed, what the teacher and the parent see). The ticket baseline is measured and tagged by cause. She has shipped one small change in this area (e.g. a Sentry alert or logging on failed-payment webhooks) | A written retry design (Stripe's built-in retry/dunning settings vs custom logic, plus teacher and parent notifications) that you've approved. The first slice is shipped with the contractor's or your help, behind a flag if needed | Retry flow live for all teachers (or a clear majority behind the flag). She owns it end to end. Failed-payment tickets are trending down from ~40/month, target `[FILL: e.g. under 15/month]` by month 6. Leading indicator: % of failed payments recovered automatically | Support ticket tags per month · Stripe recovered-payments data · Linear tickets and merged PRs · the design doc |
| 2. Test suite from ~nothing to covering the payments + scheduling core, enabling daily deploys | Tests run in CI on every PR (set up if missing). Her first tests on the payments core are merged | An agreed test plan listing the critical paths (invoice creation, webhook handling, retry logic, booking create/cancel/conflict). The payments critical paths are covered, and merges are blocked by failing tests | Payments + scheduling critical paths covered. Deploys at `[FILL: target, e.g. daily]` frequency with no deploy-caused production incident in the last 30 days | CI history · list of covered paths vs plan · Render deploy log · incident log |
| 3. Own on-call and production reliability (3 outages in August) | She has shadowed on-call since ~Nov 16 and understands the 3 August outages and their root causes. She has shipped one reliability fix or alert | She's on-call primary with you as backup. Runbooks exist for the top 3 failure modes, including the August ones. She has taken over the contractor's production knowledge before he leaves Dec 31 | She owns on-call and alerting. No repeat of an August root cause. Every incident gets a short written review within 48h. With a single engineer, also decide what happens on her days off | Sentry alert history · runbooks in Notion · incident reviews · uptime/outage count vs August |
| 4. Ready to help interview engineer #2 by spring | (Too early, so leading indicator) Her week-1 and day-30 notes on onboarding gaps feed the plan for engineer #2 | Has reviewed and edited the engineer #2 role scorecard with you | Has drafted a practical technical exercise drawn from the real codebase and run one mock interview with you | Scorecard draft · exercise doc · your notes from the mock interview |

## Buddy plan
- Buddy: `[FILL: contractor name]` (Portugal), Nov 3 – Dec 31; then you. Time blocked: **Week 1:** 15-min daily check-in at 12:30 ET plus 3 pairing blocks (Thu 60 min, Fri 90 min, one more in week 2) ≈ 4h. **Weeks 2-4:** 15-min check-in 3×/week plus 1 pairing hour/week ≈ 2h/week. **December:** on request, plus two recorded handover sessions on whatever only he knows (`[FILL: e.g. Stripe webhook quirks, Render config, cron jobs]`), done by Fri Dec 18. Reduce his other tasks by the same hours, or pay for them on top of the 10h.
- Covers: the buddy answers "how does this work / where is this / why is it like this", reviews her early PRs, and pairs on deploys and payments. You, as manager, own priorities, the milestones, access grants, the weekly 1:1 and the day-30/60/90 checkpoints. From January you're both, so keep the two apart: use a separate short "ask me anything technical" slot (2×/week, 15 min) that is explicitly not evaluation.

## Check-ins
| When | Who | Format | Questions |
|---|---|---|---|
| Weekly (Tue 11:00 ET / 9:00 MT) | You | 1:1, 30 min, video | What blocked you this week, and how long did it take to unblock? · What's the most confusing part of the system right now? · What should I take off your plate or decide for you? |
| Day 30 (Thu Dec 3) / Day 60 (Mon Jan 4) / Day 90 (Mon Feb 1) | You (you're also the founder, so add a trusted advisor or board member `[FILL]` at day 90 if you want a second view) | Written checkpoint against the milestone table. She writes her self-assessment first, you add yours, then you discuss for 45 min | For each outcome row: on track / at risk / off track, and why · What did we fail to give you (access, context, time)? · What should change in the next 30 days? · Day 30: confirm the production DB read grant · Day 60: confirm the on-call primary and Render deploy/rollback grants · Day 90: confirm Render admin and GitHub maintainer, set months 4-6 goals |

## Signals to watch
- Good signs:
  - The day-1 README PR turns into a habit: she fixes docs and adds tests without being asked.
  - By week 3-4 her questions move from "where is X" to "why does the failed-payment webhook do Y, and should it?"
  - She spots a reliability risk you didn't point out, e.g. an unhandled Stripe event or a missing alert.
  - Her PRs get larger and need fewer review rounds, and the retry design comes with a way to measure it (ticket tags, recovery rate).
- Early warnings (first ask "did we give them what they needed?"):
  - No merged PR by day 3, or still fighting the local env in week 2. Check the seed data, README and access first.
  - She's waiting overnight for answers from the contractor. Move those questions into the 11:00-13:00 ET overlap or the Notion docs.
  - The contractor's knowledge isn't transferring before Dec 31 (handover sessions slipping, no runbooks).
  - She's pulled into support firefighting so often that the invoicing work doesn't move by day 60.
- Security flags (escalate, don't wait for a review): logins from unexpected locations or overseas IPs; someone other than the person you interviewed on camera, or a camera that's always "broken"; requests to change bank or payroll details, or to send equipment to a new address, made by email or chat only (confirm on a video call you start, using contact details you already have); remote-desktop or screen-sharing tools installed on the laptop; requests for production or Stripe admin access before the milestone with no concrete task behind them.

---
Made with the free Engineer Onboarding Plan skill by Ruzora · ruzora.com/skills
