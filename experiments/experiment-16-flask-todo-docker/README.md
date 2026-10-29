# Experiment 16 — Flask To-Do API in Docker

## Aim

Build a small persistent To-Do API, cover its behavior with unit tests, and package it with Docker Compose and a named data volume.

## Endpoints

- `GET /health`: readiness response.
- `GET /api/todos`: ordered To-Do records.
- `POST /api/todos` with `{ "title": "..." }`: create; blank titles return 400.
- `PATCH /api/todos/<id>`: mark complete; missing IDs return 404.

## Run

From this directory run `python -m pip install -r requirements.txt`, `python -m unittest -v`, then `docker compose up --build -d`. Check [http://localhost:5000/health](http://localhost:5000/health) and the API endpoints; stop with `docker compose down` (the named volume remains).

## Evidence and result

Both unit tests pass under Python 3.14 with Flask 3.1.3, covering persistence within a test database, validation, and missing IDs. The SQLite context manager closes and rolls back connections correctly. Docker is unavailable here, so Compose startup and browser evidence are pending; no container run is claimed.
