# Experiment 25 — Fork-based contribution and pull request

## Aim

Prepare a focused, tested change and document the fork → feature branch → upstream pull-request workflow under the student's own GitHub account.

## Tools Required

| Tool | Purpose |
| --- | --- |
| Git and GitHub | Fork, clone, fetch upstream, branch, commit, push and propose a PR |
| Node.js 24 | Run the dependency-free JavaScript test suite |
| GitHub Actions | Run checks on the proposed branch/PR when configured by the host repository |

## Quick access links

| What to open | Link |
| --- | --- |
| Original helper and tests | [summarize-tasks.js](project/src/summarize-tasks.js) · [Node tests](project/test/summarize-tasks.test.js) |
| Proposed patch and review checklist | [upstream-change.md](upstream-change.md) |
| Test output | [Recorded tests](evidence/test-results.txt) |
| Student's GitHub repositories | [Md-Aslam-31](https://github.com/Md-Aslam-31?tab=repositories) |
| Live fork and contribution branch | [Md-Aslam-31/Spoon-Knife](https://github.com/Md-Aslam-31/Spoon-Knife) · [exp25/contributing-guide](https://github.com/Md-Aslam-31/Spoon-Knife/tree/exp25/contributing-guide) |
| Upstream pull request | [PR #41998](https://github.com/octocat/Spoon-Knife/pull/41998) · [Contribution guide](https://github.com/Md-Aslam-31/Spoon-Knife/blob/exp25/contributing-guide/CONTRIBUTING.md) |
| Portfolio index | [All experiments](../../README.md) |

## Algorithm

1. Choose the public `octocat/Spoon-Knife` training project and confirm its purpose and contribution rules.
2. Create a fork under `Md-Aslam-31`, clone the fork, and add the original source as `upstream`.
3. Fetch both remotes and create a focused feature branch from the current upstream default branch.
4. Add the original `summarizeTasks` helper and tests in this portfolio; run the tests and inspect the diff and whitespace.
5. Add a focused `CONTRIBUTING.md` on `exp25/contributing-guide` in the student's fork, then push it.
6. Open the upstream pull request and include validation evidence. The PR is open; acceptance and merge are controlled by upstream maintainers.

For local verification, from `project/` run:

```powershell
node --test
```

## Output Evidence

The original helper and six passing tests are included in this experiment directory. The live fork is `Md-Aslam-31/Spoon-Knife`, branch `exp25/contributing-guide` adds a focused contribution guide, and [upstream PR #41998](https://github.com/octocat/Spoon-Knife/pull/41998) is open. `git diff --check` passed. The upstream repository has no configured CI for this documentation PR; maintainer review and merge remain external.

## Result

The feature implementation and six tests pass locally; the student-owned fork, branch, and upstream PR are live. The PR is awaiting upstream maintainer review, and no merge is claimed.
