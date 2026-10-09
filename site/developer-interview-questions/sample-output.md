# Interview kit: First full-time engineer, senior full stack, Next.js + TypeScript + Postgres on AWS
Assumptions:
- You (CEO) run the interview. Your PT cofounder can sit in and take notes, but asks no extra questions so all 3 candidates get the same interview.
- No technical person is available to help yet (you did not mention one). The backstop section below covers that.
- You are hiring in the US, so US federal rules apply. If a candidate would be employed in another country, local rules apply and differ.
- The on-call schedule and working hours are not defined yet. Where a question needs them, they appear in [brackets] for you to fill in before next week.

## What this interview tests
| # | Must be good at | Questions that test it |
|---|---|---|
| 1 | Takes over messy agency code alone and keeps it running while improving it | Q1, Q2, Q5 |
| 2 | Keeps patient intake data safe and can get Fernhill through the clinic chain's security review by Q2 | Q3, Q4, Q6 |
| 3 | Makes sensible scope and priority calls with no tech lead above them | Q5, Q6, Q8 |
| 4 | Explains technical trade-offs and bad news to two non-technical founders in plain words | Q7, Q8 |

## Plan (60 minutes)
- 0-5 min: Introduce yourself and Fernhill in two minutes. Tell the candidate: "I'm not technical, so I'll ask about real things you've built and I'll ask a lot of follow-ups like 'what exactly did you do'. That's how I go deeper, it's not a sign anything went wrong. I'll take notes in your words. Every candidate gets the same questions." Optional: "tell me about yourself" as a 2-minute warm-up, never scored.
- 5-45 min: questions 1-6
- 45-55 min: questions 7-8
- 55-60 min: candidate's questions
(Then: score within 15 minutes, before any discussion. You and your cofounder score separately, then compare.)

## The questions
### Q1. "Walk me through the piece of software you're proudest of from the last two years, ideally a web app with real users. Who used it, roughly how many, and what did you build yourself?"
**Tests:** 1. Takes over code alone and keeps it running
**Why you ask it:** You need someone who has personally built and run a real product, not someone who sat inside a big team.
**Strong answer sounds like:**
- Names who the users were and gives a number (clinics, users, bookings per day, revenue, hours saved).
- Draws a clear line: "I built the booking flow and the database, another engineer did the billing."
- Mentions it running in production: deploying it, fixing it when it broke, watching it after launch.
- Gets more specific when you ask "what exactly", not less.
**Bluff sounds like:**
- Describes the company's product, not their part of it.
- "We" all the way through, even after you ask what they did.
- No numbers at all, or only buzzwords ("scalable, cloud-native, microservices").
- Everything went smoothly.
**Follow-up ladder:**
1. "Which part of that did you write or design yourself, start to finish?"
2. "What broke, or turned out harder than you expected, after it went live?"
3. "If you rebuilt it today, what would you do differently, and why?"

### Q2. "Our app was built by an agency and it's fragile. Tell me about a time you inherited code someone else wrote. What state was it in, and what did you do?"
**Tests:** 1. Takes over code alone and keeps it running
**Why you ask it:** The first job is taking the codebase over from the agency without breaking scheduling for the clinics that use it today.
**Strong answer sounds like:**
- Spent time reading and understanding it before changing it, and can say how long.
- Added safety nets first (tests, error alerts, backups) and then improved in small steps.
- Kept shipping features or fixes for users while cleaning up.
- Talks about the previous developers neutrally, even if the code was bad.
**Bluff sounds like:**
- "I rewrote the whole thing," with no business reason given.
- Contempt for the previous team or agency.
- No plan, no order of steps, no mention of not breaking things.
- Cannot name anything they decided to leave alone.
**Follow-up ladder:**
1. "What did you do in the first week, before you changed anything?"
2. "What did you leave alone, even though it was ugly, and why?"
3. "How did you make sure your changes didn't break things for the people using it?"

