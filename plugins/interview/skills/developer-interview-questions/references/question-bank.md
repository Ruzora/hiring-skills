# Question bank for non-technical interviewers

Base questions to tailor. Replace the bracketed parts with the user's stack, product and deliverables. Each entry gives the strong and bluff markers to adapt; write the final ladder in exact sentences.

## A. Past-work walkthrough (pick 4)

**A1. "Walk me through the piece of software you are proudest of from the last two years. Who used it, and what did you build yourself?"**
- Strong: names the users and roughly how many; draws a clear line between their part and the team's; gives one number (users, requests, revenue, time saved).
- Bluff: describes the company's product, not their part; "we" throughout; no numbers; stays at the buzzword level ("microservices, scalable, cloud-native").
- Ladder: "Which part of that did you write or design yourself?" → "What broke or was harder than expected?" → "If you rebuilt it today, what would you do differently, and why?"

**A2. "Tell me about the worst production problem you were involved in. What happened, minute by minute?"**
- Strong: a real incident with a timeline, how it was noticed, what they did first, root cause, and the change made so it would not repeat.
- Bluff: "nothing major ever broke"; a story where they were a spectator; root cause is "someone else's code"; no follow-up change.
- Ladder: "How did you find out it was broken?" → "What did you check first, and why that?" → "What did you change afterwards so it could not happen again?"

**A3. "Tell me about a time you built something with very unclear requirements. How did you decide what to build?"**
- Strong: talked to users or the founder, shipped a small version first, cut scope deliberately, can name what they left out.
- Bluff: waited for a spec; built everything; "I just figured it out".
- Ladder: "Who did you talk to before writing code?" → "What did you decide NOT to build?" → "How did you know the first version was good enough to ship?"

**A4. "Pick one technical choice you made, like a database, framework or hosting setup, for [their past product]. Why that one?"**
- Strong: compares at least one alternative; names a real cost of their choice (price, speed, hiring, lock-in); ties it to the product's needs.
- Bluff: "it's the best"; "everyone uses it"; no alternative considered; cannot name a downside.
- Ladder: "What else did you consider?" → "What did this choice cost you or make harder?" → "Would you pick it for [user's product]? Why or why not?"

**A5. "Tell me about code you inherited from someone else. What state was it in and what did you do?"**
- Strong: describes reading before changing, adding tests or monitoring first, improving in small steps while still shipping.
- Bluff: "I rewrote it all" with no reason tied to the business; contempt for the previous author; no plan.
- Ladder: "What did you do in the first week before changing anything?" → "What did you leave alone, and why?" → "How did you make sure you did not break anything?"

**A6. "What is something you shipped that users did not like or did not use? What did you learn?"**
- Strong: a specific feature, how they found out (data, feedback), what they changed.
- Bluff: "everything I shipped was well received"; blames product or sales.
- Ladder: "How did you find out?" → "What did you do next?" → "What do you do differently now before building?"

**A7. (Security or data-sensitive products) "Tell me about a time you handled sensitive data: passwords, payments, health or personal data. What did you do to protect it?"**
- Strong: specific practices (access limited to who needs it, secrets not in code, encryption, audit logs, deleting what is not needed), and a trade-off they accepted.
- Bluff: "we used a secure cloud"; "the framework handles security"; no specifics.
- If the user's product handles health or payment data, add: "Which rules applied to that data?" and listen for them to name one (for example HIPAA for US health data, PCI DSS for card payments) and say what it changed in their work.
- Ladder: "Who could see that data, and how did you decide?" → "Where were passwords and API keys stored?" → "What would you check first in our setup in week one?"

## B. Judgment and trade-offs (pick 2)

**B1. "We need [user's deliverable] in [timeframe]. What would you want to know before giving me an estimate?"**
- Strong: asks about users, must-haves vs nice-to-haves, existing code and data, who decides; gives a range and says what would change it.
- Bluff: gives an exact number immediately; or refuses any estimate.
- Ladder: "Give me a rough range anyway." → "What would make it take twice as long?" → "What would you cut to hit half the time?"

**B2. "When is it right to ship something that is not finished or not perfectly built?"**
- Strong: separates reversible from irreversible decisions (data model, security, payments vs UI), gives an example of a shortcut they took and later repaid.
- Bluff: "never, quality first" or "always, move fast"; no example.
- Ladder: "Give me an example of a shortcut you took." → "Did you go back and fix it? When?" → "What would you never cut corners on here?"

**B3. "If you joined and found our current code was messy, what would you do in your first month?"**
- Strong: learn and ship first, list the risks, fix the dangerous parts first, explain a plan to the founder in business terms.
- Bluff: "rewrite it in [favorite stack]" before understanding it.
- Ladder: "How would you decide what to fix first?" → "How would you explain that to me without jargon?" → "What would you keep shipping in the meantime?"

## C. Working with you (pick 2)

**C1. "Explain one technical decision from your past work to me as if I were a customer. Now say it in one sentence."**
- Strong: plain words, an analogy if helpful, checks that you followed, gets shorter on request.
- Bluff: more jargon when asked to simplify; impatience; cannot compress to one sentence.
- Ladder: "What does that mean for the person using the product?" → "What would go wrong if we skipped it?" → "One sentence?"

**C2. "Tell me about a time you disagreed with a manager or founder about what to build. What happened?"**
- Strong: disagreed with data or a prototype, committed once decided, can say what the other person got right.
- Bluff: never disagreed; or the other person was simply wrong; or they did it their way anyway.
- Ladder: "How did you make your case?" → "What was decided, and what did you do then?" → "Looking back, what did they see that you didn't?"

**C3. "How do you tell your manager that something will be late?"**
- Strong: early, with a new date and options (cut scope, add time), a real example.
- Bluff: "I'm never late"; tells at the deadline.
- Ladder: "When did you last do that?" → "How early did you raise it?" → "What options did you give?"

**C4. (Remote roles) "Walk me through a normal remote workday at your last job. How did you keep others aware of your progress?"**
- Strong: written updates, small pull requests (a pull request is a proposed code change for review), asks for help early, overlap hours.
- Bluff: vague; "I just work"; no habit of writing things down.
- Ladder: "What did a written update from you look like?" → "When you got stuck, how long before you asked?" → "What would you need from us in week one?"
