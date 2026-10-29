# Experiment 23 — Pull a collaborator's update

## Aim

Demonstrate how one local clone receives a commit pushed to a shared remote from another workspace, then verify the fast-forward and clean working tree.

## Tools Required

| Tool | Purpose |
| --- | --- |
| Git | Create a bare shared remote, clone, commit, push and pull |
| PowerShell | Run the repeatable local demonstration |
| Two local clones | Represent contributor and reader workspaces |

## Quick access links

| What to open | Link |
| --- | --- |
| Repeatable simulation | [simulate-collaborator-update.ps1](simulate-collaborator-update.ps1) |
| Recorded pull output | [Verification log](evidence/pull-verification.txt) |
| Update introduced in this experiment | [collaborator-update.md](collaborator-update.md) |
| Portfolio index | [All experiments](../../README.md) |

## Algorithm

1. Initialize a bare local repository to act as the shared remote and push a baseline README from the contributor clone.
2. Clone that remote into an independent reader workspace.
3. Add the collaboration note in the contributor clone, commit, and push it.
4. Run `git pull --ff-only` in the reader clone.
5. Confirm the update text, resulting commit ID, and clean reader worktree.

This isolated two-clone simulation does not claim a second human collaborator or a GitHub-side commit. The Git history and commands are real local operations; the account-side activity is intentionally not fabricated.

## Output Evidence

See [the captured run](evidence/pull-verification.txt) for the local push, fast-forward pull, final commit and clean status.

## Result

The experiment demonstrates synchronization between independent clones through a shared bare remote. It preserves a clear distinction between a locally simulated second workspace and an actual collaborator account.
