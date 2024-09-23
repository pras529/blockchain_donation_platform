from . import w3

contract_source_code = '''
pragma solidity ^0.8.0;

contract DonationContract {
    address public charity;
    bool public milestoneMet = false;

    constructor(address _charity) {
        charity = _charity;
    }

    function releaseFunds() public {
        require(milestoneMet == true, "Milestone not met");
        payable(charity).transfer(address(this).balance);
    }

    function verifyMilestone(bool _milestoneMet) public {
        milestoneMet = _milestoneMet;
    }

    receive() external payable {}
}
'''

compiled_contract = w3.eth.compile_source(contract_source_code)
contract_interface = compiled_contract['<stdin>:DonationContract']

def deploy_contract(charity_address):
    DonationContract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
    tx_hash = DonationContract.constructor(charity_address).transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return tx_receipt.contractAddress

def release_funds(contract_address):
    contract = w3.eth.contract(address=contract_address, abi=contract_interface['abi'])
    tx_hash = contract.functions.releaseFunds().transact()
    return tx_hash.hex()
