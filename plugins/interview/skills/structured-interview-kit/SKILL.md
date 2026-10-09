---
name: structured-interview-kit
description: Builds a lean structured interview loop for an engineering role, with stages, owners, time budget, fixed questions, an anchored 1-4 rubric and a legal lint. Use when you need an interview kit or loop.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/structured-interview-kit
---

# Structured Interview Kit

A complete interview loop for one engineering role that a small team can run in two weeks: who interviews, for how long, what each person asks (the same questions for every candidate), a 1-4 rubric with behavioral anchors, the scoring and debrief rules, a candidate-facing process email, and a legal lint of every question. About 15 minutes to generate.

## Inputs

Ask, in ONE message, only what is missing and changes the output (max 3):
1. **Role and level, plus the 3-6 things the hire must be good at** (or the role scorecard / job description if one exists).
2. **Who can interview** (names or roles, and roughly how many hours each can give per candidate).
3. **Anything already in the process** you must keep (a take-home, a founder chat, questions the team likes). Ask the user to paste their current questions so you can lint them.

If the user asks for automatic rejection by score, IQ tests or personality tests, say in one line each what you will not include and why (a person decides on the evidence; general-ability and personality tests add legal and adverse-impact risk a small team can't validate, and they don't test the job), then build the kit anyway.

If the user gave a job description and a team list, do not ask; proceed and list assumptions at the top. Defaults: senior engineer, 3 available interviewers, US-based employer, remote interviews by video.

## Workflow

1. **Set the competencies (4-6).** Derive them from the scorecard or JD. Each is an observable capability, not a trait: "designs a data model that survives the next 12 months of features", not "smart" or "culture fit". Mark each as **must-have** or **nice-to-have**. If the user lists "culture fit", replace it with 1-2 named behaviors they actually mean (for example "gives and takes direct feedback in writing") and say why: undefined fit is where similar-to-me bias lives.

2. **Design the lean loop.** Rules:
   - At most **4 assessed stages** after a 30-minute screen. Google's internal analysis found four interviews predicted its hire decisions with 86% confidence and each extra interview added less than 1% (reported by CNBC, 2019). More stages mostly add delay.
   - **Candidate time budget:** at most about 5 hours of live interviews in total, plus at most one work sample capped at 2-3 hours or paid. Show the total.
   - **Coverage:** every must-have competency is assessed in **exactly 2 stages** by 2 different people (two independent reads, no more). Nice-to-haves get 1. Each interviewer owns **at most 3 competencies**; more than that and they score on overall impression.
   - **Fewer than 3 people can interview** (a founder alone, or a founder plus one engineer): keep the two-reads rule by adding a paid outside reviewer (a senior contractor or fractional CTO, 2-3 hours per finalist) for the technical must-haves. If that is impossible, the same person may assess a must-have in 2 stages only if they write and submit each stage's score before the next stage starts, and the kit must state in the Coverage check that coverage is weaker. Never return questions without a kit because the team is small.
   - **One owner per stage**, named. A shadow (someone learning to interview) may join but does not score until they have shadowed twice.
   - Put the most informative, cheapest-to-fail stage first (usually the work sample or the technical conversation), so a clear miss ends the process early for both sides. Whether to continue is the hiring manager's call on the evidence.

3. **Set the clock.** Target **10 business days from first interview to offer decision.** Book all remaining stages in a single block (one day or two adjacent half-days) as soon as the candidate passes the first stage. Scores due within 24 hours of each interview. Debrief within 48 hours of the last interview. Show this as a timeline table.

4. **Write the questions per stage.** 3-4 core questions per stage, each tied to one competency, plus 2 fixed probes each. Use **behavioral** questions ("Tell me about a time you...") for experienced candidates and **situational** questions ("Here's a situation we hit last month. What would you do?") for juniors or when past experience is thin. Use [references/rubric-anchors.md](references/rubric-anchors.md) for anchors and question patterns. Every candidate gets the same questions in the same order. Interviewers may use the listed probes and neutral follow-ups ("Tell me more", "What did you do next?"), not new questions.

5. **Write the anchored rubric.** For each competency, 4 levels with behavioral anchors: what the interviewer heard or saw at that level, written so two interviewers would give the same score. Use a 1-4 scale (no middle score to hide in). Add **NE (no evidence)**: if the stage did not produce evidence, the interviewer writes NE, not 1, and the gap goes to the debrief.

