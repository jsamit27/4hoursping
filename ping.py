import requests

URL = "https://example.com/endpoint"   # replace with your endpoint

def main():
    data = {
        "param1": "value1",
        "param2": "value2"
    }
    try:
        response = requests.post(URL, json=data)
        print("Status:", response.status_code, "Response:", response.text[:100])
    except Exception as e:
        print("Request failed:", e)

if __name__ == "__main__":
    main()
