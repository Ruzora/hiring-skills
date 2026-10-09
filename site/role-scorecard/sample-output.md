# Role scorecard: Senior Software Engineer, Integrations (Senior)
Owner: CEO (technical review by the fractional CTO) · Status: draft for sign-off · 2026-10-04
Assumptions:
- Start date is January 2027. The EHR deadline is the end of Q2 2027 (June 30), which is about month 6 of the hire.
- The CEO is the hiring manager and signs this scorecard. The fractional CTO reviews technical stages but works only 10 h/week.
- Your current engineer stays on core product work. The mobile app is outside this hire (see the unicorn check).
- Calendar sync and the EHR integration are owned by the same person because they are the same kind of work: keeping data correct between our system and someone else's.
- Remote in the US means the hire works on US business hours.

## Mission
Make Harborlight's connections to outside systems reliable enough that clinics stop calling support about calendar sync, and the 30-clinic chain renews because its EHR integration works.

## Outcomes
| # | Outcome | Measure | By | Evidence it happened |
|---|---|---|---|---|
| 90d | Main causes of sync failures found and the biggest one fixed. Failures trigger an alert before a clinic calls | Written root-cause report. Sync tickets drop from ~40% of all tickets to [target]%. Alerting is live | Day 90 | Report reviewed by the fractional CTO. Ticket data from the help desk. A test failure fires an alert |
| 1 | Calendar sync stops being a top support problem | Sync tickets ≤ [target]% of all tickets, held for 3 months in a row. Sync success rate ≥ [target]% | Month 9 | Help-desk export. Sync dashboard |
| 2 | EHR integration live for the 30-clinic chain | All [N] clinics live on the scope agreed with the chain. Passes the chain's acceptance and security review | Month 6 (June 30, 2027) | Chain's written sign-off. Usage logs from all clinics |
| 3 | Integrations no longer depend on one person | Runbooks for sync and EHR. The existing engineer resolves [N] integration incidents without the new hire | Month 12 | Runbooks in the repo. Incident log shows who resolved each one |
| 4 | Integrations built to be reused | A second calendar provider or EHR connection costs ≤ [target] engineer-weeks, measured on the next one built | Month 12 | Time tracked on the next integration |

Unicorn check: The real problems need three specialties: backend integrations (sync and EHR), mobile (React Native) and ML. Nothing in your problems needs ML, so it is dropped. Mobile is a separate specialty at senior depth. **Sequence it:** this hire covers outcomes 1-4. Fix the mobile app with a React Native contractor on a fixed scope now, or make it the next hire. One person cannot fix sync, ship the EHR integration by June and rebuild a neglected app all at once.

## Level
Senior. The outcomes are ambiguous problems ("sync breaks a few times a week", "the chain wants an EHR integration") that have to become shipped, maintained systems. Nobody will write a spec, and the only technical review is 10 h/week from the fractional CTO. Hiring Mid would leave nobody to frame the problems. Budget note: $150-170k for a senior US-remote engineer with integration (and ideally healthcare) experience may be at or below market in some regions. Check current salary data before posting. If the range can't move, keep Senior and cut nice-to-haves rather than dropping the level.

## Must-haves (max 4)
| Must-have | Tied to outcome | Tested at |
|---|---|---|
| Has owned a production service that syncs with third-party APIs (OAuth, webhooks, retries, idempotency, rate limits), including being on call for it | 1, 2 | Technical interview |
| Can find the cause of an intermittent data-sync failure from logs and data, and propose a fix with its trade-offs | 90d, 1 | Work sample |
| Has scoped and shipped a project to an external customer deadline without a spec, and kept non-technical people informed on scope and risk | 2 | Founder conversation |
| Has handled sensitive or regulated customer data (health, financial) in production, with access controls and audit logging | 2 | Screen call |

