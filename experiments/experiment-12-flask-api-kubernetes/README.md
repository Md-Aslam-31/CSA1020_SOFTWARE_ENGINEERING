# Experiment 12 — Flask API in Kubernetes

## Aim

Implement and test a Flask JSON API, containerize it, and define a Kubernetes Deployment with a NodePort Service.

## API

- `GET /health` returns service health.
- `GET /api/tasks` returns the in-memory sample tasks.
- `POST /api/tasks` accepts JSON `{ "title": "..." }`; blank titles return HTTP 400.

## Run and deploy

Install `requirements.txt`, run `python -m unittest -v`, then `python app.py`. Build the image with `docker build -t campus-tasks-api:1.0 .`. Update the image reference in `k8s/api.yaml`, apply it, and verify with `kubectl get pods,service`; the manifest exposes NodePort 30500.

## Evidence and result

The four API tests pass under Python 3.14 with Flask 3.1.3. Docker and kubectl are unavailable here, so image build and cluster/browser evidence remain pending and are not claimed. The API intentionally uses in-memory data for this single-service lab; Experiment 18 adds PostgreSQL persistence.
