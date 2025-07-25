# backend/main.py

from fastapi import FastAPI
from backend.features import weather
from backend.features import agri_advisor
from backend.features import location_info
from backend.features import mandi_prices # This will now use your LIVE module

# Create the app instance
app = FastAPI()

@app.get("/")
def read_root():
    return {"Project": "KrishiMitra 2.0+ Backend"}

# --- Weather Endpoint ---
@app.get("/api/v1/weather")
def get_weather(city: str = "Udaipur", state: str = "Rajasthan"):
    weather_data = weather.get_weather_data(city, state)
    return weather_data

# --- Agri-Advisor Endpoint ---
@app.get("/api/v1/agri_advice")
async def get_agri_advice(city: str = "Udaipur", state: str = "Rajasthan", crop: str = "wheat"):
    advice_data = await agri_advisor.generate_agri_advice(city, state, crop)
    return advice_data

# --- Crop Recommendation Endpoint ---
@app.get("/api/v1/crop_recommendation")
def get_crop_recommendation(city: str = "Udaipur", state: str = "Rajasthan"):
    recommended_crops = location_info.get_recommended_crops(city, state)
    zone_name = location_info.get_agro_climatic_zone_name(city, state)
    return {
        "location": {
            "city": city,
            "state": state,
            "agro_climatic_zone": zone_name
        },
        "recommended_crops": recommended_crops
    }

# --- UPGRADED: Live Mandi Prices Endpoint ---
@app.get("/api/v1/mandi_prices")
def get_mandi_prices(state: str = "Rajasthan", commodity: str = "Wheat"):
    """
    This endpoint provides LIVE mandi prices for a given state and commodity
    from data.gov.in.
    """
    # Note: The district parameter is no longer needed here as the API
    # returns all districts for a given state.
    price_data = mandi_prices.get_live_prices_for_commodity(state, commodity)
    return price_data
