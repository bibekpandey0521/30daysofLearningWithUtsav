# https://home.openweathermap.org/data/2.5/weather?q=London&appid=API_KEY
# https://api.openweathermap.org/data/2.5/weather?q=Nepal&appid=4d7ce513e5f9caaffe4e759e5bc7371e

#pip install requests
import requests
API_KEY = "4d7ce513e5f9caaffe4e759e5bc7371e"
city = "London"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    print(weather_data)
else:
    print("An error occured.Status Code: ",response.status_code)    

