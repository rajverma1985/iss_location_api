import requests
import datetime

url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
response.raise_for_status()

iss_data = response.json()

day_dict = {
    'lat': 12.976750,
    'lng': 77.575279,
    'formatted': 0
}
day_info = requests.get("https://api.sunrise-sunset.org/json", params=day_dict)
sunrise = day_info.json()['results']['sunrise']
sunset = day_info.json()['results']['sunset']