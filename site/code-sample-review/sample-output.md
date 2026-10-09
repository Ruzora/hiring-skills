# Code sample review: Kit Brannagan-Oyelaran (kitbrannagan-example/slotkeeper), for first full-time engineer, mid/senior, Node + React

**What I looked at:** The repo's About line, the full README, the file and folder list, the contents of the public .env file, 8 of the 47 commits, and part of one code file (services/deposits.js, the confirmBooking function). Missing: the test files' contents, the other code files (webhooks, availability, routes), the React app, package.json (the list of libraries used) and the other 39 commits. So I can say what the deposit logic does, but not how good the tests are or how the rest of the app is built.

**Bottom line in plain English (3 sentences max):** This is a real, small booking-and-deposits product that deals with the same problems Pebblecart has (taking money up front, dates, duplicate payment messages), and the README shows someone who thinks about what goes wrong with payments. The history looks like steady work by Kit over about 8 weeks, with one feature (the calendar screen) built by another person, so it is probably mostly his, but that is a claim to test, not a fact. In the interview, find out whether he can explain and change the deposit logic on the spot, including one scenario where it may charge or fail incorrectly, and what he would do about the payment key he left public.

## Is it theirs? (authorship)
| Check | What we saw | What it means |
|---|---|---|
| Fork or tutorial | No "forked from" line. Not a well-known tutorial project (not a to-do, weather or clone app). The README explains specific, unusual decisions ("Why some things are weird") that tutorials rarely contain. | The starting point looks like his own. Still worth asking whether any part started from a template or course. |
| Who committed | Almost all commits shown are by "Kit Brannagan". One is "Merge pull request #3 from jpwellsby-example/calendar-ui", with the work itself, "calendar month view + drag to reschedule" (Feb 11), by J.P. Wellsby. | A second person built the calendar screen and Kit accepted it into the project. That part is not his. Ask who J.P. is and which other parts, if any, they touched. |
| History shape | 47 commits from Jan 9 to Mar 2. Most messages say what changed and why ("deposits: switch to manual capture, capture on confirm", "fix: ignore duplicate webhook events"). One vague "wip" (work in progress) on Feb 25. | Looks like real work done in steps over weeks. Commit dates and names can be set by whoever makes them, so this supports his story but does not prove it. |
| Employer or confidential code | Salon booking app. No company names, internal web addresses or customer data in what you pasted. The database address points to "localhost" (his own computer). | No sign this is a past employer's private code. |

**Authorship confidence:** Medium, because the history, the README and the code tell one consistent story under his name, but history can be manufactured and one feature is clearly someone else's, so the walkthrough has to confirm it.

