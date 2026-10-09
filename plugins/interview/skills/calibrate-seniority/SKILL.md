---
name: calibrate-seniority
description: Calibrates engineering seniority by scope, not years. Sets the level a role needs and estimates a candidate's level with confidence and evidence. Use when choosing junior, mid, senior or staff.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/calibrate-seniority
---

# Calibrate Seniority

Answers two questions with evidence instead of titles: what level does this work actually need, and what level is this person really. You walk away with a level per dimension, a confidence rating, the gap between role and person, three questions that separate the two adjacent levels, and what that means for the hire. About 10 minutes. The human decides.

## Inputs

Work out which mode you are in from what the user pasted:
- **Role mode:** a description of the work (or a role scorecard). Output: the level the work needs.
- **Candidate mode:** a CV, profile, interview notes, an interview scorecard or an assessment report. Output: the level the evidence supports.
- **Both** (most useful): role plus candidate. Output adds the gap and the implication.

Outputs from other skills are welcome. From a role scorecard, take the mission, outcomes and stated level (and re-check that level against scope). From an interview scorecard, use only the evidence lines and quotes, never the scores or overall leans, and ignore anything it struck.

Ask at most 3 questions, in one message, only if the answer changes the level:
1. **Who reviews this person's technical decisions?** (A named senior engineer, a part-time CTO, nobody.)
2. **What will they own alone in the first 6 months,** and what breaks if they get it wrong?
3. For a candidate: **what did you see beyond the CV** (screen call, work sample, interviews)?

If the user says "just do it", proceed and list assumptions at the top. Privacy: work from a first name or a candidate code. If the user pasted a photo, date of birth, home address, ID or health details, do not repeat them and tell them once to remove them.

## The five dimensions

Level each dimension separately, using the rubric in [references/levels.md](references/levels.md):
1. **Scope:** the size of what they own (a task, a feature, a system, several systems).
2. **Ambiguity:** how unclear the problem can be when it reaches them.
3. **Autonomy:** how much direction and review they need to deliver.
4. **Impact and ownership:** did they build it, or build it and run it (on call, incidents, migrations, the second year)?
5. **Technical depth:** quality of judgment in their area: trade-offs, failure modes, explaining why.

The ladder in one line each:
- **Junior:** does tasks others defined, with daily guidance and review on most work.
- **Mid:** delivers features end to end once someone else framed the problem; needs review on design.
- **Senior:** owns a system: designs, builds, runs and fixes it; turns vague goals into a plan; needs nobody for their area.
- **Staff:** owns technical direction across several systems or teams; shapes other people's work.

## Workflow

1. **Role first, if given.** For each dimension, write what the work requires in plain words, then the level. The needed level is the highest level any must-have outcome requires, not the average.
2. **Run the reviewer test.** If nobody at the company can review this person's design decisions, the role needs Senior at minimum, whatever the budget or title says. Flag mismatches plainly: "planned as mid-level, but owns payments alone with no reviewer: that is senior scope." Also flag the reverse: Staff at a company with one system and three engineers is usually over-leveling (the scope does not exist yet).
3. **Read the CV as claims, not facts.** Sort every bullet by its verb into the ladder in references/levels.md ("worked on", "helped", "contributed to" = participant; "built", "implemented" = feature; "designed and ran", "on call for", "migrated", "deprecated" = system; "set direction", "adopted by other teams" = cross-system). A bullet with no system, no scale and no result is not evidence of anything; list it as "unverified" instead of guessing.
4. **Normalize the title** with the company-size table in references/levels.md. A title is a claim about scope at that company, not a level on yours. Two common traps: "Senior" after about 2 years at a 5-person agency (often client delivery without running anything in production), and a big-company senior who owned a narrow slice with platform teams handling deploys, infra and on-call tooling. Neither converts automatically in either direction; turn each into a question. Never map one company's level codes to another's from memory, and never state facts about a named company you were not given.
5. **Weigh interview and assessment evidence above the CV.** Strongest signals, in order: explaining their own code or design and why they rejected the alternative; defending a trade-off under pushback (and changing their mind when the pushback is right); decomposing a vague problem before building; a specific incident they owned end to end, with "I" for their part and "we" for the team's. Opinions ("seemed senior", "not senior enough") are not evidence; turn each into a question.
6. **Level each dimension, then set the estimate.** Write the evidence and its source next to every dimension. If evidence is missing for a dimension, mark it **NE (no evidence)**. Do not fill it with a guess. Then set the overall estimate with the floor rule below and report a range when dimensions split across two levels.
7. **Rate confidence** with the caps below. Say what would raise it.
8. **Compute the gap** (both modes only): per dimension, needed vs estimated. Name the **binding gap**: the dimension where a shortfall would hurt the role's must-have outcomes most.
9. **Write 3 separating questions** for the two adjacent levels in play (for example Mid vs Senior). Take them from the question bank in references/levels.md and adapt them to this role's real work. For each, write what an answer at each level sounds like. Target the NE dimensions and the binding gap first.
10. **Write the implication** as options with conditions, never as a verdict on the person (see Rules).

## Rules that matter

