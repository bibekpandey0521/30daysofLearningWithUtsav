import requests

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.118 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.text[:500])
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

