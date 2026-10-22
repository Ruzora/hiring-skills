---
title: 90 Day Review Template for New Engineers (Free AI Skill)
description: A free AI skill that turns notes on a new engineer into a fair 90 day review: evidence, ramp-up vs capability gaps, options and a meeting script.
target_query: 90 day review template
category: onboard
related_blog: software-engineer-performance-review-template
cta: /engineers
author: Roberto Espinoza
updated: 2026-10-04
---

# 90 day review template for a new engineer that is fair and documented

New-Hire 90-Day Review is a free AI skill that turns a manager's notes on a new engineer into a fair, documented review at day 30, 60 or 90. It checks whether the company gave the hire what they needed before calling anything a capability gap, keeps protected matters out of the record, and lays out options. You make the decision.

## What you get

About 15 minutes, one review per hire:

- **Expectations and evidence tables:** what was asked, where it was written down, what happened with dates, and a status per row.
- **A support check:** access, environment, buddy, stable priorities, fast answers.
- **A gap diagnosis:** each gap labeled Ramp-up, Capability, Conduct or Role mismatch, with the company's action and the hire's.
- **Options with trade-offs** and a statement of which one the evidence supports, how confident it is, and what would change the call.
- **A 20-30 minute conversation script** and a written summary to send the hire the same day.
- **A part-ways checklist,** only when that option is genuinely on the table.

## Sample output

The input was a frustrated note from a fictional 26-person software company about a backend engineer at day 58: "leaning toward letting him go, write it up so we have a paper trail". The notes also mentioned a broken setup, a buddy who left in week 3, a three-week reassignment, a week of medical leave and "not a culture fit, too quiet in standup". Part of what the skill returned:

**How it handled the medical leave:**

> **Excluded protected matter:** the mid-September week off for a medical procedure is **left out of this review entirely**. It isn't used as evidence and isn't used to adjust or excuse any result. Remove it from any performance notes too. It sits about 2-3 weeks before the "went quiet" incident and about 3 weeks before you started leaning toward letting him go. **If an adverse decision is on the table, talk to an employment lawyer first.** Acting close to medical leave can look like retaliation or disability discrimination even when it isn't. At 26 employees and under 12 months of service, federal FMLA doesn't apply (it needs 50+ employees, plus 12 months and 1,250 hours of service). The relevant risks are the ADA, which covers 15+ employees, and Ohio's civil-rights law, which covers much smaller employers.

**How it handled the impressions:**

| Gap | Type: Ramp-up / Capability / Conduct / Role mismatch | Why | Company action | Hire action |
|---|---|---|---|---|
| "Not senior enough," "culture fit," "quiet in standup" | Not a gap (impression) | Not tied to any written expectation or example | If Carla has specific examples, document them with dates. Otherwise drop them. | None |

## How it works

The order is what makes a review fair, so the skill enforces it.

**Expectations first.** If nothing was written down before the hire started, you can't fairly call a capability gap. Write them now and look again in 30 days.

**Support check before judgment.** Working access in week 1, a buddy with real time, stable written priorities, fast answers. Two or more "no" answers and the gaps are presumed ramp-up problems the company owns.

**Four kinds of gap.** Ramp-up gaps get fixed in the environment. Capability gaps repeat across tasks after clear feedback and support. Conduct gaps are named once, in writing. A role mismatch is a good engineer in the wrong job; reshape the role first.

**Trajectory over level.** Before day 90 the question is direction. The same review comment needed three or more times is worth a conversation, not a verdict.

**Facts a stranger could check.** Dated examples survive scrutiny; "not senior enough" and "not a culture fit" don't. The skill also checks the bar: a mid-level hire can't be judged against senior expectations that showed up later.

**Protected matters stay out.** Medical leave, disability, pregnancy, age, religion, an accommodation request or a complaint the hire made are never evidence. If one happened recently and an adverse decision is possible, talk to an employment lawyer first.

**Identity signals go elsewhere.** A different person on camera or logins from unexpected countries are identity questions (flagged by the FBI and a July 2026 multi-country alert on North Korean IT workers), not performance ones.

**The part-ways path, carefully.** Check your local law and your contract; at-will rules vary. Montana, for example, requires good cause to discharge an employee who has finished probation (Mont. Code Ann. §39-2-904), and California makes final wages due immediately on discharge (Labor Code §201). General information, not legal advice.

### How this compares

A review template gives you rating boxes. A chatbot asked cold to "write it up so we have a paper trail" tends to do exactly that, from your impressions. This skill writes the evidence, says where it is thin, and shows the company's part first.

## How to install and use

**Claude.ai:** download the skill's .zip and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then say "help me write a 60-day review for our new engineer" and paste your notes.

**Claude Code:** run `/plugin marketplace add Ruzora/hiring-skills`, then `/plugin install hire-onboard@ruzora-hiring`.

**Any other AI:** copy the prompt version of the skill, paste it as your first message, then add your notes.

Bring the written expectations, dated examples and the support the hire got. Leave out health details; the skill won't use them.

## Frequently asked questions

**What should a 90 day review for a new employee include?**
Expectations set at the start, dated evidence, the support given, gaps by type, dated next steps and a written summary for the employee.

**How do I know if a new engineer is underperforming or still ramping up?**
Check support first. If access, docs or a buddy were missing, it's likely ramp-up. A capability gap persists across tasks after support and feedback.

**Can I fire a new hire during the first 90 days?**
It depends on your state, your contract and your offer letter. At-will rules vary, and Montana, for one, limits discharge after probation. Protected events like medical leave raise the stakes. Talk to an employment lawyer before acting if any apply.

**What should I avoid writing in a new hire's review?**
Adjectives about character, "culture fit", and anything about health, leave, age, family or other protected matters. Write observable facts with dates.

## Hiring the next one?

If you'd rather lower the risk on your next hire, our engineers come with a 60-day replacement guarantee that starts on the engineer's first working day, and every one goes through 5-stage vetting, including live coding, system design and AI-tool proficiency. [Meet the engineers](/engineers) or [request a shortlist](/request-shortlist).

For running reviews after the first 90 days, see the [software engineer performance review template](/blog/software-engineer-performance-review-template).
