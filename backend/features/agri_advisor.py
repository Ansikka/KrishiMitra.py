# backend/features/agri_advisor.py

import json
import requests
from backend.features import weather
from backend.features import location_info
from backend.features import rule_engine # <-- NEW: Import our rule engine
from backend import config

# --- THIS FUNCTION IS NOW MORE ROBUST ---
def load_knowledge_base():
    """Loads the agricultural rules from our JSON file."""
    try:
        with open('backend/data/agri_knowledge.json', 'r') as f:
            # If file is empty, json.load will raise an error
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        # If file doesn't exist or is empty/invalid, return an empty dict
        print(f"Warning: Could not load agri_knowledge.json. Error: {e}. Proceeding without it.")
        return {}

async def generate_agri_advice(city: str, state: str, crop: str):
    """
    Generates farming advice by first using a rule engine, then summarizing with an AI model.
    """
    # --- Step 1: Gather all context ---
    agro_climatic_zone = location_info.get_agro_climatic_zone_name(city, state)
    weather_data = weather.get_weather_data(city, state)
    if "error" in weather_data:
        return {"error": "Could not fetch weather data to generate advice."}

    # --- Step 2: Get structured advice from our new Rule Engine ---
    rule_based_advice = rule_engine.generate_rule_based_advice(weather_data, crop)

    # --- Step 3: Use Gemini AI to create a natural language summary ---
    prompt = f"""
    You are an expert agricultural advisor for Indian farmers. Your task is to convert a list of structured, rule-based advice points into a simple, conversational summary.

    **Context:**
    - Location: {city}, {state}, India
    - Agro-Climatic Zone (ACZ): {agro_climatic_zone}
    - Farmer's Crop: {crop}
    - Current Weather: {json.dumps(weather_data)}
    - Structured Advice Points: {json.dumps(rule_based_advice)}

    **Instructions:**
    1.  Read the structured advice points.
    2.  Combine them into 2-3 friendly, easy-to-understand bullet points.
    3.  Start with the most critical advice.
    4.  Use the emojis provided in the structured advice.
    5.  Keep the language simple and direct. Do not sound like a robot.
    
    Example Output:
    "Here is your farm advisory for today:
    * 💧 High humidity (85%) means you should watch out for fungal diseases.
    * ✅ The temperature is perfect for your wheat crop."
    """

    # --- Step 4: Call the Gemini AI Model ---
    api_key = config.GEMINI_API_KEY 
    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    payload = {"contents": [{"role": "user", "parts": [{"text": prompt}]}]}

    try:
        response = requests.post(api_url, json=payload, headers={'Content-Type': 'application/json'}, timeout=15)
        response.raise_for_status()
        result = response.json()
        
        if 'candidates' in result and result['candidates'][0]['content']['parts'][0]['text']:
            ai_summary = result['candidates'][0]['content']['parts'][0]['text']
        else:
            ai_summary = "Could not generate AI summary at this time."

    except requests.exceptions.RequestException as e:
        print(f"AI API Error: {e}")
        ai_summary = "Could not connect to the AI service."

    # --- Step 5: Combine and return the final result ---
    return {
        "agro_climatic_zone": agro_climatic_zone,
        "live_weather": weather_data,
        "rule_based_points": rule_based_advice, # We can return the raw rules for debugging
        "ai_summary": ai_summary.strip()
    }
