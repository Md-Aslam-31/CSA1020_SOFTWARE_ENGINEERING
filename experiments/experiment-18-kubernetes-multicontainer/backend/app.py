import os
import tempfile
import time

from flask import Flask, jsonify, request
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine, select
from sqlalchemy.exc import OperationalError


def create_app(database_url=None):
    app = Flask(__name__)
    default_db = os.path.join(tempfile.gettempdir(), "studyspark.sqlite").replace("\\", "/")
    url = database_url or os.environ.get("DATABASE_URL", f"sqlite:///{default_db}")
    engine = create_engine(url, pool_pre_ping=True)
    app.extensions["database_engine"] = engine
    metadata = MetaData()
    tasks = Table(
        "tasks", metadata,
        Column("id", Integer, primary_key=True),
        Column("title", String(200), nullable=False),
    )
    for attempt in range(30):
        try:
            metadata.create_all(engine)
            break
        except OperationalError:
            if attempt == 29:
                raise
            time.sleep(1)

    @app.get("/health")
    def health():
        try:
            with engine.connect() as connection:
                connection.execute(select(1))
            return jsonify(status="ok", service="studyspark-api", database="connected")
        except Exception:
            app.logger.exception("Database health check failed")
            return jsonify(status="unavailable", service="studyspark-api"), 503

    @app.get("/api/tasks")
    def list_tasks():
        with engine.connect() as connection:
            rows = connection.execute(select(tasks).order_by(tasks.c.id)).mappings().all()
        return jsonify([dict(row) for row in rows])

    @app.post("/api/tasks")
    def create_task():
        title = str((request.get_json(silent=True) or {}).get("title", "")).strip()
        if not title or len(title) > 200:
            return jsonify(error="title must contain 1 to 200 characters"), 400
        with engine.begin() as connection:
            result = connection.execute(tasks.insert().values(title=title))
            task_id = result.inserted_primary_key[0]
        return jsonify(id=task_id, title=title), 201

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
