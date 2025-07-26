# backend/features/mandi_prices.py

import requests
from backend import config

def to_int_safely(value):
    """Safely converts a value to an integer, returning 0 on failure."""
    if value is None: return 0
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return 0

def get_live_prices_for_commodity(state: str, commodity: str):
    """
    Retrieves and processes live mandi prices from data.gov.in,
    implementing sorting and summary logic as per the user's plan.
    """
    api_key = config.DATA_GOV_API_KEY
    api_url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
    
    params = {
        "api-key": api_key,
        "format": "json",
        "offset": "0",
        "limit": "500", # Get more records to find the best price
        "filters[state]": state.title(),
        "filters[commodity]": commodity.title()
    }

    try:
        response = requests.get(api_url, params=params, timeout=20)
        response.raise_for_status()
        data = response.json()
        
        records = data.get("records", [])
        if not records:
            return {"error": f"No live prices found for {commodity} in {state}. The market may be closed or data not reported today."}
            
        # --- 1. Filtering and Cleaning Logic ---
        processed_prices = []
        for record in records:
            modal_price = to_int_safely(record.get("modal_price"))
            # Only include records that have a valid price
            if modal_price > 0:
                processed_prices.append({
                    "district": record.get("district", "N/A"),
                    "market_name": record.get("market", "N/A"),
                    "modal_price": modal_price,
                    "arrival_date": record.get("arrival_date", "N/A")
                })
        
        if not processed_prices:
             return {"error": f"Price data for {commodity} in {state} is currently not available (all prices reported as 0)."}

        # --- 2. Sorting Logic (as per your plan) ---
        # Sort the list of prices from highest to lowest modal_price
        processed_prices.sort(key=lambda x: x["modal_price"], reverse=True)

        # --- 3. Price Insights / Summary Logic (as per your plan) ---
        best_mandi = processed_prices[0]
        summary = (
            f"📈 Best rate for {commodity.title()} in {state.title()} today is "
            f"₹{best_mandi['modal_price']}/quintal at {best_mandi['market_name']}."
        )

        return {
            "query": {
                "state": state,
                "commodity": commodity,
                "source": "data.gov.in (Agmarknet)"
            },
            "summary": summary, # <-- YOUR SUMMARY INSIGHT!
            "prices": processed_prices # <-- YOUR SORTED LIST!
        }

    except requests.exceptions.RequestException as e:
        print(f"Live Mandi API Error: {e}")
        return {"error": "Could not connect to the live mandi price service."}