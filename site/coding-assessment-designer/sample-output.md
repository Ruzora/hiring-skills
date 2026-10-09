# Coding assessment: Backend Engineer, mid-level, Python / Django REST Framework / Postgres / Celery
Assumptions:
- Your CTO grades every submission and runs every follow-up call; budget is about 15 minutes of grading plus a 30-minute call, which fits their 1 hour per candidate.
- Most candidates are currently employed (your last round suggests so), so unpaid candidate time is kept to about 1 hour.
- You reply to every candidate within 3 business days of their follow-up call. Change this if your process is slower.
- Model and field names in the task code (Order, Bar.payment_terms_days, Bar.discount_pct, DistributorClient) are placeholders that sound like your domain. Rename them to match your codebase before sending.
- The paid stage is optional and not designed here; see "Format and why".

## What's wrong with the current test
"Build a REST API for beer orders with auth, tests and docs" is a greenfield task, and an AI assistant produces a complete, clean, fully tested solution for it in minutes. That is why 11 of 14 submissions looked identical and why two people could not explain their own auth: the test measured who can prompt, then the call caught the gap too late. "48 hours, take as long as you need" is an uncapped weekend task, so it filters out exactly the employed, caregiving candidates you want (you lost one). It also tests nothing about your real work, which is syncing orders with distributors and getting invoices right.

## Format and why
Seeded-bug review, async: the candidate reviews a 140-line pull request in your stack (a Celery task that auto-creates invoices when a distributor marks an order delivered) for up to 60 minutes, then a 30-minute follow-up call with your CTO. AI is allowed with disclosure, because you use it on the job and a ban you cannot enforce in a take-home only penalizes the honest candidates. A mid-level engineer on order sync and invoicing spends much of the job reading code and spotting the retry bug that bills a bar twice, and an assistant does not tell them which of five problems matters most or defend that ranking live; this also fits your CTO's hour (15 minutes with the answer key, 30 on the call).

Hold the paid option in reserve. Only if two finalists are close after the follow-up, run a paid half-day trial on a non-critical task, with written terms (scope, rate, IP assignment, NDA, sandbox access only) agreed before work starts.

## Candidate brief (paste-ready)
Subject: Brightpour backend engineer: next step (about 1 hour)

Hi [Name],

Thanks for your time so far. The next step is a code review, not a build-from-scratch project. It mirrors the work: much of this role is order sync with distributors and invoicing, and most of that work is reading and changing existing code.

What to do: The attached pull request adds automatic invoicing when a distributor marks an order delivered. Review it as you would a teammate's PR. Leave comments on the lines you would change, say how much each one matters, and suggest a fix. If something in the PR description is unclear, say what you would ask, or state the assumption you made. Finish with a short note: if this PR could only get one change before merging, which one and why.

Time cap: 60 minutes, hard. Stop at 60 minutes and send what you have. We grade within that cap, and an unfinished review that gets the important things right beats a long list. If you would rather not spend the time on your own, we can do the same review together on a 60-minute call instead. Just reply and say so.

AI tools: Allowed, with disclosure. We use them too. Add one or two lines at the end saying what you used and for what. On the call we will ask about it, so use them the way you would at work.

What we look at:
- Prioritization: finding what matters most
- Impact and fixes
- Understanding (in the conversation)
- Adapting to a change
- Handling unclear requirements

Follow-up: A 30-minute video call with our CTO. You will walk us through your review, we will ask why you ranked things the way you did, and we will change one requirement and talk through how the code should change. No new code to write before the call.

Pay: This step is unpaid, which is why it is capped at 60 minutes.

Accommodations: If you need extra time or a different format for a disability-related or other reason, reply to this email and we will work it out with you.

Timeline: Please send your review by [date]. We will book the call within a few days of receiving it and you will hear back from us within 3 business days after the call, with a few sentences of feedback whatever the outcome.

Thanks,
[Your name]
Brightpour

## Task material

**PR #[n]: Auto-create invoices when a distributor marks an order delivered**

> When the distributor sync sees an order flip to DELIVERED, we now enqueue a Celery task that pulls the final lines from the distributor and creates the Invoice and its lines. Rules from the billing spec: the bar's discount applies to beer lines only; keg deposits go on the invoice as their own line and are never discounted. The due date is the bar's payment terms (net 15 or net 30) counted from the delivery date. Split deliveries happen for roughly 1 in 10 orders. Also adds a read-only invoices endpoint for the bar portal. Line numbers below are per file.

