# backend/main.py

from fastapi import FastAPI
from backend.features import weather # Using absolute import

# Create the app instance
app = FastAPI()

@app.get("/")
def read_root():
    """
    Root endpoint for the backend.
    """
    return {"Project": "KrishiMitra 2.0+ Backend"}

@app.get("/api/v1/weather")
def get_weather(city: str = "Udaipur", state: str = "Rajasthan"):
    """
    This endpoint fetches the weather for a given city and state.
    It uses the logic from our weather feature module.
    """
    # Call the function from the weather.py module
    weather_data = weather.get_weather_data(city, state)
    return weather_data
