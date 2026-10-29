# Experiment 24 — Feature branch: password-hash login helper

## Aim

Implement and test a small login-verification helper on a focused feature branch, then review and submit its change as a pull request to the student's repository.

## Tools Required

| Tool | Purpose |
| --- | --- |
| Python 3.14 and `unittest` | Implement and test password-hash verification |
| Git | Create a feature branch, commit and push the change |
| GitHub account `Md-Aslam-31` | Host the branch and pull request |
| PBKDF2-HMAC-SHA256 and `hmac.compare_digest` | Derive and compare a salted password hash safely for this teaching example |

## Quick access links

| What to open | Link |
| --- | --- |
| Login helper and its tests | [login.py](login.py) · [test_login.py](test_login.py) |
| Recorded local test output | [Test results](evidence/test-results.txt) |
| Student-owned repository | [CSA1020_SOFTWARE_ENGINEERING](https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING) |
| Pull-request page | [Open pull requests](https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING/pulls) |
| Portfolio index | [All experiments](../../README.md) |

## Algorithm

1. Create an isolated `feature-login` branch from the current main branch.
2. Store salt, iteration count and PBKDF2 password hash in each user record; never store a plaintext password.
3. Reject unknown users, empty values, malformed records, invalid salt/hash encodings, and unreasonable iteration counts.
4. Compare derived and stored hash bytes with a constant-time comparison.
5. Run the unit tests, commit only the helper and tests, push the branch, and open a PR after reviewing its diff and checks.

This helper is an educational component only. It does not provide account storage, rate limiting, session handling, MFA, password resets, or a complete production authentication system.

## Output Evidence

The local test output and source are included above. Git pushes work through the existing Git credential helper, but the GitHub PR API connector is not installed in this workspace; no PR number, review, or merge is claimed.

## Result

The original login helper and tests are complete; the tests cover valid and invalid credentials, input types, malformed hashes and salts, and iteration bounds. The feature-branch/PR submission portion is still pending. A live pull-request workflow requires the GitHub connector to be installed or the student to create the PR from a signed-in GitHub session.
