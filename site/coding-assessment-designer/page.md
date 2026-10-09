---
title: "Coding Test for Hiring Developers: Free AI-Resilient Tool"
description: "A free AI skill that designs a coding test for hiring developers that still works when candidates use AI: seeded-bug review, hidden rubric, follow-up."
target_query: coding test for hiring
category: interview
related_blog: take-home-vs-live-coding-interviews
cta: /how-we-vet
author: Roberto Espinoza
updated: 2026-10-04
---

# Coding test for hiring developers that still works when everyone has AI

Coding Assessment Designer is a free AI skill that designs a coding test for hiring developers in your stack: a seeded-bug code review, an extend-the-codebase task or a short paid trial, plus a hidden rubric and the follow-up conversation that shows whether the candidate understands their own work. Unpaid tests are capped at 2-3 hours.

## What you get

- A plain diagnosis of your current test and the format that fits your situation.
- A paste-ready candidate brief with the time cap, the AI rule, the criteria headings and an accommodation line.
- The task material itself. For a seeded-bug review, that is a real pull request in your language and domain with five planted problems, and a private answer key.
- A hidden rubric with behavioral anchors, written before any submission arrives.
- A 30-45 minute follow-up script with a live requirement change and an AI-use question.

## Sample output

From a run on a fictional 20-person Django startup whose 48-hour take-home produced 11 near-identical submissions:

**PR #[n]: Auto-create invoices when a distributor marks an order delivered**

> When the distributor sync sees an order flip to DELIVERED, we now enqueue a Celery task that pulls the final lines from the distributor and creates the Invoice and its lines. Rules from the billing spec: the bar's discount applies to beer lines only; keg deposits go on the invoice as their own line and are never discounted. The due date is the bar's payment terms (net 15 or net 30) counted from the delivery date. Split deliveries happen for roughly 1 in 10 orders. Also adds a read-only invoices endpoint for the bar portal. Line numbers below are per file.

**From the private answer key:**

| # | Line(s) | Issue | Category | Severity | What a strong candidate says |
|---|---|---|---|---|---|
| 2 | tasks.py 46 | Due date counted from `timezone.now()` (when the task runs), not from `order.delivered_at` as the PR description requires. Wrong whenever the task runs late: retries with backoff, a queue backlog, or a sync that backfills older deliveries. | Correctness / business rule | Medium | "The spec says from delivery, this uses today. Use `order.delivered_at.date()` (in the bar's timezone). Then which delivery date for split deliveries?" Links it to the ambiguity. Notes the test would have caught it if it checked the due date. |

**From the follow-up script:**

Live change: "Distributors now sometimes send a corrected order after delivery, with a line removed or a quantity changed, up to 48 hours later. How should invoicing handle that, and what in this code and its tests changes?"

## How it works

AI assistants write clean greenfield code. So a test that asks for greenfield code mostly measures access to a good assistant. The skill moves the test to what assistants don't supply on their own: deciding which of five problems matters most, fitting into an existing codebase's conventions, noticing an unclear requirement, and explaining choices live.

The rules it builds in:

- **The conversation is the test.** The submission earns a follow-up call. If a candidate can't explain a choice in their own code, or can't make a small change to it live, Understanding scores a 1 and the submission is treated as unverified, however clean it looks. Follow-up criteria carry at least 40% of the weight.
- **Seed five problems, one per category.** Correctness, data safety, failure handling, performance and maintainability, with at least one high-severity issue. One bug is only a bug if you read the brief, which rewards people who read requirements.
- **Prioritization beats count.** Three issues with the data-loss bug ranked first beats nine style comments that miss it.
- **Rubric first.** Written before any submission, so it doesn't drift toward the first one you read.
- **Respect people's time.** A stated 2-3 hour cap, piloted on someone on your team first, a live alternative for people who can't spare an evening, and feedback for everyone who submits. Anything over the 3-hour cap is paid.
- **Paid trials get written terms.** Scope, rate, IP assignment, no production access, decision date. Code written by an independent contractor is generally not "work made for hire" under 17 U.S.C. § 101, so you need a signed assignment if you might keep the work.

### How this compares

Static take-home templates are usually greenfield builds, the format AI assistants finish for the candidate. Asking a chatbot cold gets you a task, sometimes a rubric, and almost never seeded-bug code with an answer key in your stack.

## How to install and use

**Claude.ai:** download the skill's .zip and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then describe the role, the stack and your current test.

**Claude Code:** run `/plugin marketplace add Remutopia/ruzora-skills`, then `/plugin install hire-interview@ruzora-hiring`, and ask it to design a coding test.

**Any other AI (ChatGPT, Gemini and others):** copy the prompt version of the skill from the repo, paste it as the first message, then describe the role.

Say whether AI is allowed on the job, who can grade, and whether you can pay for a short trial.

## Frequently asked questions

### What is a good coding test for hiring developers in 2026?

One that tests reading and judging code, fitting into existing code, and explaining decisions live. A seeded-bug pull request review followed by a short conversation works for most mid and senior roles, and takes candidates about an hour.

### How long should a take-home coding test be?

Two to three hours, stated as a hard cap and graded within it. Pilot it on someone on your team first. If the task needs more than that, pay the candidate for it.

### How do you stop candidates using AI on a coding test?

You mostly can't in an async take-home, so don't build the test around a ban. Allow AI with disclosure, then run a follow-up where the candidate explains their code and changes it live. That part is hard to fake.

### Should you pay candidates for take-home assignments?

Pay for anything over the 3-hour cap, put the terms in writing first, and never use unpaid candidate work in your product.

## Want developers who already passed a live coding stage?

Ruzora's 5-stage vetting includes live coding, system design and AI-tool proficiency, and you get a vetted shortlist within 72 hours. See [how we vet](/how-we-vet) or [request a shortlist](/request-shortlist).

For the format trade-offs in depth, read [take-home vs live coding interviews](/blog/take-home-vs-live-coding-interviews), and for the design principles, [how to design a coding challenge](/blog/how-to-design-a-coding-challenge).
