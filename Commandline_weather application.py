#COMMAND LINE WEATHER APPLICATION

import requests
import json

# Enter your API key from OpenWeatherMap
api_key = "<API_KEY>"

# Enter the location you want to know the weather of
city = input("Enter the city name: ")

# Get the weather data from the API
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
weather_data = requests.get(url).json()

# Extract the important information from the weather data
temperature = weather_data["main"]["temp"]
humidity = weather_data["main"]["humidity"]
description = weather_data["weather"][0]["description"]

# Print the weather information
print(f"Temperature: {temperature}°F")
print(f"Humidity: {humidity}%")
print(f"Conditions: {description}")
