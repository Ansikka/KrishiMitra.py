# backend/features/rule_engine.py

import json

def load_crop_conditions():
    """Loads the ideal crop conditions from our JSON file."""
    try:
        with open('backend/data/crop_conditions.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        # If file doesn't exist or is empty/invalid, return an empty dict
        print(f"Warning: Could not load crop_conditions.json. Error: {e}. Proceeding without it.")
        return {}

def generate_rule_based_advice(weather_data: dict, crop: str):
    """
    Generates a list of actionable advice points based on a set of rules.
    """
    advice_list = []
    crop_conditions = load_crop_conditions()
    
    temp = weather_data.get("temperature_celsius", 0)
    humidity = weather_data.get("humidity_percent", 0)
    condition = weather_data.get("condition", "").lower()

    # Rule 1: High Humidity Warning
    if humidity > 80:
        advice_list.append({
            "emoji": "💧",
            "type": "warning",
            "text": f"High humidity ({humidity}%) increases the risk of fungal diseases for most crops. Ensure good air circulation."
        })

    # Rule 2: Pesticide/Fertilizer Application Warning
    if "rain" in condition or "thunderstorm" in condition:
        advice_list.append({
            "emoji": "🌧️",
            "type": "action_needed",
            "text": "Rain is expected. Avoid spraying pesticides or applying fertilizer in the next 24 hours to prevent it from washing away."
        })

    # Rule 3: Crop-Specific Temperature Check
    if crop in crop_conditions:
        ideal_temp = crop_conditions[crop]["ideal_temp_celsius"]
        if not (ideal_temp[0] <= temp <= ideal_temp[1]):
            advice_list.append({
                "emoji": "🌡️",
                "type": "warning",
                "text": f"The current temperature ({temp}°C) is outside the ideal range of {ideal_temp[0]}-{ideal_temp[1]}°C for {crop}. This may cause stress."
            })
        else:
            advice_list.append({
                "emoji": "✅",
                "type": "positive",
                "text": f"The current temperature ({temp}°C) is favorable for your {crop} crop."
            })

    # Rule 4: Default message if no other rules apply
    if not advice_list:
        advice_list.append({
            "emoji": "👍",
            "type": "info",
            "text": "Weather conditions appear stable. Continue standard farming practices and monitor daily."
        })

    return advice_list
