# backend/main.py

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse # <-- NEW IMPORT for audio
from backend.features import weather
from backend.features import agri_advisor
from backend.features import location_info
from backend.features import mandi_prices
from backend.features import disease_detection
from backend.features import govt_schemes
from backend.features import tts # <-- NEW IMPORT

# Create the app instance
app = FastAPI()

@app.get("/")
def read_root():
    return {"Project": "KrishiMitra 2.0+ Backend"}

# --- All previous endpoints remain the same ---

@app.get("/api/v1/weather")
def get_weather(city: str = "Udaipur", state: str = "Rajasthan"):
    weather_data = weather.get_weather_data(city, state)
    return weather_data

@app.get("/api/v1/agri_advice")
async def get_agri_advice(city: str = "Udaipur", state: str = "Rajasthan", crop: str = "wheat"):
    advice_data = await agri_advisor.generate_agri_advice(city, state, crop)
    return advice_data

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

@app.get("/api/v1/mandi_prices")
def get_mandi_prices(state: str = "Rajasthan", commodity: str = "Wheat"):
    price_data = mandi_prices.get_live_prices_for_commodity(state, commodity)
    return price_data

@app.post("/api/v1/detect_disease")
async def detect_disease(image: UploadFile = File(...)):
    result = disease_detection.simulate_disease_detection(image)
    return result

@app.get("/api/v1/govt_schemes")
def get_govt_schemes(state: str = "Rajasthan"):
    schemes_data = govt_schemes.get_schemes_for_state(state)
    return schemes_data

# --- NEW: Text-to-Speech Endpoint ---
@app.get("/api/v1/generate_audio")
def generate_audio(text: str = "Welcome to KrishiMitra", lang: str = "en"):
    """
    This endpoint generates and returns an MP3 audio file for the given text.
    """
    audio_stream = tts.generate_audio_from_text(text, lang)
    
    if audio_stream:
        # Return the audio as a streaming response with the correct media type
        return StreamingResponse(audio_stream, media_type="audio/mpeg")
    else:
        return {"error": "Could not generate audio."}
