# Experiment 10 — Branch merge conflict

Two contributors edit the same README sentence: main says “Install with pip or uv”; feature says “Install with uv.” Git cannot choose intent automatically.

In a disposable shared repository, create feature/setup-docs, edit and push. In a second clone, make the competing main edit, commit and push. On the feature branch run git fetch origin and git merge origin/main.

Conflict:
<<<<<<< HEAD
Install dependencies with uv.
=======
Install dependencies with pip or uv.
>>>>>>> origin/main

If both tools are supported, resolve to “Install dependencies with pip or uv.” Remove markers, review the paragraph, run git diff --check, git add README.md, git commit -m "docs: resolve setup conflict", then push the feature branch and update the PR with the reason. Otherwise follow project documentation. This is a lab procedure, not a remote conflict created in a shared repo.
