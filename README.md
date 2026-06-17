# automation scripts : Backend Automation Architectures

A collection of Python scripts and API experiments for testing and automating strict n8n workflows.

## 📂 Scripts Included

### 1. `fallback-router.py`
A high-availability router script built in Python. 
**The Problem Solved:** If a primary client API goes offline (returning a `503 Service Unavailable` error), this script automatically catches the failure and safely routes the sensitive JSON payload to a backup emergency webhook in n8n. 

## 🚀 How to use this code

1. Install the requests library:
pip install requests

1- Update the backup_webhook variable in the Python script to match your local n8n test webhook.
2- Run the script in your Linux terminal:
python3 fallback-router.py
