# Experiment 21 — Clone and edit a tracked file

## Aim

Clone a repository owned by the student, make one small, reviewable README edit in the local copy, and inspect the saved diff without changing the source repository.

## Tools Required

| Tool | Purpose |
| --- | --- |
| Git | Clone, inspect status and produce a patch |
| GitHub | Host the student's original repository |
| Text editor | Make and save the single-line change |
| Terminal | Verify the working tree and whitespace |

## Quick access links

| What to open | Link |
| --- | --- |
| Student-owned source repository | [CSA1020_SOFTWARE_ENGINEERING](https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING) |
| Original README snapshot | [Before edit](project/README.md) |
| Saved change and validation | [Patch](change.patch) · [Change note](change-note.md) · [Patch check](evidence/patch-validation.txt) |
| Portfolio index | [All experiments](../../README.md) |

## Algorithm

1. Clone the student's own repository into a disposable local folder.
2. Open the example project's README and clarify its description without changing unrelated files.
3. Save the file, inspect the diff, run `git diff --check`, and check `git status --short`.
4. Stop before staging or committing; those actions are demonstrated in Experiment 22.

The repository snapshot and patch are kept inside this report so this experiment can be reviewed without modifying the published portfolio history. Replace the placeholder clone URL below with the target URL if reproducing in a fresh folder:

```powershell
git clone https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING.git experiment-21-clone
cd experiment-21-clone
# Copy change.patch from this experiment into the clone root, then apply it.
git apply --unidiff-zero change.patch
git diff -- README.md
git diff --check
git status --short
```

## Output Evidence

| Check | Recorded result |
| --- | --- |
| Intended change | One sentence clarifies that the CampusConnect page is responsive and includes student groups |
| Files intended to change | `README.md` only |
| Staging/commit | Not performed in this exercise |
| Source repository | Unchanged; the submitted patch is a local snapshot |

## Result

The example README, proposed patch and change note are included. This portfolio stores the change as an uncommitted local example; it does not claim that a clone screenshot or remote edit was performed. Experiment 22 records the separate commit-and-push exercise.
