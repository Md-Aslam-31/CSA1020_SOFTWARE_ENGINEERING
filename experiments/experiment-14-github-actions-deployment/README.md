# Experiment 14 — GitHub Actions container publication

## Aim

Build the CampusConnect website image on pull requests and publish a commit-tagged image to GitHub Container Registry on pushes to `main`.

## Workflow

The active workflow is [`.github/workflows/experiment-14-container-deploy.yml`](../../.github/workflows/experiment-14-container-deploy.yml). It uses Docker on a PR to validate the build, then uses the repository-scoped `GITHUB_TOKEN` and `packages: write` permission to publish on a matching push. It prints an explicit rollout gate; it does not claim a cloud deployment.

## Verification and evidence

The workflow is in the root `.github/workflows` directory. [Run #1 on commit `9501251`](https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING/actions/runs/40841798194) completed successfully: GitHub Actions built and published `ghcr.io/md-aslam-31/csa1020_software_engineering/campusconnect:9501251`. Pull it with `docker pull ghcr.io/md-aslam-31/csa1020_software_engineering/campusconnect:9501251`; GHCR may require `docker login ghcr.io` if the package remains private.

The workflow currently stops at a deployment gate. No cloud target or deployment credentials were configured, so there is no public hosted app URL and no cloud deployment is claimed.
