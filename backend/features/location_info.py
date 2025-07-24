# backend/features/location_info.py

# A sample database mapping districts in Rajasthan to their Agro-Climatic Zone (ACZ)
# This new version includes recommended crops for each zone.
RAJASTHAN_ACZ_MAP = {
    # Zone IVa: Sub-Humid Southern Plains and Aravalli Hills
    "udaipur": {
        "name": "Sub-Humid Southern Plains and Aravalli Hills (Zone IVa)",
        "crops": ["Maize", "Soybean", "Gram", "Wheat", "Mustard"]
    },
    "chittorgarh": {
        "name": "Sub-Humid Southern Plains and Aravalli Hills (Zone IVa)",
        "crops": ["Maize", "Soybean", "Gram", "Wheat", "Mustard"]
    },
    "bhilwara": {
        "name": "Sub-Humid Southern Plains and Aravalli Hills (Zone IVa)",
        "crops": ["Maize", "Cotton", "Wheat", "Gram", "Groundnut"]
    },

    # Zone IIa: Transitional Plain of Luni Basin
    "pali": {
        "name": "Transitional Plain of Luni Basin (Zone IIa)",
        "crops": ["Sesame", "Mustard", "Wheat", "Barley", "Guar"]
    },
    "jodhpur": {
        "name": "Transitional Plain of Luni Basin (Zone IIa)",
        "crops": ["Bajra (Pearl Millet)", "Moong", "Moth", "Guar", "Wheat"]
    },

    # Zone Ia: Arid Western Plains
    "jaisalmer": {
        "name": "Arid Western Plains (Zone Ia)",
        "crops": ["Bajra (Pearl Millet)", "Moth Bean", "Guar", "Mustard (irrigated)"]
    },
    "barmer": {
        "name": "Arid Western Plains (Zone Ia)",
        "crops": ["Bajra (Pearl Millet)", "Moth Bean", "Guar", "Til (Sesame)"]
    },
}

def get_agro_climatic_zone_info(city: str, state: str):
    """
    Looks up all information for a given city/district.
    """
    if state.lower() == "rajasthan":
        # Return the zone's dictionary if the city is in our map, otherwise return None
        return RAJASTHAN_ACZ_MAP.get(city.lower())
    
    return None

def get_recommended_crops(city: str, state: str):
    """
    Returns a list of recommended crops for a given location.
    """
    zone_info = get_agro_climatic_zone_info(city, state)
    if zone_info and "crops" in zone_info:
        return zone_info["crops"]
    
    # Return a default list if the location is not found
    return ["General crop recommendations not available for this area."]

def get_agro_climatic_zone_name(city: str, state: str):
    """
    Returns just the name of the Agro-Climatic Zone.
    """
    zone_info = get_agro_climatic_zone_info(city, state)
    if zone_info and "name" in zone_info:
        return zone_info["name"]
    
    return f"General {state} Zone"

