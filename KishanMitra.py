import streamlit as st
from datetime import datetime
from gtts import gTTS
import base64
import os

# ------------------ Utility Function ------------------

import streamlit as st
from gtts import gTTS
import base64
from io import BytesIO

def play_audio(text, lang_code='en', autoplay=True):
    """
    Convert text to speech and play it in Streamlit.

    Args:
        text (str): Text to convert to speech.
        lang_code (str): Language code for TTS (default 'en').
        autoplay (bool): Whether audio should autoplay (default True).
    """
    # Generate TTS audio
    tts = gTTS(text=text, lang=lang_code)
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)

    # Encode audio to base64
    b64_audio = base64.b64encode(audio_bytes.read()).decode()
    autoplay_attr = 'true' if autoplay else 'false'

    # Embed in HTML audio player
    audio_html = f'''
        <audio autoplay="{autoplay_attr}" controls>
            <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mp3">
        </audio>
    '''
    st.markdown(audio_html, unsafe_allow_html=True)





# ------------------ Language Data ------------------
LANGUAGE_DATA = {
    "English": {
        "welcome": "🌾 Welcome to KrishiMitra!",
        "fertilizer": "🌱 Fertilizer Recommendation",
        "loan": "🏦 Loan/Subsidy Checker",
        "weather_alert": "🌦️ Weather Alerts",
        "crop_calendar": "📅 Crop Calendar",
        "tts_lang": "en"
    },
    "Hindi": {
        "welcome": "🌾 कृषि मित्र में आपका स्वागत है!",
        "fertilizer": "🌱 उर्वरक सिफारिश",
        "loan": "🏦 ऋण/सब्सिडी जांच",
        "weather_alert": "🌦️ मौसम अलर्ट",
        "crop_calendar": "📅 फसल कैलेंडर",
        "tts_lang": "hi"
    },
    "Bhojpuri": {
        "welcome": "🌾 कृषिमित्र में रउआ स्वागत बा!",
        "fertilizer": "🌱 खाद सिफारिश",
        "loan": "🏦 कर्ज/सब्सिडी जांच",
        "weather_alert": "🌦️ मौसम चेतावनी",
        "crop_calendar": "📅 फसल कैलेंडर",
        "tts_lang": "hi"
    },
    "Punjabi": {
        "welcome": "🌾 ਕ੍ਰਿਸ਼ੀ ਮਿਤਰ ਵਿੱਚ ਤੁਹਾਡਾ ਸੁਆਗਤ ਹੈ!",
        "fertilizer": "🌱 ਖਾਦ ਸਿਫਾਰਸ਼",
        "loan": "🏦 ਕਰਜ਼ਾ ਜਾਂ ਸਬਸਿਡੀ ਚੈੱਕਰ",
        "weather_alert": "🌦️ ਮੌਸਮ ਚੇਤਾਵਨੀ",
        "crop_calendar": "📅 ਫਸਲ ਕੈਲੰਡਰ",
        "tts_lang": "pa"
    },
    "Tamil": {
        "welcome": "🌾 கிருஷிமித்ராவிற்கு வரவேற்கிறோம்!",
        "fertilizer": "🌱 உர பரிந்துரை",
        "loan": "🏦 கடன்/தொகை சரிபார்ப்பு",
        "weather_alert": "🌦️ வானிலை எச்சரிக்கை",
        "crop_calendar": "📅 பயிர் நாட்காட்டி",
        "tts_lang": "ta"
    },
    "Telugu": {
        "welcome": "🌾 కృషిమిత్రా కు స్వాగతం!",
        "fertilizer": "🌱 ఎరువు సిఫార్సు",
        "loan": "🏦 రుణం/సబ్సిడీ తనిఖీ",
        "weather_alert": "🌦️ వాతావరణ హెచ్చరికలు",
        "crop_calendar": "📅 పంట క్యాలెండర్",
        "tts_lang": "te"
    },
    "Kannada": {
        "welcome": "🌾 ಕೃಷಿ ಮಿತ್ರಕ್ಕೆ ಸ್ವಾಗತ!",
        "fertilizer": "🌱 ರಸಗೊಬ್ಬರ ಶಿಫಾರಸು",
        "loan": "🏦 ಸಾಲ/ಸಬ್ಸಿಡಿ ತಪಾಸಣೆ",
        "weather_alert": "🌦️ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ",
        "crop_calendar": "📅 ಬೆಳೆ ದಿನದರ್ಶಿ",
        "tts_lang": "kn"
    },
    "Awadhi": {
        "welcome": "🌾 कृषिमित्र मा तोहार स्वागत बा!",
        "fertilizer": "🌱 खाद सिफारिश",
        "loan": "🏦 कर्ज/सब्सिडी जांच",
        "weather_alert": "🌦️ मौसम चेतावनी",
        "crop_calendar": "📅 फसल कैलेंडर",
        "tts_lang": "hi"
    }
}
import streamlit as st
from datetime import datetime
import pandas as pd

