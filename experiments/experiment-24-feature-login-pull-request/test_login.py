import unittest

from login import make_user_record, login


class LoginTests(unittest.TestCase):
    def setUp(self):
        self.record = make_user_record("sample-pass", salt=bytes.fromhex("00112233445566778899aabbccddeeff"))
        self.accounts = {"student": self.record}

    def test_valid_credentials(self):
        self.assertTrue(login("student", "sample-pass", self.accounts))

    def test_wrong_password(self):
        self.assertFalse(login("student", "incorrect", self.accounts))

    def test_unknown_user(self):
        self.assertFalse(login("unknown", "sample-pass", self.accounts))

    def test_empty_username_or_password(self):
        self.assertFalse(login("", "sample-pass", self.accounts))
        self.assertFalse(login("student", "", self.accounts))

    def test_non_string_inputs(self):
        self.assertFalse(login(None, "sample-pass", self.accounts))
        self.assertFalse(login("student", None, self.accounts))

    def test_non_mapping_accounts(self):
        self.assertFalse(login("student", "sample-pass", None))

    def test_malformed_user_record(self):
        self.assertFalse(login("student", "sample-pass", {"student": "plaintext"}))

    def test_bad_salt_encoding(self):
        self.assertFalse(login("student", "sample-pass", {"student": {**self.record, "salt": "not-hex"}}))

    def test_short_salt_or_wrong_hash_length(self):
        self.assertFalse(login("student", "sample-pass", {"student": {**self.record, "salt": "00"}}))
        self.assertFalse(login("student", "sample-pass", {"student": {**self.record, "password_hash": "00"}}))

    def test_invalid_iteration_count(self):
        self.assertFalse(login("student", "sample-pass", {"student": {**self.record, "iterations": True}}))
        self.assertFalse(login("student", "sample-pass", {"student": {**self.record, "iterations": 1}}))

    def test_record_builder_rejects_weak_parameters(self):
        with self.assertRaises(ValueError):
            make_user_record("sample-pass", salt=b"short")
        with self.assertRaises(ValueError):
            make_user_record("sample-pass", salt=bytes.fromhex("00112233445566778899aabbccddeeff"), iterations=999)

    def test_record_builder_generates_unique_random_salts(self):
        first = make_user_record("sample-pass")
        second = make_user_record("sample-pass")
        self.assertEqual(len(bytes.fromhex(first["salt"])), 16)
        self.assertNotEqual(first["salt"], second["salt"])
        self.assertTrue(login("student", "sample-pass", {"student": first}))


if __name__ == "__main__":
    unittest.main()
