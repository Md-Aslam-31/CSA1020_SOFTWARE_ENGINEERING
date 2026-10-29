# TeamDesk MVP — Sample Sprint Plan

## Goal and live sprint

Plan a first release that lets a small team sign in, manage tasks, assign ownership, set deadlines, and see shared progress.

- Project: [TeamDesk](https://sofenglab.atlassian.net/browse/TEAMDESK)
- Board: [Active Scrum board](https://sofenglab.atlassian.net/jira/software/c/projects/TEAMDESK/boards/69)
- Sprint: TeamDesk Sprint 1 · 29 October–5 November 2026 · active
- Scope: 10 stories, 24 estimated points; all 10 are To Do at this snapshot (0% complete).

## Epic groups

| Epic | Scope |
|---|---|
| [TEAMDESK-13 — Identity and task ownership](https://sofenglab.atlassian.net/browse/TEAMDESK-13) | TD-01 to TD-03: account roles, task lifecycle, and assignee. |
| [TEAMDESK-14 — Task planning and collaboration](https://sofenglab.atlassian.net/browse/TEAMDESK-14) | TD-04 to TD-07: deadline/priority, labels, links, and comments. |
| [TEAMDESK-15 — Team visibility and reporting](https://sofenglab.atlassian.net/browse/TEAMDESK-15) | TD-08 to TD-11: team board, reminder, export, and shortcuts. |
| [TEAMDESK-16 — Release prioritization and governance](https://sofenglab.atlassian.net/browse/TEAMDESK-16) | TD-12: automatic sprint planning is deferred this release. |

Each of the 12 stories has a native epic parent. Taxonomy remains in labels and descriptions; native MoSCoW/Kano dropdown fields were unavailable through the connected Jira operations.

## Sprint commitment and evidence

| Jira story | Requirement | MoSCoW | Kano hypothesis | Points | Status |
|---|---|---|---|---:|---|
| TEAMDESK-1 | Sign in and assign a role | Must | Basic | 3 | To Do |
| TEAMDESK-2 | Create, edit, archive a task | Must | Basic | 2 | To Do |
| TEAMDESK-3 | Assign a task to a teammate | Must | Basic | 3 | To Do |
| TEAMDESK-4 | Set due date and priority | Must | Performance | 3 | To Do |
| TEAMDESK-5 | Add task labels | Should | Performance | 2 | To Do |
| TEAMDESK-6 | Attach reference links | Should | Performance | 2 | To Do |
| TEAMDESK-7 | Comment on a task | Should | Performance | 2 | To Do |
| TEAMDESK-8 | View a team board | Should | Performance | 2 | To Do |
| TEAMDESK-9 | Receive overdue reminders | Could | Attractive | 3 | To Do |
| TEAMDESK-10 | Export tasks to CSV | Could | Attractive | 2 | To Do |

The 2-point keyboard-shortcut story (TEAMDESK-11, Could) and 1-point automatic-planning story (TEAMDESK-12, Won’t-Have this release) remain outside the sprint. Estimates are relative sizing; no actual capacity or delivery velocity is established.

## Prerequisites and Definition of Done

Jira holds 12 native `blocks` links: TEAMDESK-1 blocks 2/3; TEAMDESK-2 blocks 4/5/6/7/8; TEAMDESK-3 blocks 8; TEAMDESK-4 blocks 9/12; TEAMDESK-8 blocks 11/12. These complement each story's external service and acceptance notes.

For future implementation, a story is Done only after its acceptance evidence is demonstrated, permissions and data boundaries are checked, the change is reviewed, relevant checks pass, and documentation is updated. The active sprint board currently shows all 10 items To Do; no implementation is claimed.

## Risks and review cadence

- Validate team roles and account access before task-level authorization.
- Prevent reminders from exposing task details to unauthorized recipients.
- Define task archive/export retention and protect private links.
- Confirm achievable sprint capacity before treating 24 points as a commitment.

Planning cadence is a kickoff and capacity review, daily blocker review, evidence-based demonstration, and a retrospective note. No such events are claimed as completed.
