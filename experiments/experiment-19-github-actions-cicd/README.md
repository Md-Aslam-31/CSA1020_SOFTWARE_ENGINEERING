# Experiment 19 — GitHub Actions CI/CD

## Aim

Run the Experiment 16 Flask tests on pull requests, build the container on pull requests and pushes, and publish a SHA-tagged image to GHCR from pushes to `main`.

## Workflow

The active workflow is [`.github/workflows/experiment-19-cicd.yml`](../../.github/workflows/experiment-19-cicd.yml). It installs the pinned requirements, runs `unittest`, builds the image, and publishes with the repo-scoped `GITHUB_TOKEN` only on push. The final stage is a deployment gate pending a protected environment and target.

## Quick access links

| What to open | Link |
| --- | --- |
| Workflow definition and successful run | [Workflow source](../../.github/workflows/experiment-19-cicd.yml) · [Run #4 with container and persistence checks](https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING/actions/runs/40846745039) |
| Published image | `ghcr.io/md-aslam-31/csa1020_software_engineering/campus-todos:9501251` |
| Test application and Compose configuration | [Experiment 16 API](../experiment-16-flask-todo-docker/app.py) · [Compose file](../experiment-16-flask-todo-docker/compose.yaml) |
| Portfolio index | [All experiments](../../README.md) |

## Verification and evidence

The two unit tests pass locally under Python 3.14. [Run #4](https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING/actions/runs/40846745039) completed successfully: hosted Actions installed the requirements, ran the tests, built the container, and published `ghcr.io/md-aslam-31/csa1020_software_engineering/campus-todos:9501251`. Pull it with `docker pull ghcr.io/md-aslam-31/csa1020_software_engineering/campus-todos:9501251`; GHCR may require `docker login ghcr.io` if the package remains private.

The current workflow ends at an explicit deployment gate. No cloud platform credentials or deployment target were configured, so no cloud URL is claimed. Run #4 additionally verifies that a created task persists after the application container restarts with its named volume.
