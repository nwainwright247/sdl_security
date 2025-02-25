import requests

nessus_url = "nessus_domain"
access_key = "ACCESS_KEY"
secret_key = "SECRET_KEY"

headers = {
    "X-ApiKeys": f"accessKey={access_key}; secretKey={secret_key}",
    "Content-Type": "application/json"
}

response = requests.get(f"{nessus_url}/scans", headers=headers)
scans = response.json()["scans"]

for scan in scans:
    print(f"Scan Name: {scan['name']}, Status: {scan['status']}")


splunk_hec_url = "splunk_domain"
splunk_token = "SPLUNK_TOKEN"

data = {"event": scans}

headers = {
    "Authorization": f"Splunk {splunk_token}",
    "Content-Type": "application/json"
}

requests.post(f"{splunk_hec_url}/services/collector", headers=headers, json=data)
