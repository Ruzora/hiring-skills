---
name: role-scorecard
description: Turns a vague engineering hire into a role scorecard with mission, measurable 12-month outcomes, must-haves, competencies and an interview map. Use when defining a role before writing the job post.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/role-scorecard
---

# Role Scorecard

You walk away with a one-page scorecard for one engineering role: why it exists, what success looks like at month 12, what is truly required, how each requirement gets tested, and the wording traps removed. Everything later in hiring (job post, screening, interviews, the debrief, the 90-day review) is scored against it. About 10 minutes.

## Inputs

Read what the user gave. If any of these is missing AND would change the scorecard, ask in ONE message, max 3 questions:

1. **The problem.** What is broken, slow or missing today that this person fixes? (One example beats a list of technologies.)
2. **The setting.** Company stage, engineering team size, who the hire reports to, and whether anyone technical will review their work.
3. **Hard constraints.** Location or time-zone overlap, budget range, start date.

If the user only pasted a wish list ("rockstar full-stack dev, React, Node, AWS, ML a plus"), do not ask about the stack. Ask about the problem. If the user says "just draft it", proceed and list your assumptions at the top.

## Workflow

1. **Write the mission in one sentence, in business terms.** "Make checkout reliable enough that sales can promise 99.9% to enterprise buyers", not "Build and maintain backend services". If you cannot write it from the input, that is your first question.

2. **Write 3-5 outcomes for month 12.** Each one is a result a stranger could check on day 365, with a measure and a date. Then add one 90-day outcome so the first review has something to check.
   - Test each outcome: "Could two people disagree about whether this happened?" If yes, rewrite it.
   - Activities are not outcomes. "Write clean code" and "collaborate with product" become "Ship the billing rewrite to 100% of customers by month 6 with zero lost invoices".
   - If the user gave no numbers, write the outcome with a bracketed placeholder: "cut p95 API latency from [current] to [target]". Never invent the company's metrics.

3. **Run the unicorn check.** List the distinct specialties the outcomes need (for example backend, mobile, ML, infrastructure, design). More than two at senior depth means the role is two roles. Say so and offer either a split or a sequence ("hire for outcomes 1-3 now; outcome 4 is a later hire or a contractor").

4. **Set the level by scope, not years.** Use this ladder and pick one, with the reason:
   - **Junior:** well-defined tasks; needs review on most work.
   - **Mid:** owns features end to end once someone else has framed the problem.
   - **Senior:** takes an ambiguous problem to a shipped, maintained system; makes and explains trade-offs; unblocks others.
   - **Staff:** sets technical direction across teams or for the whole product.
   At a company with no other senior engineer, the hire must operate without a spec and without a reviewer. If the outcomes need that, the level is Senior at minimum, whatever the budget says. Flag budget/level mismatches plainly.

5. **Separate must-haves from nice-to-haves.** For each candidate requirement ask: "Would we turn away an otherwise excellent person who lacks this, if they could learn it in 90 days?" If no, it is a nice-to-have. Max 4 must-haves, each tied to a named outcome.

6. **Convert proxies into evidence.** Replace years, degrees and brand names with the thing they stand in for:
   - "5+ years of Python" becomes "has owned a Python service in production, including being on call for it".
   - "CS degree required" becomes the specific knowledge needed, or is removed.
   - "Ex-FAANG" becomes "has worked on a system with [the scale you actually have]".
   Put each removed proxy in the "Not required" list with one line on why.

7. **Write 4-6 competencies with evidence anchors.** For each: a strong signal and a weak signal, both observable in an interview or work sample. "Strong: walks through a past design decision, names the option they rejected and why. Weak: describes the system but cannot say why it was built that way."

8. **Map every competency and must-have to exactly one interview stage** (screen call, work sample, technical interview, reference check, founder conversation). Anything mapped to no stage is either dropped or gets a stage. Anything mapped to every stage gets owned by one.

9. **Write deal-breakers.** 2-4, job-related and observable ("cannot overlap 4 working hours with US Eastern", "cannot explain trade-offs in their own past work"). Never "culture fit": replace it with two named behaviors you will actually look for.

10. **Lint the language** with the table in Rules. List each flagged phrase and its replacement.

11. **List open questions** for the hiring manager: anything you assumed that a wrong guess would change.

## Rules that matter

