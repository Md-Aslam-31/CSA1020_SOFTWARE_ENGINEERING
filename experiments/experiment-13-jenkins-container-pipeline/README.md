# Experiment 13 — Jenkins container CI/CD

## Aim

Define checkout, dependency install, unit test, Docker build, and gated deployment pipeline.

## Tools Required

| Tool | Purpose |
| --- | --- |
| Jenkins with Pipeline and Credentials plugins | Orchestrate the stages and keep registry credentials outside source control |
| Linux Jenkins agent labeled `python-docker` | Provide Python, pip, Git, and Docker CLI access to a Docker daemon |
| Python and Flask requirements | Install and run the Experiment 12 API tests |
| Git and this portfolio repository | Supply the Jenkinsfile, API source, and Docker build context |
| GitHub Container Registry (GHCR) | Receive the account-scoped image after the `main` branch pipeline passes |

No Jenkins password or registry token is stored in this repository. Configure a Jenkins username/password credential named `ghcr-md-aslam-31`; use a GitHub token with only the required package write permission as its password.

## Quick access links

| What to open | Link |
| --- | --- |
| Pipeline definition | [Jenkinsfile](Jenkinsfile) |
| API and passing tests used by this pipeline | [Experiment 12 API](../experiment-12-flask-api-kubernetes/app.py) · [API tests](../experiment-12-flask-api-kubernetes/test_app.py) |
| Pipeline run evidence | No Jenkins instance is available in this environment; see the [reproducible setup steps](#algorithm). |
| Portfolio index | [All experiments](../../README.md) |

## Algorithm

1. Provision a Jenkins controller and a Linux agent with the `python-docker` label. The agent needs Git, Python/pip, Docker CLI and an available Docker daemon.
2. Create a Pipeline job from this repository and configure SCM checkout of `main`.
3. The pipeline installs the Experiment 12 pinned requirements and runs its unit tests.
4. After tests pass, build a run-number-tagged `campus-tasks-api` image from Experiment 12's Docker context.
5. On `main`, authenticate with Jenkins credential `ghcr-md-aslam-31`, tag the image under `ghcr.io/md-aslam-31/csa1020_software_engineering`, publish it, and log out.
6. Review the pipeline log and GHCR package. Cloud deployment remains behind a gate until a target, protected credentials and a health-check/rollback plan are configured.

## Output Screenshots

Reproducible files and commands are included. External execution is only reported when verified.

## Result

The original pipeline is included and targets the user's GHCR namespace. Jenkins, Docker and a configured agent/credential are not available here, so no Jenkins build, registry publication from Jenkins, or cloud deployment is claimed. The GitHub Actions runs are documented separately under Experiments 14 and 19 and are not represented as Jenkins evidence.
