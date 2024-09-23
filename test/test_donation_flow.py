import unittest
from app.donation_flow import track_donations

class DonationFlowTest(unittest.TestCase):
    def test_track_donations(self):
        total = track_donations(1)
        self.assertEqual(total, 100)  # Assume the total donated is 100 for this project.
