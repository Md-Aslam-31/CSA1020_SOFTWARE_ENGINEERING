# Experiment 16 — Flask To-Do API in Docker

## Aim

Build a small persistent To-Do API, cover its behavior with unit tests, and package it with Docker Compose and a named data volume.

## Tools Required

- Python 3.14, Flask and `unittest` for development and verification.
- Docker Desktop and Docker Compose for the app/database container stack.
- A browser or HTTP client to check readiness and CRUD responses.

## Quick access links

| What to open | Link |
| --- | --- |
| Flask API | [app.py](app.py) |
| Automated tests | [test_app.py](test_app.py) · [Recorded test output](evidence/test-results.txt) |
| Container configuration | [Dockerfile](Dockerfile) · [Compose file](compose.yaml) |
| Portfolio index | [All experiments](../../README.md) |

## Endpoints

- `GET /health`: readiness response.
- `GET /api/todos`: ordered To-Do records.
- `POST /api/todos` with `{ "title": "..." }`: create; blank titles return 400.
- `PATCH /api/todos/<id>`: mark complete; missing IDs return 404.

## Run

From this directory run `python -m pip install -r requirements.txt`, `python -m unittest -v`, then `docker compose up --build -d`. Check [http://localhost:5000/health](http://localhost:5000/health) and the API endpoints; stop with `docker compose down` (the named volume remains).

## Algorithm

1. Create the API endpoints for readiness, list, create and completion updates.
2. Store data in SQLite and allow the database path to be overridden for isolated tests and container persistence.
3. Validate titles and IDs and return clear HTTP status codes for invalid or missing records.
4. Test create/list, persistence and error handling with a temporary test database.
5. Start the Compose stack, call `/health`, create a record, and confirm it remains after a service restart while the named volume is retained.

## Evidence and result

Both unit tests pass under Python 3.14 with Flask 3.1.3, covering persistence within a test database, validation, and missing IDs. The captured output is at [evidence/test-results.txt](evidence/test-results.txt). The SQLite context manager closes and rolls back connections correctly. Docker is unavailable here, so Compose startup and browser evidence are pending; no container run is claimed.
