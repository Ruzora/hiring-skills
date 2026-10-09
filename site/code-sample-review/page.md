---
title: Evaluate a GitHub Profile Before Hiring (Free AI Skill)
description: A free AI skill that helps non-technical hirers evaluate a GitHub profile or code sample, check authorship and get the interview questions to ask.
target_query: evaluate github profile
category: screen
related_blog: how-to-audit-code-a-contractor-wrote
cta: /how-we-vet
author: Roberto Espinoza
updated: 2026-10-04
---

# Evaluate a GitHub profile or code sample before you hire

Code Sample Review is a free AI skill that helps you evaluate a GitHub profile or code sample before hiring, even if you can't read code. It checks whether the work is the candidate's own, traces the riskiest function for possible bugs, and turns each finding into an interview question with what a real author and a bluffer would say.

Most advice on reviewing a developer's GitHub assumes you can read code. This skill assumes you cannot, and never counts an empty profile against anyone.

## What you get

- **A three-sentence bottom line** you can read aloud to a cofounder.
- **An authorship table:** fork or tutorial, who committed, history shape, and any sign of an employer's confidential code.
- **Up to eight code signals,** each with the file it came from, what it suggests and a confidence level, with jargon explained.
- **Authorship questions** naming a specific file or decision, each with "a real author will..." and "a bluff sounds like...".
- **A 10-minute screen-share plan** with one small change request that authors find in seconds.
- **The limits** of what a code sample can tell you.

## Sample output

From a real run. The input: a non-technical founder hiring a first engineer pasted a candidate's README, file list, eight commits, part of a payments file and a public `.env` file, and asked whether 60 contributions a year "seems low".

> | Who committed | Almost all commits shown are by "Kit Brannagan". One is "Merge pull request #3 from jpwellsby-example/calendar-ui", with the work itself, "calendar month view + drag to reschedule" (Feb 11), by J.P. Wellsby. | A second person built the calendar screen and Kit accepted it into the project. That part is not his. Ask who J.P. is and which other parts, if any, they touched. |

> 1. **"In confirmBooking in deposits.js, walk me through this: a customer books 10 days ahead, and the salon confirms 8 days later, 2 days before the appointment. What happens to the deposit?"**
>    What the code appears to do: it counts the days left until the appointment (2), so it takes the "less than 7 days" path and tries to collect the hold placed when the customer booked. But that hold is now 8 days old, and the README says holds expire after 7 days. If so, the collection fails and the booking is marked `deposit_failed`. [...] This is a possible bug to confirm with the candidate, not a verdict.

> - The ~60 contributions last year is not a negative. Most professional engineers do their real work in private company repos, which GitHub does not show on a profile by default. "Green squares every day" is a myth; plenty of strong senior engineers have almost none.

The same run also flagged a possible double charge if Confirm is clicked twice. A founder who cannot read JavaScript can still ask both questions and judge the answers.

## How it works

**Authorship before quality.** A public repo may be a fork, a tutorial, a team project or someone else's work. Quality only matters for the parts that are theirs, so forks, commit authors and history come first.

**History supports, never proves.** Git lets whoever makes a commit set its date, so a long, tidy history can be manufactured. The skill uses history to pick questions, not to reach conclusions.

**Absence is not a signal.** GitHub hides private contributions unless the developer turns that setting on, and even then shows only daily counts. Many strong senior engineers have almost nothing public because their work lives in company repos.

**Signals that need no taste.** Run instructions in the README, tests on the risky parts, errors handled, secrets kept out of the repo. A non-engineer can check all of these; "elegant code" they cannot, so the skill leaves it out.

**Trace one risky function.** The skill walks the function that touches money or dates through a concrete case (booked 10 days out, confirm clicked twice) and turns any break into a "possible bug" question. Country, school and bootcamp are never signals.

**AI-written code is fine; not understanding it is the problem.** The skill does not guess whether AI wrote the code. It writes questions that show whether the candidate can explain and change it.

**Never run it.** Reading the code is enough. Do not install or run it on a company laptop.

### How this compares

A static code review checklist is written for engineers reviewing a teammate's pull request. Asking a chatbot cold to "review this GitHub" usually returns a technical critique you cannot act on, and often treats a sparse profile as a warning sign. This skill writes for the person who cannot read code, starts with "is it theirs?", and hands you questions to ask.

## How to install and use

**Claude.ai:** download the skill's .zip from this page and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then paste the README, file list, commits and a code file or two.

**Claude Code:** run `/plugin marketplace add Remutopia/ruzora-skills`, then `/plugin install hire-screen@ruzora-hiring`. Ask it to review a candidate's code sample and the skill loads on its own.

**Any other AI (ChatGPT, Gemini, Copilot):** copy the prompt version from this page, paste it as your first message, then paste what you copied from the repo.

## Frequently asked questions

### How do I evaluate a developer's GitHub profile if I'm not technical?
Check authorship first: is it a fork, who made the commits, does the history show work over weeks. Then look for checkable signals like run instructions, tests and committed secrets. Turn every one into a question and ask the candidate to walk you through the repo on a screen share.

### Is an empty GitHub profile a red flag?
No. Most professional code lives in private company repos, and GitHub hides private contributions by default. Ask for a walkthrough of past work instead.

### How can I tell if a candidate actually wrote the code?
Ask them to open the repo on a screen share, explain a specific function and make a small change. Authors find the file in seconds and admit what is ugly. Bluffers repeat the README.

### Is it free?
Yes. No signup and no email gate. Use it, change it and share it under CC-BY-4.0.

---

**Need someone who has already been tested on real code?** See [how we vet engineers](/how-we-vet): 5-stage vetting, including live coding, system design and AI-tool proficiency. Or [request a shortlist](/request-shortlist) and get a vetted shortlist within 72 hours. To check code a contractor already delivered, read [how to audit code a contractor wrote](/blog/how-to-audit-code-a-contractor-wrote).
