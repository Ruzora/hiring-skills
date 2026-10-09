Can you turn these into scorecards + a debrief? We're Tallgrass Ledger, 14 people, fintech (AP automation for mid-size companies), hiring a Senior Backend Engineer (Python/Postgres). Candidate is Dana R. Debrief is tomorrow at 10. Our role scorecard says must-haves are: backend design for money-moving systems, coding quality, ownership. Nice-to-have: mentoring.

Notes below are copy-pasted from our Google Doc, sorry for the mess.

---

**Marcus (CTO), system design, 60 min**
- asked her to design the payment run scheduler (batch ACH payouts, retries, idempotency)
- started by asking volumes, how many customers, cutoff times for ACH. good
- proposed a jobs table + worker pool, used an idempotency key per payout = (invoice_id, attempt_group). explained why a retry must not double pay
- when I asked what happens if the worker dies mid-batch she said mark rows "in_flight" with a lease timeout and a reconciler job. didn't need a hint
- didn't bring up observability until I asked, then gave decent answer (alerts on stuck in_flight > lease)
- she's probably early 40s, wondering if she'd be ok with startup pace vs big bank
- overall strong yes, best design interview this quarter

**Priya (Senior Eng), live coding, 60 min**
- problem: parse a CSV of invoices, dedupe by vendor + amount + date window, output totals
- took ~8 min asking clarifying qs (what counts as dupe, timezone) which I thought was a lot
- wrote it in Python, worked for main case. missed the case where amounts are strings with commas, found it herself when I said "try the sample file"
- no tests until I asked, then wrote 2 pytest cases quickly
- talked through complexity fine
- strong accent, communication might be an issue with the team?
- solution was ok but honestly the last candidate (Ken) was faster
- lean no. not sure she's senior

**Jordan (CEO/founder), values + ownership, 45 min**
- great culture fit!! super easy to talk to, reminded me of me at my first startup
- told story about owning a reconciliation bug at her last job (regional bank): noticed mismatch in nightly report nobody was assigned to, traced to a rounding issue in FX conversion, fixed it, then wrote the runbook and set up an alert. said "I" for the fix and "we" for the rollout
- asked good questions about our runway and on-call
- mentioned she has two kids so might need flexible hours, fine with us but flagging
- she asked if she could mentor juniors, likes that, said she ran the intern program at the bank for 2 years but didn't go into details
- strong yes, I'd hire her tomorrow. Marcus and I already chatted and we agree
