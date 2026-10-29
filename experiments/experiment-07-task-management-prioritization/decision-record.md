# TeamDesk — MoSCoW and Kano Decision Record

**Context:** A small team needs a first usable task-management workflow. Priorities below are proposed scope decisions; impact and feasibility are qualitative estimates. Kano categories are provisional hypotheses and need paired functional/dysfunctional questions with real users.

| Jira / ID | Requirement | MoSCoW | Kano hypothesis | Impact / feasibility | Acceptance evidence | Depends on |
|---|---|---|---|---|---|---|
| [TEAMDESK-1](https://sofenglab.atlassian.net/browse/TEAMDESK-1) / TD-01 | Sign in and assign a role | Must | Basic | High / High | Member signs in and sees only role-authorized actions. | User identity service |
| [TEAMDESK-2](https://sofenglab.atlassian.net/browse/TEAMDESK-2) / TD-02 | Create, edit, and archive a task | Must | Basic | High / High | Title and owner are required; edits persist; archived task leaves the active board. | TD-01 |
| [TEAMDESK-3](https://sofenglab.atlassian.net/browse/TEAMDESK-3) / TD-03 | Assign a task to a teammate | Must | Basic | High / High | Assignee is visible and can be changed by a team member. | TD-01 |
| [TEAMDESK-4](https://sofenglab.atlassian.net/browse/TEAMDESK-4) / TD-04 | Set due date and priority | Must | Performance | High / Medium | Due date and priority are visible; overdue work is marked clearly. | TD-02 |
| [TEAMDESK-5](https://sofenglab.atlassian.net/browse/TEAMDESK-5) / TD-05 | Add task labels | Should | Performance | Medium / Medium | Member applies one or more labels and filters by them. | TD-02 |
| [TEAMDESK-6](https://sofenglab.atlassian.net/browse/TEAMDESK-6) / TD-06 | Attach reference links | Should | Performance | Medium / Medium | Valid URL can be saved with a readable label. | TD-02 |
| [TEAMDESK-7](https://sofenglab.atlassian.net/browse/TEAMDESK-7) / TD-07 | Comment on a task | Should | Performance | Medium / Medium | Comments show author and time in chronological order. | TD-01, TD-02 |
| [TEAMDESK-8](https://sofenglab.atlassian.net/browse/TEAMDESK-8) / TD-08 | View a team board | Should | Performance | High / Medium | Active tasks are grouped by status and show owner and priority. | TD-02, TD-03 |
| [TEAMDESK-9](https://sofenglab.atlassian.net/browse/TEAMDESK-9) / TD-09 | Receive overdue reminders | Could | Attractive | Medium / Medium | An opted-in member receives a reminder after a task becomes overdue. | TD-04 |
| [TEAMDESK-10](https://sofenglab.atlassian.net/browse/TEAMDESK-10) / TD-10 | Export tasks to CSV | Could | Attractive | Low / Medium | Export includes title, owner, priority, due date, and status. | TD-02 |
| [TEAMDESK-11](https://sofenglab.atlassian.net/browse/TEAMDESK-11) / TD-11 | Use keyboard shortcuts | Could | Attractive | Low / Medium | Documented shortcuts work without intercepting text entry. | TD-08 |
| [TEAMDESK-12](https://sofenglab.atlassian.net/browse/TEAMDESK-12) / TD-12 | Auto-generate a sprint plan | Won’t this release | Indifferent | Low / Low | Outside first release; manual prioritization remains available. | TD-04, TD-08 |

## Release rationale

The Must scope establishes identity, task persistence, ownership, and basic scheduling. Labels, reference links, comments, and shared board visibility are important enhancements with manual workarounds, so they sit in Should. Reminders, CSV export, and shortcuts are optional conveniences. Automatic planning is deferred because it adds complexity before the team has validated a stable manual workflow.

MoSCoW answers “what belongs in this release?”; Kano estimates “how might presence or absence affect satisfaction?” The models are deliberately independent: TD-04 is Must plus Performance, and TD-12 is Won’t this release plus Indifferent. Reassess with user interviews and paired Kano questions before turning hypotheses into validated findings.

Live statuses are all To Do. The workspace holds requirements and prioritization evidence, not an implemented task-management product.
