# CampusCart — One-Week Sprint Plan

## Sprint goal

Let a campus member find an active marketplace listing and let a seller publish a basic listing.

## Live sprint

- Jira project: [CampusCart Marketplace (CCART)](https://sofenglab.atlassian.net/browse/CCART)
- Backlog: [Live Scrum board](https://sofenglab.atlassian.net/jira/software/c/projects/CCART/boards/67/backlog)
- Dates: 29 October–5 November 2026
- State: Active; no work is represented as completed in this plan.

## Candidate sprint backlog

The active sprint includes four foundational stories, totaling 18 native Jira Story point estimate values: create account/sign in (5), search listings by category (5), view listing details (3), and create a listing (5). Listing detail depends on search; listing creation depends on account access. Estimates are relative planning values and should be checked against actual team capacity before they are treated as a commitment.

The live project contains eight stories; four are in the active sprint and four remain in the backlog. Jira is the authoritative view of the current membership and statuses; see the linked board.

## Prerequisites and acceptance

| Story | Estimate | Prerequisite | Acceptance evidence |
| --- | ---: | --- | --- |
| Create account and sign in | 5 | None | Valid email creates an account; invalid input produces a clear error; signed-in member sees the profile. |
| Search listings by category | 5 | Listing catalogue | Category and keyword narrow active listings; empty results explain the outcome. |
| View listing details | 3 | Category search | Detail shows price, condition, seller, and image placeholders; closed listings cannot be contacted. |
| Create a listing | 5 | Account access | Required listing fields validate and a saved listing appears in search. |

Jira contains native `blocks` links for the dependencies. The other four stories remain for later planning: save listing, message seller, mark listing sold, and report a listing.

## Risks and review controls

- Confirm account verification and seller contact privacy before implementation.
- Use active listings only in search and hide sold items from buyer results.
- Confirm required listing fields and marketplace moderation ownership.
- Review only behavior that can be demonstrated with acceptance evidence; leave all four issues To Do until actual work is complete.

Planning cadence: agree scope and capacity at sprint planning, inspect blockers daily, demonstrate evidenced behavior at review, and record one practical process change at the retrospective. These are planned events, not completed events.

## Events

- Planning: agree on goal, available capacity, acceptance examples, and who will review each story.
- Daily check-in: inspect progress and blockers, and update issue status only when work changes.
- Review: demonstrate the sign-in, listing search/detail, and listing creation flows that actually work.
- Retrospective: record one practice to keep and one improvement for the next sprint.

## Definition of Done

Acceptance criteria pass; the change is reviewed; no known blocker prevents the demonstrated flow; and Jira status reflects the evidence. Do not mark stories Done before implementation and acceptance evidence exist. At the time of this report, the sprint is active and no outcome is claimed.
