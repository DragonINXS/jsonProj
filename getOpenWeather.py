# Prints weather for a location on CLI

APPID = '8f43be26063516a1fe188911d7f5e113'

import json
import requests
import sys
from geopy import geocoders

# credentials for GeoNames
gn = geocoders.GeoNames(username='dragonINXS')


# get location from CLI
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, state_abv zipCode')
    sys.exit()


inputLocation = ' '.join(sys.argv[1:])

print('\n\nWeather in:', inputLocation.title())

# gets lon and lat for the loaction (needed for OpenWeather API call)
geoLocation = gn.geocode(inputLocation)
lat = geoLocation.latitude
lon = geoLocation.longitude
#print(geoLocation.latitude, geoLocation.longitude)

# what to exclude in call and perferred units
part = 'minutely,hourly,daily'
units = 'imperial'
#print(geoLocation.raw)


# get JSON data from OpenWeather
url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&units={units}&appid={APPID}' 
#print(url)

response = requests.get(url)
response.raise_for_status()

# loads json into python variable
weatherData = json.loads(response.text)

w = weatherData['current']

# prints the weather
print(
    '\n'
    'Current Temp:', w['temp'], 'F\n'
    'Feels like:', w['feels_like'], 'F\n'
    'Humidity:', w['humidity'], '%\n'
    'Cloud Cover:', w['clouds'], '%'
)

#print(response.text)

