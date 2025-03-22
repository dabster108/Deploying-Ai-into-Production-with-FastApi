import requests
import json

url = "http://localhost:8080/analyze"
data = {"text": "This is great, I can totally relate."}

# Send POST request and pass the sample request data
response = requests.post(url, json=data)

# Check if the request was successful before printing
if response.status_code == 200:
    print(response.json())  # Print prediction response
else:
    print(f"Error {response.status_code}: {response.text}")  # Print error message
