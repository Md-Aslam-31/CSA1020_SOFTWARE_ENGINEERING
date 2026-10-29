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
| Portfolio index | [All experiments](../../README.md) |

## Algorithm

1. Choose a public upstream project and confirm its contribution rules and license.
2. Create a fork under `Md-Aslam-31`, clone the fork, and add the original source as `upstream`.
3. Fetch both remotes and create a focused feature branch from the current upstream default branch.
4. Add `summarizeTasks`, run the tests, and inspect the diff and whitespace.
5. Commit only the helper, tests and package script; push the branch to the student's fork.
6. Open a pull request from the fork branch to the chosen upstream, include test output, and follow maintainer feedback.

For local verification, from `project/` run:

```powershell
node --test
```

## Output Evidence

The original feature patch, tests and local test log are included. The required account-side fork and pull request are not created: no GitHub connector/API is installed in this workspace, and the browser interface here is unavailable for authenticated GitHub writes. No fork, branch URL, CI run or PR is fabricated.

## Result

The feature implementation and six tests are complete locally. The remote fork/PR portion remains pending. After connecting GitHub or using the student's signed-in GitHub UI, follow the checklist in [upstream-change.md](upstream-change.md) and add the resulting fork, branch and PR links here.