`invoicing/tasks.py` (new)
```python
import logging
from datetime import timedelta
from decimal import Decimal, ROUND_HALF_UP

from celery import shared_task
from django.utils import timezone

from distributors.client import DistributorAPIError, DistributorClient
from invoicing.models import Invoice, InvoiceLine
from orders.models import Order, Product

logger = logging.getLogger(__name__)

CENT = Decimal("0.01")


def _money(value):
    return Decimal(str(value)).quantize(CENT, rounding=ROUND_HALF_UP)


@shared_task(
    bind=True,
    autoretry_for=(DistributorAPIError,),
    retry_backoff=True,
    max_retries=5,
)
def create_invoice_for_order(self, order_id):
    order = Order.objects.select_related("bar", "distributor").get(id=order_id)
    client = DistributorClient(order.distributor.api_token)

    try:
        remote = client.get_order(order.distributor_order_id)
    except DistributorAPIError:
        logger.warning(
            "Distributor fetch failed for order %s (distributor=%s, token=%s)",
            order.id,
            order.distributor.name,
            order.distributor.api_token,
        )
        raise

    invoice = Invoice.objects.create(
        order=order,
        bar=order.bar,
        issued_at=timezone.now(),
        due_date=timezone.now().date() + timedelta(days=order.bar.payment_terms_days),
    )

    discount = order.bar.discount_pct / Decimal("100")
    total = Decimal("0.00")

    for item in remote["lines"]:
        product = Product.objects.get(sku=item["sku"], brewery=order.brewery)
        quantity = int(item["quantity"])
        unit_price = _money(item["unit_price"])
        line_total = _money(unit_price * quantity * (1 - discount))

        InvoiceLine.objects.create(
            invoice=invoice,
            product=product,
            description=product.name,
            quantity=quantity,
            unit_price=unit_price,
            amount=line_total,
        )
        total += line_total

        deposit = _money(item.get("keg_deposit", "0"))
        if deposit:
            deposit_total = _money(deposit * quantity)
            InvoiceLine.objects.create(
                invoice=invoice,
                product=product,
                description=f"Keg deposit: {product.name}",
                quantity=quantity,
                unit_price=deposit,
                amount=deposit_total,
            )
            total += deposit_total

    invoice.total = total
    invoice.save(update_fields=["total"])

    client.mark_invoiced(order.distributor_order_id, invoice_number=invoice.number)
    return invoice.id
```

`distributors/sync.py` (changed)
```python
from django.db import transaction
from django.utils.dateparse import parse_datetime

from invoicing.tasks import create_invoice_for_order
from orders.models import Order


def apply_status_update(order, payload):
    new_status = payload["status"]
    became_delivered = (
        order.status != Order.Status.DELIVERED
        and new_status == Order.Status.DELIVERED
    )

    order.status = new_status
    if became_delivered:
        order.delivered_at = parse_datetime(payload["delivered_at"])
    order.save(update_fields=["status", "delivered_at"])

    if became_delivered:
        transaction.on_commit(lambda: create_invoice_for_order.delay(order.id))
```

`invoicing/views.py` (new)
```python
from rest_framework import permissions, viewsets

from invoicing.models import Invoice
from invoicing.serializers import InvoiceSerializer


class InvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return (
            Invoice.objects.filter(bar_id=self.request.user.bar_id)
            .prefetch_related("lines")
            .order_by("-issued_at")
        )
```

`invoicing/tests/test_tasks.py` (new)
```python
import pytest

from invoicing.models import Invoice
from invoicing.tasks import create_invoice_for_order


@pytest.mark.django_db
def test_create_invoice_for_delivered_order(order_factory, mock_distributor):
    order = order_factory(status="DELIVERED", bar__payment_terms_days=30)
    mock_distributor.get_order.return_value = {
        "lines": [
            {"sku": "HAZY-IPA-HALF", "quantity": 2, "unit_price": "185.00", "keg_deposit": "30.00"},
        ]
    }

    create_invoice_for_order(order.id)

    assert Invoice.objects.filter(order=order).exists()
```

Seeded ambiguity (not a bug, do not score as one): "counted from the delivery date" with split deliveries. First drop or last drop? A strong candidate asks or states an assumption.

### Answer key (private)
| # | Line(s) | Issue | Category | Severity | What a strong candidate says |
|---|---|---|---|---|---|
| 1 | tasks.py 21-26, 42-47, 84 | No idempotency and no transaction. If `mark_invoiced` (line 84) raises `DistributorAPIError`, `autoretry_for` reruns the whole task and creates a second Invoice for the same order. If `Product.objects.get` fails mid-loop, a half-built invoice with a wrong total is left behind. | Failure handling | High | "A flaky distributor API means the bar gets billed twice. Make it idempotent: a unique constraint on Invoice.order plus `get_or_create` or an early return if an invoice exists, wrap the invoice and lines in `transaction.atomic()`, and move `mark_invoiced` into its own retried step after commit so a failed ack never re-creates the invoice." Ranks this first. |
| 2 | tasks.py 46 | Due date counted from `timezone.now()` (when the task runs), not from `order.delivered_at` as the PR description requires. Wrong whenever the task runs late: retries with backoff, a queue backlog, or a sync that backfills older deliveries. | Correctness / business rule | Medium | "The spec says from delivery, this uses today. Use `order.delivered_at.date()` (in the bar's timezone). Then which delivery date for split deliveries?" Links it to the ambiguity. Notes the test would have caught it if it checked the due date. |
| 3 | tasks.py 34-39 | The distributor's API token is written to the logs on every failed fetch. Anyone with log access (or your log vendor) can call the distributor's API as you. | Data safety / security | Medium | "Never log credentials. Log order id and distributor name only, and rotate any token already in the logs." |
| 4 | tasks.py 52-53 | One `Product` query per line (N+1). Fine for a 5-line order, slow when month-end or a backfill invoices hundreds of orders. | Performance at realistic scale | Low | "Fetch all SKUs in one query before the loop (`Product.objects.filter(sku__in=..., brewery=...)` into a dict), and use `bulk_create` for the lines." |
| 5 | test_tasks.py 18 | The test only asserts an invoice exists. It checks no total, no discount on beer vs. deposit, no due date and no retry behavior, so it passes with bugs 1 and 2 present. | Maintainability / tests | Low | "Assert the total (2 x 185.00 discounted plus 60.00 undiscounted deposit), the due date from `delivered_at`, and add a test that running the task twice yields one invoice." |