- **Outcomes before skills.** A list of technologies tells you who to source, not who to hire. In practice, interviewers who score against outcomes argue about evidence, while interviewers who score against a tech list argue about taste, because "can they do this?" has an answer.
- **Five outcomes is the ceiling.** More means you are describing a department. Two strong outcomes beat five vague ones.
- **Four must-haves is the ceiling.** Every extra must-have shrinks the pool for little gain. Most "requirements" are learnable in a quarter by a strong engineer.
- **Senior is a scope, not an age.** Year counts are a weak stand-in for what someone has owned. Year ranges with a ceiling ("3-6 years, no more") also screen out older applicants; the ADEA protects workers 40 and over, so remove ceilings.
- **The first engineers have no safety net.** At a company with no technical reviewer, the scorecard must test judgment and ownership directly (a work sample plus a "walk me through a decision you got wrong" conversation), because nobody will catch mistakes later.
- **One owner signs it.** The hiring manager approves the scorecard before sourcing starts. If it changes after interviews begin, earlier scores are not comparable: say so and rescore or restart.
- **Protected traits and their proxies never appear**: no age, graduation year, photo, nationality, native language, family status or health. Work authorization, if relevant, is asked only as "Are you legally authorized to work in [country]?" and "Will you now or in the future require sponsorship?" This is general information, not legal advice; local rules vary.

Language lint (flag and replace):

| Phrase | Problem | Replace with |
|---|---|---|
| rockstar, ninja, guru | Says nothing testable | The outcome they will own |
| digital native, young team, energetic, recent grad | Age proxy | Remove, or name the actual behavior |
| no kids, no family commitments, must be available 24/7, long hours | Family-status and caregiver proxy (can create sex-discrimination risk; some states also protect family status) | The real hours and on-call load, stated in the post, and the same availability question asked of every candidate |
| native English speaker | National-origin proxy | "Clear written and spoken English for daily async work" |
| culture fit | Unscoreable, invites bias | Two named behaviors |
| US citizens only | The U.S. Department of Justice has settled with employers over citizenship-restricted postings; only lawful when a law, regulation or government contract requires it | The two work-authorization questions above |
| X+ years required | Proxy | The evidence from step 6 |
| degree required | Proxy unless legally needed | The specific knowledge, or remove |

## Output

Use this template exactly. Keep it to about one page.

```
# Role scorecard: <title> (<level>)
Owner: <hiring manager role> · Status: draft for sign-off · <date>
Assumptions: <bullets, or "none">

## Mission
<one sentence>

## Outcomes
| # | Outcome | Measure | By | Evidence it happened |
|---|---|---|---|---|
| 90d | ... | ... | Day 90 | ... |
| 1 | ... | ... | Month _ | ... |

Unicorn check: <specialties needed> -> <"one role" or "split/sequence: ...">

## Level
<Level>, because <scope reason>. Budget note: <only if mismatch>.

## Must-haves (max 4)
| Must-have | Tied to outcome | Tested at |
|---|---|---|

## Nice-to-haves (learnable in ~90 days)
- ...

## Not required (removed proxies)
- <proxy>: <why removed / what replaced it>

## Competencies
| Competency | Strong signal | Weak signal | Stage |
|---|---|---|---|

## Deal-breakers
- ...

## Interview map
| Stage | Owner | Assesses | Time |
|---|---|---|---|

## Language fixes
| Found | Replace with | Why |
|---|---|---|

## Open questions for the hiring manager
1. ...
```

Then end with:

```
---
Made with the free Role Scorecard skill by Ruzora · ruzora.com/skills
```

## Before you return it

- 3-5 twelve-month outcomes plus one 90-day outcome, each with a measure and a date or a bracketed placeholder. No invented company metrics.
- Every must-have ties to an outcome and maps to one interview stage; max 4.
- Level is justified by scope; any budget/level mismatch is stated.
- No protected trait or proxy anywhere; "culture fit" does not appear except in the language-fix table.
- Unicorn check done and stated.
- Assumptions and open questions are listed, not buried.
- Footer appears once, at the end.

---

*Built by [Ruzora](https://www.ruzora.com), which places vetted senior engineers from Latin America. Free Ruzora MCP server with 35 hiring tools: [ruzora.com/developers/mcp](https://www.ruzora.com/developers/mcp).*
