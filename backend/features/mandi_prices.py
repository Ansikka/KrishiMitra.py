# backend/features/mandi_prices.py

import requests
from backend import config # Import our config file to get the API key

def to_int_safely(value):
    """
    A helper function to safely convert a value to an integer.
    Returns 0 if the value is not a valid number.
    """
    if value is None:
        return 0
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return 0

def get_live_prices_for_commodity(state: str, commodity: str):
    """
    Retrieves live mandi prices from the data.gov.in API.
    This version has robust error handling for messy real-world data.
    """
    # --- 1. Set up the API request parameters ---
    api_key = config.DATA_GOV_API_KEY
    api_url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
    
    params = {
        "api-key": api_key,
        "format": "json",
        "offset": "0",
        "limit": "100", # Get up to 100 records
        "filters[state]": state.title(),
        "filters[commodity]": commodity.title()
    }

    # --- 2. Make the live API call ---
    try:
        response = requests.get(api_url, params=params, timeout=20)
        response.raise_for_status()
        data = response.json()
        
        # --- 3. Process the response ---
        records = data.get("records", [])
        if not records:
            return {"error": f"No live prices found for {commodity} in {state}. The market may be closed or data not reported today."}
            
        # Clean up the data to match our desired format
        processed_prices = []
        for record in records:
            processed_prices.append({
                "district": record.get("district", "N/A"),
                "market_name": record.get("market", "N/A"),
                "min_price": to_int_safely(record.get("min_price")),
                "max_price": to_int_safely(record.get("max_price")),
                "modal_price": to_int_safely(record.get("modal_price")),
                "arrival_date": record.get("arrival_date", "N/A")
            })

        return {
            "query": {
                "state": state,
                "commodity": commodity,
                "source": "data.gov.in (Agmarknet)"
            },
            "prices": processed_prices
        }

    except requests.exceptions.RequestException as e:
        print(f"Live Mandi API Error: {e}")
        return {"error": "Could not connect to the live mandi price service."}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {"error": "An unexpected error occurred while processing mandi prices."}
