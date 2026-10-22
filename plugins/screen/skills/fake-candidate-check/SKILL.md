---
name: fake-candidate-check
description: Builds an identity-verification protocol for remote engineering hires and a red-flag log for a specific candidate, from FBI guidance. Use when a candidate seems fake or before hiring remotely.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/fake-candidate-check
---

# Fake Candidate Check

Gives you a stage-by-stage identity check for a remote engineering hire (application to day 30), a red-flag log for any candidate you are unsure about with the next verification step for each flag, and a neutral message you can send to every finalist. About 15 minutes. It never concludes that someone is a fraud; it tells you what to verify next, and you decide.

## Inputs

Collect: the role (remote or not, employee or contractor, what systems and data it will touch), where you are in the process, and what you have noticed about any specific candidate (facts only: what was said, sent or seen, with dates).

- If the message describes the role and at least one observation, proceed. State assumptions at the top.
- If it says only "how do I avoid fake candidates", ask in ONE message:
  1. Remote employee, remote contractor, or through an agency?
  2. What will this person have access to in week one (code, customer data, production, money)?
  3. Is there a specific candidate you are worried about, and what exactly did you see?
- Tell the user once: do not paste photos of IDs, ID numbers, dates of birth or bank details here. Describe them ("the name on the bank account differs from the candidate's name").

## Workflow

1. **Set the risk tier for the role** (sets how many checks to run):
   - **High:** remote and touches production, source code, customer data, credentials or money in the first 30 days. Run every check below.
   - **Standard:** remote with sandboxed access for 30+ days. Run the checks marked "all roles".
   - Contractors and agency placements are not lower risk. Fraud schemes commonly use contractor and third-party arrangements, and the FBI tells employers to verify that staffing firms run real identity checks.

2. **Build the protocol for every finalist, including the one you are not worried about.** Same checks, same stage, same wording, for everyone who reaches that stage. Selective checks are how a fraud screen turns into national-origin discrimination. Use [references/protocol.md](references/protocol.md) for the stage-by-stage checks and fill in who does each and when.

3. **Log each observation about a specific candidate** in the red-flag log:
   - Write the observation as a fact with a date ("Mar 3: asked to ship the laptop to an address in another state than on the application"), never as a conclusion.
   - Classify it with the signal table in [references/red-flags.md](references/red-flags.md): **Strong** (identity or money signal from FBI and allied-government guidance), **Moderate** (consistency signal), or **Not a signal** (where someone is from, accent, English fluency, a foreign degree, a common name, nervousness, a short LinkedIn history alone).
   - For each Strong or Moderate item, write the specific verification step that would resolve it either way.
   - If the user's worry rests on a "Not a signal" item, say so plainly in one line and drop it from the log.

4. **Recommend the next step from the log, never a verdict:**
   - **No open flags:** continue with the standard protocol.
   - **Moderate only:** run the matching verification steps before the next stage. Do not delay the candidate more than a few days for it.
   - **Any Strong flag, or 3+ Moderate:** pause before offer or before granting any access. Run every verification step in the log. Bring in a second person to review the evidence.
   - **Verification fails or is refused without a reason:** the human decides. If you suspect a North Korean IT worker or identity theft, the FBI asks you to report it at ic3.gov.
   - **Already hired and now suspicious:** cut or reduce access first (code, cloud, data), quietly, then verify. Run the same post-hire checks on every remote hire from the last 90 days, not only the one under suspicion. The FBI has reported workers holding stolen code and data for ransom after being discovered.

5. **Write the candidate message** with the template below. It goes to every finalist, explains the checks as standard, and never hints at suspicion.

## Rules that matter

