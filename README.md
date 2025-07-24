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

**KrishiMitra 2.0** is an open-source, AI-powered digital assistant tailored for Indian farmers. It aims to bridge the tech divide in agriculture by offering real-time, location-specific, and accessible information in **multiple Indian languages**. From detecting crop diseases to delivering weather alerts and government schemes — it's your **digital farming buddy**.

---

## 🔥 Key Features

| Feature | Description |
|--------|-------------|
| 🧠 **Crop Disease Detection** | Upload crop photo → AI detects disease → Get organic & chemical remedies |
| 💬 **BhashaBuddy** | Converts advice to local languages and speaks aloud (via TTS) |
| ☁️ **Weather Forecasting** | Accurate local weather data using OpenWeather API |
| 📊 **Mandi Prices** | Real-time market rates from Agmarknet |
| 🌱 **Crop Recommender** | Suggests ideal crops based on region, soil, and season |
| 🧾 **Govt. Schemes** | Lists major & women-specific agricultural schemes |
| 🤖 **Chatbot (Coming Soon)** | NLP-based chatbot for instant farm Q&A |

---

## 🧠 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python + FastAPI (setup in progress)
- **Machine Learning (Planned)**: OpenCV, Scikit-learn
- **APIs**: OpenWeatherMap, Agmarknet, Language tools
- **Modules & Libraries**: `gTTS`, `Pillow`, `Geopy`, `Requests`, `json`, `pandas`

---

## 📁 Project Structure

```bash
KrishiMitra/
├── modules/
│   ├── disease_detection.py
│   ├── remedies.py
│   ├── weather.py
│   ├── crop_recommender.py
│   └── advisory_logic.py
├── data/                # JSON/CSV resources
├── assets/              # Images/audio/icons
├── krishimitra_app.py   # Streamlit frontend
├── main.py              # FastAPI backend (WIP)
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.8+
- `pip` installed

### 🛠️ Installation

```bash
pip install -r requirements.txt
```

### ▶️ Run the App

```bash
streamlit run krishimitra_app.py
```

For API testing (once backend is ready):

```bash
uvicorn main:app --reload
```

---

## 🏛️ Government Schemes Integrated

Includes major national schemes such as:

- **PM-KISAN**, **PMFBY**, **KCC**, **Soil Health Card**, **eNAM**, **RKVY**, **PUSA Krishi**
- **For Women**: Mahila Kisan Sashaktikaran Yojana, Annapurna Scheme, and more

---

## 🌱 Future Roadmap

- ✅ Weather Advisory + Voice Output
- 🔄 Backend APIs with FastAPI
- 🤖 Chatbot using NLP (HuggingFace / Langchain)
- 📱 Mobile-responsive PWA
- 📡 Automated SMS Alerts
- 📰 Real-time Agri News & Notifications

---

## 👐 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---

## 🙏 Acknowledgements

- NumFOCUS & Open Science Labs  
- ICAR (Indian Council of Agricultural Research)  
- Government of India Open Data APIs  
- And the **farmers who inspire us every day** 🌾

<p align="center"><b>Made with love, code, and purpose — for India's farmers 🇮🇳</b></p>
