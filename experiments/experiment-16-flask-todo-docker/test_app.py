import tempfile,unittest
from pathlib import Path
import app
class Tests(unittest.TestCase):
 def setUp(self):self.tmp=tempfile.TemporaryDirectory();app.DB=Path(self.tmp.name)/"test.db";self.c=app.app.test_client()
 def tearDown(self):self.tmp.cleanup()
 def test_create_list(self):
  self.assertEqual(self.c.post("/api/todos",json={"title":"Submit lab"}).status_code,201)
  self.assertEqual(self.c.get("/api/todos").json[0]["title"],"Submit lab")
 def test_validation_missing(self):
  self.assertEqual(self.c.post("/api/todos",json={"title":" "}).status_code,400)
  self.assertEqual(self.c.patch("/api/todos/999").status_code,404)
if __name__=="__main__":unittest.main()
