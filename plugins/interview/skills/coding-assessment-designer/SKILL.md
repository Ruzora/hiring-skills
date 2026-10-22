---
name: coding-assessment-designer
description: Designs an AI-resilient coding test for a developer role (seeded-bug review, extend-a-codebase or paid trial) with a hidden rubric and follow-up. Use when you need a coding test or take-home.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/coding-assessment-designer
---

# Coding Assessment Designer

A ready-to-send coding assessment for one role: the right format for your situation, the candidate brief, the task material (including a seeded-bug code sample in your stack when that format fits), a hidden grading rubric written before any submission arrives, and the follow-up conversation that tests whether the candidate understands what they submitted. About 15 minutes to generate; candidates spend at most 2-3 hours unless you pay them.

## Inputs

Ask, in ONE message, only what is missing (max 3):
1. **Role, level and stack** (language, framework, database), plus one sentence on what the person will build in their first months.
2. **AI rule for the test:** allowed, allowed with disclosure, or not allowed. If the user has no view, default to **allowed with disclosure** and say why in one line (a ban you cannot enforce in a take-home only penalizes the honest candidates).
3. **Constraints:** is anyone technical available to grade and run a 30-45 minute follow-up? Can you pay for a trial? Are most candidates currently employed?

**The stack is the one thing you never assume** when the format needs code: the task material is written in it, and code in the wrong language is useless. If the user has not named a language and framework, ask for them (together with any other missing item, in the same single message) and wait before writing task material. Everything else can be a stated assumption. If the user already described the role, stack and current test, do not ask; proceed with stated assumptions.

## Workflow

1. **Diagnose the current test, if there is one.** Name its failure mode plainly. The common ones: greenfield "build X from scratch" (an AI assistant produces a complete, clean solution, so the submissions all look alike), uncapped "should take a weekend" (filters out employed and caregiving candidates, and seniors decline), algorithm puzzles for a product role (tests recall, not the job), and grading the code alone with no conversation.

