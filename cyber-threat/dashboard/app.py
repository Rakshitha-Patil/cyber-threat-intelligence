import streamlit as st
import json
from web3 import Web3
from datetime import datetime

st.title("🔐 Cyber Threat Intelligence Dashboard")

w3 = Web3(Web3.HTTPProvider("http://ganache:8545"))

# Load contract
with open("contract.json") as f:
    contract_data = json.load(f)

contract = w3.eth.contract(
    address=Web3.to_checksum_address(contract_data["address"]),
    abi=contract_data["abi"]
)

# ✅ DEFINE threats FIRST
threats = contract.functions.getThreats().call()

# ✅ THEN use it
st.metric("Total Alerts", len(threats))

st.subheader("🚨 Live Threat Feed")

for t in reversed(threats):
    org, msg, ts = t

    time_str = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

    if "DDoS" in msg or "Ransomware" in msg:
        st.error(f"{msg}\n🕒 {time_str}")
    elif "Phishing" in msg or "Malware" in msg:
        st.warning(f"{msg}\n🕒 {time_str}")
    else:
        st.info(f"{msg}\n🕒 {time_str}")

    st.markdown("---")