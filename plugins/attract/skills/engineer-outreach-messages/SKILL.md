---
name: engineer-outreach-messages
description: Writes honest 3-touch outreach to passive senior engineers plus a referral ask for a founder's network. Use when you need a recruiter outreach template or to message engineers who aren't applying.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/engineer-outreach-messages
---

# Engineer Outreach Messages

You walk away with a 3-message sequence per candidate (email plus a short LinkedIn version), a referral ask you can send to your own network today, and a simple tracking sheet. About 10 minutes for a batch of 3-10 people.

## Inputs

Read what the user gave you. You need three things; ask for the missing ones in ONE message (at most 3 questions):

1. **The role in one breath:** what the hire will own, stack, pay range, location/remote rule, company stage. (A job post or role scorecard is enough.)
2. **The people:** for each candidate, what the user actually knows about them and HOW they found them (a repo, a conference talk, a blog post, a former colleague's intro, a search). Also where the person lives if known (country matters for privacy rules).
3. **Who signs it** (name and title) and whether a referral bonus exists.

If the user has no specific detail on a candidate, do not invent one. Write the message with a `[SPECIFIC: one real thing about their work]` slot and tell the user to fill it or skip that person.

## Workflow

1. **Write the one-line pitch** for the role: what they'd own + why now + range. Every message reuses it. If there is no pay range, put `[FILL: range]` and tell the user that leaving it out costs replies (LinkedIn data (2023) found 91% of US respondents say a salary range affects whether they apply, as reported by Search Engine Journal).
2. **Build a personalization line per candidate** from the user's facts only, and classify its strength: STRONG (their own work: code, talk, post, a product they built), WEAK (title and company only), NONE. For NONE, recommend skipping or finding one real detail first; a generic message to a senior engineer is worse than no message. Also check each person against the role's location rule: if they live outside it, either say so plainly in the message ("this role is US/Canada; would relocating or a later remote opening interest you?") or mark them Skip. Don't hide it until the call.
3. **Write touch 1, 2, 3** per the rules. Touch 2 and 3 are shared templates with a per-candidate line, so a batch stays fast.
4. **Write the referral ask** (network email + a forwardable blurb + a LinkedIn post).
5. **Write the tracking sheet** and the opt-out rule.
6. **Self-check** and return.

## Rules that matter

**Honesty (non-negotiable)**
1. **Say how you found them, truthfully.** "I read your post on Postgres partitioning" only if the user said so. If they came from a search, write "I found your profile looking for engineers who have run Django at scale." Fake familiarity ("loved your work!") is the fastest way to be ignored by seniors, who get these weekly.
2. **No fake urgency or scarcity.** No "only 2 seats left", "closing Friday", fake "Re:" or "Following up on our call" subject lines, unless literally true.
3. **Don't overstate the company.** Funding, customers and growth numbers come from the user only. "Well-funded" with no number reads as a dodge; give the number or say nothing.
4. **Never reference a protected characteristic** (gender, ethnicity, age, nationality, disability, religion) as the reason you reached out, even with good intent. Outreach is about their work.
5. **Opt-outs are permanent.** Any "not interested", "stop", or no reply after touch 3 goes on a do-not-contact list. Don't switch channels to reach someone who said no. Every message after the first ends with an easy out ("If now's not the time, just say so and I won't follow up").
6. **EU/UK candidates (GDPR).** If you collected their details yourself (not from them), Article 14 GDPR requires telling them, at the latest at first contact, who you are and how to reach you, where you got their details, why you are using them and on what legal basis, how long you keep them, and that they can object or ask for access or deletion. In practice: one line in touch 1 naming the source and offering deletion, plus a link to a short privacy notice that covers the rest. One line alone is not enough. General information, not legal advice.

**What earns a reply**
7. **First message carries the offer, not a teaser.** In under 120 words (not counting the signature and the EU/UK data-source/privacy line): one true line about them, what they'd own, stack, stage, pay range, remote rule, and one small ask (a 20-minute call, no prep). "Can I tell you about an exciting opportunity?" with nothing else gets deleted.
8. **The founder or hiring manager signs it**, from their own address, in plain text. No logos, no tracking-pixel newsletter look, no recruiting alias.
9. **Subject line = specific and boring.** "Owning payer integrations at a 14-person health startup" beats "Quick question" or "Exciting opportunity".
10. **Use the right inbox.** Personal email or LinkedIn, never their current work email (their employer can read it, and it puts them in an awkward spot).
11. **Cadence:** touch 1 on day 0; touch 2 on day 4-5 adding ONE new fact (a real problem, the team, a link to something you shipped), never "just bumping this"; touch 3 on day 10-14, short, closing the loop. Then stop. Y Combinator's guide to hiring the first engineer expects "two or three emails before you get a reply" and says cold outreach can take up to 6 months to produce a hire, so plan volume, not hope.
12. **Network first.** The same YC guide calls your personal network "the most important source by far" for early hires. The referral ask is usually the highest-return message in this kit, so send it first.

**Referral ask**
13. **Ask for a specific person, not "anyone".** "Who is the best backend engineer you've worked with who'd hate a big-company job?" gets names; "know anyone looking?" gets silence. Most good candidates aren't looking.
14. **Make forwarding effortless:** a 3-sentence blurb they can paste, with the range. Promise you'll tell them what happened.
15. **Bonus only if real.** State the amount and when it pays, or don't mention one.

## Output

Return exactly this:

```
## Assumptions
- <assumptions, or "None">

## Role pitch (one line)
<what they'd own + why now + range>

## Candidates
| Candidate | How found | Personalization line | Strength | Send? |
|---|---|---|---|---|
| <as user named them> | <source> | <the line, or [SPECIFIC: ...]> | STRONG / WEAK / NONE | Yes / Fill detail first / Skip |

## Touch 1 (day 0)
### <Candidate>
**Subject:** ...
<email body, under 120 words, signed by the user>

**LinkedIn version (2 sentences):** ...

<repeat per candidate>

## Touch 2 (day 4-5), template
**Subject:** Re: <touch-1 subject>  (same thread)
<under 80 words; one new fact; easy out>
Per-candidate new fact: <candidate>: <fact>

## Touch 3 (day 10-14), template
<under 50 words; closes the loop; easy out; no guilt>

## Referral ask
### Email to your network
**Subject:** ...
<under 150 words; asks for a specific kind of person by name>

### Forwardable blurb
<3 sentences with range and how to reach you>

### LinkedIn post
<under 100 words>

## Tracking sheet (copy into a spreadsheet)
| Name | Channel | How found | Touch 1 | Touch 2 | Touch 3 | Reply | Next step | Do not contact |
|---|---|---|---|---|---|---|---|---|

## Rules for sending
- <3-5 bullets: cadence dates for this batch, opt-out handling, GDPR line if any EU/UK person, stop after touch 3>

---
Made with the free Engineer Outreach Messages skill by Ruzora · ruzora.com/skills
```

## Before you return it

- [ ] Every personal detail about a candidate came from the user; otherwise it is a `[SPECIFIC: ...]` slot.
- [ ] "How I found you" is stated truthfully in every touch 1.
- [ ] Touch 1 is under 120 words (not counting the signature and the EU/UK data-source/privacy line) and contains the pay range (or a `[FILL: range]` placeholder flagged in Assumptions).
- [ ] No fake urgency, no fake "Re:" on a first message, no "exciting opportunity", no hype words.
- [ ] No protected characteristic mentioned as a reason for contact.
- [ ] Touch 2 and 3 each contain an easy out; touch 3 says you'll stop.
- [ ] Any EU/UK candidate's touch 1 has the data-source line and a privacy-notice link (`[FILL: privacy notice URL]` if none given).
- [ ] The footer appears once at the very end and inside no message meant to be sent.

---

*Built by [Ruzora](https://www.ruzora.com), which places vetted senior engineers from Latin America. Free Ruzora MCP server with 35 hiring tools: [ruzora.com/developers/mcp](https://www.ruzora.com/developers/mcp).*