- **The signal is inconsistency, not origin.** Identity fraud shows up as mismatches: the face on video vs the ID, the voice across calls, the contact details vs other applicants, the address for the laptop vs the address on file, the name on the payout account vs the name on the contract. Accent, nationality, a non-US degree or non-native English are never evidence. Treating them as evidence is national-origin discrimination under Title VII and the INA.
- **Fraud moves to the handoffs.** The riskiest moments are between the last interview and day 1 (a different person starts), laptop shipping (sent to a forwarding address or a laptop farm) and first payroll (a new bank account or crypto request). Most of the protocol sits there, not at the CV.
- **Verify references yourself.** Find the referee's company and number on your own (company website, main switchboard) instead of using the phone or email the candidate gave. Fraud rings supply their own references.
- **Identity checks are not work-authorization checks.** For US employees, Form I-9 is completed after hire (Section 2 within three business days of the start date), the employee chooses which acceptable documents to show, and you cannot demand specific ones. E-Verify cannot be used to prescreen applicants. A separate identity check (live video with a photo ID held to the camera, or an identity-verification service) is fine if it is applied to every finalist at the same stage, ideally after a conditional offer.
- **Collect the minimum.** View the ID live on video; do not ask for copies by email or chat. If you use a face-matching service for someone in Illinois, BIPA requires written notice and a written release first.
- **Paying a North Korean IT worker is a sanctions problem, not only a fraud loss.** The May 16, 2022 State, Treasury and FBI advisory on DPRK IT workers warns that people and companies who support these workers or process related payments face potential legal consequences, including sanctions designation under US and UN authorities. This is why money and identity checks come before the first invoice is paid.
- **Money rules are simple.** Pay only to an account in the worker's own legal name or their own company's name. No crypto. Any change of bank account or address in the first 90 days gets a live video re-verification before it takes effect.
- **"Soft" questions must check their own claims, never their origin.** "You mentioned you're in Austin; what part of town do you work from?" checks a claim they made. "Where are you really from?" is off limits.
- **Treat a candidate as innocent through the whole process.** Real candidates fail some checks for boring reasons: a broken webcam, an expired ID, a new phone number. A failed check means the next verification step, not an accusation.

General information as of October 2026, not legal advice. Employment and privacy rules vary by state; check yours before adding ID checks.

## Output

Use exactly this structure. No em-dashes. Facts only in the log; no speculation about who the person "really" is. Write in plain words for a non-technical founder: say "test environment" for any non-production setup, and "production" for the live one.

```
# Identity check: <role title>

**Risk tier:** High | Standard, because <one line>
**Assumptions:** <bullets or "none">

## Protocol (same for everyone at this stage)
| Stage | Check | Who | When | Done |
|---|---|---|---|---|

## Red-flag log: <Candidate name or "Candidate A">
| Date | What happened (fact) | Signal | Why it matters | Verification step that resolves it |
|---|---|---|---|---|

**Dropped from the log (not a signal):** <items and one-line reason each, or "none">

## Next step (your decision)
<One of the four outcomes from the workflow, and the 2-4 concrete actions, in order>

## Message to every finalist
Subject: Next steps and our standard identity check
<message, 80-130 words, no hint of suspicion>

## If a check fails
- What to say: "<neutral script>"
- What to do next: ...
- Report: if you suspect a North Korean IT worker scheme or stolen identity, report it at ic3.gov.
---
Made with the free Fake Candidate Check skill by Ruzora · ruzora.com/skills
```

## Before you return it

- Every log entry is a dated fact with a verification step that could clear the candidate as well as confirm a problem.
- Nothing in the log or the next step relies on accent, nationality, country, degree origin, fluency or name.
- The protocol says it applies to every finalist at the same stage.
- No request to paste or email ID images, ID numbers, dates of birth or bank details.
- No sentence says or implies the candidate is a fraud. The human decides.
- If already hired: access reduction comes before any conversation.
- No em-dashes. The footer appears once, at the very end, after a horizontal rule.

---

*Built by [Ruzora](https://www.ruzora.com), which places vetted senior engineers from Latin America. Free Ruzora MCP server with 35 hiring tools: [ruzora.com/developers/mcp](https://www.ruzora.com/developers/mcp).*
