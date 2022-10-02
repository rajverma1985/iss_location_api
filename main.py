## To do:
# 1. track where ISS is w.r.t your location
# 2. location tracker from lat and lon using API: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# 3. https://www.latlong.net/Show-Latitude-Longitude.html >> get the location using this.

import requests

url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)

print(response.json())
