# Experiment 10 — Local merge exercise evidence

The exercise used a disposable repository under the task workspace, not the portfolio repository.

## Commands

```text
git init -b main
git add task-plan.md
git commit -m "Add weekly task plan baseline"
git switch -c feature/quiet-study-blocks
git add task-plan.md
git commit -m "Prioritize quiet study blocks"
git switch main
git add task-plan.md
git commit -m "Emphasize early deadline review"
git merge feature/quiet-study-blocks
# Git reported a content conflict in task-plan.md (expected exit code 1).
# Kept both ideas in one focus line, then:
git add task-plan.md
git commit -m "Resolve weekly focus conflict"
git log --graph --oneline --all
```

## Commit evidence

- Baseline: `8dfaf05` — Add weekly task plan baseline
- Feature branch: `3710ae8` — Prioritize quiet study blocks
- Main branch: `50773dd` — Emphasize early deadline review
- Merge resolution: `120e7c8` — Resolve weekly focus conflict
- The feature and main edits diverged from the same baseline and Git stopped for a manual resolution.
