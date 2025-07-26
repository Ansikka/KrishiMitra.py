# backend/features/weather.py

import requests
from backend import config # Import our new config file

def get_weather_data(city: str, state: str):
    """
    Fetches real weather data from the OpenWeatherMap API.
    """
    # The URL for the OpenWeatherMap API
    # We use an f-string to insert our variables into the URL
    api_url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city},{state},IN"  # Query for city, state, and country (India)
        f"&appid={config.WEATHER_API_KEY}" # Use the key from our config file
        f"&units=metric" # Get temperature in Celsius
    )

    try:
        # Make the request to the API
        response = requests.get(api_url)
        
        # This will raise an error if the request failed (e.g., 404 Not Found)
        response.raise_for_status() 
        
        # Convert the JSON response text into a Python dictionary
        data = response.json()

        # Extract only the data we need
        processed_data = {
            "city": data["name"],
            "temperature_celsius": data["main"]["temp"],
            "condition": data["weather"][0]["main"],
            "humidity_percent": data["main"]["humidity"],
            "wind_speed_kph": data["wind"]["speed"] * 3.6 # Convert m/s to km/h
        }
        return processed_data

    except requests.exceptions.RequestException as e:
        # Handle cases where the API call fails (e.g., network error, invalid city)
        print(f"API Request Error: {e}")
        return {"error": "Could not retrieve weather data."}
    except KeyError:
        # Handle cases where the API response is not what we expect
        return {"error": "Unexpected data format from weather API."}