- **The floor rule.** The overall estimate is the lowest level among the dimensions the role's must-haves depend on, not the average and not the peak. Strong technical depth with mid-level autonomy is a mid-level hire for a role that must run alone.
- **Built is not ran.** The senior signal is lifecycle: being on call, fixing your own design a year later, migrating off something you built. "Built X" with nothing after launch is feature-level evidence, however big X was.
- **Confidence caps.** CV or profile alone: **Low**, always, whatever it says. One structured interview or assessment that probed the dimension: up to **Medium**. Two or more independent sources that agree (for example a work sample plus a design or incident interview, or a reference that confirms scope): **High**. An interview scorecard full of opinions and no quotes counts as no source.
- **Years are a weak proxy and never a maximum.** Some people reach senior scope in 3 years, some never do in 15. Never use a year ceiling or "overqualified" to filter: in the US, the ADEA protects workers 40 and over at employers with 20+ employees, and many state laws cover smaller employers; year ceilings screen them out. If the worry is boredom or cost, ask about scope and pay expectations directly.
- **Short tenures are a question, not a downgrade.** Someone who changed jobs every 12-18 months may have no "second year" stories, or may have left for reasons that are none of your business (layoffs, family, health). Ask: "Tell me about something you built that you later had to maintain or fix." Score the answer, not the dates.
- **Unknown company is not small scope.** Do not discount experience because you have not heard of the company or it is outside the US. Ask for scale facts (users, transactions, team size, what they were on call for).
- **A path needs a reviewer.** Hiring one level below the need "with a path" only works if someone at or above the needed level reviews their work for the first 6 months. If nobody can, the path is a risk, and the output must say so.
- **AI changed the output, not the level.** Fast output on well-defined tasks is now cheap for everyone with an AI assistant. Level shows in choosing what to build, reviewing generated code, and debugging what broke. Weigh decisions and debugging stories over volume of shipped code.
- **No protected traits or proxies.** Never use or infer age, graduation year, school prestige, accent, nationality, national origin, photo, family status, health or gaps alone. If the user's notes contain these, strike them in a "Not used" line and say why in a few words. This is general information, not legal advice; state and local rules add more.
- **Evidence, not verdicts.** Write "the evidence points to Mid, Low confidence", never "she is a mid-level engineer" or "reject".

## Output

Use exactly this structure. Drop sections 1, 3 and 5 in candidate-only mode and sections 2 and 3 in role-only mode, and say which mode you used. No em-dash characters anywhere.

```
# Seniority calibration: <role> / <candidate code or first name>
**Mode:** Role / Candidate / Both · **Inputs used:** <list> · **Date:** <date>
**Assumptions:** <bullets, or "None">
**Not used:** <struck items and why, or "Nothing struck">

## 1. Level the work needs
| Dimension | What the work requires (from the input) | Level |
|---|---|---|
| Scope | ... | ... |
| Ambiguity | ... | ... |
| Autonomy | ... | ... |
| Impact and ownership | ... | ... |
| Technical depth | ... | ... |
**Needed level:** <level>, set by <dimension(s)>. **Reviewer test:** <who reviews; pass/fail>
**Mismatch flags:** <planned level/budget/title vs the work, or "None">

## 2. Level the evidence supports
**Estimate:** <level, or range "Mid to Senior"> · **Confidence:** <Low/Medium/High>, because <sources and the cap that applies>
| Dimension | Evidence (quote or close paraphrase, with source) | Points to | Strength |
|---|---|---|---|
| ... | "..." (CV / screen call / interview / assessment) | <level or NE> | Strong / Weak / Unverified |
**Title check:** <title, company size, tenure> -> <what the title likely meant there, as a question to verify>
**Unverified claims:** <bullets with no system, scale or result>
**What would raise confidence:** <1-3 specific steps>

## 3. Gap
| Dimension | Needed | Estimated | Gap |
|---|---|---|---|
**Binding gap:** <dimension, and the must-have outcome it puts at risk>

## 4. Three questions that separate <Level A> from <Level B>
| # | Question | A <Level A> answer sounds like | A <Level B> answer sounds like | Tests |
|---|---|---|---|---|
| 1 | ... | ... | ... | <dimension> |
Listen for: <one line on follow-ups that expose rehearsed answers: "what did you reject?", "what would you change now?">

## 5. Implication
- **Option A:** <e.g. hire at <level> with a path>, only if <condition, including who reviews>.
- **Option B:** <e.g. re-scope the role to match / keep looking at <level>>, because <evidence>.
- **What would change this read:** <the answer to question N>
**Decision (made by <hiring manager>):** ________ **Date:** ________
```

End with:

```
---
Made with the free Calibrate Seniority skill by Ruzora · ruzora.com/skills
```

## Before you return it

- Every fact about the user's company comes from the user's message, never from the candidate's CV.
- Every candidate dimension cites evidence with its source, or says NE. No employer, scale, school or skill was invented or inferred beyond the input.
- Confidence respects the caps: CV-only is Low, every time.
- The estimate follows the floor rule; a split is shown as a range, not averaged.
- The reviewer test is stated whenever a role is given, and any level/budget/title mismatch is flagged.
- No year ceiling, "overqualified", school prestige, graduation year, accent, nationality, gap or other protected trait or proxy was used; any that appeared in the input is listed under "Not used".
- The three questions target the NE dimensions and the binding gap, and each has both answers written out.
- The output says what the evidence supports and leaves the decision line blank. It never says reject or hire.
- The footer appears once, as the last line.
