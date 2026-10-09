# Reference check plan: Theo M., Senior React Native Engineer (remote US)

**Assumptions:** The team is a "yes, pending references". The risks come from your debrief (CTO, PM, and the CV gap). Theo has left Kindlewise; if he still works there, get his OK before calling anyone there. The CV dates for Kindlewise and Arcwell were not provided, so they are "unknown" until you check them. I removed both questions you asked for. Sick days touch disability and medical-leave protections, and past pay is covered by salary-history bans that also apply to asking through a referee (a remote US hire can bring a ban into play depending on where Theo lives). The job-related versions are in the script. · **Who calls:** you. If you hand the calls to your vendor, the FCRA steps in section 7 apply.

## 1. Risks to test
| # | Risk (confirmable or refutable) | Source (which interview / note) | Best referee |
|---|---|---|---|
| 1 | May not have *led* the move from Expo managed to bare workflow or the Stripe payments rewrite at Kindlewise. He may have been a team member, and the backend payment pieces (webhooks, retries) may have been someone else's. | System design interview (strong on mobile, fuzzy on payments backend); CTO's read | Sandra (manager): who led and who made the design decisions. Leo (peer): who built what, especially the server side |
| 2 | Waits for others to define a vague brief instead of driving it himself. | Product interview (PM) | Sandra first, Leo second. Ideally a Kindlewise PM (see missing referee types) |
| 3 | The 8-month Arcwell Labs contract in 2024 may not have happened as described (company, role, length). | CV / debrief; website down | Raj, once verified. Otherwise a different Arcwell contact |
| 4 | Quality under deadline pressure. This is a default senior-level risk added to round out the set, because it ties into the payments work. | Default for senior level (not raised in the debrief) | Leo (peer: code quality), Sandra |

