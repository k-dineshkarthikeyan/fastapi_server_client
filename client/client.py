import requests

url = "http://fastapi:8000/ping"
params = {"message": "This is a new test message"}
try:
    response = requests.post(url, json=params)
    response.raise_for_status()
    if response.status_code == 200:
        print("Client has sent a successfull ping")
    print(response.json())
except Exception as e:
    print(f"following error happened on client: {e}")
