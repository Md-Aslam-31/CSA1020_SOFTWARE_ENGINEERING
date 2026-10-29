# Experiment 14 — GitHub Actions container publication

## Aim

Build the CampusConnect website image on pull requests and publish a commit-tagged image to GitHub Container Registry on pushes to `main`.

## Workflow

The active workflow is [`.github/workflows/experiment-14-container-deploy.yml`](../../.github/workflows/experiment-14-container-deploy.yml). It uses Docker on a PR to validate the build, then uses the repository-scoped `GITHUB_TOKEN` and `packages: write` permission to publish on a matching push. It prints an explicit rollout gate; it does not claim a cloud deployment.

## Verification

The workflow is in the root `.github/workflows` directory where GitHub Actions discovers it. A successful run requires pushing these changes to `main` and checking the repository Actions tab and GHCR package page. The local authoring environment has no Docker or GitHub CLI, so no run log or image URL is claimed in this report.
