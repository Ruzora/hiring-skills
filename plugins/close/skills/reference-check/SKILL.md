---
name: reference-check
description: Builds a reference-check plan for an engineering finalist: referee identity checks, a call script aimed at the risks found in interviews, and a risk register. Use when checking references.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/reference-check
---

# Reference Check

Give it what worried you during the interviews and the referees the candidate named. In about 10 minutes you get: a check that each referee is a real person who actually worked with the candidate, a 15-minute call script aimed at those specific worries, a list of questions you must not ask, and a risk register to fill in as you call. You decide what the answers mean.

## Inputs

Collect:
1. **The open risks from the interview loop.** Debrief notes, scorecard gaps, or just "what still worries you". If the user has none, use the default risks for the level (see Workflow step 1) and say so.
2. **The referees**: name, claimed title and company, relationship to the candidate (manager, peer, report, client), contact details as given by the candidate.
3. **The candidate's claims you want confirmed**: titles, dates, team size, "I led X". Pull them from the CV or notes if pasted.
4. **Who is calling**: the user themselves, or a background-check or reference-check company. This changes the legal steps.

Ask at most 3 questions, in one message, only if the answer changes the plan: no risks and no notes at all, no referee details, or unclear whether an outside company is doing the calls. Otherwise proceed with stated assumptions.

Privacy: don't paste the candidate's ID documents, date of birth or health information here. Keep referee details to name, company, title and work contact.

## Workflow

1. **Turn worries into 2-4 named risks.** Each risk is one sentence that a referee could confirm or refute: "May not have led the payments migration as claimed", "Slows down when requirements are unclear". If no risks were given, use the defaults: senior and above: scope of ownership, quality under deadline pressure, how they handle disagreement; mid-level: speed of learning, need for supervision, code quality. More than 4 risks means the interview loop has not done its job; say so and pick the 4 that matter most.
2. **Map each risk to the best referee.** A manager the candidate reported to beats a peer for performance and ownership. A peer beats a manager for collaboration and code quality. A direct report is best for leadership. If no referee was a manager, ask the candidate for one by role: "Who was your manager during the migration project?" Peer-only references are a gap to note, not an automatic problem.
3. **Verify every referee before calling** (the fraud check). Fake references are part of the fake-candidate kit, and the FBI's January 2025 advisory on North Korean IT workers tells employers to verify identity throughout hiring. For each referee:
   - Find them yourself, not through the candidate's links: the company website, their professional profile history (account age, work history that matches, connections at that company), conference talks, commit history in the company's public repos.
   - Reach them through a channel the candidate did not supply: the company's main phone line (ask to be put through), or an email at the company's domain. A personal Gmail and a mobile number given by the candidate are not enough on their own.
   - Confirm overlap: same company, same period, and a working relationship. Ask the referee early in the call: "When did you work with them, and what was your role relative to theirs?" Then check the dates against the CV.
   - Red flags: the company can't be found or no longer exists and nobody else from it can be reached; the referee only takes calls at times the candidate arranges; the referee can't name one specific project; answers that sound read from the CV; two referees with the same writing style or phone carrier pattern; a referee who is enthusiastic but can't describe a single weakness or disagreement.
   - If a referee can't be verified, don't accuse anyone. Ask the candidate for an alternative referee at a company you can verify, and record "unverified" in the register.
4. **Get consent and set expectations.** Tell the candidate which references you will call and when. Never contact a current employer without the candidate's explicit OK, and treat any backchannel (a person the candidate did not name) as unverified, single-source information: never the sole reason for a no, and the candidate gets a chance to respond to any factual concern it raises.
5. **Write the call script** from the bank in [references/question-bank.md](references/question-bank.md): the same 5 core questions for every referee (so answers can be compared across referees and candidates), plus 1-2 targeted questions per risk for that referee. 15 minutes. The calibration and rehire questions are mandatory.
6. **Build the "do not ask" box** for the caller, and include what to do if a referee volunteers protected information: stop, don't write it down, redirect to the work.
7. **Prepare the register** so each call fills it in: risk, what each referee said (quote), status (resolved / confirmed / mixed / unverified), and what to do (offer as planned, add to the 90-day plan, follow up with the candidate, or pause).
8. **Add the legal steps** that apply (Rules below), in one short box.
9. **Draft the two short emails**: the request to the candidate for referees (by role), and the request to each referee for a 15-minute call.

## Rules that matter

