---
title: Recruiter Outreach Template for Engineers (Free AI Skill)
description: A free AI skill that writes honest 3-touch outreach to senior engineers, plus a referral ask for your network. No fake urgency, no made-up flattery.
target_query: recruiter outreach template
category: attract
related_blog: do-referral-hires-perform-better
cta: /request-shortlist
author: Roberto Espinoza
updated: 2026-10-04
---

# Recruiter outreach template for senior engineers, written per person

Engineer Outreach Messages is a free AI skill that writes a 3-touch outreach sequence to passive senior engineers, plus a referral ask for a founder's own network. A template gives everyone the same message. This skill writes from what you actually know about each person, refuses to fake it when you know nothing, and puts the pay range in the first message.

## What you get

For a batch of 3-10 people, in about 10 minutes:

- **A candidate table** rating each personalization line STRONG, WEAK or NONE, with a send, fill-detail-first or skip call.
- **Touch 1 per person** (email under 120 words, plus a two-sentence LinkedIn version), then shared templates for touch 2 (day 4-5) and touch 3 (day 10-14).
- **A referral kit:** an email to your network, a forwardable blurb, and a LinkedIn post.
- **A tracking sheet** with a do-not-contact column, and sending rules for this batch.

## Sample output

The input came from a fictional Series A founder hiring a Staff Mobile Engineer. He listed four people, one of whom he knew nothing about ("can you just make something up that sounds personal"), and wanted to say "the role closes Friday" to speed things up. Part of what the skill returned:

**From the assumptions it flagged:**

- **I left out "the role closes Friday."** Unless you really have a hard deadline, that is fake urgency, and senior engineers see through it fast. It also clashes with how slow this channel is: YC's guide expects two or three emails before a reply. If something real is driving the date (for example, you plan to make an offer to another finalist next week), say that plainly in touch 2 instead.
- **Raj: I did not make anything up.** A made-up personal detail is the fastest way to lose a senior engineer, and it can hurt the friend who sent you the list. His touch 1 has a `[SPECIFIC: ...]` slot. Find one real thing about his work before sending, or skip him.

**Touch 1 for the candidate whose talk the founder had watched:**

> **Subject:** Owning offline sync for a React Native app with 9k daily drivers
>
> Hi Dana,
>
> I watched your React Native meetup talk on YouTube about offline sync with SQLite and conflict resolution. That's the core problem in the role I'm hiring for.
>
> I'm CEO of Harborline: dispatch and route software for regional moving companies, 22 people, $14M Series A closed in June. Our Staff Mobile Engineer will own our React Native driver app, which is offline-first with about 9k daily active drivers. Range is $200-235k plus equity, remote in the US or Canada with 4 hours of overlap with Central time.
>
> Would you be open to a 20-minute call? No prep needed.
>
> Tomás Reyes
> CEO, Harborline
> [FILL: your email]

## How it works

**The offer goes in the first message.** One true line about the person, what they'd own, the stack, stage, pay range, remote rule and a small ask: a 20-minute call, no prep. According to LinkedIn data (2023) reported by Search Engine Journal, 91% of US respondents say a salary range affects whether they apply, so a missing range gets flagged.

**Personalization has to be real.** The skill only uses details you give it. If you found someone through a search, the message says so. If you know nothing, it leaves a slot to fill and recommends skipping that person.

**No fake urgency.** "Closing Friday", "only two seats" and fake "Re:" subject lines get cut unless they are true.

**Three touches, then stop.** Touch 2 adds one new fact (a real problem, the team, something you shipped) instead of "just bumping this". Touch 3 closes the loop. Y Combinator's guide to hiring a first engineer expects two or three emails before a reply and warns that cold outreach can take up to six months to produce a hire.

**Opt-outs are permanent.** A "no" goes on the do-not-contact list, and you don't switch channels to try again. For candidates in the EU or UK, the first message says where you found their details and links a short privacy notice, because Article 14 of the GDPR requires that information, plus who you are, why you hold their data and their right to object, no later than first contact.

**The founder signs it,** in plain text, sent to the candidate's personal email or LinkedIn. Never their current work inbox, where their employer can read it.

**Ask your network first.** The same YC guide calls your personal network "the most important source by far" for early hires. The referral ask names a specific kind of person, because "know anyone looking?" gets silence.

### How this compares

A static template is identical for every recipient, and recipients can tell. A chatbot asked cold will often write "I was impressed by your work" about someone it knows nothing about, and add the fake deadline if asked. This skill refuses both.

## How to install and use

**Claude.ai:** download the skill's .zip and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then say "write outreach to these engineers" and paste the role plus your notes on each person.

**Claude Code:** run `/plugin marketplace add Remutopia/ruzora-skills`, then `/plugin install hire-attract@ruzora-hiring`.

**Any other AI:** copy the prompt version of the skill, paste it as your first message, then add your role and candidate notes.

For each person, include how you found them and one real thing about their work.

## Frequently asked questions

**How long should a recruiting message to a software engineer be?**
Under 120 words for the first message: enough for the role, the range and one real line about them.

**How many times should I follow up with a candidate who doesn't reply?**
Twice, so three messages total, spaced about 4-5 days and then 10-14 days after the first. Each follow-up adds something new. After the third, stop.

**Should I include salary in a cold recruiting message?**
Yes. Senior engineers use it to decide whether a call is worth their time.

**Is it legal to cold email candidates in Europe?**
It can be, with care. If you collected their details yourself, GDPR Article 14 requires telling them, at first contact at the latest, who you are, where you got their details, why, and that they can object. The skill adds a source line plus a privacy-notice link. This is general information, not legal advice.

**What's a good referral request message?**
One that asks for a specific kind of person and includes a short blurb with the pay range that your contact can forward.

## Not getting replies?

Outreach is slow by design. If you need senior engineers sooner, we send a vetted shortlist within 72 hours of senior engineers in Latin America, working US hours. [Request a shortlist](/request-shortlist) or [browse the engineers](/engineers).

Wondering whether referral hires are worth the effort? Read [do referral hires perform better](/blog/do-referral-hires-perform-better).
