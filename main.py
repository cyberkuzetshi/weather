import datetime as dt
import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = '6b0769274692e24c0ca7c748e2a0e0ec'
CITY = 'Astana'

def kelvin_to_celcius_fahrenheit(kelvin):
    celcius = kelvin - 273.15
    fahrenheit = celcius * (9/5) + 32
    return celcius, fahrenheit

url = BASE_URL + 'appid=' + API_KEY + '&q=' + CITY

responce = requests.get(url).json()

temp_kelvin = responce['main']['temp']
temp_celcius, temp_fahrenheit = kelvin_to_celcius_fahrenheit(temp_kelvin)
feels_like_kelvin = responce['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celcius_fahrenheit(feels_like_kelvin)
wind_speed = responce['wind']['speed']
humidity = responce['main']['humidity']
description = responce['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(responce['sys']['sunrise'] + responce['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(responce['sys']['sunset'] + responce['timezone'])

print(f"Temp in {CITY}: {temp_celcius:.2f} or {temp_fahrenheit:.2f}")
print(f"Temp in {CITY} feels like: {feels_like_celsius:.2f} or {feels_like_fahrenheit:.2f}")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}m/s")
print(f"General weather in {CITY}: {description}")
print(f"Sun rises in {CITY} at {sunrise_time} local time")
print(f"Sun sets in {CITY} at {sunset_time} local time")