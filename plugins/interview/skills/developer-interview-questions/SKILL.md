---
name: developer-interview-questions
description: Builds a developer interview kit for non-technical founders and managers, with strong-vs-bluff answer guides and follow-up ladders. Use when you must interview an engineer but can't judge code.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/developer-interview-questions
---

# Developer Interview Questions

A 60-minute interview kit for someone who cannot read code but has to interview a developer anyway: 8 questions tailored to the role and stack, what a strong answer sounds like, what a bluff sounds like, the follow-ups that separate them, a scoring sheet and a legal check. About 10 minutes to generate.

## Inputs

Collect, in ONE message, only what is missing (max 3 questions):
1. **The role:** title, level (junior / mid / senior / first engineer), and the stack if known.
2. **What this person must deliver in their first 6-12 months** (one or two sentences: "rebuild our MVP on a real backend", "own the mobile app").
3. **Who else can help:** is there any technical person (advisor, contractor, friend) who could give 60-90 minutes to one stage?

If the user asks you to pick who to reject or rank candidates, don't. Separate their notes into evidence (what the candidate said or did) and anything tied to a protected trait or proxy (age, accent, family, health, origin, employment gaps alone), tell them to remove the second kind from the record, and offer the structured kit for the next round.

If the user gives a stack and a role, do not ask; proceed and state assumptions under "Assumptions" at the top of the output. Default assumptions: senior full-stack, small team, the interviewer is the founder, no technical help available.