### Q3. "Fernhill stores patient intake forms, so there's health information in our database. Tell me about a time you handled sensitive data like health, payment or personal data. What did you do to protect it, and which rules applied to it?"
**Tests:** 2. Keeps patient data safe and gets through the security review
**Why you ask it:** You will be holding health information and a bigger clinic chain will review your security by Q2. This hire owns that.
**Strong answer sounds like:**
- Names a rule and what it changed in their work, for example "HIPAA, so we had to sign agreements with every vendor that touched the data and keep logs of who viewed records."
- Specific practices you can repeat back: only certain people could see the data, passwords and keys were kept out of the code, data was encrypted, there was a log of who accessed what, old data was deleted.
- Names a trade-off they accepted, for example "it made debugging slower because engineers couldn't look at real records."
- Has been through, or helped with, a security review or questionnaire before.
**Bluff sounds like:**
- "We used AWS, which is secure" or "the framework handles security."
- Cannot name any rule, or names HIPAA but cannot say what it changed day to day.
- No specific practices, only words like "best practices" and "industry standard."
- No downside to anything they did.
**Follow-up ladder:**
1. "Who could see that data, and who decided that?"
2. "Where were the passwords and API keys stored, and what went wrong or almost went wrong there?"
3. "If you joined Fernhill, what would you check first in our setup in week one, and what would you leave for later?"

### Q4. "Tell me about the worst production problem you were involved in. What happened, minute by minute?"
**Tests:** 2. Keeps patient data safe and gets through the security review
**Why you ask it:** When Fernhill breaks, clinics cannot book or check in patients, and if data leaks it's a health-data incident. You need someone who has handled a real outage calmly and fixed the cause.
**Strong answer sounds like:**
- A real incident with a timeline: how they found out, what they checked first, how long it lasted.
- Their own role in it is clear: "I was on call, I rolled back the release."
- A root cause in plain terms, including their own mistake if it was one.
- A change they made afterwards so it would not happen again (an alert, a test, a checklist).
**Bluff sounds like:**
- "Nothing major ever broke."
- They watched while someone else fixed it.
- The cause was "someone else's code" and the story ends there.
- No change made afterwards.
**Follow-up ladder:**
1. "How did you find out it was broken, and what did you personally do first?"
2. "What did it cost: users affected, hours down, data lost or exposed?"
3. "What did you change afterwards so it couldn't happen again, and what did you decide not to change?"

### Q5. "If you joined Fernhill and found the agency's code was even messier than we think, what would you do in your first month?"
**Tests:** 1. Takes over code alone, 3. Makes sensible scope and priority calls
**Why you ask it:** Rewriting everything is the most common way a first engineer burns six months. You want someone who stabilizes, protects the data, and keeps shipping.
**Strong answer sounds like:**
- Learns the code and ships something small first, before big changes.
- Makes a list of risks and fixes the dangerous ones first (patient data, backups, logins) before cosmetic ones.
- Plans the hand-off from the agency: getting access to everything (AWS account, domain, database, passwords) into Fernhill's control.
- Says they would explain the plan to you in business terms.
**Bluff sounds like:**
- "I'd rewrite it in [their favorite tool]" before having seen it.
- No order of priorities; everything is equally urgent.
- Nothing about keeping clinics running during the change.
- Nothing about getting control of accounts from the agency.
**Follow-up ladder:**
1. "How would you decide what to fix first, and what would be on that list?"
2. "What would it cost us to do it your way: what features would wait?"
3. "When would a full rewrite actually be the right call, and what would you need to see before suggesting one?"

### Q6. "We need to pass a security review for a large clinic chain by Q2. What would you want to know before giving me an estimate of what that takes?"
**Tests:** 2. Gets through the security review, 3. Makes sensible scope and priority calls
**Why you ask it:** This is a real deadline tied to your biggest deal. You need someone who can scope it, give a range, and tell you what would make it slip.
**Strong answer sounds like:**
- Asks questions back: what the review covers (a questionnaire, an outside audit, specific standards), what the current setup is, who at the agency still has access, whether there are signed agreements with vendors.
- Gives a range, not one exact number, and says what would move it.
- Separates must-do-before-review from can-do-after.
- Mentions getting the chain's questionnaire early so there are no surprises.
**Bluff sounds like:**
- An exact number right away with no questions ("six weeks").
- Refuses to give any estimate at all.
- "It's just a checklist, easy."
- Cannot say what would make it take longer.
**Follow-up ladder:**
1. "Give me a rough range anyway, based on what you've done before."
2. "What would make it take twice as long?"
3. "If we only had half that time, what would you do first and what would you skip?"

