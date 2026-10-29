import unittest
from app import app,TASKS
class ApiTests(unittest.TestCase):
 def setUp(self): self.c=app.test_client();TASKS[:]=[{"id":1,"title":"Read","done":False}]
 def test_health(self): self.assertEqual(self.c.get("/health").json["status"],"ok")
 def test_list(self): self.assertEqual(len(self.c.get("/api/tasks").json),1)
 def test_create(self): self.assertEqual(self.c.post("/api/tasks",json={"title":"Write"}).status_code,201)
 def test_empty_title(self): self.assertEqual(self.c.post("/api/tasks",json={"title":" "}).status_code,400)
if __name__=="__main__":unittest.main()
