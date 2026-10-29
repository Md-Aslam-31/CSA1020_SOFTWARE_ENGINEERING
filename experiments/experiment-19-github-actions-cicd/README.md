# Experiment 19 — GitHub Actions CI/CD

## Aim

Run the Experiment 16 Flask tests on pull requests, build the container on pull requests and pushes, and publish a SHA-tagged image to GHCR from pushes to `main`.

## Workflow

The active workflow is [`.github/workflows/experiment-19-cicd.yml`](../../.github/workflows/experiment-19-cicd.yml). It installs the pinned requirements, runs `unittest`, builds the image, and publishes with the repo-scoped `GITHUB_TOKEN` only on push. The final stage is a deployment gate pending a protected environment and target.

## Verification and evidence

The two unit tests pass locally under Python 3.14. The workflow will execute after the pushed commit and can be checked in the repository Actions tab; no hosted run or deployment URL is claimed before that run is observed.
