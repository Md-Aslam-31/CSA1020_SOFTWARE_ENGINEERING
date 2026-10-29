import tempfile
import unittest
from pathlib import Path

from app import create_app


class StudySparkApiTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.database = Path(self.tempdir.name) / "test.sqlite"
        self.app = create_app(f"sqlite:///{self.database.as_posix()}")
        self.client = self.app.test_client()

    def tearDown(self):
        self.app.extensions["database_engine"].dispose()
        self.tempdir.cleanup()

    def test_database_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["database"], "connected")

    def test_create_and_list_task(self):
        response = self.client.post("/api/tasks", json={"title": "Review lecture notes"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["title"], "Review lecture notes")
        self.assertEqual(self.client.get("/api/tasks").json, [response.json])

    def test_rejects_blank_and_long_title(self):
        self.assertEqual(self.client.post("/api/tasks", json={"title": " "}).status_code, 400)
        self.assertEqual(self.client.post("/api/tasks", json={"title": "x" * 201}).status_code, 400)


if __name__ == "__main__":
    unittest.main()
