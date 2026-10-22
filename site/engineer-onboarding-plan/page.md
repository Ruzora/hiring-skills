---
title: 30 60 90 Day Plan for Software Engineer (Free AI Skill)
description: A free AI skill that builds a 30-60-90 day plan for a new software engineer: least-privilege access, a first PR by day 3, a buddy plan, scorecard milestones.
target_query: 30 60 90 day plan for software engineer
category: onboard
related_blog: onboarding-remote-engineers-first-90-days
cta: /engineers
author: Roberto Espinoza
updated: 2026-10-04
---

# 30 60 90 day plan for a software engineer, built from your role and your stack

Engineer Onboarding Plan is a free AI skill that builds a 30-60-90 day plan for a new software engineer. It ties every milestone to what the role must achieve, gets a first pull request merged by day 3, and starts access at least privilege, as the FBI advises employers of remote IT workers.

## What you get

A plan you can paste into a doc and run with a calendar, in about 10 minutes:

- **Before day 1:** a checklist with an owner and due date per line.
- **Day-1 access table:** each system, its day-1 level, and the milestone that upgrades it.
- **Week 1, day by day,** built around a first PR merged by day 3.
- **30-60-90 milestones,** one row per role outcome, with the evidence to check.
- **Buddy plan, check-ins and signals to watch,** including security signals to escalate at once.

## Sample output

The input came from a fictional 9-person seed startup whose first engineer starts next month. The founder pasted four scorecard outcomes and mentioned that the hire wanted admin on hosting and payments on day one. Part of what the skill returned:

**Day-1 access (excerpt):**

| System | Day-1 access | Upgrade to | Granted at | Approved by |
|---|---|---|---|---|
| Stripe | **Test mode / sandbox only** (test API keys in the dev vault). No live dashboard | (1) Live dashboard **View only** → (2) Developer role (webhooks, API keys) for the retry work. Owner/Administrator, bank accounts and payouts stay with you | (1) Day ~8 (Nov 12), after the invoicing walkthrough · (2) Day ~45 (Dec 18), when the first retry slice is ready to ship | You |
| Postgres | Local/dev database with fake seed data only | Read-only role on production (read replica if you have one), for invoicing analysis and incident debugging. **No production write**: schema and data changes go through migrations in the deploy pipeline | Day ~30 (Dec 3), after the day-30 checkpoint | You |

**One milestone row (excerpt):**

| Role outcome (from scorecard) | Day 30: on track if | Day 60: on track if | Day 90: on track if | Evidence to look at |
|---|---|---|---|---|
| 3. Own on-call and production reliability (3 outages in August) | She has shadowed on-call since ~Nov 16 and understands the 3 August outages and their root causes. She has shipped one reliability fix or alert | She's on-call primary with you as backup. Runbooks exist for the top 3 failure modes, including the August ones. She has taken over the contractor's production knowledge before he leaves Dec 31 | She owns on-call and alerting. No repeat of an August root cause. Every incident gets a short written review within 48h. With a single engineer, also decide what happens on her days off | Sentry alert history · runbooks in Notion · incident reviews · uptime/outage count vs August |

## How it works

**Milestones come from the role.** Each outcome on your role scorecard becomes a row: a small shipped change in that area by day 30, a scoped piece delivered with help by day 60, ownership with measurable progress by day 90. Without outcomes, a plan can't tell you at day 90 whether the hire is working.

**First PR merged by day 3.** Small, real, through the whole pipeline. The best one fixes whatever was wrong in the setup docs. No merge by day 3? Look at the environment before the person.

**Least privilege from day 0.** The FBI's January 2025 advisory on North Korean IT workers tells employers to practice the principle of least privilege, disable local admin accounts and limit who can install remote desktop tools. Day 1 gets what the first PR needs: the repo through pull requests, staging, a dev database with fake data. Production and customer data come at a milestone, never because someone asked. Every grant goes in an access register, which doubles as your offboarding list.

**Paperwork before access.** Confidentiality and IP assignment are signed before the first login. For contractors this matters more: under 17 U.S.C. §101, software written by an independent contractor generally isn't "work made for hire", so without a written assignment the contractor can own the code.

**Identity doesn't stop at the offer.** The same advisory says to watch for address or payment changes during onboarding. A last-minute laptop address change isn't treated as fraud; it gets confirmed on a video call before shipping.

**A buddy with real time.** A peer, not the manager. Daily 15 minutes in week 1, then two or three times a week, blocked on the calendar and taken off the buddy's sprint load. For a first engineer with no peer, the plan names who covers it.

**Trajectory over output.** At day 30, look for sharper questions and fewer review rounds, not ticket counts.

### How this compares

Generic templates skip access and security and give every role the same milestones. A chatbot asked cold tends to write "learn the codebase" in month one and "take ownership" in month three. This skill ties milestones to your outcomes and stack, and says no to day-1 admin with a reason.

## How to install and use

**Claude.ai:** download the skill's .zip and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then say "build an onboarding plan for our new engineer" and paste the details.

**Claude Code:** run `/plugin marketplace add Ruzora/hiring-skills`, then `/plugin install hire-onboard@ruzora-hiring`.

**Any other AI:** copy the prompt version of the skill, paste it as your first message, then add your details.

Bring the start date, stack, manager and the role's outcomes.

## Frequently asked questions

**What should a 30-60-90 day plan for a software engineer include?**
Access and setup before day 1, a first merged PR in week one, milestones per role outcome at 30, 60 and 90 days, a buddy, a check-in calendar and the evidence you'll use at each checkpoint.

**When should a new developer get production access?**
When a milestone needs it, not on day one. Start with what the first pull request needs and grant more as the work requires, logging every grant.

**How long does it take a new software engineer to be productive?**
Usually months. Judge the trend in the first 30 days, not the output.

**What does an onboarding buddy do for an engineer?**
Answers day-to-day questions and pairs on the first tasks. A peer, not the manager, with blocked time.

**Does this work for remote and contractor hires?**
Yes. It sets overlap hours for remote hires and requires a signed IP assignment before a contractor gets access.

## Want an engineer who has been onboarded before?

Senior engineers in Latin America, working US hours, with a 60-day replacement guarantee that starts on the engineer's first working day. [Meet the engineers](/engineers) or [request a shortlist](/request-shortlist).

For the full guide on running the first three months, read [onboarding remote engineers in the first 90 days](/blog/onboarding-remote-engineers-first-90-days).
