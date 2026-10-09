# IP and account-ownership checklists

General information as of 2026-10, not legal advice. Have counsel draft or review assignment language.

## IP checklist

| Item | What good looks like | If missing |
|---|---|---|
| Written IP assignment | Signed agreement with present-tense language ("hereby assigns") covering all work product, code, documentation and inventions created for the company | Contractor code is generally not "work made for hire" (17 U.S.C. 101), so the contractor may own it. Get a confirmatory assignment drafted by counsel, with consideration (a payment) |
| Signed before work started | Assignment dated on or before the first commit | Confirmatory assignment covering past work, by date range and repositories |
| Pre-existing material | Contractor lists their own prior code or tools they bring; company gets a perpetual, royalty-free license to anything they incorporate | Ask for the list now; review the repo for code they reused |
| Open-source use | Contractor discloses open-source components and licenses they added; no copyleft code in proprietary parts without approval | Run a dependency license scan; ask the contractor for a list |
| Confidentiality | Confidentiality clause that survives the end of the engagement | Add it in the next amendment |
| Moral rights | Waiver or consent where local law gives authors moral rights (common outside the US) | Ask local counsel for non-US contractors |
| Subcontractors | Contractor must get the same assignment from anyone they bring in, and tell you who they are | Ask who else touched the code |
| Return of materials | On termination: return or delete company data and credentials, and confirm in writing | Add to offboarding |

## Account ownership checklist

Every account below should be owned by a company-controlled identity (a shared admin mailbox or a founder's company account), with billing on a company card. Contractors get member or role access, never ownership.

| Account | Check | Fix |
|---|---|---|
| Source code (GitHub, GitLab, Bitbucket) | Organization owned by the company; contractor is a member, not the owner; repos are not in their personal account | Transfer repos into the company org; make two company people owners |
| Cloud (AWS, GCP, Azure) | Root or organization account email is a company address; billing on company card | Move root email; rotate root credentials; enable MFA held by the company |
| Domain registrar and DNS | Registered to the company; login on company email | Transfer the registrar account; check the auto-renew |
| App stores (Apple, Google Play) | Developer accounts in the company's legal name | Transfer the apps or the account |
| Email and identity provider | Contractor uses company login with company-controlled MFA recovery | Move 2FA recovery to company devices |
| CI/CD, secrets, API keys | Secrets stored in company vaults; keys issued to company accounts | Rotate keys the contractor created under personal accounts |
| Third-party services (Stripe, Twilio, analytics, error tracking, OpenAI or other model APIs) | Accounts in company name, company card | Recreate or transfer; update keys |
| Password manager | Company vault; contractor access by shared folder | Revoke personal-vault sharing |
| Design and docs (Figma, Notion, Google Drive) | Files in company workspace | Transfer ownership |

## Offboarding (ready from day one)
- Remove access the same day the engagement ends: code host, cloud, identity provider, chat, password manager.
- Rotate any secret the contractor could see.
- Confirm in writing that company data was returned or deleted.
- Keep the signed assignment and the final invoice together in one folder; investors will ask.