- **Check references to test specific risks, not to collect compliments.** Candidates pick referees who like them. Generic questions ("Was she a good engineer?") get generic praise. Questions about a named project, a ranking, and a rehire decision get signal.
- **Listen for enthusiasm, not for negatives.** Referees rarely say bad things. The signal is the gap between "yes, absolutely, I'd try to hire her today" and "yes, she'd be fine in the right role". A pause before the rehire question, faint praise, or "she was very reliable" for a senior engineer are data. Write down the exact words.
- **Ask for a ranking.** "Of the engineers at her level you've worked with, is she in the top 5%, 10%, 25% or 50%?" Referees who will not say anything negative will still often refuse to say "top 5%".
- **Check the referee's dates against the whole CV, not only the job they share.** The overlap the referee describes must fit the candidate's dates at that company and must not collide with the candidate's other jobs on the CV (a referee who "managed him in 2023" when the CV puts him at another company in 2023 is a mismatch). Write the referee's stated dates in the register next to the CV dates.
- **A factual mismatch is a stop sign.** If a referee contradicts a title, dates, or the candidate's role in a project ("I led that, she worked on part of it"), pause the offer and ask the candidate about it neutrally. A different memory of a project is common. A fabricated title or employer is not.
- **One vague negative does not outweigh structured interview evidence.** Two referees independently describing the same weakness does matter: add it to the 90-day plan or reconsider.
- **Never ask about**: age, health, disability, sick days or absences, medical or family leave, pregnancy or family plans, religion, national origin or citizenship, race, marital status, arrest record, workers' compensation claims, union activity, or salary. Salary is on the list because pay-history bans in many states and cities also cover asking through someone else: California's Labor Code 432.3 bars seeking an applicant's salary history "personally or through an agent". For a remote role, the candidate's location can bring a ban into play even if your state has none, and past pay is a poor guide to what the role is worth anyway: price the role from your own band. Ask only about job-related behavior, the same way for every candidate.
- **When an outside company makes the calls, federal consumer-reporting law applies.** Under the Fair Credit Reporting Act (FCRA), a reference check run by a background-check or reference-check company is a consumer report, and when it gathers opinions about character or work through interviews it is an "investigative consumer report". Before ordering: a clear disclosure in a standalone document and the candidate's written authorization; for investigative reports, a disclosure within 3 days of ordering that one may be made (15 U.S.C. 1681d). Before rejecting anyone based on it: a pre-adverse-action notice with a copy of the report and the summary of rights, a waiting period (5 business days is common practice, not a statutory number), then a final adverse-action notice naming the agency. Calls the employer makes itself are not consumer reports, but keep notes and apply the same fairness rules. General information as of 2026-10, not legal advice; states add their own rules.
- **Do references last and fast.** Run them once the team is a "yes, pending references", within 2 working days, with the candidate's consent. Earlier wastes referees' goodwill on candidates you won't hire; later costs you the candidate.

## Output

Use exactly this structure.

```
# Reference check plan: <candidate code or first name>, <role>

**Assumptions:** <...> · **Who calls:** <you / outside company (FCRA steps below apply)>

## 1. Risks to test
| # | Risk (confirmable or refutable) | Source (which interview / note) | Best referee |
|---|---|---|---|

## 2. Referee verification
| Referee | Claimed role and relationship | How to verify independently | Red flags in what was provided | Status |
|---|---|---|---|---|
**Missing referee types:** <e.g. no manager; what to ask the candidate for>

## 3. Call script (15 minutes, same core for everyone)
**Opening (read as written):** <who you are, that the candidate gave permission, 15 minutes, answers stay confidential to the hiring team>
**Verify the relationship:** <when, what role relative to the candidate>
**Core questions (every referee):**
1. ...
**Targeted questions for <referee>:** <risk # -> question + the follow-up if the answer is vague>
**Close:** "Is there anything I should have asked and didn't?" / "Anyone else who worked closely with them I should talk to?"

## 4. Do not ask (keep this next to you on the call)
<list> · **If they volunteer it:** <script>

## 5. Notes and risk register (fill in during calls)
| Risk | Referee A said (quote) | Referee B said (quote) | Status | Action |
|---|---|---|---|---|
**Rehire answer, word for word:** A: ___ B: ___
**Ranking answer:** A: ___ B: ___
**Factual mismatches:** ___

## 6. How to read the results
<4-6 lines: what would resolve each risk, what would confirm it, what is a stop sign. The hiring manager decides.>

## 7. Legal steps that apply
<employer-made calls OR outside company: the FCRA sequence; one line "General information as of 2026-10, not legal advice.">

## 8. Emails
**To the candidate:** <subject + body asking for referees by role, timing, consent>
**To each referee:** <subject + body, 15 minutes, 2 proposed times>
```

## Before you return it

- Every targeted question ties to a named risk; no question is generic filler.
- Every referee has an independent verification route that does not rely on contact details from the candidate.
- No question touches the "never ask" list, including pay. If the user asked for one of those, the output says it was removed and why, in one line.
- Nothing about the candidate or referees is invented. Unknowns say "unknown".
- The plan never tells the user to reject the candidate; it says what each outcome would mean and leaves the call to them.
- The legal box matches who is calling.
- The footer is the last line, after a horizontal rule, and does not appear in the emails.

End the output with:

---
Made with the free Reference Check skill by Ruzora · ruzora.com/skills
