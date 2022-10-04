from datetime import datetime
import requests


# my location
day_dict = {
    'lat': 12.976750,
    'lng': 77.575279,
    'formatted': 0
}
day_info = requests.get("https://api.sunrise-sunset.org/json", params=day_dict)
sunrise = day_info.json()['results']['sunrise'].split('T')[1].split(':')[0]
sunset = day_info.json()['results']['sunset'].split('T')[1].split(':')[0]


print(sunrise)
print(sunset)
