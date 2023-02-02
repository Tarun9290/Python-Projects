#A weather application - 
It allows the users to check the current weather and forecast for a given location.

import requests
import json

def weather_app(api_key, city_name):
    # Make the API call to get the weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)

    # Check if the API call was successful
    if response.status_code == 200:
        # Parse the JSON data
        data = json.loads(response.text)

        # Extract the weather information
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        # Display the weather information
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather}")
    else:
        print("Failed to get weather data")

# Example usage
api_key = "YOUR_API_KEY"
city_name = "London"

weather_app(api_key, city_name)
