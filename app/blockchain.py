from web3 import Web3
from . import w3

# Interact with the Ethereum blockchain
def create_donation_transaction(user, project, amount):
    # Sample transaction for donation
    tx = {
        'to': project.charity_address,
        'value': w3.toWei(amount, 'ether'),
        'gas': 21000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'nonce': w3.eth.getTransactionCount(user.address),
    }
    signed_tx = w3.eth.account.signTransaction(tx, user.private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash.hex()

def get_transaction_receipt(tx_hash):
    return w3.eth.getTransactionReceipt(tx_hash)
