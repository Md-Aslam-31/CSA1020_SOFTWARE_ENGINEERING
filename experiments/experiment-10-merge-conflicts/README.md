# Experiment 10 — Resolve a Git merge conflict

## Aim
Create a controlled conflict on one shared line, inspect Git markers, reconcile both changes, and complete the merge.

## Tools required
Git and the task-plan sample in this directory.

## Quick access links

| What to open | Link |
| --- | --- |
| Faculty demo | [Interactive conflict walkthrough](https://md-aslam-31.github.io/CSA1020_SOFTWARE_ENGINEERING/experiments/experiment-10-merge-conflicts/demo/) |
| Task-plan source | [Resolved plan](app/task-plan.md) |
| Conflict and resolution evidence | [Command/session log](evidence/session-log.md) · [Conflict markers](evidence/conflicted-task-plan.md.txt) · [Resolved file](evidence/resolved-task-plan.md) · [Merge graph](evidence/merge-history.txt) |

## Algorithm

1. Commit a baseline task plan on `main` in a disposable Git repository.
2. Create `feature/weekly-focus` and edit the focus statement.
3. Make a different edit to the same line on `main`.
4. Merge the feature branch to trigger the conflict and inspect Git's conflict markers.
5. Resolve the line by preserving both priorities, stage the resolution, complete the merge and inspect history.

## Result
The conflict was created in a disposable Git repository. The conflicting versions and resolution are preserved in evidence/ and shown in the public walkthrough. The merged focus keeps both intents: quiet study blocks and early deadline review. The PR portion of the lab still needs a GitHub feature-branch change and PR record.

## Output Evidence
[Command and commit log](evidence/session-log.md) · [Conflict markers](evidence/conflicted-task-plan.md.txt) · [Resolved plan](evidence/resolved-task-plan.md) · [Merge graph](evidence/merge-history.txt)

## Access
[Sample task plan](app/task-plan.md)

## Output Evidence

The evidence directory contains the conflicting file, resolved plan, commit/merge history and command transcript. The screenshots from the reference's separate planner are not reused; this experiment records the original local CampusNotes task-plan scenario.
