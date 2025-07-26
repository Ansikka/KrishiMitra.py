# backend/features/govt_schemes.py

import json

def load_schemes_data():
    """Loads the government schemes data from our JSON file."""
    try:
        with open('backend/data/govt_schemes.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Warning: govt_schemes.json not found or is invalid.")
        return {}

def get_schemes_for_state(state: str):
    """
    Retrieves a list of all relevant government schemes for a given state,
    including both national and state-specific schemes.
    """
    all_schemes = load_schemes_data()
    
    # Always include national schemes
    national_schemes = all_schemes.get("national_schemes", [])
    
    # Get state-specific schemes (case-insensitive)
    state_specific_schemes = all_schemes.get("state_specific_schemes", {}).get(state.title(), [])
    
    if not national_schemes and not state_specific_schemes:
        return {"error": "No scheme data is currently available."}
        
    return {
        "query": {
            "state": state
        },
        "national_schemes": national_schemes,
        "state_specific_schemes": state_specific_schemes
    }

