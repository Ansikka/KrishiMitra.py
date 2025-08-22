<p align="center">
  <img src="https://img.icons8.com/color/96/tractor.png" width="80"/>
</p>

<h1 align="center">🌾 KrishiMitra 2.0 — AI-Powered Assistant for Indian Farmers</h1>

<p align="center">
  Empowering Indian agriculture with AI | Multilingual Support | Disease Detection | Smart Farming
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-green?style=flat&logo=python"/>
  <img src="https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?&style=flat&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Open%20Source-%2312100E.svg?&style=flat&logo=github"/>
  <img src="https://img.shields.io/badge/Made%20for-GSSoC-orange"/>
</p>

---

## ✨ Overview

**KrishiMitra 2.0** is an open-source, AI-powered digital assistant tailored for Indian farmers. With a mission to bridge the tech gap in agriculture, it provides real-time solutions for:

- 🌾 Crop disease detection  
- 💬 Multilingual remedies (via TTS)  
- 📊 Mandi price tracking  
- ☁️ Weather updates  
- 🌱 Crop recommendations  
- 🧾 Government scheme info

All through a **simple, easy-to-use Streamlit interface**.

---

## 🔥 Features

| Feature | Description |
|--------|-------------|
| 🧠 **Crop Disease Detection** | Upload a photo → AI detects disease → Gives remedies (organic & chemical) |
| 💬 **BhashaBuddy** | Converts advice into local languages + speaks it aloud via TTS |
| ☁️ **Weather Forecasting** | Accurate weather insights for proactive planning |
| 📊 **Mandi Prices** | Real-time prices for crops in your local mandi |
| 🌱 **Crop Recommender** | Suggests crops based on region, season, and soil |
| 🧾 **Govt. Schemes** | Latest schemes for farmers (male & female) |
| 🤖 **ChatBot (Coming Soon)** | Get farming advice instantly using Q&A bot |

---

## 🧠 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python
- **ML Libraries**: OpenCV, scikit-learn *(upcoming)*
- **APIs**:
  - [OpenWeatherMap](https://openweathermap.org/)
  - [Agmarknet (Mandi Prices)](https://agmarknet.gov.in/)
- **Tools**:
  - `gTTS` (Google Text-to-Speech)
  - `Pillow` (Image processing)
  - `Geopy` (Geolocation)
  - `Requests` (API calls)

---

## 📁 Project Structure

```bash
KrishiMitra/
├── modules/            # All logic modules
│   ├── disease_detection.py
│   ├── remedies.py
│   ├── weather.py
│   └── crop_recommender.py
├── data/               # JSON / CSV files
├── assets/             # Images / audio
├── krishimitra_app.py  # Main Streamlit app
├── requirements.txt    # All dependencies
└── README.md

🚀 Getting Started
✅ Prerequisites
Python 3.8+
Streamlit (pip install streamlit)
Other libraries: gTTS, Pillow, requests, geopy, opencv-python

Install :

bash command

pip install -r requirements.txt
▶️ Run the App

bash command

streamlit run krishimitra_app.py


🤝 Contributing
We welcome contributions from developers, researchers, and agri-enthusiasts!
To contribute:

Fork the repo

Create a new branch

Make your changes

Open a Pull Request

📌 Future Roadmap
 AI-powered ChatBot assistant

 Voice Command Interface in regional languages

 Farmer crop diary & reminders

 Disease prediction via time-series ML models

 Full mobile app version

🧑‍🌾 Made For
This project is proudly made for Girlscript Summer of Code 2025 (GSSoC) and aims to uplift the farming ecosystem in India through accessible AI tools.

📜 License
This project is licensed under the MIT License.

🌟 Star this repo to support the cause of smart agriculture in India!
yaml
Copy
Edit

---

Let me know if you want:
- Translated content in Hindi/Tamil/etc.
- Custom logo/banner
- GitHub-friendly `.md` formatting with emojis/icons optimized for dark/light themes
- Contribution guidelines