### Q7. "Pick one technical choice from your past work, like a database, a hosting setup or how you handled logins. Explain it to me as if I were one of our clinic owners. Now say it in one sentence."
**Tests:** 4. Explains trade-offs to non-technical founders
**Why you ask it:** This is the "explain it to me" check. They will report to two non-technical founders and talk to clinic security reviewers. If they cannot make it understandable after two tries, that is evidence, not a style issue.
**Strong answer sounds like:**
- Plain words; jargon gets explained or dropped.
- An everyday comparison if it helps, and checks that you followed.
- Gets shorter and clearer when you ask for one sentence.
- Names what the choice cost or what they gave up.
**Bluff sounds like:**
- More jargon when you ask them to simplify.
- Impatience, or "it's complicated, you'd need to be technical."
- Cannot get it down to one sentence after two tries.
- The "why" is "it's the best" or "everyone uses it."
**Follow-up ladder:**
1. "What does that mean for the person using the product?"
2. "What did that choice cost you, or make harder?"
3. "What else did you consider, and why did you decide against it? One sentence."

### Q8. "Tell me about the last time you had to tell a manager or founder that something important would be late. What happened?"
**Tests:** 4. Explains bad news to non-technical founders, 3. Makes sensible scope and priority calls
**Why you ask it:** With no tech lead between you and them, you only find out the security review is at risk if they tell you early and clearly.
**Strong answer sounds like:**
- A specific, recent example with what was late and by how much.
- Raised it early, not on the deadline day.
- Came with options: cut scope, move the date, or get help.
- Says what they learned about estimating since.
**Bluff sounds like:**
- "I'm never late."
- Told them at the deadline.
- No options, only the bad news.
- Blames the manager, product or sales for the delay.
**Follow-up ladder:**
1. "How early did you raise it, and what exactly did you say?"
2. "What did the delay cost the business or the customer?"
3. "What would you do differently next time, and what do you now do earlier?"

## Red flags for this role
- Wants to rewrite the Next.js app from scratch before shipping anything or understanding why it's fragile.
- Treats security as someone else's job ("AWS handles that", "the framework handles that") or cannot say what HIPAA changes in day-to-day work.
- Has only worked inside large teams with a dedicated security, DevOps or QA group and cannot name what they would do alone.
- Has never put software in front of real users or been responsible when it broke.
- Cannot give any estimate for the Q2 security review, even a range.
- Talks about past teammates, managers or the agency with contempt.
- Picks tools because they are new or interesting, not because they fit a 6-person company with one engineer.

## Where a technical reviewer comes in
This interview can tell you about depth, ownership and how clearly they explain things. It cannot tell you whether their code or their security setup is actually good. Plan one more stage for your top 1-2 candidates:
- **Who:** a senior engineer you hire for a few hours on a freelance basis, ideally one who has worked on a health-data product. Not the agency that built your MVP, since this person may end up reviewing that agency's work.
- **When:** after this interview, before any offer.
- **How long:** a 60-90 minute call where the candidate walks the reviewer through code they wrote (an open-source project or a paid work sample), plus an hour or two of the reviewer's time to write up notes.
- **What they check:** whether the code is clear and safe, how the candidate handles data and passwords, whether their security answers from Q3 hold up in practice, and how they react to questions about their own code.
- **If nobody is available yet:** give finalists a short paid work sample (3-4 hours, paid at a fair rate) built on a small sample Next.js + Postgres app, for example "add a patient intake form that stores answers safely and logs who viewed them." Never give candidates your real code with patient data in it. Then pay a freelance senior engineer for a few hours to review all submissions with the same checklist.

