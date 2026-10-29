# Campus Library Management System Project Overview

Published in the [Campus Library Management System Confluence space](https://sofenglab.atlassian.net/wiki/spaces/CAMPUSLIB/pages/5603329/Library+Management+System+Project+Overview). The live page contains the same seven-story scope and a live Jira Issues macro.

## Objective and current progress

Help students locate, reserve, and collect campus-library books, and help librarians monitor availability and circulation.

LIBSYS Sprint 1 runs 29 October–5 November 2026. It contains seven stories and 21 estimated points. Current Jira status: **To Do 7 · In Progress 0 · Done 0 · 0/7 complete (0%)**. This is a live planning snapshot; no software work or approval is claimed.

## Requirements and planned delivery

| Jira issue | Requirement | Points | Planned responsibility | Dates | Prerequisite |
|---|---|---:|---|---|---|
| [LIBSYS-1](https://sofenglab.atlassian.net/browse/LIBSYS-1) | Search books by title | 2 | Frontend | 29–30 Oct | Catalog data |
| [LIBSYS-2](https://sofenglab.atlassian.net/browse/LIBSYS-2) | Search books by author | 2 | Frontend | 29–30 Oct | Catalog data |
| [LIBSYS-3](https://sofenglab.atlassian.net/browse/LIBSYS-3) | Show copy availability | 3 | Backend | 30 Oct–2 Nov | Catalog and circulation records |
| [LIBSYS-4](https://sofenglab.atlassian.net/browse/LIBSYS-4) | Reserve an available copy | 5 | Full stack | 2–4 Nov | LIBSYS-1, 2, and 3 |
| [LIBSYS-5](https://sofenglab.atlassian.net/browse/LIBSYS-5) | Notify reader when hold is ready | 3 | Backend | 4–5 Nov | LIBSYS-4 |
| [LIBSYS-6](https://sofenglab.atlassian.net/browse/LIBSYS-6) | View librarian circulation dashboard | 3 | Frontend | 2–5 Nov | Availability and circulation data |
| [LIBSYS-7](https://sofenglab.atlassian.net/browse/LIBSYS-7) | Generate a monthly circulation report | 3 | Backend | 3–5 Nov | LIBSYS-6 and accurate loan/return records |

Responsibilities are proposed roles, not separate assigned accounts. Estimates are relative planning values, not measured velocity or a commitment.

## Acceptance and review workflow

- Search returns title/author matches and helpful empty results; availability is checked against current circulation data.
- Reservations are limited to eligible available copies; duplicate requests and cancellation follow documented rules.
- Hold notices identify the relevant copy and avoid duplicate messages.
- Dashboard and monthly report totals use the same source records and agreed month boundaries.
- For future implementation, require reviewed changes, acceptance evidence, permission checks, relevant checks passing, and updated documentation before marking Done.

Planning cadence: kickoff and capacity review at sprint start, brief blocker checks during the week, an evidence-based demonstration at review, and one documented improvement at retrospective. These events are planned; they are not represented as already held.

## Risks and next steps

- Confirm minimum catalogue fields and missing-data behavior.
- Define a single source of truth and stale-data handling for availability.
- Agree hold queue, cancellation, and notification failure rules with a librarian.
- Reconcile the monthly report to a small hand-checked sample before acceptance.
- Update statuses and the 0/7 progress figure only when work changes and evidence exists.
