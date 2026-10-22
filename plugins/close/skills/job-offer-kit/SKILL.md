---
name: job-offer-kit
description: Builds a job offer kit for an engineering hire: pre-close questions, verbal offer script, written offer email, negotiation playbook and close plan. Use when making or negotiating a job offer.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/job-offer-kit
---

# Job Offer Kit

Tell it who you're hiring, what you can pay, and what you know about the candidate's situation. In about 10 minutes you get: the questions to ask before you make the offer, a script for the offer call, a paste-ready offer email, an equity explanation in plain words with your numbers, a negotiation playbook with your flex order decided in advance, and a plan to keep the candidate warm until day one. You make the offer; this gets it ready.

## Inputs

Collect:
1. **Role, level, start date wanted, and where the candidate will work** (US state or country). The candidate's work location decides which pay and contract rules apply, not your HQ.
2. **The package**: base salary band (minimum, target, maximum you would go to), equity (number of options or shares, and if known the total fully diluted shares, strike price, vesting schedule), sign-on budget if any, benefits in one line.
3. **What you know about the candidate**: what they said they care about, their stated salary expectation, other offers or processes, their decision date, who else is involved in their decision.

Ask at most 3 questions, in one message, only when the answer changes the kit: no salary band at all, no idea where the candidate works, or no equity details when equity is part of the offer. Otherwise proceed and mark assumptions in brackets, e.g. [assumed: 4-year vesting, 1-year cliff].

If the user's plan contains a problem (asking for current salary, a 24-hour exploding offer, a non-compete for a California worker, promising future equity verbally), fix it in the kit and say what you changed in section 0. Don't lecture.

## Workflow

1. **Check the plan against the rules** below and list fixes in section 0.
2. **Pre-close.** If the user has not asked the pre-close questions, write them for a short call before the offer. If they have, use the answers. Goal: no number in the offer surprises the candidate, and you know the decision criteria and timeline before you name a number.
3. **Set the numbers before the call.** Opening offer, the flex order (what you give first, second, third), and the walk-away point. Open at or slightly below target, never at your maximum, so you have room to say yes once. If the candidate's stated number is inside your band and a competing offer is live, open at target. Keep the base inside the band you would defend to the current team: an outlier salary for one hire becomes a retention problem with the others.
4. **Write the verbal offer script.** The founder or hiring manager calls, by phone or video, not email first. Order: why them (2-3 specific things from the interviews), what they will own in the first 6 months, then the numbers, then silence. Ask for their reaction, not a decision.
5. **Write the offer email** to send within a few hours of the call, with the formal letter attached or to follow. Use [references/offer-letter-checklist.md](references/offer-letter-checklist.md) for what goes in and what stays out.
6. **Write the equity explainer** with the user's actual numbers, using the plain-words template in [references/equity-and-negotiation.md](references/equity-and-negotiation.md). If a number is missing, show the formula and mark the blank instead of guessing.
7. **Build the negotiation playbook**: the likely asks for this candidate (from what they said they care about) and the response to each, trading rather than conceding.
8. **Plan the counteroffer and the deadline** honestly (Rules).
9. **Write the close plan** from verbal yes to day one.

## Rules that matter

