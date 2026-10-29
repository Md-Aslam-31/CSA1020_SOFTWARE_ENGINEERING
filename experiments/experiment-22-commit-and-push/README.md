# Experiment 22 — Commit and push an original repository change

## Aim

Stage a focused experiment update, record it in Git, push it to the student's GitHub repository, and verify the published commit.

## Tools Required

| Tool | Purpose |
| --- | --- |
| Git | Stage, commit, push and verify history |
| GitHub account `Md-Aslam-31` | Own the portfolio remote |
| Terminal and text editor | Review and record the change |

## Quick access links

| What to open | Link |
| --- | --- |
| Student-owned repository | [CSA1020_SOFTWARE_ENGINEERING](https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING) |
| Main-branch history | [GitHub commits](https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING/commits/main) |
| Recorded pushed commit | [Document successful hosted experiment workflows](https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING/commit/66964f9) |
| Portfolio index | [All experiments](../../README.md) |

## Algorithm

1. Inspect the change and confirm only the intended report files are staged.
2. Run `git diff --check` and review `git diff --cached`.
3. Commit with a descriptive message.
4. Push `main` to `origin` using the configured Git credential helper; no token is copied into the report.
5. Compare local HEAD with `git ls-remote origin refs/heads/main`, then check `git status --short`.

## Output Evidence

[Evidence record](evidence/git-push-record.md) captures the actual authoring commit and push for this portfolio.

## Result

The report update committed as `66964f9` (`Document successful hosted experiment workflows`) and was pushed to `origin/main`; Git returned `9bf86fc..66964f9 main -> main`. Later updates to this experiment will advance repository HEAD, while this report preserves the historical commit used as the example. No access token or password is included.
