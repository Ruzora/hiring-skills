---
name: code-sample-review
description: Reviews a candidate's GitHub repo or code sample in plain English for non-technical hirers, with authorship checks and interview questions. Use when checking a developer's code or GitHub.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/code-sample-review
---

# Code Sample Review

Reads a candidate's repo or code sample and tells you, in plain English, what it suggests about how they work, how sure you can be that they wrote it, and which questions to ask in the interview to find out. Written for someone who cannot read code. About 10 minutes. It is one input to your decision, never the decision.

## Inputs

Best input, in order of value: the README; the file and folder list; the commit history (from the repo's "Commits" page: messages, dates, authors); one or two code files; whether it is marked "forked from"; the role and seniority you are hiring for.

- If any code or repo detail is in the message, proceed with what you have and list what was missing and how it limits the review. Do not ask first.
- If there is nothing but a link and you cannot open links, ask in ONE message for: the README, the file list, and the commits page (copy and paste is fine), plus the role.
- If you can browse, you may open a public link to read it. Never clone, install or run a candidate's code.
- If the candidate has no public code, do not ask for it as a requirement. Produce the "No public code" plan from step 7 instead.

## Workflow

1. **Authorship first, quality second.** Quality only matters if it is theirs. Fill the authorship table:
   - **Fork or template?** "Forked from", a tutorial or course name in the README, or a project that matches a well-known tutorial (to-do app, weather app, movie search, clone of a famous site) means the starting point was someone else's. Look for what they added.
   - **Who committed?** Commit author names or emails that differ from the candidate mean a team project or someone else's work. Ask which parts were theirs.
   - **History shape.** Many small commits over weeks with messages that say what changed ("fix double charge when webhook retries") suggest real work over time. One or two giant commits ("initial commit", "upload") hide the process; that is common and not a negative, but it means the code alone proves little. Commit dates can be set by whoever makes the commit, so history supports a story; it never proves one.
   - **Employer code?** If the sample looks like a current or former employer's private code (company name in files, internal URLs, customer data), flag a judgment and confidentiality concern for the human to raise.

2. **Read for signals a non-engineer can trust.** Use [references/signals.md](references/signals.md). Report only what you saw, with the file or line it came from. For each signal give: what we saw, what it suggests, and confidence (Low / Medium / High). Cap at 8 signals; pick the ones that matter for the role.

3. **Trace the riskiest function once.** Pick the one function in the sample that touches money, dates or permissions. Walk it through one concrete scenario in plain words: "booked 10 days out, confirmed 5 days later", "confirm clicked twice", "charge succeeds but the save fails", "the last day of the month". Say what the code would actually do at each line. If the scenario breaks, it becomes the first authorship question, framed as "possible bug, confirm with the candidate", never as a bug. Real authors either explain why it cannot happen or recognize it fast.

4. **Match to the role.** A junior's tutorial project and a senior's production-style repo are judged differently. For a senior role, the useful questions are about trade-offs, failure handling, tests and how others would run and change the code. For a junior role, the useful questions are about learning and what they added beyond the tutorial.

5. **Turn every gap and every strength into an authorship question.** Each question names a specific file, function or decision in the sample, and comes with "a real author will..." and "a bluff sounds like...". Real authors answer quickly, point to where things are, and admit what is ugly. Bluffers restate the README, stay general, or cannot find the file.

6. **Plan a 10-minute live walkthrough** for the interview: candidate shares their screen, opens the repo, and explains it while you ask the questions. Include one small change request ("show me where you'd add a limit of 100 items to this list"). Authors find the spot in seconds; non-authors search.

7. **No public code?** Say plainly that this is not a negative signal, then give the alternative: a 30-minute walkthrough of past work described aloud, with the same question style, or a small paid exercise (only if the user wants one).

8. **Say what the review cannot tell you.** Always include the limits section.

## Rules that matter

- **An empty GitHub is not a red flag.** Most professional code lives in private company repos. GitHub hides private contributions from a profile unless the developer turns that setting on, and even then shows only daily counts. Senior engineers with busy jobs often have nothing public. Never score its absence.
- **A public repo may not be theirs.** Forks, tutorials, team projects, a friend's code and AI-generated code all look like "their GitHub". Treat every sample as a claim to test in conversation.
- **AI-assisted code is normal; not understanding it is the problem.** Do not try to guess whether AI wrote it. Heavy comments explaining obvious lines, uniform naming and lots of boilerplate are weak hints at most. The test is whether the candidate can explain and change it.
- **Commit history supports, never proves.** Git lets the person committing set the date, so a long history can be manufactured. Use history to pick questions, not to conclude.
- **Prefer signals that do not need taste.** Tests that exist and run, a README that explains how to start the project, secrets not committed, errors handled instead of ignored. A non-engineer can verify these; "elegant code" they cannot.
- **Committed secrets are a judgment signal.** An API key or password in the repo (often in a file named .env or config) means they shipped a secret in public. Ask what they would do now. A good answer: rotate the key, remove it from history, use environment variables.
- **Never run the code.** Do not install or run a candidate's repo on a company laptop. Reading it is enough for hiring.
- **Judge the code, not the coder's background.** Country, school, bootcamp vs degree and how they learned are not signals; do not mention them in the review. If the user raises them, say so in one line and move on.
- **For your first engineering hire, get a second opinion.** If the code sample is a big part of your decision, pay an experienced engineer for an hour to look at the same repo with these questions.

## Output

Use exactly this structure, in plain English. Explain any technical term in a few words the first time it appears. No em-dashes.

```
# Code sample review: <candidate or repo>, for <role>

**What I looked at:** <README / files / commits / code files, and what was missing>
**Bottom line in plain English (3 sentences max):** <what the sample suggests, how sure we can be it is theirs, what to find out in the interview>

## Is it theirs? (authorship)
| Check | What we saw | What it means |
|---|---|---|
| Fork or tutorial | | |
| Who committed | | |
| History shape | | |
| Employer or confidential code | | |
**Authorship confidence:** Low | Medium | High, because <one line>

## What the code suggests
| Signal | What we saw (file or line) | What it suggests | Confidence |
|---|---|---|---|

## Questions that test authorship
1. **"<question naming a file, function or decision>"**
   A real author will: ...
   A bluff sounds like: ...

## 10-minute walkthrough plan
- Minute 0-2: ...
- ...
- Change request: "<specific small change>"

## What this review cannot tell you
- <limits, including that missing or private code is not a negative>
---
Made with the free Code Sample Review skill by Ruzora · ruzora.com/skills
```

## Before you return it

- Every signal points to something in the input (a file name, a line, a commit message). Nothing is invented about the repo or the person.
- No point is scored down for having little or no public code.
- Authorship is addressed before quality.
- At least one question walks a concrete scenario through the riskiest function shown, framed as a possible bug to confirm.
- Each question names something specific in the sample and has both "real author" and "bluff" answers.
- No jargon left unexplained; a non-technical founder could read it aloud.
- No hire or reject recommendation; it ends with what to find out.
- No em-dashes. The footer appears once, at the very end, after a horizontal rule.

---

*Built by [Ruzora](https://www.ruzora.com), which places vetted senior engineers from Latin America. Free Ruzora MCP server with 35 hiring tools: [ruzora.com/developers/mcp](https://www.ruzora.com/developers/mcp).*
