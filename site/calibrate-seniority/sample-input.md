Hi. Two things, sorry this is long. We're Haulwise, 11 people, seed ($4M last spring), software for small freight brokers (load board + carrier payments). Engineering is me (CTO, cofounder) plus two engineers: one frontend, one full stack who mostly does the load board.

**The role.** We want to hire a mid-level backend engineer, 3-5 years max (we don't want someone too senior who gets bored or costs too much). Budget is $125-140k, US remote. They would own carrier payouts: we pay truckers after delivery, quick-pay (same day for a fee) or standard 30 days. Today it's a cron job I wrote 18 months ago that calls our bank's ACH API, plus a lot of manual fixing in a spreadsheet when payouts fail or double up. Twice this year a carrier got paid twice. Over the next 6 months they'd rebuild payouts properly and add invoicing for brokers. From January I'm going to be mostly on enterprise sales calls and fundraising, so honestly they'll work pretty much alone. Maybe they help us interview engineer #4 later in the year.

**The candidate.** Got a referral, first name Camila. Here's her CV (copy-paste, formatting lost):

Camila R. | Senior Software Engineer
Brightpixel Studio (digital agency, 6 people), Senior Software Engineer, Mar 2025 to present
- Lead developer on e-commerce and booking projects for 8+ clients
- Built and deployed REST APIs in Node.js / TypeScript (Postgres, Redis)
- Worked on Stripe payment integration for a furniture retailer, including webhooks
- Led a team of 2 junior devs on a hotel booking app
- Improved page load times by 40%
Brightpixel Studio, Software Engineer, Jan 2024 to Mar 2025
- Developed features for client web apps (React, Node.js)
- Contributed to CI/CD setup with GitHub Actions
Full-stack bootcamp, 2023
Operations Analyst, Andes Cargo Logistics, 2017 to 2022
- Managed carrier settlements and payment exceptions for 300+ trucking partners
- Built Excel/VBA tools to reconcile carrier invoices against delivery records, cut monthly close from 6 days to 2
Education: B.S. Industrial Engineering, 2016

**My 30-min screen call notes:**
- really knows freight payments from the ops side, explained quick-pay vs standard terms better than our sales guy
- Stripe webhooks: said they had duplicate webhook events causing double emails, "we added an idempotency check with the lead dev from the client". when I asked who designed it she said the client's lead dev wrote the spec, she implemented
- asked how she'd rebuild our payouts: talked about a payouts table with statuses and retries, then asked me what our bank does on a failed ACH return, which I didn't know offhand
- after launch most agency projects are handed to the client's team, she said she was "on call for the first 2 weeks" on the booking app
- good energy, seemed senior to me
- not sure about her degree, it's from a small university in Peru, never heard of it. also graduated 2016 so she's older than she looks on paper? not sure if that matters

What level do we actually need, and what level is she? Should we move her forward?
