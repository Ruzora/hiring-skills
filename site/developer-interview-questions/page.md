---
title: "Questions to Ask a Developer in an Interview (Non-Technical)"
description: "A free AI skill that writes developer interview questions for non-technical founders, with strong vs bluff answer guides and follow-up ladders."
target_query: questions to ask a developer in an interview
category: interview
related_blog: how-to-interview-a-developer-when-youre-not-technical
cta: /how-we-vet
author: Roberto Espinoza
updated: 2026-10-04
---

# Questions to ask a developer in an interview, when you can't read code

Developer Interview Questions is a free AI skill that builds a 60-minute interview kit for founders and managers who are not technical. For each of 8 questions tailored to your stack, you get what a strong answer sounds like, what a bluff sounds like, and 2-3 follow-ups that separate them. It also checks your own questions for legal problems.

## What you get

- 8 questions mapped to the 3-4 things this hire must be good at, written in your product's terms (no "what is REST" trivia).
- For each: why you ask it, strong and bluff markers you can hear without technical knowledge, and a follow-up ladder.
- A red-flag list for your company stage.
- Where an outside technical reviewer plugs in, a 1-4 scoring sheet, and a legal check of any questions you paste in.

## Sample output

From a run on a fictional 6-person health-tech startup whose CEO pasted her own draft questions:

**Q3. "Fernhill stores patient intake forms, so there's health information in our database. Tell me about a time you handled sensitive data like health, payment or personal data. What did you do to protect it, and which rules applied to it?"**
**Tests:** 2. Keeps patient data safe and gets through the security review
**Why you ask it:** You will be holding health information and a bigger clinic chain will review your security by Q2. This hire owns that.
**Strong answer sounds like:**
- Names a rule and what it changed in their work, for example "HIPAA, so we had to sign agreements with every vendor that touched the data and keep logs of who viewed records."
- Specific practices you can repeat back: only certain people could see the data, passwords and keys were kept out of the code, data was encrypted, there was a log of who accessed what, old data was deleted.
- Names a trade-off they accepted, for example "it made debugging slower because engineers couldn't look at real records."
- Has been through, or helped with, a security review or questionnaire before.
**Bluff sounds like:**
- "We used AWS, which is secure" or "the framework handles security."
- Cannot name any rule, or names HIPAA but cannot say what it changed day to day.
- No specific practices, only words like "best practices" and "industry standard."
- No downside to anything they did.
**Follow-up ladder:**
1. "Who could see that data, and who decided that?"
2. "Where were the passwords and API keys stored, and what went wrong or almost went wrong there?"
3. "If you joined Fernhill, what would you check first in our setup in week one, and what would you leave for later?"


**From the review of her own draft questions:**

| Your question | Keep / replace | Why | Use instead |
|---|---|---|---|
| "How many years of React do you have?" | Replace | Years measure time spent, not skill. Five years of copying the same pattern looks the same as five years of owning a product | Q1 and Q7: ask what they built with React and Next.js and why they made the choices they did |

## How it works

The skill rests on one idea: you can't judge the code, but you can judge depth. A person who built something gets more specific with each follow-up. A person repeating something they read gets vaguer, repeats themselves, or answers a slightly different question. So every question comes with a ladder that always moves the same way: what exactly did *you* do, what went wrong or what did it cost, and what would you change.

A few rules it applies that first-time interviewers usually miss:

- **Every real decision has a cost.** Ask what a choice cost them. "There was no downside" is a weak answer from anyone above junior.
- **"I" versus "we".** "We" is normal on a team. But if they still can't name their own piece after you ask directly, ownership scores a 1.
- **Failure stories carry the most signal.** A specific failure with a specific lesson beats any success story.
- **Confidence is not competence.** The sheet scores specifics, costs and ownership, not fluency.
- **Same questions, same order, scored within 15 minutes.** Structured interviews were the highest-ranked predictor of job performance in Sackett and colleagues' 2022 re-analysis in the Journal of Applied Psychology (validity about .42).

A non-technical interview cannot confirm technical skill, so the kit also says where a technical reviewer comes in.

### How this compares

A static question list leaves you alone with the answers. Asking a chatbot cold usually gets you technical questions you can't grade ("explain the event loop"). This skill writes the grading guide for a non-technical listener and catches illegal questions in your own draft.

## How to install and use

**Claude.ai:** download the skill's .zip and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then start a chat with something like "I'm interviewing a senior full-stack developer next week and I'm not technical."

**Claude Code:** run `/plugin marketplace add Ruzora/hiring-skills`, then `/plugin install hire-interview@ruzora-hiring`. Ask for an interview kit and describe the role.

**Any other AI (ChatGPT, Gemini and others):** copy the prompt version of the skill from the repo, paste it as the first message, then describe your role.

Paste any questions you already planned; it reviews them too.

## Frequently asked questions

### What questions should a non-technical founder ask a developer?

Ask about their own past work, not definitions. "Walk me through something you built that you're proud of. What part did you build yourself?" followed by "What went wrong?" and "What would you change?" tells you more than any trivia question, because you can hear whether the answers get more specific or more vague.

### How do I know if a developer is bluffing in an interview?

Watch for answers that stay at buzzword level after two follow-ups, a choice with "no downside", "we" with no "I" even when asked directly.

### What questions are illegal to ask a developer candidate?

In the US, don't ask about age or graduation year, family or plans for children, national origin or accent, religion, health or disability, or salary history where it's banned. Ask lawful versions instead, like "Are you legally authorized to work in the US?" This is general information, not legal advice; states add more rules.

### Can I hire an engineer without a technical person on the team?

Yes, but plan one outside check: a technical reviewer for 60-90 minutes on a code walkthrough or a short paid work sample.

## Want engineers already vetted for technical depth?

Ruzora runs 5-stage vetting, including live coding, system design and AI-tool proficiency, and sends a vetted shortlist within 72 hours. See [how we vet engineers](/how-we-vet) or [request a shortlist](/request-shortlist).

For the full how-to, read [how to interview a developer when you're not technical](/blog/how-to-interview-a-developer-when-youre-not-technical). Hiring an agency or freelancer for a project instead of an employee? Use [questions to ask an app developer before you hire](/blog/questions-to-ask-an-app-developer).
