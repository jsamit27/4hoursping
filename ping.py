import time
import requests

URL = "https://example.com/endpoint"   # replace with your endpoint

while True:
    try:
        data = {
            "param1": "value1",
            "param2": "value2"
        }
        response = requests.post(URL, json=data)
        print("Status:", response.status_code, "Response:", response.text[:100])
    except Exception as e:
        print("Request failed:", e)
    
    time.sleep(4 * 60 * 60)  # sleep 4 hours