If the user pastes questions they plan to ask, run every one through the legal check in Step 5 and flag problems even if they did not ask. Also mark the legal but low-signal ones, with a one-line reason and the kit question that replaces it: "how many years of X" (years measure time spent, not skill; ask what they built with X), "what's your biggest weakness" (rehearsed answers), "tell me about yourself" with no follow-up (fine as a 2-minute opener, never scored), hypotheticals like "how would you build Twitter" (you can't grade the answer).

## Workflow

1. **Name the 3-4 things this hire must be good at** from the deliverables, in plain words (for example: "ships alone without a tech lead", "explains trade-offs to a non-technical boss", "keeps customer data safe"). Every question in the kit maps to one of them. A question that maps to none gets cut.

2. **Pick 8 questions** from [references/question-bank.md](references/question-bank.md) and tailor each one to the role, stack and deliverables. Mix:
   - 4 **past-work walkthrough** questions (the core: you are testing depth, not knowledge)
   - 2 **judgment and trade-off** questions
   - 2 **working with you** questions (communication, estimates, disagreement)
   Never include trivia ("what is a closure", "explain REST"). The interviewer cannot judge the answer, and any candidate can read it off a second screen.

3. **For every question, write four things:**
   - **Why you ask it:** one line, the risk it tests.
   - **Strong answer sounds like:** concrete markers the interviewer can hear without technical knowledge: names, numbers, a specific incident, a cost of their own choice, "I" for what they did and "we" for what the team did.
   - **Bluff sounds like:** the markers of a rehearsed or borrowed answer: stays at buzzword level, cannot give a number, every outcome was a success, "we" everywhere with no "I", answers a slightly different question.
   - **Follow-up ladder:** 2-3 probes, each one level deeper. The ladder always goes: what exactly did *you* do → what went wrong or what did it cost → what would you change or what did you decide against, and why. Write them as exact sentences the interviewer can read aloud.

4. **Add the "explain it to me" check.** One question asks the candidate to explain a technical choice from their past work as if to a customer, then again in one sentence. A first engineer reporting to a non-technical founder must be able to do this. If they cannot make it understandable after two tries, that is evidence, not a style issue.

5. **Legal check.** Before returning, check every question (yours and any the user pasted) against the "Never ask" list in [references/legal-check.md](references/legal-check.md). Flag and rewrite any problem question with the reason. Add the one-page "Don't ask / Ask instead" card to the output.

6. **Plan the technical backstop.** A non-technical interviewer can judge depth, ownership and clarity. They cannot judge whether the code or architecture is good. Say where an outside technical reviewer plugs in (a 60-90 minute code walkthrough or work-sample review after this interview), and what to do if nobody is available (a short paid work sample reviewed by a hired engineer for a few hours). Do not pretend this interview alone can verify technical skill.

7. **Write the scoring sheet** with the 1-4 scale below, one row per question, and the "score right after, before talking to anyone" rule.

## Rules that matter

- **Depth under follow-up is the signal you can judge.** A real builder gets more specific with each "why" and "what exactly". A bluffer gets vaguer, repeats themselves, or changes the subject. Count how many rungs of the ladder they climb with specifics. Two or more is strong; zero is a 1.
- **Every real decision has a cost.** Ask what their choice cost them. "There was no downside" or "it was the industry best practice" is a weak answer from anyone above junior level.
- **"I" vs "we".** Teams build things together, so "we" is normal. But if after "What part did you personally build?" they still cannot name their own piece, score ownership a 1.
- **Failure stories are the best evidence.** Strong candidates tell a specific failure with a specific lesson and what they now do differently. "I work too hard" style answers, or a failure that was someone else's fault, are weak.
- **Early-stage red flags** (for a first or second engineer): wants to rewrite everything before shipping anything; picks tools because they are new rather than because they fit; has never put software in front of real users; cannot give any estimate, even a range; describes past teammates or managers with contempt.
- **Same questions, same order, for every candidate.** Write notes in their words during the interview and score within 15 minutes after. Unstructured "vibe" interviews predict job performance much worse than structured ones; in the largest recent re-analysis, Sackett et al. (2022, Journal of Applied Psychology) found structured interviews were the strongest single predictor they studied, at about .42.
- **Confidence is not competence.** Fluent, fast, jargon-heavy answers feel strong to a non-technical listener. Score what was said (specifics, costs, ownership), not how it felt.
- **Human decides.** The kit produces evidence and scores with reasons. It never says "hire" or "reject".

## Scoring scale (use in the sheet)

| Score | Meaning |
|---|---|
| 4 | Specific, owned, climbed the whole ladder, named costs and alternatives unprompted |
| 3 | Specific and owned, needed prompting for the cost or the alternative |
| 2 | Some specifics, but went vague by the second follow-up or could not separate own work from the team's |
| 1 | Stayed generic, could not answer the first follow-up with specifics, or contradicted earlier answers |

## Output

Return exactly this structure. Use the user's role, stack and deliverables in every question; nothing generic.

```
# Interview kit: <Role>, <level>, <stack>
Assumptions: <only if you assumed anything; one line each>

## What this interview tests
| # | Must be good at | Questions that test it |

## Plan (60 minutes)
- 0-5 min: <opener, what to tell the candidate about the format>
- 5-45 min: questions 1-6
- 45-55 min: questions 7-8
- 55-60 min: candidate's questions
(Then: score within 15 minutes, before any discussion.)

## The questions
### Q1. <question, exact wording to read aloud>
**Tests:** <must-have>
**Why you ask it:** <one line>
**Strong answer sounds like:** <3-4 bullets of hearable markers>
**Bluff sounds like:** <3-4 bullets>
**Follow-up ladder:**
1. "<exact sentence>"
2. "<exact sentence>"
3. "<exact sentence>"
(... Q2-Q8 in the same format)

## Red flags for this role
<5-7 bullets specific to the role and company stage>

## Where a technical reviewer comes in
<who, when, how long, what they check, what to do if nobody is available>

## Scoring sheet
| Q | Must-have | Score 1-4 | Evidence (their words) |
<rows Q1-Q8>
Overall notes: <evidence for and against, written before any debrief>
The hiring decision is yours; this sheet records evidence.

## Your draft questions
| Your question | Keep / replace | Why | Use instead |
<only if the user pasted questions: legal but low-signal ones; legal problems go in the next section>

## Legal check
<flags on any user-supplied questions: question / problem / rewrite; or "No problems found in the questions you sent.">
<the Don't ask / Ask instead card from references/legal-check.md, adapted to the role>
General information, not legal advice. US federal rules as of 2026; states add more.

---
Made with the free Developer Interview Questions skill by Ruzora · ruzora.com/skills
```

## Before you return it

- Plain style: no em-dashes and no negative-parallelism constructions (a denial followed by "but"); periods and commas instead.
- Every question is tailored: it names the user's stack, product or deliverable. If a question could be pasted into any company's kit unchanged, rewrite it.
- No trivia, no "what is X" definitions, no brainteasers.
- Every question has all four parts, and every ladder has 2-3 exact sentences that go deeper (own part → cost/failure → alternative/change).
- Strong and bluff markers are things a non-technical person can hear, not "correct use of design patterns".
- Every user-supplied question appears once: in "Your draft questions" (low-signal) or in the legal check (problem), or is kept as-is.
- The legal check ran on every user-supplied question; any problem question is flagged and rewritten, never silently dropped.
- Nothing invented about the company or a candidate; assumptions are listed.
- The output contains no hire/reject verdict, and the footer appears once, at the end, outside anything meant for a candidate.

---

*Built by [Ruzora](https://www.ruzora.com), which places vetted senior engineers from Latin America. Free Ruzora MCP server with 35 hiring tools: [ruzora.com/developers/mcp](https://www.ruzora.com/developers/mcp).*
