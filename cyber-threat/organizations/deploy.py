from web3 import Web3
from solcx import compile_source, install_solc
import json

# Install Solidity compiler
install_solc('0.8.0')

# Connect to Docker Ganache
w3 = Web3(Web3.HTTPProvider("http://host.docker.internal:8545"))
account = w3.eth.accounts[0]

# Read contract
with open("ThreatLog.sol", "r") as file:
    contract_source = file.read()

# Compile contract
compiled = compile_source(contract_source, solc_version="0.8.0")
contract_id, contract_interface = compiled.popitem()

bytecode = contract_interface['bin']
abi = contract_interface['abi']

# Deploy contract
Contract = w3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = Contract.constructor().transact({'from': account})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("✅ Contract deployed at:", tx_receipt.contractAddress)

# Save contract.json
contract_data = {
    "address": tx_receipt.contractAddress,
    "abi": abi
}

with open("contract.json", "w") as f:
    json.dump(contract_data, f)

print("✅ contract.json updated")