import unittest
from login import login
class LoginTests(unittest.TestCase):
 def test_valid(self):self.assertTrue(login("student","demo-pass",{"student":"demo-pass"}))
 def test_invalid_password(self):self.assertFalse(login("student","wrong",{"student":"demo-pass"}))
 def test_unknown_user(self):self.assertFalse(login("other","demo-pass",{"student":"demo-pass"}))
if __name__=="__main__":unittest.main()
