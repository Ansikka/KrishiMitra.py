# KrishiMitra - Empowering Farmers with Smart Agriculture Tools

**KrishiMitra** is an all-in-one AI-powered digital assistant tailored to support Indian farmers by providing vital agricultural insights, government schemes, real-time mandi prices, weather updates, crop disease detection, and multilingual support. It aims to bridge the technology gap for rural farmers and help improve productivity and decision-making in agriculture.

---

## Features

- **Multi-Language Support**: Hindi, Punjabi, Bhojpuri, Tamil, Telugu, Kannada, Awadhi
- **Text-to-Speech**: Using gTTS and custom dictionaries
- **Daily Task Reminders**: Select and schedule daily agricultural tasks
- **Mandi Prices**: Real-time prices for crops (wheat, rice, mustard, pulses, vegetables, fruits, etc.)
- **Weather Forecast**: Location-based weather forecasts and alerts
- **Crop Disease Detection**: (Coming soon) Upload crop images for ML-based disease detection
- **BhashaBuddy (Language Helper)**: Converts agricultural messages into native languages
- **Chatbot**: (Coming soon) AI-powered chatbot for agricultural queries
- **Government Schemes**: Lists men and women-centric schemes for financial assistance, insurance, and innovation
- **Map Locator**: (Planned) Location-based mandi locators and nearest agriculture centers

---

## Project Structure

```
KrishiMitra/
│
├── assets/               # Crop images or icons
├── data/                 # JSON files (schemes, prices, translations)
├── modules/              # Feature-specific Python scripts
├── krishimitra_app.py    # Main Streamlit app
├── farmer.py             # Chatbot and advanced features (module)
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
├── LICENSE               # MIT License
├── .env.example          # Environment variable template
├── .gitignore            # Git ignore rules
└── test_basic.py         # Basic test script
```

---

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Libraries**:
  - gTTS for text-to-speech
  - Pillow for image processing
  - pandas for data handling
  - openai for chatbot (optional)
  - streamlit_chat for chat UI (optional)
  - requests, geopy for weather/location (future)
  - OpenCV and ML models for disease detection (future)

---

## Getting Started

### Prerequisites
- Python 3.8+

### Install dependencies
```bash
pip install -r requirements.txt
```

### Set up environment variables
- Copy `.env.example` to `.env` and add your OpenAI API key if using the chatbot:
```
OPENAI_API_KEY=your-openai-api-key-here
```

### Run the App
```bash
streamlit run krishimitra_app.py
```

---

## Government Schemes Included
- PM-KISAN, PMFBY, KCC, Soil Health Card, eNAM, RKVY, PUSA Krishi
- Women-specific schemes: Mahila Kisan Sashaktikaran, Annapurna Scheme, and more

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

Made with ❤️ for our Farmer!!
