import streamlit as st
from datetime import datetime
import base64
import pandas as pd
from gtts import gTTS
import os
from streamlit_chat import message
import openai
import plotly.express as px
import plotly.graph_objects as go
import json
import random

# Set background image
def set_bg_local(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Update this path to your local image file
set_bg_local("C:\\Users\\chait\\OneDrive\\Desktop\\OpenSource Contribution\\KrishiMitra.py\\open.jpeg")

# OpenAI API key
openai.api_key = "your-openai-api-key"  # Replace with your actual OpenAI API key

# Language Data
LANGUAGE_DATA = {
    "English": {
        "welcome": "🌾 Welcome to KrishiMitra!",
        "fertilizer": "🌱 Fertilizer Recommendation",
        "loan": "🏦 Loan/Subsidy Checker",
        "weather_alert": "🌦️ Weather Alerts",
        "crop_calendar": "📅 Crop Calendar"
    },
    "Hindi": {
        "welcome": "🌾 कृषि मित्र में आपका स्वागत है!",
        "fertilizer": "🌱 उर्वरक सिफारिश",
        "loan": "🏦 ऋण/सब्सिडी जांच",
        "weather_alert": "🌦️ मौसम अलर्ट",
        "crop_calendar": "📅 फसल कैलेंडर",
    },
    "Bhojpuri": {
        "welcome": "🌾 कृषिमित्र में रउआ स्वागत बा!",
        "fertilizer": "🌱 खाद सिफारिश",
        "loan": "🏦 कर्ज/सब्सिडी जांच",
        "weather_alert": "🌦️ मौसम चेतावनी",
        "crop_calendar": "📅 फसल कैलेंडर",
    },
    "Punjabi": {
        "welcome": "🌾 ਕ੍ਰਿਸ਼ੀ ਮਿਤਰ ਵਿੱਚ ਤੁਹਾਡਾ ਸੁਆਗਤ ਹੈ!",
        "fertilizer": "🌱 ਖਾਦ ਸਿਫਾਰਸ਼",
        "loan": "🏦 ਕਰਜ਼ਾ ਜਾਂ ਸਬਸਿਡੀ ਚੈੱਕਰ",
        "weather_alert": "🌦️ ਮੌਸਮ ਚੇਤਾਵਨੀ",
        "crop_calendar": "📅 ਫਸਲ ਕੈਲੰਡਰ",
    },
    "Tamil": {
        "welcome": "🌾 கிருஷிமித்ராவிற்கு வரவேற்கிறோம்!",
        "fertilizer": "🌱 உர பரிந்துரை",
        "loan": "🏦 கடன்/தொகை சரிபார்ப்பு",
        "weather_alert": "🌦️ வானிலை எச்சரிக்கை",
        "crop_calendar": "📅 பயிர் நாட்காட்டி",
    },
    "Telugu": {
        "welcome": "🌾 కృషిమిత్రా కు స్వాగతం!",
        "fertilizer": "🌱 ఎరువు సిఫార్సు",
        "loan": "🏦 రుణం/సబ్సిడీ తనిఖీ",
        "weather_alert": "🌦️ వాతావరణ హెచ్చరికలు",
        "crop_calendar": "📅 పంట క్యాలెండర్",
    },
    "Kannada": {
        "welcome": "🌾 ಕೃಷಿ ಮಿತ್ರಕ್ಕೆ ಸ್ವಾಗತ!",
        "fertilizer": "🌱 ರಸಗೊಬ್ಬರ ಶಿಫಾರಸು",
        "loan": "🏦 ಸಾಲ/ಸಬ್ಸಿಡಿ ತಪಾಸಣೆ",
        "weather_alert": "🌦️ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ",
        "crop_calendar": "📅 ಬೆಳೆ ದಿನದರ್ಶಿ",
    },
    "Awadhi": {
        "welcome": "🌾 कृषिमित्र मा तोहार स्वागत बा!",
        "fertilizer": "🌱 खाद सिफारिश",
        "loan": "🏦 कर्ज/सब्सिडी जांच",
        "weather_alert": "🌦️ मौसम चेतावनी",
        "crop_calendar": "📅 फसल कैलेंडर",
    }
}

# Sidebar for Language
st.sidebar.title("🌐 Select Language")
language = st.sidebar.selectbox("Choose your preferred language:", list(LANGUAGE_DATA.keys()))
lang_content = LANGUAGE_DATA[language]

# Main UI
st.title(lang_content["welcome"])

# Chatbot
st.subheader("🧠 Ask KrishiMitra (Chatbot)")
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ask your farming-related question...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )
    reply = response['choices'][0]['message']['content']
    st.session_state.messages.append({"role": "assistant", "content": reply})

