import requests

URL = "https://cron-jobs-for-everyone.fly.dev/populate-redis"   # Your deployed FastAPI endpoint

def main():
    data = {
        "calendar_id": "efficient.ai.agency@gmail.com",
        "redis_url": "redis://default:675d88cdab9e49858ccd124a7e643914@fly-efficient-ai-1.upstash.io:6379"
    }
    try:
        response = requests.post(URL, json=data, headers={"Content-Type": "application/json"})
        print("Status:", response.status_code, "Response:", response.text[:200])
    except Exception as e:
        print("Request failed:", e)

if __name__ == "__main__":
    main()
