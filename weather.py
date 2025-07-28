# weather.py
import requests

def get_weather(city, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        print("DEBUG: Status Code =", response.status_code)  # 👈 Add this
        print("DEBUG: Response Text =", response.text)        # 👈 And this

        if response.status_code == 200:
            data = response.json()
            return {
                "description": data["weather"][0]["description"],
                "temp": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
        else:
            return None
    except Exception as e:
        print("DEBUG: Exception occurred:", e)  # 👈 Add this
        return None
