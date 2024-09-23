import unittest
from app.notifications import notify_donors
from app.models import Notification

class NotificationsTest(unittest.TestCase):
    def test_notify_donors(self):
        notify_donors(1, "Milestone achieved!")
        notification = Notification.query.filter_by(user_id=1).first()
        self.assertIsNotNone(notification)
        self.assertEqual(notification.message, "Milestone achieved!")