for i, msg in enumerate(st.session_state.messages):
    message(msg["content"], is_user=(msg["role"] == "user"), key=str(i))

# Voice Assistance
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    audio_file = open("output.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")

# Map Locator
st.subheader("📍 Locate Nearby Services")
data = pd.DataFrame({
    'lat': [26.9124, 26.8467, 26.5045],
    'lon': [75.7873, 80.9462, 80.2270],
    'service': ['Krishi Center Jaipur', 'Agri Input Store Lucknow', 'Fertilizer Unit Kanpur']
})
st.map(data)

# Fertilizer Recommendation
st.header(lang_content["fertilizer"])
fertilizer_info = {
    "Wheat": {
        "Black": "Apply 120 kg N, 60 kg P₂O₅, 40 kg K₂O per hectare. Use Urea, DAP, and MOP.",
        "Red": "Apply 100 kg N, 50 kg P₂O₅, 30 kg K₂O per hectare. Add 5 tonnes FYM before sowing.",
        "Sandy": "Use 90 kg N, 45 kg P₂O₅, and 25 kg K₂O. Split N into 2–3 doses.",
        "Brown": "Apply 110 kg N, 55 kg P₂O₅, 35 kg K₂O per hectare. Include organic manure."
    },
    "Rice": {
        "Black": "Apply 100 kg N, 50 kg P₂O₅, 50 kg K₂O per hectare. Use split application for N.",
        "Red": "Use 90 kg N, 40 kg P₂O₅, and 40 kg K₂O. Add zinc sulphate @ 25 kg/ha.",
        "Sandy": "Apply 80 kg N, 30 kg P₂O₅, and 30 kg K₂O. Water management is essential.",
        "Brown": "Use 90:45:45 NPK with green manure incorporation before transplanting."
    },
    "Maize": {
        "Black": "Apply 120 kg N, 60 kg P₂O₅, 40 kg K₂O. Use basal + top dressing method.",
        "Red": "Use 100:50:30 NPK with 5 tonnes FYM. Zinc and Boron may be needed.",
        "Sandy": "Apply 80 kg N, 40 kg P₂O₅, 20 kg K₂O. Split nitrogen application in 3 stages.",
        "Brown": "100 kg N, 50 kg P₂O₅, 30 kg K₂O per hectare. Use organic compost pre-sowing."
    },
    "Potato": {
        "Black": "150:80:120 NPK kg/ha. Apply FYM @ 25 tons/ha before sowing.",
        "Red": "120:60:100 NPK + 2 tonnes of compost. Potassium is critical for tuber growth.",
        "Sandy": "100:40:80 NPK. Add micronutrients like Boron if deficiency appears.",
        "Brown": "130:70:110 NPK. Ensure deep ploughing and ridge formation."
    },
    "Sugarcane": {
        "Black": "Apply 250:115:115 NPK. Apply in 3 split doses with organic matter.",
        "Red": "Use 225:100:100 NPK with 10 tonnes FYM. Micronutrients essential.",
        "Sandy": "200:90:90 NPK. Add press mud or compost for better results.",
        "Brown": "240:110:110 NPK + green manure or biofertilizer for soil enrichment."
    },
    "Tomato": {
        "Black": "100:60:60 NPK per ha. Add 10–15 tonnes FYM. Split nitrogen.",
        "Red": "80:40:50 NPK + Boron and Magnesium. Add neem cake for pest resistance.",
        "Sandy": "70:35:45 NPK. Frequent irrigation needed.",
        "Brown": "90:50:50 NPK + Trichoderma enriched compost for disease control."
    },
    "Mustard": {
        "Black": "80:40:30 NPK + 5 kg Zinc Sulphate. Ideal for higher oil yield.",
        "Red": "70:35:25 NPK. Sulphur application helps oil quality.",
        "Sandy": "60:30:20 NPK. Add FYM and maintain moisture.",
        "Brown": "75:40:25 NPK. Use neem-coated urea."
    }
}
crop = st.selectbox("Select Crop", list(fertilizer_info.keys()))
soil = st.selectbox("Soil Type", list(fertilizer_info[crop].keys()))
if st.button("Get Recommendation"):
    st.success(fertilizer_info[crop][soil])

