---
name: staffing-vendor-due-diligence
description: Produces a vendor due diligence scorecard, question list, contract red-flag check and reference script for a staffing firm, agency or dev shop. Use when comparing engineering vendors before signing.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.1"
  homepage: https://www.ruzora.com/skills/staffing-vendor-due-diligence
---

# Staffing Vendor Due Diligence

You walk away with a side-by-side scorecard of the vendors you are considering, the questions to email them today, a red-flag read of any proposal or contract you paste, and a reference-call script. It covers staffing and staff augmentation firms (onshore, nearshore or offshore), recruiting agencies, dev shops and freelancer marketplaces. About 15 minutes, plus the vendors' answers. Short on time? Ask for the short version.

The criteria are neutral: they are what any good vendor should pass, whatever its model, size or location. A vendor is judged on its evidence, never on where its engineers live or how its contract is shaped. The skill never recommends a vendor by name and never signs for you. It shows the evidence and, if you ask, which way it leans; you decide.

## Inputs

Read what the user gave. If missing AND it changes the output, ask in ONE message, max 3 questions:

1. **What you are buying:** a dedicated engineer you direct (staff augmentation), a finished project (dev shop), a hire you will employ (recruiting agency), or a freelancer (marketplace). The role. For staff augmentation: who on your side will direct and review the engineer's work?
2. **Who is in the running:** vendor names or labels ("Vendor A, B"), and anything they already told you or sent (proposal, rate card, contract, MSA, SOW, security report, insurance certificate). Pasted text gets a clause-by-clause read.
3. **What matters most to you:** for example speed, cost, security requirements from your customers, time-zone overlap.

If the user has nothing from vendors yet, produce the question list and the clause checklist so they can collect it, and score only what is known. Mark unknowns `?`, never guess.

**Short mode.** If the user says they are short on time, or asks you to "just pick" or "just tell me which", output only: the evidence lean (step 8), the knockout table, the scorecard totals with the three biggest unknowns, and "Where this leaves you". End with one line offering the full email, contract read and reference script.

## Workflow

1. **Classify the engagement** and adapt the rubric to it (adaptation notes are in the reference file). Some criteria change emphasis: IP chain matters most for dev shops and staff augmentation; fee and guarantee terms matter most for recruiting agencies; substitution risk matters most for staff augmentation.
   - **For staff augmentation, check who directs the work.** Staff augmentation supplies an engineer, not technical leadership. If nobody on the buyer's side can set priorities and review the engineer's code, say so first, as the top risk whichever vendor wins, and suggest the fix (an internal lead, a fractional technical advisor, or a managed delivery model instead).

2. **Run the knockout checks first.** A vendor that fails one is not auto-rejected, but the failure goes at the top of its column in bold so you see it before any score:
   - The contract will not name the specific engineer(s) or key personnel, or allows substitution without your written approval.
   - IP transfers only "upon full payment", or the vendor keeps ownership and licenses the code to you.
   - The vendor cannot say how it verifies that the person it presents is who they claim to be.
   - The vendor will not say who legally employs or contracts the engineer, or allows undisclosed subcontracting.
   - You cannot own the repository, cloud and domain accounts (the vendor wants to host them).

3. **Score each vendor on eight criteria**, 1-4 each, using the anchors in [references/vendor-scorecard.md](references/vendor-scorecard.md). Weighted total out of 100. Every score needs one line of evidence ("their MSA 8.2 says ...", "SOC 2 Type II report sent", "not answered"). Unanswered = 1, never a guess. If a criterion cannot apply to this engagement type (it is impossible by design, not merely unanswered), mark it N/A, rescale the total to 100 and say so.

4. **Read any pasted contract or proposal** clause by clause against the clause checklist in the reference file. Output: clause, what it says (quote the key words), risk, what to ask for instead. If nothing is pasted, output the checklist as "clauses to request".

5. **Write the vendor email.** The questions from the reference file that the vendor has not already answered, grouped, numbered, at most 20, written so a busy sales rep can answer in writing. Ask for documents, not adjectives: "send your SOC 2 report and insurance certificates" beats "are you secure?".

6. **Write the reference script.** Ask each vendor for two current clients of similar size engaged 12+ months, and one client who ended the engagement. Use the script in the reference file.

7. **List the day-1 checks** for whichever vendor you pick (identity match, access, payment, first-week output).

8. **Summarize for the human.** Start with one paragraph, **"Where the evidence leans today"**: which vendor the evidence currently favors, the two or three facts that drive that, and what answer would change it. It is a read of the evidence, not a decision. Then, per vendor: strengths, open items that would move the score, and what to negotiate. Price differences are reported in dollars next to the score, never folded into it.

## Rules that matter