## Hidden rubric (private)
| Criterion | Weight | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|
| Prioritization (submission) | 20% | Finds the duplicate-invoice bug and ranks it first, plus at least 2 others; no flood of style nits | Finds the duplicate-invoice bug but does not rank it first, or finds it plus 1 other | Finds 2-3 real issues but misses the duplicate-invoice bug | Mostly style or naming comments; misses the real issues |
| Impact and fixes (submission) | 20% | Explains impact in business terms (bar billed twice, wrong due date, leaked token) and gives a specific, workable fix for each | Specific fixes, impact stated for most | Fixes are vague ("add error handling") or impact is missing | No fixes, or fixes that would not work |
| Understanding (follow-up) | 30% | Explains every comment in their own words, defends the ranking, handles "why not X" with real trade-offs (for example unique constraint vs. lock) | Explains most comments; minor gaps under questioning | Struggles to explain why some comments matter; answers drift from what they wrote | Cannot explain their own comments. Treat the submission as unverified, however good it looks |
| Adapting to a change (follow-up) | 20% | Reasons through the live change correctly, names what code and tests change, spots a new edge case unprompted | Correct approach with some prompting | Partial approach; misses the interaction with retries or deposits | Cannot reason about the change |
| Handling unclear requirements | 10% | Asked about split deliveries or stated a clear assumption in the review, and explains the trade-off on the call | Raises it on the call when prompted lightly | Notices only when pointed at it | Silently guessed; no awareness the rule was unclear |

Conversation criteria (Understanding plus Adapting) carry 50% of the weight.

## Follow-up conversation (30-45 min)
1. "Walk me through your review as if I'm the teammate who wrote this PR. Start with what you'd want me to fix first." (listen for: leads with the duplicate-invoice risk, uses business terms, does not read the comments out in order)
2. "If you could only leave one comment on this PR, which one and why?" (listen for: a clear choice and a reason tied to money or customers, not "they're all important")
3. "You suggested [their fix for issue 1, for example a unique constraint]. What else did you consider, and why not that?" (listen for: real alternatives such as `select_for_update`, an idempotency key on the task, or checking for an existing invoice, and what each costs)
4. "The billing spec says due date from the delivery date, and about 1 in 10 orders is split across two drops. What would you do?" (listen for: asks who decides, proposes first vs. last drop with a reason, suggests confirming with whoever owns billing rather than guessing)
5. "Month-end, a distributor's API is down for 2 hours and then 400 orders flip to DELIVERED at once. What breaks first?" (listen for: retries piling up, duplicate invoices if not fixed, N+1 load, rate limits on the distributor API, due dates drifting if still using now())

Live change: "Distributors now sometimes send a corrected order after delivery, with a line removed or a quantity changed, up to 48 hours later. How should invoicing handle that, and what in this code and its tests changes?" (listen for: does not create a second invoice; proposes a credit note or an amended invoice depending on whether it was already sent to the bar; keeps it idempotent; keeps deposits undiscounted on the correction; names the tests they would add)

AI question: "Your note says you used [tool] for [task]. Show me one thing it suggested that you changed or threw out, and why." (listen for: a concrete example and their own judgment on top of the tool; an honest "I used it to check my reasoning on X" is fine; vague answers or a review they cannot explain line by line are the red flag)

## Grader notes
- Pilot result needed: your CTO (or one trusted engineer outside the hiring loop) does the review cold before the first candidate gets it. If they need more than about 40 minutes of the 60-minute cap, cut the PR (drop views.py first). Confirm the 5 issues are the only ones they would flag as real; if they find a sixth, fix it or add it to the key before sending.
- Red flags:
  - Misses the duplicate-invoice bug entirely, or calls it low severity, in an invoicing role.
  - A long, polished review that the candidate cannot explain on the call, especially fixes they cannot reason about when you ask "why not X".
  - Comments on views.py or sync.py that invent problems the code does not have, confidently stated (often unchecked AI output).
  - Silently picks a due-date rule for split deliveries and treats it as fact.
  - In the live change, proposes deleting and re-creating the invoice after it was already sent to the bar.
- Score each criterion with evidence before discussing with anyone. The hiring decision belongs to a person, using this as evidence.

General information, not legal advice. US rules as of 2026.

---
Made with the free Coding Assessment Designer skill by Ruzora · ruzora.com/skills
