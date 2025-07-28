import streamlit as st
from datetime import datetime
from gtts import gTTS
import base64
import os
import pandas as pd
from chatbot import ask_groq
from weather import get_weather
import streamlit.components.v1 as components

API_KEY = "Your_OpenWeather_API_Key"  # Replace with your actual OpenWeather API key
GROQ_API_KEY = "Your_Groq_API_Key"  # Replace with your actual Groq API key

# ------------------ Utility Function ------------------
def play_audio(text, lang_code='en'):
    tts = gTTS(text=text, lang=lang_code)
    filename = "temp_audio.mp3"
    tts.save(filename)
    with open(filename, "rb") as audio_file:
        audio_bytes = audio_file.read()
    b64 = base64.b64encode(audio_bytes).decode()
    audio_html = f'<audio autoplay="true" controls="controls"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
    st.markdown(audio_html, unsafe_allow_html=True)
    os.remove(filename)

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
    # other languages...
}

# ------------------ Sidebar for Language ------------------
st.sidebar.title("🌐 Select Language")
language = st.sidebar.selectbox("Choose your preferred language:", list(LANGUAGE_DATA.keys()))
lang_content = LANGUAGE_DATA[language]
tts_lang = lang_content["tts_lang"]

# ------------------ Main UI ------------------
st.title(lang_content["welcome"])
if st.button("🔊 Read Aloud"):
    play_audio(lang_content["welcome"], tts_lang)

# ------------------ Fertilizer Recommendation ------------------
with st.expander(lang_content["fertilizer"]):
    crop = st.selectbox("Select Crop", ["Wheat", "Rice", "Maize", "Cereals", "Sugarcane", "Potato", "Tomato"])
    soil = st.selectbox("Soil Type", ["Black", "Red", "Sandy", "Brown"])

    if st.button("Get Recommendation"):
        rec = f"For {crop} in {soil} soil, use NPK 20:20:0 at 50kg/acre."
        st.session_state["recommendation"] = rec
        st.success(rec)

    if "recommendation" in st.session_state and st.button("🔊 Listen Recommendation"):
        play_audio(st.session_state["recommendation"], tts_lang)

# ------------------ Loan/Subsidy Checker ------------------
with st.expander(lang_content["loan"]):
    age = st.number_input("Enter your age", min_value=18, max_value=80)
    holding = st.selectbox("Land holding (acres)", ["<1", "1-5", ">5"])

    if st.button("Check Eligibility"):
        eligible = "You are eligible for KCC and PM-KISAN schemes."
        st.session_state["eligibility"] = eligible
        st.info(eligible)

    if "eligibility" in st.session_state and st.button("🔊 Listen Eligibility"):
        play_audio(st.session_state["eligibility"], tts_lang)

# ------------------ Weather Alerts ------------------
with st.expander(lang_content["weather_alert"]):
    today = datetime.now().strftime("%d-%m-%Y")
    st.write(f"📅 Today's Date: {today}")

    city = st.text_input("Enter your city for weather updates", value="")
    if city:
        weather = get_weather(city, API_KEY)
        if weather:
            st.success(f"🌤️ Weather in {city}: {weather['description']}")
            st.info(f"🌡️ Temperature: {weather['temp']}°C (Feels like {weather['feels_like']}°C)")
            st.info(f"💧 Humidity: {weather['humidity']}%")
            st.info(f"🌬️ Wind Speed: {weather['wind_speed']} m/s")
            if "rain" in weather["description"].lower():
                st.warning("⚠️ Rain Alert! Please take precautions.")
        else:
            st.error("❌ Failed to fetch weather data. Please check the city name or API key.")

# ------------------ Crop Calendar ------------------
with st.expander(lang_content["crop_calendar"]):
    season = st.selectbox("Choose Season", ["Rabi", "Kharif", "Zaid"])

    if st.button("Show Calendar"):
        calendar = f"For {season}, sow Wheat, Mustard, and Barley."
        st.session_state["calendar"] = calendar
        st.success(calendar)

    if "calendar" in st.session_state and st.button("🔊 Listen Calendar"):
        play_audio(st.session_state["calendar"], tts_lang)

# ------------------ Mandi Prices ------------------
with st.expander('📈 Mandi Prices'):
    mandi_data = {
        "Crop": ["Wheat", "Rice", "Mustard", "Maize", "Barley", "Soybean", "Cotton", "Groundnut", "Sugarcane",
                 "Potato", "Onion", "Tomato", "Bajra", "Jowar", "Urad Dal", "Moong Dal", "Chana", "Masoor Dal",
                 "Banana", "Apple", "Brinjal", "Carrot", "Cabbage", "Peas"],
        "Price (₹/qtl)": [
            "₹2200", "₹1800", "₹5500", "₹1700", "₹1600", "₹4800", "₹6600", "₹5500", "₹340",
            "₹1200", "₹900", "₹1100", "₹2150", "₹2738", "₹6600", "₹7275", "₹5400", "₹6000",
            "₹1500", "₹3000", "₹900", "₹1100", "₹850", "₹1400"
        ]
    }
    st.table(pd.DataFrame(mandi_data))

# ------------------ Chatbot (Subtle Integration) ------------------
with st.expander("💬 Chat Assistant"):
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.chat_input("Ask your question...")

    if user_input:
        with st.spinner("Thinking..."):
            ai_response = ask_groq(user_input, GROQ_API_KEY)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("AI", ai_response))
        st.session_state["last_ai_response"] = ai_response  # ✅ Store last response

    if "last_ai_response" in st.session_state and st.button("🔊 Listen to AI Response"):
        play_audio(st.session_state["last_ai_response"], tts_lang)

    for sender, msg in st.session_state.chat_history:
        with st.chat_message("user" if sender == "You" else "assistant"):
            st.markdown(msg)


# ------------------ Footer ------------------
st.markdown("---")
st.markdown("Made with ❤️ for Indian Farmers - KrishiMitra")
