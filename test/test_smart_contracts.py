import unittest
from app.smart_contracts import deploy_contract

class SmartContractTest(unittest.TestCase):
    def test_deploy_contract(self):
        charity_address = '0x456'
        contract_address = deploy_contract(charity_address)
        self.assertIsNotNone(contract_address)
