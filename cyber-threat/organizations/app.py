import os
import time
import random
import json
import numpy as np
from web3 import Web3
from model import train_model

ORG_NAME = os.getenv("ORG_NAME", "Unknown")

# Train model once
model = train_model()

# Blockchain connection
w3 = Web3(Web3.HTTPProvider("http://host.docker.internal:8545"))
with open("contract.json") as f:
    contract_data = json.load(f)

contract = w3.eth.contract(
    address=contract_data["address"],
    abi=contract_data["abi"]
)

account = w3.eth.accounts[0]

# Simulate network data


def generate_alert(org_name):
    alerts = [
        "High-risk DDoS pattern detected.",
        "Possible Sybil Attack - Multiple new nodes from same IP.",
        "Phishing attempt blocked on local gateway.",
        "Ransomware activity detected - Files encrypted.",
        "Malware signature identified in incoming traffic.",
        "Brute force login attempts detected.",
        "Insider data access anomaly detected."
    ]

    alert_msg = random.choice(alerts)
    return f"[{org_name}] Alert: {alert_msg}"

def generate_data():
    return [[
        random.randint(0, 8000),  # src_bytes
        random.randint(0, 8000),  # dst_bytes
        random.randint(1, 50),    # count
        random.randint(1, 10)     # srv_count
    ]]
while True:
    data = generate_data()

    prediction = model.predict(data)[0]
    if prediction == 1:
        msg = generate_alert(ORG_NAME)

        print(msg)

        contract.functions.addThreat(
        ORG_NAME,
        msg
        ).transact({'from': account})

    else:
        print(f"[{ORG_NAME}] NORMAL → {data.tolist()}")

    time.sleep(5)