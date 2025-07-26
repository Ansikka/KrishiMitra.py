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

**KrishiMitra 2.0** is an open-source, AI-powered digital assistant tailored for Indian farmers. With a mission to bridge the tech gap in agriculture, it provides real-time solutions for **crop disease detection**, **multilingual remedies**, **mandi prices**, **weather updates**, and more — all through an intuitive interface.

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
- **ML Libraries**: OpenCV, scikit-learn (upcoming)
- **APIs**: OpenWeatherMap, Agmarknet
- **Tools**: `gTTS`, `Pillow`, `Geopy`, `Requests`

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
├── krishimitra_app.py  # Main app
├── requirements.txt
└── README.md