# Loan/Subsidy Info
st.header(lang_content["loan"])
age = st.number_input("Enter your age", min_value=18, max_value=80)
holding = st.selectbox("Land holding (acres)", ["<1", "1-5", ">5"])
if st.button("Check Eligibility"):
    schemes = []
    if age < 40:
        schemes.append("Kisan Credit Card (KCC)")
        schemes.append("PM-KISAN")
        schemes.append("Youth Agri Loan (NABARD)")
    elif age >= 60:
        schemes.append("Senior Farmer Pension Scheme")
    if holding == "<1":
        schemes.extend([
            "PM-KISAN",
            "KALIA Scheme (Odisha)",
            "YSR Rythu Bharosa (Andhra Pradesh)",
            "Mukhya Mantri Krishi Ashirwad (Jharkhand)"
        ])
    elif holding == "1-5":
        schemes.extend([
            "NABARD Subsidized Loans",
            "Solar Pump Subsidy",
            "Crop Insurance Scheme (PMFBY)",
            "Fasal Bima Yojana"
        ])
    elif holding == ">5":
        schemes.extend([
            "NABARD Long-Term Projects",
            "Warehouse Construction Loans",
            "Tractor Subsidy Scheme"
        ])
    schemes = list(set(schemes))
    if schemes:
        st.success("✅ You are eligible for the following schemes:")
        for scheme in schemes:
            st.markdown(f"- {scheme}")
    else:
        st.warning("❌ Not eligible for current subsidies based on given inputs.")

# Government Schemes
st.subheader("📜 Government Schemes")
schemes = {
    "PM-KISAN": "₹6000/year in 3 installments",
    "PMFBY": "Crop insurance at low premium",
    "KCC": "Credit up to ₹3 lakh @ 4% interest",
    "NABARD": "Irrigation and farm infra support",
    "Mahila Kisan Sashaktikaran": "Skill, input and support for women farmers"
}
st.json(schemes)

# Weather Alerts
st.header(lang_content["weather_alert"])
region = st.selectbox("Select Region", ["Punjab", "UP", "MP", "Bihar"])
weather_data = {
    "Punjab": "🌧️ Light rain expected tomorrow",
    "UP": "☀️ Clear skies today",
    "MP": "⛈️ Thunderstorms likely in evening",
    "Bihar": "🌦️ Cloudy with chances of rain"
}
st.warning(weather_data[region])
if st.button("🔊 Listen to Alert"):
    text_to_speech(weather_data[region])

# Crop Calendar
st.header(lang_content["crop_calendar"])
season = st.selectbox("Choose Season", ["Rabi", "Kharif", "Zaid"])
calendar_data = {
    "Rabi": "Wheat, Mustard, Barley",
    "Kharif": "Paddy, Maize, Bajra",
    "Zaid": "Watermelon, Cucumber"
}
st.success(calendar_data[season])

# Mandi Prices
st.subheader("💸 Mandi Prices")
mandi_data = {
    "wheat": "₹2200/qtl",
    "rice": "₹1800/qtl",
    "mustard": "₹5500/qtl",
    "maize": "₹1700/qtl",
    "barley": "₹1600/qtl",
    "soybean": "₹4800/qtl",
    "cotton": "₹6600/qtl",
    "groundnut": "₹5500/qtl",
    "sugarcane": "₹340/qtl",
    "potato": "₹1200/qtl",
    "onion": "₹900/qtl",
    "tomato": "₹1100/qtl",
    "bajra": "₹2150/qtl",
    "jowar": "₹2738/qtl",
    "urad dal": "₹6600/qtl",
    "moong dal": "₹7275/qtl",
    "chana": "₹5400/qtl",
    "masoor dal": "₹6000/qtl",
    "banana": "₹1500/qtl",
    "apple": "₹3000/qtl",
    "brinjal": "₹900/qtl",
    "carrot": "₹1100/qtl",
    "cabbage": "₹850/qtl",
    "peas": "₹1400/qtl"
}
st.table(mandi_data)

# Crop Economics Visualization
st.subheader("📊 Crop Economics Analysis")

