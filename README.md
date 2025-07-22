# KrishiMitra - Empowering Farmers with Smart Agriculture Tools

KrishiMitra is an all-in-one AI-powered digital assistant tailored to support Indian farmers by providing vital agricultural insights, government schemes, real-time mandi prices, weather updates, crop disease detection, and multilingual support. It aims to bridge the technology gap for rural farmers and help improve productivity and decision-making in agriculture.

## Features

- **Multi-Language Support**
  - Supports regional languages including Hindi, Punjabi, Bhojpuri, Tamil, Telugu, Kannada, and Awadhi.
  - Text-to-speech and translated messages using gTTS and custom dictionaries.
- **Daily Task Reminders**
  - Farmers can select and schedule daily agricultural tasks.
  - Tasks are displayed prominently for better time and farm management.
- **Mandi Prices**
  - Real-time mandi prices for crops like wheat, rice, mustard, pulses, vegetables, fruits, and more.
  - Helps farmers make informed decisions on crop selling.
- **Weather Forecast**
  - Location-based weather forecasts and alerts to prevent crop damage and plan irrigation.
- **Crop Disease Detection**
  - Upload crop images to detect diseases using machine learning models (coming soon).
  - Early diagnosis improves crop yield and reduces loss.
- **BhashaBuddy (Language Helper)**
  - Converts agricultural messages into native languages to support low-literacy farmers.
- **Chatbot (Coming Soon)**
  - An intelligent chatbot for answering agricultural queries, farming techniques, and more.
- **Government Schemes**
  - Lists both men and women-centric schemes for financial assistance, insurance, and innovation.
- **Map Locator (Planned)**
  - Integration of location-based mandi locators and nearest agriculture centers.

---

## Project Structure

```
KrishiMitra/
│
├── assets/               # Crop images or icons
├── data/                 # JSON files (schemes, prices, translations)
├── modules/              # Feature-specific Python scripts
├── krishimitra_app.py    # Main Streamlit app
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

---

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Libraries:**
  - gTTS for text-to-speech
  - Pillow for image processing
  - requests, geopy for weather/location
  - OpenCV and ML models for disease detection (future)

---

## Getting Started

**Prerequisites:** Python 3.8+

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run the App:**
```bash
streamlit run krishimitra_app.py
```

---

## Government Schemes Included
- PM-KISAN, PMFBY, KCC, Soil Health Card, eNAM, RKVY, PUSA Krishi
- Women-specific schemes: Mahila Kisan Sashaktikaran, Annapurna Scheme, and more.

---

## Future Improvements
- Chatbot with NLP
- Smart crop recommendation system
- Automated SMS alerts
- Real-time news and alerts for farmers

---

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgements
- NumFOCUS and Open Science Labs
- Indian Council of Agricultural Research (ICAR)
- Government of India Open Data APIs
- Farmers who inspire innovation every day 🌾

---

Made with love for our Farmer!!
