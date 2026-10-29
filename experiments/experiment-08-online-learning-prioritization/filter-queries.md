# ClassSpring Jira query set

These are reproducible JQL query strings for Jira's advanced issue search. They are query instructions, not saved filter links. Confirm that project key and labels match the live board before saving a filter.

| View | JQL |
|---|---|
| Active sprint | `project = CLSPRG AND sprint in openSprints() ORDER BY Rank ASC` |
| To Do delivery work | `project = CLSPRG AND sprint in openSprints() AND statusCategory = "To Do" ORDER BY priority DESC` |
| Must-have scope | `project = CLSPRG AND labels = moscow-must ORDER BY priority DESC` |
| Should-have scope | `project = CLSPRG AND labels = moscow-should ORDER BY priority DESC` |
| Could-have scope | `project = CLSPRG AND labels = moscow-could ORDER BY priority DESC` |
| Deferred scope | `project = CLSPRG AND labels = moscow-wont ORDER BY priority DESC` |
| Kano Basic hypotheses | `project = CLSPRG AND labels = kano-basic ORDER BY key ASC` |
| Kano Performance hypotheses | `project = CLSPRG AND labels = kano-performance ORDER BY key ASC` |
| Kano Attractive hypotheses | `project = CLSPRG AND labels = kano-attractive ORDER BY key ASC` |
| Blocked/dependent stories | `project = CLSPRG AND issueLinkType in ("blocks", "is blocked by") ORDER BY priority DESC` |

Kano labels describe unvalidated expectations until learner research has been completed. Do not interpret the query as a survey result.
