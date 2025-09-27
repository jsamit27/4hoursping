import requests

URL = "https://cron-jobs-for-everyone.fly.dev/populate-redis"
data = {
    "calendar_id": "efficient.ai.agency@gmail.com",
    "redis_url": "redis://default:675d88cdab9e49858ccd124a7e643914@fly-efficient-ai-1.upstash.io:6379"
}
headers = {
    "Content-Type": "application/json",
    "x-api-key": "https://cron-jobs-for-everyone.fly.dev/popuate-redis"  # must match what the endpoint is checking!
}
response = requests.post(URL, json=data, headers=headers)
print("Status:", response.status_code)
print("Response:", response.text)