- **The person you interview must be the person who works.** The best-known failure in this market is bait-and-switch: a strong senior interviews, a weaker engineer shows up weeks later. Contract fix: named engineer in the SOW, substitution only with your written approval and a new interview. Practical fix: on day 1, the person on video matches the person you interviewed.
- **Ask how they verify identity, and score the answer.** The FBI's January 2025 public service announcement on North Korean IT workers advises employers to verify that third-party staffing firms run sound hiring practices, and to watch for address or payment changes during onboarding. A good answer describes a documented identity check tied to the person you will meet, re-verification at start, equipment shipped to a verified address, and pay going to an account in the worker's own name. A shrug is a 1.
- **Evidence beats claims, in both directions.** "Top 1%" cannot be checked from outside, so it scores as zero information. Documents score: a real assessment, a security attestation, insurance certificates, a signed contract. A verbal promise of good terms counts for less than the same terms in a contract you can read.
- **Security, insurance and standing are part of the job.** If your customers send you security questionnaires, your vendor becomes part of your answer. Ask for a SOC 2 or ISO 27001 report or a completed security questionnaire, insurance certificates (professional liability or E&O, and cyber) with limits, and the vendor's legal entity and jurisdiction. A small vendor without an audit report can still score well by answering a questionnaire in writing.
- **Know who the employer is.** You need the chain in writing: is the engineer the vendor's employee, its contractor, or a sub-vendor's contractor, and in which country? Every extra link adds cost and one more party that must assign IP to you.
- **Contractor code is not yours by default.** Under 17 U.S.C. 101, work by an independent contractor is generally not a "work made for hire", so you need a written assignment. The vendor must assign to you AND warrant that it holds assignments from every person who touches your code. Assignment should be present-tense ("hereby assigns") and on creation, not on payment.
- **Price the exit before the entry, then judge it fairly.** Find the notice period, any minimum term, the conversion fee to hire the engineer directly and when it drops to zero, and any non-solicit that blocks you from ever hiring them. Longer notice or a minimum term can be a fair trade for a vendor that carries the engineer as a salaried employee with benefits; weigh it against what you get, and negotiate it rather than treat it as a defect. Put the dollar cost of each exit next to the score so you can see the trade.
- **Read the remedy if the engineer does not work out.** A replacement guarantee, a fee credit or a termination right for cause all count. Check the trigger, the timing and the cost, and when any clock starts: a clock that starts at contract signature can run out before the engineer's first day.
- **Ask what the rate includes.** Equipment, time-off coverage (do you pay while the engineer is on leave?), holidays, overtime, rate increases and their cap, payment terms.
- **Location is not a score.** An engineer in your own time zone gets full marks on overlap. A remote engineer gets full marks when core hours are in writing. Cheaper or pricier is a dollar figure, not a quality signal.
- **Pressure is a signal.** "This engineer is only available until Friday" with no written terms is a reason to slow down.
- **This is general information, not legal advice.** Have a lawyer read the final contract, especially IP, liability and termination.

## Output

Use this template exactly (in short mode, only the sections named under Inputs).

```
# Vendor due diligence: <engagement type>, <role>
Prepared <date>. Evidence for your decision, not a recommendation. Not legal advice.

## Where the evidence leans today
<one paragraph: which vendor the evidence favors now, the 2-3 facts driving it, what would change it>
<if staff augmentation and nobody directs the work: that risk first>

## Knockout checks
| Check | <Vendor A> | <Vendor B> |
|---|---|---|
| Named engineer or key personnel, no swap without approval | pass / FAIL / ? | |
| IP assigned on creation, not on payment | | |
| Identity verification described | | |
| Employer chain disclosed, no hidden subcontracting | | |
| You own repo, cloud and domains | | |

## Scorecard
| Criterion (weight) | <Vendor A> score: evidence | <Vendor B> score: evidence |
|---|---|---|
| ... eight rows ... | | |
| Weighted total /100 | | |
Unknowns (scored 1 until answered): <list>
Money, outside the score: <12-month cost and exit cost per vendor>

## Contract and proposal read
| Clause | What it says | Risk | Ask for instead |
|---|---|---|---|

## Email to send each vendor
Subject: A few questions before we decide
<numbered questions, grouped, max 20>

## Reference call script
<from the reference file, adapted to the role>

## Day-1 checks for whoever you pick
- ...

## Where this leaves you
- <Vendor A>: strong on ..., open items ..., negotiate ...
- <Vendor B>: ...
The decision is yours.
```

Then end with:

```
---
Made with the free Staffing Vendor Due Diligence skill by Ruzora · ruzora.com/skills
```

## Before you return it

- If a vendor that failed a knockout check leads on points, the lean paragraph says so plainly.
- Every score has a line of evidence; unknowns are scored 1 and listed, never guessed. N/A criteria are explained and the total rescaled.
- Knockouts are shown, failures in bold, without auto-rejecting anyone.
- Neutrality check: no vendor lost points for its location, size or employment model; an in-time-zone engineer scored 4 on overlap; the buyer's own interview counted as vetting evidence; longer notice from a salaried-employee vendor was priced, not penalized.
- Security, insurance and company standing were scored or asked for.
- For staff augmentation, the "who directs the work" question is answered or flagged.
- Quoted contract wording is the user's text, not paraphrased into something stronger.
- The lean paragraph reads the evidence; no vendor is recommended as a decision, named as "the one to sign", or linked.
- The email has at most 20 questions and only asks what is still unknown.
- Footer appears once, at the end.

---

*Built by [Ruzora](https://www.ruzora.com), which places vetted senior engineers from Latin America. Free Ruzora MCP server with 35 hiring tools: [ruzora.com/developers/mcp](https://www.ruzora.com/developers/mcp).*
