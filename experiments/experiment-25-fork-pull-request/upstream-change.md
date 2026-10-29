# Proposed upstream change

## Summary

Add a small JavaScript helper that summarizes CampusConnect tasks by workflow state and calculates completed/remaining counts and percentage. Keep the input immutable and reject malformed or duplicate task IDs.

## Files in the proposed patch

- `project/src/summarize-tasks.js` — implementation.
- `project/test/summarize-tasks.test.js` — six Node.js built-in tests.
- `project/package.json` — zero-dependency test command.

## Review checklist

- [x] Empty input returns zero counts and zero percent.
- [x] Valid state counts and rounded completion are derived from the input.
- [x] Input arrays and task objects are not mutated.
- [x] Unknown states, malformed tasks and duplicate IDs are rejected.
- [ ] Apply this patch on a feature branch in a fork owned by `Md-Aslam-31`.
- [ ] Open a pull request against the selected upstream repository and record its URL.

The helper and tests are original coursework content. This report does not claim a remote fork or upstream PR until one is actually created.
