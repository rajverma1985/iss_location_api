import time
import requests
from datetime import datetime
from email_module.mail import send_email

# my location
my_location = {
    'lat': 12.976750,
    'lng': 77.575279,
    'formatted': 0
}


def iss_is_visible():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()
    iss_lat = float(iss_data['iss_position']['latitude'])
    iss_lon = float(iss_data['iss_position']['longitude'])
    if my_location['lat'] - 5 <= iss_lat <= my_location['lat'] + 5 \
            and my_location['lng'] - 5 <= iss_lon <= my_location['lng'] + 5:
        return True


def is_night():
    day_info = requests.get("https://api.sunrise-sunset.org/json", params=my_location)
    sunrise = int(day_info.json()['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(day_info.json()['results']['sunset'].split('T')[1].split(':')[0])
    if datetime.now().hour >= sunset or datetime.now().hour < sunrise:
        return True
    return False


# check if iss is at your location post sunset and before sunrise
while True:
    time.sleep(20)
    if iss_is_visible() and is_night():
        send_email()
