import unittest

# Validation functions copied/imported from contacts_manager.py

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def validate_email(email):
    return email == "" or ("@" in email and "." in email)


class TestContactsManager(unittest.TestCase):

    # Phone Validation Tests
    def test_valid_phone(self):
        self.assertTrue(validate_phone("9876543210"))

    def test_phone_too_short(self):
        self.assertFalse(validate_phone("12345"))

    def test_phone_contains_letters(self):
        self.assertFalse(validate_phone("98765abcde"))

    def test_phone_too_long(self):
        self.assertFalse(validate_phone("12345678901"))

    # Email Validation Tests
    def test_valid_email(self):
        self.assertTrue(validate_email("test@example.com"))

    def test_empty_email(self):
        self.assertTrue(validate_email(""))

    def test_invalid_email_no_at(self):
        self.assertFalse(validate_email("testexample.com"))

    def test_invalid_email_no_dot(self):
        self.assertFalse(validate_email("test@examplecom"))


if __name__ == "__main__":
    unittest.main()