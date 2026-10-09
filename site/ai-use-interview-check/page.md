---
title: "How to Tell if a Candidate Is Using AI in an Interview"
description: "A free AI skill that sets your interview AI policy, gives fair signs of hidden AI help and an AI-fluency pairing exercise with a rubric."
target_query: how to tell if candidate is using ai in interview
category: interview
related_blog: using-ai-tools-in-a-coding-interview
cta: /how-we-vet
author: Roberto Espinoza
updated: 2026-10-04
---

# How to tell if a candidate is using AI in an interview, and what to do instead of guessing

AI-Use Interview Check is a free AI skill that helps engineering teams decide whether candidates may use AI in each interview stage, then redesigns the stages so that rule holds. It lists signs of hidden AI help taken from the answers and the work, never from the person, and gives you a 45-60 minute AI-fluency pairing exercise with a rubric.

## What you get

- **A stance per stage** (allowed, allowed with disclosure, or not allowed) and a keep/change/drop table for your current stages.
- **A paste-ready candidate policy note**, including the line that assistive technology is not "AI use" and how to ask for an accommodation.
- **Signals worth probing**, each paired with the follow-up that tests it, and a short list of things that are never evidence.
- **A script for when you suspect hidden help.**
- **An AI-fluency pairing exercise** in your stack with three planted traps, an observer checklist and an anchored rubric.

## Sample output

From a run on a fictional legal-tech startup whose CTO suspected a candidate because of long pauses, glances to the side and a heavy accent, and wanted to ban AI everywhere:

**About the candidate the CTO suspected:**

Not evidence:
- Long pause before every answer.
- Looking slightly to the right.
- A heavy accent, and the guess that he was reading a translation or ChatGPT.

These three must be removed from the record and must not be scored. A pause and a glance to the side are explained by thinking, a second monitor, notes or nerves, and an accent says nothing about AI use. Scoring them would track national origin and disability, which invites a discrimination claim.

What it shows: a strong system design answer on its own shows nothing either way. Vagueness about his own resume project is the one real content signal, and it is a reason to probe, not a verdict. It fits several explanations: hidden help, a project where his role was smaller than the resume suggests, a confidentiality concern, or a weak answer to a broad question. One vague answer, without a recorded follow-up ladder, cannot tell these apart.

**From the pairing-exercise rubric:**

| Criterion | Weight | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|
| Verification of AI output | 30% | Runs and tests every accepted change; finds the `toLikePattern` escaping bug; explains why the output was wrong | Tests most changes; finds the bug with a nudge from failing results | Tests occasionally; bug found only when pointed to | Accepts output untested; bug ships |

## How it works

Most "AI cheating" is a format problem: a ban on a take-home nobody supervises, or live puzzle questions an assistant answers in seconds. Watching the screen share doesn't fix it: some interview-assist tools market themselves as invisible to screen sharing (CNBC, March 2025). In a small 2025 survey by interviewing.io (67 respondents), 81% of FAANG interviewers said they suspected AI cheating.

So the skill starts with the rule, then fits the format to it:

- **If your team codes with AI every day, interview with it too,** in most stages, plus one stage that measures how well people steer it. A ban only makes sense where you can see it hold: a live conversation, a camera-on exercise, or in person. Never ban AI in an async take-home.
- **Keep one no-AI conversation** on the candidate's own past work. Hidden help shows up as answers that collapse at the second follow-up.
- **Use content signals only.** An answer to a slightly different question, identical structure on every answer, a story with no friction, or not being able to change their own code live. Accent, native language, eye movement, pauses, appearance and typing speed are not evidence. They track disability, culture and nerves, and scoring them invites a discrimination claim.
- **Don't let a black-box detector decide.** A false flag lands on a real person. If a tool applies AI to recorded video interviews for an Illinois-based role, the state's AI Video Interview Act requires notice, an explanation and consent first.
- **Score steering, not speed.** In the pairing exercise you plant the traps yourself: an ambiguous requirement, a subtle bug in "teammate's AI-generated" starter code, and a moment where AI is the wrong tool. The rubric weights verification of AI output highest.

Company practice is split, which is why a written rule matters. Shopify's CEO wrote in April 2025 that "reflexive AI usage is now a baseline expectation." Meta reportedly began piloting an AI-enabled coding interview in 2025. Amazon, according to Business Insider's reporting, tells candidates they can be disqualified for unauthorized generative AI use.

### How this compares

Most articles on this list body-language tells (eyes to the side, long pauses) that are unreliable and risky to act on. Asking a chatbot cold usually adds "use a proctoring tool". This skill gives you a policy, a format that enforces it, and probes instead of guesses.

## How to install and use

**Claude.ai:** download the skill's .zip and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then describe how your team uses AI and list your interview stages.

**Claude Code:** run `/plugin marketplace add Remutopia/ruzora-skills`, then `/plugin install hire-interview@ruzora-hiring`, and ask for an AI-use interview policy.

**Any other AI (ChatGPT, Gemini and others):** copy the prompt version of the skill from the repo, paste it as the first message, then describe your process.

## Frequently asked questions

### How can you tell if a candidate is using ChatGPT during an interview?

Not reliably from how they look or sound. Ask follow-ups on their own past work and their own code: "What exactly did you do?", "What went wrong?", "Change it so that...". Real experience gets more specific under follow-up. Hidden help usually doesn't.

### Should candidates be allowed to use AI in coding interviews?

If your engineers use AI on the job, allow it in most stages and assess how well they use it. Keep one live, no-AI conversation about their own work to check fundamentals.

### Are AI cheating detection tools reliable?

You usually can't inspect how they decide, and a false flag hurts a real person. Use them as a prompt to probe, never as the decision.

### Is looking away from the camera a sign of cheating?

No. People look away to think, to read notes, or for reasons tied to disability or culture. Keep it out of your notes.

## Want engineers already tested on AI-tool skill?

Ruzora's 5-stage vetting includes live coding, system design and AI-tool proficiency, and you get a vetted shortlist within 72 hours. See [how we vet](/how-we-vet) or [request a shortlist](/request-shortlist).

For more on the policy debate, read [using AI tools in a coding interview](/blog/using-ai-tools-in-a-coding-interview).