# Assuming play_audio and LANGUAGE_DATA are already defined

# ------------------ Sidebar for Language ------------------
st.sidebar.title("🌐 Select Language")
language = st.sidebar.selectbox("Choose your preferred language:", list(LANGUAGE_DATA.keys()))
lang_content = LANGUAGE_DATA[language]

# ------------------ Main UI ------------------
st.title(lang_content["welcome"])

def tts_button(label, text):
    """Reusable TTS button"""
    if st.button(label):
        play_audio(text, lang_content["tts_lang"])

tts_button("🔊 Read Aloud", lang_content["welcome"])

# ------------------ Fertilizer Recommendation ------------------
st.header(lang_content["fertilizer"])
crop = st.selectbox("Select Crop", ["Wheat", "Rice", "Maize", "Cereals", "Sugarcane", "Potato", "Tomato"])
soil = st.selectbox("Soil Type", ["Black", "Red", "Sandy", "Brown"])

if st.button("Get Recommendation"):
    rec = f"For {crop} in {soil} soil, use NPK 20:20:0 at 50kg/acre."
    st.success(rec)
    tts_button("🔊 Listen Recommendation", rec)

# ------------------ Loan/Subsidy Checker ------------------
st.header(lang_content["loan"])
age = st.number_input("Enter your age", min_value=18, max_value=80)
holding = st.selectbox("Land holding (acres)", ["<1", "1-5", ">5"])

if st.button("Check Eligibility"):
    eligible = "You are eligible for KCC and PM-KISAN schemes."
    st.info(eligible)
    tts_button("🔊 Listen Eligibility", eligible)

# ------------------ Weather Alerts ------------------
st.header(lang_content["weather_alert"])
today = datetime.now().strftime("%d-%m-%Y")
st.write(f"Today's Date: {today}")
st.warning("⚠️ Heavy Rain Expected in your region today.")

# ------------------ Crop Calendar ------------------
st.header(lang_content["crop_calendar"])
season = st.selectbox("Choose Season", ["Rabi", "Kharif", "Zaid"])

if st.button("Show Calendar"):
    calendar = {
        "Rabi": "Sow Wheat, Mustard, and Barley.",
        "Kharif": "Sow Rice, Maize, and Cotton.",
        "Zaid": "Sow Watermelon, Cucumber, and Muskmelon."
    }.get(season, "No calendar info available.")
    
    st.success(f"For {season} season: {calendar}")
    tts_button("🔊 Listen Calendar", f"For {season} season: {calendar}")

# ------------------ Mandi Prices ------------------
st.subheader("Market Prices (Mandi)")

mandi_data = {
    "Wheat": "₹2200/qtl", "Rice": "₹1800/qtl", "Mustard": "₹5500/qtl", "Maize": "₹1700/qtl",
    "Barley": "₹1600/qtl", "Soybean": "₹4800/qtl", "Cotton": "₹6600/qtl", "Groundnut": "₹5500/qtl",
    "Sugarcane": "₹340/qtl", "Potato": "₹1200/qtl", "Onion": "₹900/qtl", "Tomato": "₹1100/qtl",
    "Bajra": "₹2150/qtl", "Jowar": "₹2738/qtl", "Urad Dal": "₹6600/qtl", "Moong Dal": "₹7275/qtl",
    "Chana": "₹5400/qtl", "Masoor Dal": "₹6000/qtl", "Banana": "₹1500/qtl", "Apple": "₹3000/qtl",
    "Brinjal": "₹900/qtl", "Carrot": "₹1100/qtl", "Cabbage": "₹850/qtl", "Peas": "₹1400/qtl"
}

# Convert to DataFrame for better display
mandi_df = pd.DataFrame(list(mandi_data.items()), columns=["Crop", "Price"])
st.table(mandi_df)

# ------------------ Footer ------------------
st.markdown("---")
st.markdown("Made with ❤️ for Indian Farmers - KrishiMitra")