## What the code suggests
| Signal | What we saw (file or line) | What it suggests | Confidence |
|---|---|---|---|
| README explains how to run it | README "Setup": `npm install`, `cp .env.example .env`, `npm run migrate && npm run dev` | Another engineer could get it running in a few steps. Good sign for a first hire, who will be the one writing these instructions for whoever joins next. | High |
| README explains choices and trade-offs | "Why some things are weird": uses Stripe "manual capture" (putting a hold on the customer's card and collecting it later) and notes holds expire after 7 days; notes webhooks (automatic messages Stripe sends to your app about payments) can arrive twice | He understands real payment edge cases beyond the happy path. This maps closely to taking preorder deposits for bakeries. | High |
| Duplicate payment messages handled | README line about a unique key on stripe_event_id; file `db/migrations/002_payments_unique_event.sql` (a migration is a script that changes the database structure); commit "fix: ignore duplicate webhook events (unique stripe_event_id)" | He found and fixed a real-world problem (Stripe sending the same message twice) using a database rule that refuses duplicates. Solid, standard approach. | High |
| Tests exist, with an admitted gap | `test/deposits.test.js` and `test/availability.test.js`; README TODO: "tests for the cancellation flow" | Tests exist for the two riskiest areas (money and time slots). We did not see what they check. Cancellations are untested, and he says so openly. | High that they exist; Low on how good they are |
| Secret committed in public | `.env` is in the repo with `STRIPE_SECRET_KEY=sk_test_51Hx...` | He published a payment key. The "sk_test" part means it is a test-mode key (it cannot move real money), which lowers the risk, but it is still a habit you do not want near Pebblecart's live Stripe account. He also has a `.env.example` file, so he knows the right pattern and slipped here. | High |
| Errors are handled, partly | `confirmBooking`: the Stripe call is wrapped in `try/catch`; on failure it logs a warning and marks the booking `deposit_failed` | Failed payments are recorded instead of silently ignored. But the last step (saving "confirmed" after a successful charge) is outside that protection. See the scenario questions below. | Medium |
| Structure | `src/routes`, `src/services` (deposits, availability), `src/db/migrations`, separate `client/` for the React app | Organized by job, the way most professional Node apps are. Easy to find where things live. | Medium |
| Honest about known problems | README TODO: "timezone bug when salon and customer are in different zones" | He tracks his own bugs openly. Relevant to you: bakery pickup times and preorder cutoffs are exactly where timezone bugs show up. | Medium |

## Questions that test authorship
1. **"In confirmBooking in deposits.js, walk me through this: a customer books 10 days ahead, and the salon confirms 8 days later, 2 days before the appointment. What happens to the deposit?"**
   What the code appears to do: it counts the days left until the appointment (2), so it takes the "less than 7 days" path and tries to collect the hold placed when the customer booked. But that hold is now 8 days old, and the README says holds expire after 7 days. If so, the collection fails and the booking is marked `deposit_failed`. The same question applies to "booked 10 days out, confirmed 5 days later": if no hold was placed for bookings more than 7 days out, there is nothing to collect. The code checks days until the appointment, while the expiry depends on how old the hold is. This is a possible bug to confirm with the candidate, not a verdict.
   A real author will: open the file quickly, follow the 7-day check out loud, and either explain what prevents this (for example, a hold is only created within 7 days of the appointment, or a nightly job refreshes old holds) or spot the issue within a minute and say how he would fix it.
   A bluff sounds like: repeating the README sentence about 7-day holds without tracing the actual case, or saying "Stripe handles that" without pointing to where.

2. **"What happens in confirmBooking if the salon owner clicks Confirm twice quickly, for a booking 10 days out?"**
   What the code appears to do: both clicks can read the booking as "pending" before either one saves "confirmed", so both may create a new charge. Nothing visible stops two charges (Stripe offers an "idempotency key", a tag that makes it ignore a repeated request, and none is used here). Possible double charge; confirm with him.
   A real author will: see the gap fast, explain the difference between this and the duplicate-webhook fix he already built, and suggest a fix (a database lock, or an idempotency key such as the booking ID).
   A bluff sounds like: "the status check handles that", without explaining what happens when both clicks arrive at the same moment.

3. **"In confirmBooking, what if Stripe takes the money but saving 'confirmed' to the database fails right after?"**
   A real author will: notice the final save is outside the try/catch, say the booking would stay "pending" with the customer already charged, and that a retry could charge again. Then describe a fix (record the payment first, use Stripe's webhook to reconcile, or an idempotency key).
   A bluff sounds like: "that never happens" or a general answer about "error handling" with no reference to the actual lines.

4. **"I noticed a Stripe key in your .env file, which is public. What would you do about that now?"**
   A real author will: own it without drama, say it is a test key, and still list the steps: cancel ("rotate") the key in Stripe, remove the file from the repo and its history, add .env to the ignore list, and keep using .env.example with placeholders.
   A bluff sounds like: "it's only a test key, it doesn't matter", with no plan, or not knowing the file is public.

5. **"Tell me about the commit 'fix: ignore duplicate webhook events' on March 2. How did you find out duplicates were happening?"**
   A real author will: tell a specific story (a double entry, a log line, reading Stripe's docs), explain what the unique key on stripe_event_id does, and what the app does when it rejects a duplicate.
   A bluff sounds like: describing webhooks in general terms, or not knowing what the 002 migration file contains.

6. **"Pull request #3 came from J.P. Wellsby. Who is J.P., and what did you change or check before merging the calendar work?"**
   A real author will: say plainly who J.P. is and which parts are J.P.'s, describe what he reviewed or pushed back on, and be clear about what in the repo is his own.
   A bluff sounds like: vague ownership of everything ("we built it together") or being unable to say where the calendar code ends and his begins.

7. **"Your README lists a timezone bug between salon and customer. What is the bug, and how would you fix it?"**
   A real author will: describe a concrete case (for example, a customer in another zone sees a slot an hour off, or the 7-day count shifts by a day near midnight) and a fix (store all times in one standard zone and convert only for display).
   A bluff sounds like: "timezones are hard" with no specific example from this app.

8. **"What does deposits.test.js actually check? Would any of those tests catch the scenario from question 1?"**
   A real author will: name specific cases the tests cover, admit which ones are missing, and say what test he would add first.
   A bluff sounds like: "it tests the deposits" without naming a single case.

## 10-minute walkthrough plan
- Minute 0-2: Kit shares his screen and opens the slotkeeper repo. Ask him to explain in two sentences what the app does and which parts he built himself versus J.P.
- Minute 2-5: Open services/deposits.js together. Ask question 1 (booked 10 days out, confirmed 8 days later). Let him trace it line by line. Watch for how fast he finds the file and whether he reasons from the code or from memory.
- Minute 5-7: Ask question 2 (Confirm clicked twice) or question 3 (charge succeeds, save fails), whichever question 1 did not already open up.
- Minute 7-8: Ask question 4 about the public Stripe key.
- Change request (minute 8-10): "Show me where you'd stop a booking from being confirmed if the appointment start time has already passed." A real author goes straight to confirmBooking and points to where the check belongs, near the existing "pending" check, in seconds. Someone who did not write it will search around.

## What this review cannot tell you
- Only part of one code file was visible. I could not judge the tests, the webhook code, the availability logic or the React app.
- The authorship picture comes from commit names and dates, which anyone can set. Only the live walkthrough can confirm he wrote this.
- The ~60 contributions last year is not a negative. Most professional engineers do their real work in private company repos, which GitHub does not show on a profile by default. "Green squares every day" is a myth; plenty of strong senior engineers have almost none.
- One repo cannot tell you how he works with others, communicates with a non-technical founder, estimates work or handles a production emergency. Those come from the rest of the interview and references.
- The possible bugs above are things to confirm with him, not proof of mistakes. There may be code we did not see that prevents them.
- Do not download or run his code on a company laptop; reading it is enough.
- Because this is your first engineering hire and the money logic matters to Pebblecart, consider paying an experienced engineer for an hour to look at the same repo with these questions before Friday.
---
Made with the free Code Sample Review skill by Ruzora · ruzora.com/skills