6. **Lint every question** (yours and the user's) against [references/legal-lint.md](references/legal-lint.md). Flag, explain and rewrite problems. Include the lint table in the output even if it is clean.

7. **Write the scoring and debrief rules** and the candidate-facing process email (stages, length, who they meet, AI-use rule for any work sample, when they will hear back).

## Rules that matter

- **Structure is the point.** Structured interviews (same questions, anchored scoring) were the highest-ranked predictor of job performance in Sackett et al.'s 2022 re-analysis in the Journal of Applied Psychology (validity about .42). Most of that benefit is lost if interviewers improvise questions or score from memory.
- **Independent scoring before any discussion.** Each interviewer submits written scores with evidence before the debrief, and does not discuss the candidate in chat or the hallway first. The first opinion voiced otherwise anchors everyone else.
- **Debrief order:** the least senior interviewer speaks first, the hiring manager last. Discuss competencies where scores differ by 2 or more points first; they hold the most information.
- **Evidence or it doesn't count.** A score without a quote or an observed behavior is not discussed. "Seemed sharp" is not evidence. "Found the off-by-one in the pagination query within 5 minutes and explained why it only failed on the last page" is.
- **A wide split with no evidence is void.** If two assessors of the same competency differ by 2 or more points and neither wrote a quote or observed behavior, both scores are struck and the competency becomes NE. Never average a 1 and a 4 into a 2.5; the average describes a candidate nobody met.
- **Score the stage you ran, not the candidate you remember.** An interviewer who saw an earlier stage's scores before their own interview (because they share a calendar invite thread, a spreadsheet or a chat) scores that competency NE. Hide scores until every form is in.
- **Must-have rule:** a must-have competency scored 1 by both of its assessors is a serious gap. The debrief must name it and decide explicitly, in writing, whether anything outweighs it. The decision stays with the hiring manager.
- **Change questions between candidates, not during.** If a question isn't working, replace it for every later candidate and note the date, so scores stay comparable.
- **Bias traps to name in the kit:** halo (one strong answer lifts every score), similar-to-me (same school, same old employer, same hobbies), contrast effect (scoring against the previous candidate instead of the anchors), and "presentation polish" standing in for skill.
- **Speed is part of fairness.** Strong engineers are often in several processes at once. A loop that takes six weeks selects for whoever is least in demand.
- **Human decides.** The kit organizes evidence. It never outputs hire or reject.

## Output

Return exactly this structure, filled for the user's role:

```
# Structured interview kit: <Role>, <level>
Assumptions: <one line each, only if any>

## Competencies
| # | Competency (observable) | Must / Nice | Why it matters in this role |

## The loop
| Stage | Format | Owner | Length | Competencies assessed |
Candidate time: <total live hours> + <work sample hours or "paid trial">

## Coverage check
| Competency | Stage A | Stage B | Assessors |
(Each must-have appears in exactly 2 stages with 2 different assessors.)

## Timeline (target: offer decision within 10 business days of first interview)
| Day | What happens | Who |

## Rubric
### <Competency 1>
| Score | Anchor (what you heard or saw) |
| 4 | ... |
| 3 | ... |
| 2 | ... |
| 1 | ... |
| NE | Not assessed in this stage, note why |
(... every competency)

## Interview guides
### Stage <n>: <name>, <owner>, <length>
Opening (2 min, read aloud): <script>
| # | Question (read as written) | Competency | Probes (use only these) |
Closing (5 min): candidate questions, next steps exactly as in the timeline.
(... every stage)

## Scoring form (one per interviewer, submit before the debrief)
| Competency | Score 1-4 or NE | Evidence: quote or observed behavior |
Submitted within 24 hours. Do not discuss the candidate before submitting.

## Debrief (30 minutes)
<agenda with the order and rules from "Rules that matter", the must-have rule, and the closing line: "Decision: made by <hiring manager>, recorded with the evidence that drove it.">

## Candidate email: what to expect
<paste-ready email, under 150 words>

## Legal lint
| Question | Issue | Rewrite |
<or "No issues found in the questions reviewed.">
General information, not legal advice. US federal rules as of 2026; states and cities add more.

---
Made with the free Structured Interview Kit skill by Ruzora · ruzora.com/skills
```

## Before you return it

- Plain style: no em-dashes and no negative-parallelism constructions (a denial followed by "but"); periods and commas instead.
- Every must-have competency appears in exactly 2 stages, with 2 different assessors; no interviewer owns more than 3 competencies. With fewer than 3 interviewers, the kit uses a paid outside reviewer or the same-person fallback with each score written before the next stage, and says coverage is weaker.
- Anything the user asked for that the kit leaves out (auto-reject, IQ or personality tests) is named in one line with the reason.
- Live interview time is about 5 hours or less, and the work sample is capped at 2-3 hours or paid. If the user's existing process breaks these limits, say so and show the trimmed version.
- Every anchor describes behavior someone can hear or see; no anchor uses words like "good", "strong" or "excellent" without saying what that looks like.
- Every question is tied to one competency and is the same for every candidate.
- The legal lint covered every question the user pasted; any problem is flagged with a rewrite.
- The timeline adds up to 10 business days or fewer from first interview to decision, or explains why not.
- The candidate email contains no internal rubric details and no footer.
- No hire/reject verdict anywhere. Nothing invented about the company; assumptions listed.