## Scoring sheet
| Q | Must-have | Score 1-4 | Evidence (their words) |
|---|---|---|---|
| Q1 | Takes over code alone | | |
| Q2 | Takes over code alone | | |
| Q3 | Keeps patient data safe | | |
| Q4 | Keeps patient data safe | | |
| Q5 | Takes over code alone, scope calls | | |
| Q6 | Security review, scope calls | | |
| Q7 | Explains to non-technical founders | | |
| Q8 | Explains bad news, scope calls | | |

Scale: 4 = specific, owned, climbed the whole ladder, named costs and alternatives without being asked. 3 = specific and owned, needed prompting for the cost or the alternative. 2 = some specifics, but went vague by the second follow-up or could not separate their own work from the team's. 1 = stayed generic, could not answer the first follow-up with specifics, or contradicted earlier answers.
Count the ladder rungs: two or more answered with specifics is strong, zero is a 1. Score what was said, not how confident it sounded.

Overall notes: <evidence for and against, written before any debrief>
The hiring decision is yours; this sheet records evidence.

## Your draft questions
| Your question | Keep / replace | Why | Use instead |
|---|---|---|---|
| "Tell me about yourself" | Keep as a 2-minute warm-up, never scored | Fine to settle nerves, but with no follow-up it gives you a rehearsed summary and nothing to judge | Q1, which asks the same thing about a real project and lets you dig in |
| "What's your biggest weakness?" | Replace | Answers are rehearsed ("I care too much"), so everyone sounds the same | Q4 (worst production problem) or Q8 (something that was late): real failures with real lessons |
| "How many years of React do you have?" | Replace | Years measure time spent, not skill. Five years of copying the same pattern looks the same as five years of owning a product | Q1 and Q7: ask what they built with React and Next.js and why they made the choices they did |

## Legal check
| Your question | Problem | Rewrite |
|---|---|---|
| "Are you comfortable with on call? Some of us have kids so we try to keep it light, do you have a family?" | Asking about family, children or marital status is a protected area (sex, family status, and pregnancy or plans for children under federal law; marital status in many states). Even with good intentions, it can be used as evidence of discrimination. | "This role includes on-call for production issues, [describe your actual schedule, for example one week in four, including some nights]. Can you meet that schedule?" Ask every candidate the same way, and describe your schedule rather than asking about their life. |
| "Where are you based originally?" (asked because one candidate has an accent) | National origin and accent are protected. Asking where someone is from, or scoring on accent, is not allowed. Communication concerns about accent are exactly the kind of note that must not be in the record. | For work status: "Are you legally authorized to work in the US?" and "Will you now or in the future require visa sponsorship?" For time zone: "This role needs overlap with [your hours and time zone]. Can you meet that schedule?" For communication: use Q7 and Q8 with every candidate and score what they said, not how they sound. |

Remove any note about the candidate's accent from your records. If communication is a real requirement, Q7 tests it the same way for everyone: can they make a technical choice clear to a clinic owner in plain words.

**Don't ask / Ask instead (keep this next to you during the interviews)**
| Don't ask | Ask instead |
|---|---|
| "Where are you from?" / "Is English your first language?" / "Are you a citizen?" | "Are you legally authorized to work in the US?" and "Will you now or in the future require visa sponsorship?" |
| "Do you have kids? Can you handle on-call with a family?" | "This role has on-call [your schedule]. Can you meet that schedule?" (ask every candidate) |
| "How old are you?" / "When did you graduate?" | Nothing. If there is a legal minimum age, "Are you at least 18?" |
| "Any health issues we should know about?" (including because you're a health company) | "Can you perform the essential functions of this job, described here, with or without reasonable accommodation?" |
| "What do you make now?" | "What salary range are you looking for?" |
| "Do you observe any holidays?" | "The team works [hours/days]. Can you meet that schedule?" |
| "Have you ever been arrested?" | Nothing in the interview. Follow your state's fair-chance rules for any background check later. |
| "Would you fit in with our small founding team?" | "Describe the team setup where you did your best work." |
| Anything about religion, pregnancy, sexual orientation, gender identity, disability, genetic or family medical history | Nothing. These are never part of the interview or the evaluation. |

General information, not legal advice. US federal rules as of 2026; states add more.

---
Made with the free Developer Interview Questions skill by Ruzora · ruzora.com/skills
