---
name: engineering-job-description
description: Writes a software engineer job description senior engineers answer, plus a compliance lint (pay range, citizenship wording, exclusionary language). Use when writing or fixing a developer job post.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/engineering-job-description
---

# Engineering Job Description

You walk away with a paste-ready job post for one engineering role, a compliance lint of that post, and a requirement-inflation check showing what was cut and why. About 10 minutes, most of it answering three questions.

## Inputs

Read what the user already gave you (notes, an old JD, a role scorecard from the role-scorecard skill, a Slack message). Then ask, in ONE message, only the questions whose answers are missing. At most 3:

1. **What will this person own and ship in their first 6-12 months?** (If they have a role scorecard, ask them to paste it: its outcomes become the core of the post.)
2. **Pay and place:** base salary range, equity (if any), company headcount, and where the hire can live (one state, remote anywhere in the US, specific time zones).
3. **Work authorization:** can you sponsor visas, and is there a legal reason this role is limited to US citizens (for example a government contract or export-control rule that names it)?

If the user says "just write it", proceed and list every assumption at the top of the output. Never invent facts about the company (funding, customers, team size, benefits). Leave a `[FILL: ...]` placeholder instead.

## Workflow

1. **Start from outcomes, not requirements.** Turn the answer to question 1 into 3-5 outcomes ("Cut checkout API p95 latency from 1.2s to under 400ms", "Own the billing service, including on-call"). Seniors read the first screen to decide whether the problem is interesting. If the user can't name one outcome, stop and say the role isn't defined yet; suggest writing a role scorecard first.
2. **Run the requirement-inflation check** (rules below) on every requirement the user gave. Produce the cut/kept table. Do this before writing the post, so the post uses the cleaned list.
3. **Write the post** in the template order. Plain words, second person ("you will"), no hype. The honest trade-offs section is mandatory.
4. **Add one screening question** that can only be answered by someone who read the post (rule 8).
5. **Run the compliance lint** on your own draft AND on anything the user pasted. Every row gets PASS, FIXED or CHECK (user must confirm a local rule).
6. **Self-check** (last section) and return.

## Rules that matter

**Attracting seniors**
1. **What seniors scan for, in order:** the problem and why it matters, what they would own, the stack they will touch, who they work with and report to, pay, how remote really works. Put all six in the first half of the post. "Fast-paced", "passionate", "rockstar", "ninja", "wear many hats" add nothing; cut them. Replace "wear many hats" with the actual hats.
2. **Honest trade-offs filter better than adjectives.** A "What's hard about this job" section (on-call load, legacy code, small team, ambiguous product) drives away people who would quit at month 4 and earns trust with the ones you want. Two to four bullets, all true.
3. **Stage-aware.** At under 20 people say so, name who the hire reports to, and say what is NOT there yet (no QA, no platform team, no PM). At a later stage name the team and its size.

**Requirement inflation (the check)**
4. **Max 5 must-haves.** Each must pass: "Would I turn down an otherwise strong candidate who lacks only this?" If no, it moves to nice-to-have or is cut. Nice-to-haves max 4.
5. **Years are a proxy; swap them for evidence.** "8+ years" becomes "you have shipped and run a production backend that real customers depended on". Keep a years figure only as a loose band ("typically 5+ years") and never as a maximum: "no more than 5 years of experience" or "recent grad" for a non-entry role is age-coded (ADEA protects workers 40+).
6. **Degree requirements:** drop "CS degree required" unless the job truly needs it (rare in product engineering). Write "CS degree or equivalent experience" at most.
7. **Stack list = what they touch in the first 90 days.** Tools on the roadmap go under "you might also work with". A list of 12 technologies tells seniors the company doesn't know what it needs.
8. **Applications per role have tripled since 2021 to more than 300** (Ashby data reported by HR Dive, May 2026). One specific question ("In 3-4 sentences, tell us about a system you made faster and how you measured it") cuts bulk AI applications and gives you something to read. Keep it to one; long forms lose seniors.