## Nice-to-haves (learnable in ~90 days)
- EHR integration experience (HL7, FHIR or a specific EHR vendor's API)
- Google Calendar / Microsoft Graph API experience
- Node/TypeScript and React (our stack)
- AWS
- Familiarity with HIPAA compliance work

## Not required (removed proxies)
- 5+ years React and Node: replaced by evidence of owning a production integration service.
- CS degree: the knowledge needed is integration design and debugging, which the work sample tests directly.
- ML experience: no outcome needs it.
- React Native/mobile: sequenced to a contractor or a later hire.
- Frontend depth: the outcomes are backend and integration work.

## Competencies
| Competency | Strong signal | Weak signal | Stage |
|---|---|---|---|
| Debugging under ambiguity | Forms hypotheses from the logs, rules them out in order, and states what they'd instrument next | Guesses a fix without evidence, or asks for the answer | Work sample |
| Integration design | Explains how they handled duplicates, partial failures and the other side's API changing, and names the option they rejected | Describes the happy path only | Technical interview |
| Ownership and judgment | Walks through a decision they got wrong: what they missed, how they found out, what they changed | Blames others, or can't name one | Founder conversation |
| Raises bad news early | Gives an example of flagging a slipping deadline early, with options and a recommendation | Says problems surfaced at the deadline | Founder conversation |
| Leaves things others can run | References confirm runbooks, decision notes and teammates who could cover for them | References say "only they knew how it worked" | Reference check |

## Deal-breakers
- Cannot work at least [4] hours a day overlapping US clinic business hours
- Answers no to "Are you legally authorized to work in the US?" or yes to "Will you now or in the future require sponsorship?" (if you won't sponsor)
- Cannot explain the trade-offs in their own past work
- Hides or downplays problems instead of raising them early (tested by the "raises bad news early" competency)

## Interview map
| Stage | Owner | Assesses | Time |
|---|---|---|---|
| Screen call | CEO | Regulated-data must-have, time-zone overlap, work authorization, pay range | 30 min |
| Work sample (paid, time-boxed) | Fractional CTO | Debugging a sanitized sync-failure scenario | 2-3 h candidate, 1 h review |
| Technical interview | Fractional CTO + current engineer | Third-party integration must-have, integration design | 75 min |
| Founder conversation | CEO | Deadline delivery, ownership and judgment, raising bad news | 45 min |
| Reference check | CEO | Leaves things others can run | 2 × 20 min |

## Language fixes
| Found | Replace with | Why |
|---|---|---|
| Rockstar Full Stack Developer | Senior Software Engineer, Integrations | "Rockstar" can't be tested. "Full stack" doesn't match the outcomes |
| 5+ years React and Node | "Has owned a production service that syncs with third-party APIs, including on-call" | Years are a weak stand-in for what someone has owned |
| CS degree required | Remove | Proxy. The work sample tests the real skill |
| ML experience a plus | Remove | Not tied to any outcome |
| AWS (as a requirement) | Nice-to-have | Learnable within a quarter |
| culture fit | "Raises bad news early with options" and "writes things down so others can run them" | Can't be scored and invites bias |
| young, energetic team | Remove | Age proxy (the ADEA protects workers 40 and over) |
| Native English speaker | "Clear written and spoken English for daily async work" | National-origin proxy |

## Open questions for the hiring manager
1. Which EHR does the chain use, and does it offer an API or FHIR endpoint? If it needs HL7 interfaces or vendor certification, EHR experience moves to must-have and the June date needs checking.
2. What exactly does the chain need: appointment sync, billing, clinical notes? What is the firm deadline, and who on their side signs off?
3. What are today's baselines (sync tickets per week, current app-store rating)? And what is the mobile plan: contractor, your current engineer, or a later hire?
4. Can the fractional CTO give about 3-4 hours per finalist for the work sample review and technical interview? If not, who reviews?
5. Do you have a HIPAA business associate agreement (BAA) in place with the chain, and who owns compliance? This is general information, not legal advice.

---
Made with the free Role Scorecard skill by Ruzora · ruzora.com/skills
