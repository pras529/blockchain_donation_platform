import unittest
from app.verifications import verify_project_milestone

class VerificationTest(unittest.TestCase):
    def test_verify_milestone(self):
        result = verify_project_milestone(1, "valid_data")
        self.assertTrue(result)
