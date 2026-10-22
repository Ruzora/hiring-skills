# Hiring Skills for Engineering Teams

**Hiring Skills is a free set of 21 AI skills that help founders, CEOs and hiring managers hire software engineers**: plan the role, write the post, screen fairly, catch fake candidates, run structured interviews, check references, make the offer and onboard the hire. Each skill runs inside Claude (or any AI that reads a prompt) and produces a finished artifact you can use in the next ten minutes: a scorecard, an interview kit, a reference script, an offer email, a 30-60-90 plan.

Written for people hiring without a recruiting team: a founder hiring engineer number one, a manager running a loop alone, an ops lead who suddenly owns a technical hire.

*By Roberto Espinoza, founder of [Ruzora](https://www.ruzora.com). Updated 2026-10-22.*

**Quick install (Claude Code):** `/plugin marketplace add Ruzora/hiring-skills` · **Claude.ai / other AIs:** grab a zip or prompt from the [latest release](https://github.com/Ruzora/hiring-skills/releases/latest).

## Why these and not a template

- **Decision rules, not lists.** Every skill encodes what an experienced engineering hiring manager does: thresholds, red flags, the order to do things in, and when to stop.
- **Tested before publishing.** Each skill was run on a realistic input and on an adversarial one (an illegal interview question, a request to auto-reject, a fake candidate), and compared against the same request with no skill. A skill shipped only if it clearly beat the plain answer and caught every trap.
- **The human decides.** Skills organize evidence and suggest questions. None of them rejects a candidate, and none scores on protected traits or proxies for them.
- **Current law, cited.** Pay-transparency rules, contractor tests, fraud advisories and AI-in-hiring laws are cited to primary sources and dated. This is general information, not legal advice.

## The skills

<!-- catalog:start -->
### Plan the hire (`hire-plan`)

Decide what to hire, when, and what it really costs.

| Skill | What you get | Guide |
|---|---|---|
| [Engineer Hiring Cost Compare](plugins/plan/skills/engineer-hiring-cost-compare/SKILL.md) | Builds a neutral 12-month cost and risk comparison of six ways to add an engineer, on your own numbers. | [guide](site/engineer-hiring-cost-compare/page.md) |
| [International Engineer Hiring Plan](plugins/plan/skills/international-engineer-hiring/SKILL.md) | Builds an engagement plan for hiring an engineer in another country: contractor vs EOR vs vendor, risk register, setup checklist, questions for counsel. | [guide](site/international-engineer-hiring/page.md) |
| [Role Scorecard](plugins/plan/skills/role-scorecard/SKILL.md) | Turns a vague engineering hire into a role scorecard with mission, measurable 12-month outcomes, must-haves, competencies and an interview map. | [guide](site/role-scorecard/page.md) |
| [Staffing Vendor Due Diligence](plugins/plan/skills/staffing-vendor-due-diligence/SKILL.md) | Produces a vendor due diligence scorecard, question list, contract red-flag check and reference script for a staffing firm, agency or dev shop. | [guide](site/staffing-vendor-due-diligence/page.md) |

### Attract candidates (`hire-attract`)

Job posts and outreach that senior engineers answer.

| Skill | What you get | Guide |
|---|---|---|
| [Engineer Outreach Messages](plugins/attract/skills/engineer-outreach-messages/SKILL.md) | Writes honest 3-touch outreach to passive senior engineers plus a referral ask for a founder's network. | [guide](site/engineer-outreach-messages/page.md) |
| [Engineering Job Description](plugins/attract/skills/engineering-job-description/SKILL.md) | Writes a software engineer job description senior engineers answer, plus a compliance lint (pay range, citizenship wording, exclusionary language). | [guide](site/engineering-job-description/page.md) |

### Screen and verify (`hire-screen`)

Screen CVs, profiles and candidates fast, and catch fake ones.

| Skill | What you get | Guide |
|---|---|---|
| [Code Sample Review](plugins/screen/skills/code-sample-review/SKILL.md) | Reviews a candidate's GitHub repo or code sample in plain English for non-technical hirers, with authorship checks and interview questions. | [guide](site/code-sample-review/page.md) |
| [Deepfake Interview Check](plugins/screen/skills/deepfake-interview-check/SKILL.md) | Produces a respectful liveness script, observer checklist and escalation steps to catch deepfake or stand-in candidates. | [guide](site/deepfake-interview-check/page.md) |
| [Fake Candidate Check](plugins/screen/skills/fake-candidate-check/SKILL.md) | Builds an identity-verification protocol for remote engineering hires and a red-flag log for a specific candidate, from FBI guidance. | [guide](site/fake-candidate-check/page.md) |
| [Resume Triage](plugins/screen/skills/resume-triage/SKILL.md) | Triages engineering CVs against a role's must-haves with evidence scores, blind mode, prompt-injection flags and screening-call questions. | [guide](site/resume-triage/page.md) |

### Interview and assess (`hire-interview`)

Interview kits, take-homes, rubrics and debriefs that predict performance.

| Skill | What you get | Guide |
|---|---|---|
| [AI-Use Interview Check](plugins/interview/skills/ai-use-interview-check/SKILL.md) | Sets an AI-use policy for developer interviews, matches each stage to it, gives fair cheating tells and an AI-fluency pairing exercise with rubric. | [guide](site/ai-use-interview-check/page.md) |
| [Calibrate Seniority](plugins/interview/skills/calibrate-seniority/SKILL.md) | Calibrates engineering seniority by scope, not years. Sets the level a role needs and estimates a candidate's level with confidence and evidence. | [guide](site/calibrate-seniority/page.md) |
| [Coding Assessment Designer](plugins/interview/skills/coding-assessment-designer/SKILL.md) | Designs an AI-resilient coding test for a developer role (seeded-bug review, extend-a-codebase or paid trial) with a hidden rubric and follow-up. | [guide](site/coding-assessment-designer/page.md) |
| [Developer Interview Questions](plugins/interview/skills/developer-interview-questions/SKILL.md) | Builds a developer interview kit for non-technical founders and managers, with strong-vs-bluff answer guides and follow-up ladders. | [guide](site/developer-interview-questions/page.md) |
| [Interview Scorecard](plugins/interview/skills/interview-scorecard/SKILL.md) | Turns raw interview notes into an anchored scorecard per interviewer and a debrief memo with evidence, disagreements and bias flags. | [guide](site/interview-scorecard/page.md) |
| [Structured Interview Kit](plugins/interview/skills/structured-interview-kit/SKILL.md) | Builds a lean structured interview loop for an engineering role, with stages, owners, time budget, fixed questions, an anchored 1-4 rubric and a legal lint. | [guide](site/structured-interview-kit/page.md) |

### Close the hire (`hire-close`)

References, offers and contracts, including international hires.

| Skill | What you get | Guide |
|---|---|---|
| [Contractor Classification Check](plugins/close/skills/contractor-classification-check/SKILL.md) | Checks whether a contractor engineer looks like an employee under IRS, DOL and state tests, plus IP and account ownership, with questions for counsel. | [guide](site/contractor-classification-check/page.md) |
| [Job Offer Kit](plugins/close/skills/job-offer-kit/SKILL.md) | Builds a job offer kit for an engineering hire: pre-close questions, verbal offer script, written offer email, negotiation playbook and close plan. | [guide](site/job-offer-kit/page.md) |
| [Reference Check](plugins/close/skills/reference-check/SKILL.md) | Builds a reference-check plan for an engineering finalist: referee identity checks, a call script aimed at the risks found in interviews, and a risk register. | [guide](site/reference-check/page.md) |

### Onboard and review (`hire-onboard`)

Onboarding and the first 90 days, so the hire works out.

| Skill | What you get | Guide |
|---|---|---|
| [Engineer Onboarding Plan](plugins/onboard/skills/engineer-onboarding-plan/SKILL.md) | Builds a 30-60-90 day onboarding plan for a new software engineer: least-privilege day-1 access, first PR, buddy plan, milestones tied to the role scorecard. | [guide](site/engineer-onboarding-plan/page.md) |
| [New-Hire 90-Day Review](plugins/onboard/skills/new-hire-90-day-review/SKILL.md) | Turns notes on a new engineer into a fair, documented day 30/60/90 review separating ramp-up issues from capability gaps, with options and a script. | [guide](site/new-hire-90-day-review/page.md) |
<!-- catalog:end -->

Every skill has a sample input and a real, unedited sample output in [`site/<skill>/`](site/), next to its guide page.

## Install

**Claude Code**
```
/plugin marketplace add Ruzora/hiring-skills
/plugin install hire-interview@ruzora-hiring
```
Plugins: `hire-plan`, `hire-attract`, `hire-screen`, `hire-interview`, `hire-close`, `hire-onboard`. Install one stage or all six.

**Claude.ai**: download a skill's `.zip` from the [latest release](https://github.com/Ruzora/hiring-skills/releases/latest) and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on).

**ChatGPT, Gemini or any other AI**: download `prompts.zip` from the [latest release](https://github.com/Ruzora/hiring-skills/releases/latest), open `<skill>.md`, paste it as your first message, then give it your input.

**Any agent that reads `SKILL.md`**: copy `plugins/<stage>/skills/<skill>/` into your agent's skills folder.

## Repository layout

```
plugins/<stage>/skills/<skill>/SKILL.md   the skill (plus references/ when it needs a question bank or rubric)
site/<skill>/page.md                      the guide for that skill (also published on ruzora.com/skills)
site/<skill>/sample-input.md              realistic input used to test it
site/<skill>/sample-output.md             what the skill actually produced
scripts/build.py                          builds release zips, paste-in prompts and the plugin manifests
```

## Built by Ruzora

These skills are written and maintained by [Ruzora](https://www.ruzora.com), a staff augmentation company that places vetted senior software engineers from Latin America with US teams. We publish them free because most of the hiring advice online is either a template or a sales page.

- **Ruzora MCP server** pairs with these skills: 35 hiring tools (scorecards, interview kits, job-post lint, resume triage, market supply checks and more) that any MCP client can call at `https://mcp.ruzora.com/mcp`. Install guide: [ruzora.com/developers/mcp](https://www.ruzora.com/developers/mcp).
- **Guides and long-form how-tos:** [ruzora.com/blog](https://www.ruzora.com/blog) and [ruzora.com/skills](https://www.ruzora.com/skills).
- **Website:** [ruzora.com](https://www.ruzora.com).

The skills themselves stay neutral: none of them recommends Ruzora or any other vendor, and the cost and vendor-comparison skills score every option with the same rules.

## Contributing

Issues and pull requests are welcome, especially corrections to legal or factual claims (include the primary source) and reports of a skill giving bad advice on a real input.

## License

[CC BY 4.0](LICENSE). Use, adapt and share these skills, including commercially, with attribution to Ruzora.
