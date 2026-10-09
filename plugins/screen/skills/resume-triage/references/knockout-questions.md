# Screening-call question bank

Pick 4 for the call: 2 logistics, 2 evidence. Ask every candidate for the role the same 4, in the same order, and write down the answer before forming a view. A "knockout" here means a must-have the call can confirm or rule out; the human still makes the call.

## Logistics (use this wording; it is the lawful version)

| Topic | Ask exactly | Never ask instead |
|---|---|---|
| Work authorization | "Are you legally authorized to work in the US?" (or the country of the role) | "Where are you from?", "Are you a citizen?", "Where were you born?" |
| Sponsorship | "Will you now or in the future require sponsorship for employment visa status?" | "What visa are you on?", "When does your green card come?" |
| Hours overlap | "This role needs you online from 10am to 2pm Eastern on weekdays. Does that work for you?" | "Where do you live?", "Is that your home country?" |
| Start date | "If we moved ahead, when could you start?" | "Are you planning a family?", "Any upcoming medical leave?" |
| Pay | "Our range for this role is $X to $Y. Does that work for you?" Share the range first. | "What do you make now?" or any salary-history question (banned in many states and cities) |
| Contractor roles | "Do you invoice as an individual or through a company?" | Any question about nationality or immigration status |

## Evidence questions (pick the 2 that match the must-haves)

Each is hard to fake because it asks for a specific moment. Strong answers name a thing, a number and a decision; weak ones stay at the level of a job description.

| Must-have type | Question | Strong answer includes | Weak answer sounds like |
|---|---|---|---|
| Owned production code | "Tell me about the last thing you shipped that real users touched. What was your part, start to finish?" | A named feature, who used it, what they personally wrote vs reviewed, one thing that went wrong after launch | "We built a lot of features as a team", no single example, only tools named |
| Incidents / on-call | "Walk me through the last production incident you were in. What did you do in the first hour?" | Time of day, how they found out, the first command or dashboard they checked, the fix, what changed after | Generic incident process, "we followed the runbook", no detail they would only know by being there |
| Databases | "What is the biggest table you have worked with, and what broke as it grew?" | Rough row count or size, a slow query or migration, the index or change they made and why | "We used Postgres a lot", definitions of indexing with no story |
| Scaling / performance | "Tell me about something that got slow. How did you find out why?" | A measurement before and after, the tool they used to find it, a trade-off they accepted | "Optimized performance" with no numbers or method |
| Frontend | "What was the hardest UI state bug you fixed?" | The user action that triggered it, how they reproduced it, the root cause | Framework vocabulary without a concrete bug |
| Integrations / payments | "Tell me about an external API that behaved badly. What did you do?" | Retries, idempotency, webhooks arriving twice, a specific vendor quirk | "Integrated with Stripe and Twilio" and nothing more |
| Leading others | "Tell me about a technical decision you pushed for that the team disagreed with." | Who disagreed, the argument on each side, what happened, whether they were right | "I always align stakeholders", no conflict described |
| AI coding tools | "Show me, in words, how you used an AI coding tool on your last real task. Where did it get it wrong?" | A specific task, what they accepted, what they rejected and how they caught it | "I use it for everything" or "I never use it", no failure example |

## Follow-up that separates real from rehearsed

After any answer, ask one of: "What would you do differently now?", "What did you personally type, versus review?", "What number would tell you it worked?" People who did the work answer quickly and add detail. Rehearsed answers repeat themselves in different words.

## Gaps and job changes (only if needed, same wording for everyone)

"Anything about your timeline you'd like to walk me through?" Then listen. Do not ask why someone was out of work, about health, family or plans for children.
