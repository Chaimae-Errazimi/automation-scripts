
# ============================
# my business account: high-availability failover router
# target client: entreprise logistics / healthcare 
# description: attempts to hit the primary API. if the primary 
# API is offline (503 error), it safely routes to a backup emergency webhook.
# ============================

import requests 

# 1. endpoints 
primary_API = "https://httpbin.org/status/503"
backup_webhook = "http://localhost:5678/webhook-test/emergency-alert"

important_data = {"patient_id": "8899", "status": "discharged"} 

print("attempting to reach primery server...")

# 2. the request 
response = requests.post(primary_API, json=important_data)

# 3. the fallback logic
if response.status_code == 200:
    print("primary server caught the data")

elif response.status_code == 503:
    print("warning: primary server is down (503). initiating fallback...")

    # fire data to the backup n8n webhook instead! 
    backup_response = requests.post(backup_webhook, json=important_data)

    if backup_response.status_code == 200:
        print("fallback success: data safely stored in emergency n8n queue")

else:
    print(f"unknown error: status {response.status_code}")