# Load JSON data
def load_crop_data(file_path="crop_economics.json"):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        st.error("Crop economics JSON file not found!")
        return {}

# Calculate economics with enhanced calculations
def calculate_economics(crop_data):
    results = []
    for crop, data in crop_data.items():
        # Base calculations
        input_cost = (
            data["seed_cost"] +
            data["fertilizer"] +
            data["labor_cost"] +
            data["irrigation_cost"] +
            data["pest_control_cost"]
        )
        
        # Introduce yield variability (±10%)
        yield_variability = random.uniform(0.9, 1.1)
        adjusted_yield = data["yield"] * yield_variability
        
        # Introduce market price fluctuation (±5%)
        price_fluctuation = random.uniform(0.95, 1.05)
        adjusted_price = data["market_price"] * price_fluctuation
        
        # Calculate income and profit
        income = adjusted_yield * adjusted_price
        profit = income - input_cost
        
        # Calculate profit margin
        profit_margin = (profit / income * 100) if income > 0 else 0
        
        results.append({
            "Crop": crop.capitalize(),
            "Input Cost": round(input_cost, 2),
            "Income": round(income, 2),
            "Profit": round(profit, 2),
            "Profit Margin (%)": round(profit_margin, 2),
            "Adjusted Yield": round(adjusted_yield, 2),
            "Adjusted Price": round(adjusted_price, 2)
        })
    return pd.DataFrame(results)

# Load and process data
crop_data = load_crop_data()
if crop_data:
    df = calculate_economics(crop_data)
    
    # Display data table
    st.write("### Crop Economics Data")
    st.dataframe(df)
    
    # Bar chart for profit comparison
    st.write("### Profit Comparison Across Crops")
    fig_profit = px.bar(
        df,
        x="Crop",
        y="Profit",
        color="Crop",
        title="Profit by Crop",
        labels={"Profit": "Profit (₹)"},
        text="Profit",
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    fig_profit.update_traces(texttemplate="₹%{text:,.2f}", textposition="auto")
    fig_profit.update_layout(
        xaxis_title="Crop",
        yaxis_title="Profit (₹)",
        showlegend=False,
        template="plotly_white"
    )
    st.plotly_chart(fig_profit, use_container_width=True)
    
    # Optional grouped bar chart for input cost, income, and profit
    st.write("### Detailed Economics (Input Cost vs Income vs Profit)")
    show_grouped = st.checkbox("Show Grouped Bar Chart", value=False)
    if show_grouped:
        fig_grouped = go.Figure()
        fig_grouped.add_trace(go.Bar(
            x=df["Crop"],
            y=df["Input Cost"],
            name="Input Cost",
            marker_color="#FF4B4B",
            text=df["Input Cost"],
            texttemplate="₹%{text:,.2f}",
            textposition="auto"
        ))
        fig_grouped.add_trace(go.Bar(
            x=df["Crop"],
            y=df["Income"],
            name="Income",
            marker_color="#36A2EB",
            text=df["Income"],
            texttemplate="₹%{text:,.2f}",
            textposition="auto"
        ))
        fig_grouped.add_trace(go.Bar(
            x=df["Crop"],
            y=df["Profit"],
            name="Profit",
            marker_color="#4CAF50",
            text=df["Profit"],
            texttemplate="₹%{text:,.2f}",
            textposition="auto"
        ))
        fig_grouped.update_layout(
            barmode="group",
            title="Input Cost vs Income vs Profit by Crop",
            xaxis_title="Crop",
            yaxis_title="Amount (₹)",
            legend_title="Metric",
            template="plotly_white"
        )
        st.plotly_chart(fig_grouped, use_container_width=True)
    
    # Display additional metrics
    st.write("### Additional Metrics")
    st.write(f"Highest Profit Crop: **{df.loc[df['Profit'].idxmax(), 'Crop']}** (₹{df['Profit'].max():,.2f})")
    st.write(f"Highest Profit Margin: **{df.loc[df['Profit Margin (%)'].idxmax(), 'Crop']}** ({df['Profit Margin (%)'].max():.2f}%)")

# Task Selection
st.subheader("📋 Task for Today")
tasks = ["Irrigation", "Apply pesticide to paddy", "Harvest tomatoes"]
task = st.selectbox("Select Task", tasks)
st.success(f"Your task for today: {task}")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ for Indian Farmers - KrishiMitra")