## 2. Referee verification
| Referee | Claimed role and relationship | How to verify independently | Red flags in what was provided | Status |
|---|---|---|---|---|
| Sandra Okafor | Engineering Manager, Kindlewise. Theo's manager 2022–2025 | Find Kindlewise's main phone line on its own website and ask to be put through, or email her at the Kindlewise domain. Check her professional profile: account age, Kindlewise history covering 2022–2025, connections at Kindlewise (Leo is a good cross-check). Look for her on the Kindlewise team or engineering pages, in talks, or in public repos. Early in the call, ask for her dates and her role relative to Theo. | Both contact routes came from the candidate and are personal (Gmail, cell), not company channels. "Manager 2022–2025" may collide with the 2024 Arcwell contract: was Arcwell a side gig during Kindlewise, or did he leave and come back? Compare against the CV dates. | Unverified (pending) |
| Leo Brandt | Senior Engineer, Kindlewise. Peer | Confirm the email domain is Kindlewise's real domain (the one on its website, not a lookalike). Find his profile history independently, cross-check against Sandra and Kindlewise, and look for his commits in any public Kindlewise repos. | None so far. The company-domain email is a good sign but not enough alone. | Unverified (pending) |
| Raj (last name unknown) | "CTO at Arcwell Labs". Relationship unknown | Ask Theo for Raj's full name, his professional profile, and one more Arcwell colleague. Then check that Arcwell existed: archived copies of the website (Wayback Machine), the state business registry, startup databases, and other people who list Arcwell Labs in their work history. If Theo can, have him show a contract or invoice with Arcwell's name and dates (redact pay and personal details; you don't need them). | No last name, phone only, website down, and nobody else from the company offered. Several fraud red flags at once. | Unverified. Don't call until Raj is identified independently. Don't accuse; ask for an alternative. |

**Missing referee types:** You have no manager reachable through a company channel yet (Sandra's channels are all personal). Ask Theo for (a) someone who worked on the server side of the Stripe payments flow at Kindlewise, or the engineer who owned the backend, and (b) a product manager he worked with at Kindlewise, which is the best test of risk 2. If Raj can't be verified, ask for (c) any Arcwell colleague or client contact you can verify independently.

## 3. Call script (15 minutes, same core for everyone)
**Opening (read as written):** "Hi [name], this is [your name], cofounder at Pebblepath. Theo has applied for a Senior React Native Engineer role with us and gave us permission to speak with you. This will take about 15 minutes. What you tell me stays within our hiring team. Is now still a good time?"

**Verify the relationship:** "When did you work with Theo, from what month and year to what month and year? What was your role relative to his?" Write the dates exactly as stated, next to the CV dates (both Kindlewise and Arcwell). For Sandra, also ask: "Was he with Kindlewise the whole time from 2022 to 2025, or was there a break?"

**Core questions (every referee):**
1. "How did you work with him, for how long, and what was your role relative to his?" (covered above; confirm here)
2. "What was he responsible for, and what's the most important thing he built or fixed while you worked together?" Follow-up: "What part of that was his specifically?"
3. "Thinking of engineers at his level you've worked with, would you put him in the top 5%, 10%, 25% or 50%?" If he or she hedges: "What would have put him a band higher?"
4. "What did you coach him on, or what feedback did he get more than once?" If "nothing": "If you were his manager again, what would you work on with him first?"
5. "If you were building a team tomorrow, would you hire him again? For what kind of role?" Write down the exact words and whether there was a pause.

**Targeted questions for Sandra (manager):**
- Risk 1: "Who led the move from Expo managed to bare workflow? Who made the main design decisions?" Then: "And the Stripe payments rewrite: who designed the webhook handling and retries on the server side?" If vague: "If I asked Theo to walk me through why the webhooks and retries were built that way, would he know?"
- Risk 2: "When he got a loosely defined problem, what did he do in the first week?" Follow-up: "How much direction did he need compared with other senior engineers on your team?"
- Risk 4: "Tell me about a deadline where something had to give. What did he cut, and what did he refuse to cut?"
- Reliability (job-related replacement for the sick-days question): "When he committed to a date, how often did it hold? What did he do when it slipped?"

**Targeted questions for Leo (peer):**
- Risk 1: "On the payments rewrite, who built what? What happened when it broke in production, and who was on point?" If vague: "Who would you have called at 2am about a failed webhook?"
- Risk 4: "How often did his code come back from review or production with problems?"
- Risk 2: "When product handed the team a rough idea, what did Theo do with it?"
- Optional (AI-assisted work): "How did he use AI coding tools, and how did he check what they produced?"

**Targeted questions for Raj (only after he's verified):**
- Risk 3: "What was Arcwell building, how big was the team, and what exactly was Theo's contract scope? What were his start and end dates?" Follow-up: "Who else at Arcwell worked with him day to day?"
- Risk 2: "How defined was the work when you handed it to him, and what did he do with the gaps?"

**Close:** "Is there anything I should have asked and didn't?" / "Anyone else who worked closely with him I should talk to?"

## 4. Do not ask (keep this next to you on the call)
Sick days, absences, or medical/family leave · health, stress, or "personal issues" · family, kids, pregnancy, marital status · age · where he's from, citizenship, native language (confirm work authorization with Theo on Form I-9 after the offer) · religion or holidays · arrests or criminal history (your vendor's lawful, consented check covers this) · **salary, bonus, or equity at Kindlewise or Arcwell** · workers' comp, union activity, complaints filed.
Sick-day question removed: protected territory. Use the reliability question about dates held instead. Salary question removed: salary-history bans cover asking through others. Price the role from your own band and ask Theo for his expectations.
· **If they volunteer it:** "Thanks, I'm going to keep this to his work, so I won't note that. Can you tell me more about how he handled the payments rewrite?" Don't write it down, and don't let it influence the decision.

## 5. Notes and risk register (fill in during calls)
| Risk | Referee A (Sandra) said (quote) | Referee B (Leo) said (quote) | Status | Action |
|---|---|---|---|---|
| 1. Led the Expo→bare migration + Stripe rewrite | | | resolved / confirmed / mixed / unverified | |
| 2. Waits for vague briefs to be defined | | | | |
| 3. Arcwell contract as described (Raj or alternative: ___) | | | | |
| 4. Quality under deadline pressure | | | | |
| Dates stated vs CV (Kindlewise: CV ___ / stated ___; Arcwell: CV ___ / stated ___) | | | | |

**Rehire answer, word for word:** A: ___ B: ___ (Raj/alt: ___)
**Ranking answer:** A: ___ B: ___ (Raj/alt: ___)
**Factual mismatches:** ___

## 6. How to read the results
- **Risk 1:** It's resolved if Sandra and Leo both name Theo as the person who drove the migration decisions, and say who owned the payments backend. If Theo owned the mobile side and someone else owned the server side, that matches the interview and is fine if he described it that way. "I led that, he worked on part of it" from either referee is a factual mismatch: pause and ask Theo neutrally.
- **Risk 2:** If both referees independently describe him waiting for direction, that's confirmed. Decide whether it fits a 16-person startup or goes into the 90-day plan with a named product partner. One vague mention doesn't outweigh the interview evidence.
- **Risk 3:** If Arcwell or Raj can't be verified, record "unverified" and ask Theo for an alternative you can verify. Arcwell dates that collide with Sandra's "2022–2025 manager" account without a clear explanation are a factual mismatch.
- **Risk 4 and overall:** "Yes, in the right role" or a pause on rehire, praise only for reliability, or refusing "top 25%" are reservations. Probe them; don't ignore them. If neither verified referee can be reached through a company channel, treat the reference picture as incomplete.
- You and your cofounders decide what this adds up to.

## 7. Legal steps that apply
- **You make the calls:** These aren't consumer reports. Still, get Theo's consent and tell him who you'll call, don't contact any current employer without his OK, ask every referee the same core questions, keep your notes, and stay off the section 4 list. Treat any backchannel as single-source and give Theo a chance to respond.
- **If you give the reference interviews to your vendor ($40 each):** These become *investigative consumer reports* under FCRA. Before ordering, check that Theo's existing standalone disclosure and written authorization actually cover reference interviews and not only the criminal and employment check. Send him notice within 3 days of ordering that an investigative report may be made (15 U.S.C. 1681d). If you might decide against him based on it: send a pre-adverse-action notice with a copy of the report and the summary of rights, wait (5 business days is common practice), then send the final adverse-action notice naming the vendor. Also note that a vendor will likely run a generic script. It won't press on risks 1–3, and checking Raj is still your job either way.
- **Criminal check:** Austin's fair-chance hiring ordinance may apply to employers your size (15+). Confirm with counsel or your vendor that the criminal check runs only after a conditional offer.
- General information as of 2026-10, not legal advice.

## 8. Emails
**To the candidate:**
Subject: Pebblepath: references, next step
Hi Theo,
Thanks again for your time with the team. We'd like to move to references and aim to finish this week.
I'll call Sandra Okafor and Leo Brandt. To round things out, could you also send:
1. Someone who worked on the server side of the Stripe payments flow at Kindlewise (or the engineer who owned that backend)
2. A product manager you worked with at Kindlewise
3. Raj's full name and professional profile from Arcwell Labs, plus one other Arcwell colleague or client contact. Since the Arcwell site is down, a contract or invoice showing Arcwell's name and your dates would also help (please black out pay and any personal details).
I'll contact Kindlewise people through the company's main channels. Please confirm you're OK with that, and let me know if there's anyone you'd prefer I not contact yet.
Thanks,
[Your name], Cofounder, Pebblepath

**To each referee:**
Subject: 15 minutes about Theo M.?
Hi [Name],
I'm [your name], cofounder at Pebblepath in Austin. Theo M. is a finalist for a Senior React Native Engineer role with us and listed you as a reference, with his permission.
Could we speak for 15 minutes? Two options (Central Time):
- Tuesday, Oct 6, 11:00 am
- Wednesday, Oct 7, 2:00 pm
If neither works, just send a time that does. What you share stays within our hiring team.
Thank you,
[Your name], Cofounder, Pebblepath · [work phone]

---
Made with the free Reference Check skill by Ruzora · ruzora.com/skills