2. **Pick the format** with this rule, and say why in two sentences:
   - **Seeded-bug review** (default for mid and senior): the candidate reviews a short pull request (a proposed code change, 80-150 lines in the user's stack) with 5 planted problems, then discusses it live. Tests reading code and judgment, which is most of the job. 45-60 minutes live, or 45 minutes async plus a 30-minute discussion.
   - **Extend an existing small codebase** (when you need to see them build): a 300-800 line repo in the user's stack with conventions and tests; the task is to add one feature and fix one failing test. Capped at 2-3 hours, then a 30-45 minute follow-up where you change a requirement.
   - **Paid trial** (for a first engineer, a final-stage tie-breaker, or any task over the 3-hour cap): 1-3 days of paid, well-scoped work with written terms. See [references/paid-trial-terms.md](references/paid-trial-terms.md).
   - If nobody technical can grade or run the follow-up, say so plainly: recommend paying an outside engineer for 2-3 hours per finalist rather than grading it yourself, because the follow-up conversation is half the signal.

3. **Set the time cap.** Unpaid work: a hard cap of 2-3 hours, stated in the brief, and graded within that cap. Pilot the task on a current engineer or the outside reviewer first: if they need more than about two thirds of the cap, cut scope. Anything over the 3-hour cap is paid. Always offer a live alternative (the same task, done on a call) for candidates who cannot spare the time.

4. **Write the task material.** Use [references/formats.md](references/formats.md).
   - For seeded-bug review: write the actual code in the user's stack, about the user's domain, with exactly 5 seeded issues across the categories in the reference (one must be a business-rule bug that is only visible if the candidate reads the brief), plus the hidden answer key.
   - For extend-a-codebase: write the repo outline (files, what each does, the conventions), the feature request, the failing test to fix, and what the grader checks.

5. **Write the hidden rubric before anyone submits.** 4-5 criteria, each scored 1-4 with behavioral anchors. The follow-up conversation carries at least 40% of the weight. Keep the key and rubric private; give candidates the criteria headings only.

6. **Write the follow-up conversation** (30-45 minutes): walkthrough, a "why this and not that" question on a real choice in their submission, a live requirement change, a scale or failure question, and the AI-use question matching the policy. Exact sentences.

7. **Write the candidate brief** (paste-ready email): what to do, time cap, AI rule, the criteria headings, how the follow-up works, pay if any, how to ask for an accommodation, and when they will hear back.

## Rules that matter

- **The conversation is the test; the submission is the ticket to it.** If a candidate cannot explain a choice in their own submission, or cannot make a small change to it live, score Understanding a 1 and treat the submission as unverified evidence, however clean the code looks.
- **No format is AI-proof.** Resilient formats test what an assistant does not supply on its own: knowing which of five problems matters most, fitting into existing conventions, asking about an unclear requirement, and explaining trade-offs live. Grade those.
- **Prioritization beats count in a review.** A candidate who finds 3 issues and ranks the data-loss bug first beats one who lists 9 style nits and misses it.
- **Seed one ambiguity on purpose** (an unclear requirement in the brief). Strong candidates ask about it or state the assumption they made. Silent guessing is a signal.
- **Rubric first, submissions second.** A rubric written after reading submissions drifts toward whichever one you saw first.
- **Respect the candidate's time.** A 2-3 hour cap, stated and honored, a live alternative, and feedback of at least a few sentences to everyone who submits. Never use unpaid candidate work in your product.
- **Paid trials need written terms before work starts:** scope, hours, rate, who owns the work, confidentiality, no production or customer-data access, AI rule, and decision date. Code written by an independent contractor is generally not "work made for hire" under US copyright law (17 U.S.C. § 101), so the paperwork needs a written IP assignment if you might keep the work.
- **Accommodations:** if a candidate asks for extra time or a different format for a disability-related reason, consider it seriously. For job demonstrations, the EEOC says the employer must provide a reasonable accommodation that does not cause undue hardship, or let the applicant describe how they would do the task.
- **Human decides.** The rubric produces evidence and scores; a person makes the call.

## Output

Return exactly this structure:

```
# Coding assessment: <Role>, <level>, <stack>
Assumptions: <one line each, only if any>

## What's wrong with the current test
<2-4 sentences, or "No current test." >

## Format and why
<format, live/async, length, AI rule; 2-3 sentences of reasoning>

## Candidate brief (paste-ready)
<email: task, time cap, AI rule, criteria headings, follow-up, pay if any, accommodation line, response date>

## Task material
<For seeded-bug review: the full code block of the pull request with a short PR description, then:>
### Answer key (private)
| # | Line(s) | Issue | Category | Severity | What a strong candidate says |
<For extend-a-codebase: repo outline, feature request, failing test, grader checklist>

## Hidden rubric (private)
| Criterion | Weight | 4 | 3 | 2 | 1 |
<4-5 rows; Understanding (from the follow-up) >= 40% combined with the other conversation criteria>

## Follow-up conversation (30-45 min)
1. "<exact question>" (listen for: ...)
...
Live change: "<the requirement change>" (listen for: ...)
AI question: "<matching the policy>" (listen for: ...)

## Grader notes
- Pilot result needed: <who pilots, cap check>
- Red flags: <3-5 specific to this task>
- Score each criterion with evidence before discussing with anyone. The hiring decision belongs to a person, using this as evidence.

## Paid trial terms (only if the format is a paid trial)
<checklist from references/paid-trial-terms.md filled in>

General information, not legal advice. US rules as of 2026.

---
Made with the free Coding Assessment Designer skill by Ruzora · ruzora.com/skills
```

## Before you return it

- Plain style: no em-dashes and no negative-parallelism constructions (a denial followed by "but"); periods and commas instead.
- The format fits the inputs: seeded-bug review unless there is a reason to build or to run a paid trial, and the reason is stated.
- Unpaid time is capped at 3 hours or less, stated in the brief, and a live alternative is offered; anything longer is paid.
- Task code is written in the stack the user named; if they named none, you asked instead of writing code.
- Seeded-bug code is real code in the user's stack and domain, compiles in principle, and has exactly 5 issues that match the answer key line by line, including one business-rule bug tied to the brief.
- The rubric has behavioral anchors and was written without reference to any submission; the follow-up carries at least 40% of the weight.
- The follow-up includes a live requirement change and an AI-use question matching the policy.
- The brief contains no answer key, no rubric anchors and no footer.
- No hire/reject verdict. Nothing invented about the company; assumptions listed.

---

*Built by [Ruzora](https://www.ruzora.com), which places vetted senior engineers from Latin America. Free Ruzora MCP server with 35 hiring tools: [ruzora.com/developers/mcp](https://www.ruzora.com/developers/mcp).*