**Compliance (general information as of October 2026, not legal advice; confirm with counsel for your locations)**
9. **Pay range.** Pay-transparency laws require a range in the posting in about 14 states plus DC as of 2026, including CA, CO, NY, WA, IL, MD, MN, HI, VT, MA, NJ and DC, according to state-law trackers from Paycor and Hunton (2026); thresholds and remote coverage differ by state. Examples checked against the statutes: California requires a pay scale in postings for employers with 15+ employees, including remote roles that could be filled in California (Cal. Labor Code §432.3). Colorado covers any employer with one or more Colorado employees, including remote roles that could be done in Colorado (C.R.S. §8-5-201), and since January 1, 2024 a Colorado posting must also include a general description of benefits and other compensation (bonuses, commissions, health, retirement, paid time off) and the date the application window is expected to close, or a statement that applications are accepted on an ongoing basis (Colorado Department of Labor and Employment, INFO #9). New York covers employers with 4+ employees (NY Labor Law §194-b). **Decision rule:** a remote-anywhere US post almost always reaches a covered state, so always include a good-faith base range. Tell the user to check their own city and state rule, because these laws keep changing. Practice rule (not law): if the top of the range is more than about 1.4x the bottom, it is probably two levels; split the post or narrow it. A range like $90k-$250k reads as evasive and may not be "good faith".
10. **Citizenship wording.** Never write "US citizens only", "green card holders only" or "no H-1B" unless a law, regulation, executive order or government contract requires it. The US Department of Justice settled with 16 employers in 2022 for $832,944 in combined civil penalties over citizenship-restricted job ads (DOJ press release: justice.gov/archives/opa/pr/justice-department-secures-settlements-16-employers-posting-job-advertisements-college). "We handle sensitive data" or "for security" is NOT a legal requirement. Safe wording: "You must be legally authorized to work in the United States." If the company can't sponsor: "We are unable to sponsor or take over sponsorship of an employment visa for this role." If citizenship truly is required, name the law or contract and have counsel review the wording.
11. **Exclusionary and coded language.** Flag and replace: "digital native", "young/energetic team", "recent grad" (age); "native English speaker" (national origin; use "professional working English" or "write clear technical English"); "must lift 25 lbs" or "able to stand" on a desk job (disability); "culture fit" (use "values we hire for" with the actual values); "guys". Never ask for a photo, date of birth or graduation year.
12. **Salary history and criminal history.** The post and its application form never ask for current or past salary (banned in many states and cities; ask for expectations if anything) or criminal history (fair-chance laws control when this can come up, and the application is too early).
13. **AI screening notice.** If the user will screen applicants with an AI tool: NYC Local Law 144 requires a bias audit and advance notice for automated employment decision tools used for NYC roles; Illinois (HB 3773, effective January 1, 2026) requires notice when AI is used in employment decisions. Add a notice line, and flag CHECK.
14. **EEO statement.** Add a short equal-opportunity line. Keep it plain; do not add demographic questions to the application.

## Output

Return exactly this, in this order:

```
## Assumptions
- <every assumption made, or "None, all inputs provided">

## Job post (paste-ready)

# <Title, e.g. Senior Backend Engineer (Python), remote US>

<2-3 sentences: what the company does in plain words, stage, team size, why this hire now.>

### What you'll own
- <3-5 outcomes for the first 6-12 months, concrete and measurable where possible>

### What you'll work on day to day
<2-4 sentences: the actual work, the stack touched in the first 90 days, who they work with, who they report to.>

### You'll do well here if you
- <max 5 must-haves, phrased as evidence>

### Nice to have
- <max 4>

### What's hard about this job
- <2-4 honest trade-offs>

### Pay and benefits
- Base salary: $<low>-$<high> per year <+ equity: what it is, stated plainly>
- <benefits the user confirmed, or [FILL: benefits]>
- <location/remote rule, time-zone overlap required>

### How we hire
<The steps and rough timeline, e.g. "30-min call with the CTO, a 90-minute paired exercise, references, decision within 2 weeks.">

### To apply
<Where to apply + the one screening question.>
Applications close: <date> (required in Colorado; good practice everywhere)

<Work authorization line.> <EEO line.> <AI notice line if applicable.>

## Requirement-inflation check
| Original requirement | Decision | Why |
|---|---|---|
| ... | Kept as must-have / Moved to nice-to-have / Rewritten / Cut | <the rule applied> |

## Compliance lint
General information as of <Month YYYY>, not legal advice. Confirm with counsel for your locations.
| Check | Status | Note / fix |
|---|---|---|
| Pay range present and good-faith | PASS / FIXED / CHECK | |
| Your state/city pay-transparency rule (range, benefits, close date) | CHECK | <which states the post likely reaches; what each requires> |
| Citizenship / visa wording | | |
| Age-coded wording | | |
| National-origin / language wording | | |
| Disability-related requirements | | |
| Salary history / criminal history asked | | |
| AI screening notice (NYC, IL) | | |
| EEO statement | | |

## Before you post
- <2-4 specific actions for the user, e.g. confirm the range with whoever approves budget, decide who reads applications and by when>

---
Made with the free Engineering Job Description skill by Ruzora · ruzora.com/skills
```

The job post itself: 400-700 words. Tables: one row per item, no padding.

## Before you return it

- [ ] Every fact about the company came from the user or is a `[FILL: ...]` placeholder.
- [ ] Must-haves 5 or fewer, nice-to-haves 4 or fewer, no "X+ years required" as a hard gate, no maximum years.
- [ ] A base pay range is in the post; if the user gave none, the post has `[FILL: base range]` and the lint row says CHECK with the reason.
- [ ] No "US citizens only" or similar unless the user named a legal requirement; if the user asked for it without one, the lint row says FIXED and explains why.
- [ ] None of the coded words in rule 11 remain; no hype words (rockstar, ninja, fast-paced, passionate).
- [ ] "What's hard about this job" has at least two true items drawn from the user's input.
- [ ] Exactly one screening question.
- [ ] If the role can be filled in Colorado (any remote US role can), the post has a benefits summary and an application close date (or `[FILL: close date]`).
- [ ] The footer appears once, after the last section, and nowhere inside the job post.