- **Never ask for salary history.** Ask what they're looking for. Pay-history bans exist in many states and cities, and the location that counts is often where the candidate works. Price the offer from your band and the market, not from their current pay. If the user's plan says "beat their current salary by 10%", replace it with "anchor to our band; their stated expectation is the reference point".
- **Speed is part of the offer.** Make the verbal offer within one or two working days of the final interview, and send the written offer the same day as the call. Every extra day gives competing processes time to finish.
- **Pre-close before you offer.** Three things must be known before the call: what else is in play and its timeline, how they will decide (their top 2-3 criteria in their words), and what they would do if their current employer counters. An offer made without these is a guess.
- **Trade, don't concede.** When they ask for more, ask what else is open first ("If we solve the base, is there anything else between you and a yes?"), then trade: "If I can get to X, are you ready to accept today?" Aim for one round, two at most. Use the flex order you decided before the call.
- **Know what each lever is for.** A sign-on bonus fixes a one-time loss (a bonus or unvested equity they leave behind) without raising the salary band. Equity fits someone who believes in the company and can afford lower cash. Start date is cheap for you and often worth a lot to them. Title inflation is the expensive lever: it sets expectations you will pay for at the next review. If you want a sign-on bonus to be repayable when someone leaves early, have counsel draft that condition. In California, since 2026-01-01 (AB 692, Labor Code 926 and Business and Professions Code 16608), repayment is allowed only if it sits in a separate agreement, the worker gets at least 5 business days to consult a lawyer, it is prorated and interest-free, the retention period is 2 years or less, the worker may choose to receive the bonus at the end of the period instead, and repayment applies only if they quit or are fired for misconduct. Other states have their own limits, so counsel checks it.
- **Deadlines: honest, not exploding.** Give a decision date of about 3-5 business days, explain the real reason ("we have two other finalists we'd need to update"), and extend once if they ask for a concrete reason (a final round elsewhere). A 24-hour exploding offer to a senior engineer signals that they won't be treated well, and a forced yes is the yes most likely to renege. Never invent a competing finalist.
- **Counteroffers: raise them early, never bid against them.** In the pre-close, ask: "If your manager offers you more to stay, what will you do?" Then ask them to talk through their resignation conversation. If a counter comes, go back to their own reasons for looking, in their words. Re-open your offer only if your number was below the band you set, never to win an auction.
- **Equity in plain words, both units.** Give the number of options and the percentage of fully diluted shares; a share count alone means nothing. Explain vesting, cliff, strike price, the exercise window after leaving, and dilution. Never state what the equity "will be worth". Illustrative exit math is labeled as an example, with the note that investors with preferred shares are paid back before common holders. Add: "This is not tax advice; talk to a tax advisor about your situation."
- **Nothing important is verbal only.** Every promise (equity, refresh grants, title review in 6 months, remote policy) is either in the written offer or not made. Future grants are never promised on the call.
- **The offer letter is not meant to be an employment contract.** Unless you intend a contract, the letter states that employment is at will (in the states where that applies) and avoids words like "guaranteed", "permanent" or a fixed term. Have counsel review the template once, then reuse it. Contingencies are listed (reference check, background check with written consent, proof of authorization to work completed on Form I-9 within 3 business days of the start date). Never make the offer conditional on citizenship.
- **No non-compete for California workers.** Since 2024 California makes it unlawful to include one in an employment contract for a California employee (Business and Professions Code 16600.1), with limited exceptions. Several other states restrict them too. Confidentiality and IP-assignment agreements are normal; non-competes need counsel.
- **The close continues after yes.** The weeks between acceptance and day one are when candidates back out. Plan contact: a call from a future teammate, equipment shipped early, the first-week plan sent, founder check-in a few days before the start.

- **Name only the laws this skill lists.** California rules for hires are listed in [references/offer-letter-checklist.md](references/offer-letter-checklist.md). For any other state, describe the issue and write "ask counsel to confirm" (for example "your state may restrict non-competes; ask counsel to confirm"). Never state thresholds, amounts or section numbers that aren't in this skill.

General information as of 2026-10, not legal or tax advice.

## Output

Use exactly this structure.

```
# Offer kit: <candidate code or first name>, <role>

**Assumptions:** <...>

## 0. Changes to your plan
| What the plan said | What the kit does instead | Why (one line) |
|---|---|---|
(or "None.")

## 1. Pre-close call (10 minutes, before the offer)
<5-6 questions, each with what you are listening for>

## 2. Your numbers (internal, do not send)
| | Base | Equity | Sign-on | Start date | Other |
|---|---|---|---|---|---|
| Opening offer | | | | | |
| Flex 1 / 2 / 3 | | | | | |
| Walk-away | | | | | |
**Deadline to give:** <date and the honest reason>

## 3. Verbal offer script
<opening, why them (2-3 specifics), what they'd own, the numbers, the question to ask, what to say if they ask for time>

## 4. Offer email (send within hours of the call)
Subject: ...
<body; attach or follow with the letter>

## 5. Offer letter checklist
<in / leave out, adapted to this hire; counsel review line>

## 6. Equity in plain words (send to the candidate)
<template filled with their numbers; blanks marked; not-tax-advice line>

## 7. Negotiation playbook
| If they say | You say / do | Lever and limit |
|---|---|---|

## 8. Counteroffer and deadline
<script for the pre-close counter question, the resignation rehearsal, and the response if a counter arrives; deadline extension rule>

## 9. Close plan: yes to day one
| When | What | Who |
|---|---|---|
```

## Before you return it

- No question or line asks for current or past salary, bonus or equity.
- Every number in the kit comes from the user or is marked [assumed] or left as a blank. Nothing about the candidate is invented.
- Equity shows both the option count and the percentage, or shows the formula with a blank.
- No "will be worth", no promised future grants, no "guaranteed".
- The deadline is at least 3 business days unless the user gave a real reason otherwise, and the reason given is true as far as the user said.
- Legal lines carry "as of 2026-10" and "not legal or tax advice"; state-dependent points say so.
- Plain punctuation: no em-dash characters anywhere, including inside brackets and blanks.
- The footer is the last line, after a horizontal rule, and never inside the email or the equity text the candidate will see.

End the output with:

---
Made with the free Job Offer Kit skill by Ruzora · ruzora.com/skills

---

*Built by [Ruzora](https://www.ruzora.com), which places vetted senior engineers from Latin America. Free Ruzora MCP server with 35 hiring tools: [ruzora.com/developers/mcp](https://www.ruzora.com/developers/mcp).*
