#  KrishiMitra - Empowering Farmers with Smart Agriculture Tools

**KrishiMitra** is an all-in-one AI-powered digital assistant tailored to support Indian farmers by providing vital agricultural insights,
government schemes, real-time mandi prices, weather updates, crop disease detection, and multilingual support. It aims to bridge the technology
gap for rural farmers and help improve productivity and decision-making in agriculture.

##  Features

###  Multi-Language Support
- Supports regional languages including **Hindi**, **Punjabi**, **Bhojpuri**, **Tamil**, **Telugu**, **Kannada**, and **Awadhi**.
- Text-to-speech and translated messages using `gTTS` and custom dictionaries.

###  Daily Task Reminders
- Farmers can select and schedule daily agricultural tasks.
- Tasks are displayed prominently for better time and farm management.

###  Mandi Prices
- Real-time mandi prices for crops like wheat, rice, mustard, pulses, vegetables, fruits, and more.
- Helps farmers make informed decisions on crop selling.

###  Weather Forecast
- Location-based weather forecasts and alerts to prevent crop damage and plan irrigation.

###  Crop Disease Detection
- Upload crop images to detect diseases using machine learning models (coming soon).
- Early diagnosis improves crop yield and reduces loss.

###  BhashaBuddy (Language Helper)
- Converts agricultural messages into native languages to support low-literacy farmers.

###  Chatbot (Coming Soon)
- An intelligent chatbot for answering agricultural queries, farming techniques, and more.

###  Government Schemes
- Lists both men and women-centric schemes for financial assistance, insurance, and innovation.

###  Map Locator (Planned)
- Integration of location-based mandi locators and nearest agriculture centers.

### File Management
KrishiMitra/

├── assets  

├── data/           

├── modules/      

├── krishimitra_app.py 

├── README.md        

└── requirements.txt    

### Tech Stack
- Frontend: Streamlit

- Backend: Python

- Libraries: gTTS for text-to-speech; Pillow for image processing requests; geopy for weather/location; OpenCV and ML models for disease detection (future).

### How to get started
#### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/KrishiMitra.py.git
cd KrishiMitra.py
```
#### 2. Prerequisites
- Install Python 3.8+
- Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```
#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
#### 4. Run the app
```bash
streamlit run krishimitra_app.py
```

### Government Schemes included: 
1. PM-KISAN
2. PMFBY
3. KCC
4. Soil Health Card
5. eNAM
6. RKVY
7. PUSA Krishi.

### Women-specific schemes: 
1. Mahila Kisan Sashaktikaran
2. Annapurna Scheme, and more.

### Future Improvements:
1. Chatbot with NLP
2. Smart crop recommendation system
3. Automated SMS alerts
4. Real-time news and alerts for farmers

## About Contributions
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

#### License
This project is licensed under the MIT License. See the LICENSE file for details.

#### Acknowledgements
NumFOCUS and Open Science Labs
Indian Council of Agricultural Research (ICAR)
Government of India Open Data APIs

```bash
Farmers who inspire innovation every day 🌾
Made with love for our farmers.
```
