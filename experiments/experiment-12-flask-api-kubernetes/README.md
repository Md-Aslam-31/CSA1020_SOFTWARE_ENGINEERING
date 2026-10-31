# Experiment 12 — Flask API in Kubernetes

## Aim

Implement and test a Flask JSON API, containerize it, and define a Kubernetes Deployment with a NodePort Service.

## Tools Required

- Python 3.14 and Flask from `requirements.txt` for local API execution.
- `unittest` for endpoint and validation checks.
- Docker Desktop for the image build and container run.
- Kubernetes and `kubectl` for applying and inspecting the manifest.
- A browser or HTTP client for endpoint checks.

## Quick access links

| What to open | Link |
| --- | --- |
| API implementation and tests | [app.py](app.py) · [test_app.py](test_app.py) |
| Kubernetes Deployment and Service | [api.yaml](k8s/api.yaml) |
| Recorded API test output | [4 passing tests](evidence/api-tests.txt) |
| Hosted image, kind deployment and evidence artifact | [Successful Actions run #1](https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING/actions/runs/41172431105) · open its `experiment-12-kind-evidence` artifact |
| Portfolio index | [All experiments](../../README.md) |

## API

- `GET /health` returns service health.
- `GET /api/tasks` returns the in-memory sample tasks.
- `POST /api/tasks` accepts JSON `{ "title": "..." }`; blank titles return HTTP 400.

## Run and deploy

Install `requirements.txt`, run `python -m unittest -v`, then `python app.py`. Build the image with `docker build -t campus-tasks-api:1.0 .`. Update the image reference in `k8s/api.yaml`, apply it, and verify with `kubectl get pods,service`; the manifest exposes NodePort 30500.

## Algorithm

1. Implement health and task-list endpoints with JSON responses.
2. Validate task creation input and reject blank titles with HTTP 400.
3. Exercise both success and invalid-input cases using the unit tests.
4. Package the API and dependencies in the Docker image.
5. Apply a Deployment and NodePort Service, then inspect pods and reachability when a cluster is available.

## Evidence and result

The four API tests pass under Python 3.14 with Flask 3.1.3; the captured output is in [evidence/api-tests.txt](evidence/api-tests.txt). The hosted GitHub Actions job built the image, deployed it to kind, exercised the NodePort service through port-forward, and uploaded cluster/API evidence in [run #1](https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING/actions/runs/41172431105). Docker and kubectl remain unavailable locally; the successful hosted run is the container/cluster evidence. The API intentionally uses in-memory data for this single-service lab; Experiment 18 adds PostgreSQL persistence.
