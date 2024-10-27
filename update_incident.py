import requests
import json

# ServiceNow credentials and instance URL
instance_url = 'https://your_instance.service-now.com/api/now/table/incident/{sys_id}'
user = 'your_username'
password = 'your_password'

# Incident sys_id and updated data
sys_id = 'your_incident_sys_id'
update_data = {
    "state": "Resolved",
    "comments": "Incident resolved via Python script."
}

# Set the headers for the request
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Update incident
url = instance_url.format(sys_id=sys_id)
response = requests.patch(url, auth=(user, password), headers=headers, data=json.dumps(update_data))

if response.status_code == 200:
    print("Incident updated successfully.")
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")
