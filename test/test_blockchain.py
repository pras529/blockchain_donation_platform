import unittest
from app.blockchain import create_donation_transaction

class BlockchainTest(unittest.TestCase):
    def test_create_transaction(self):
        user = {'address': '0x123', 'private_key': 'key123'}
        project = {'charity_address': '0x456'}
        tx_hash = create_donation_transaction(user, project, 0.1)
        self.assertIsNotNone(tx_hash)
