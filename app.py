# app.py - The Streamlit User Interface for KrishiMitra

import streamlit as st
import requests
import pandas as pd
from io import BytesIO

# --- Page Configuration ---
st.set_page_config(
    page_title="KrishiMitra - AI Farming Assistant",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Backend API URL ---
BACKEND_URL = "http://127.0.0.1:8000"

# --- 1. BHASHABUDDY: TRANSLATION DICTIONARY ---
translations = {
    "en": {
        "header": "KrishiMitra",
        "subheader": "Your AI-powered assistant for smart farming decisions in India.",
        "bhashabuddy_header": "BhashaBuddy",
        "choose_language": "Choose Language:",
        "sidebar_info": "Select a language for a fully translated experience.",
        "tab_expert_diagnosis": "👩‍⚕️ Expert Diagnosis",
        "tab_mandi": "📈 Mandi Prices",
        "tab_health": "🌿 Crop Health",
        "tab_schemes": "📜 Govt. Schemes",
        "tab_recommendations": "🌍 Crop Recommendations",
        "expert_header": "🧠 Expert Diagnosis & Productivity Plan",
        "expert_desc": "Describe your crop's situation to get a detailed action plan from our AI agronomist.",
        "enter_crop": "1. Enter Your Crop:",
        "crop_stage": "2. Select Crop Stage:",
        "problem_desc": "3. Describe the Problem (e.g., 'yellow spots on lower leaves'):",
        "goal": "4. What is your primary goal?",
        "get_plan_button": "Generate Expert Plan",
        "ai_spinner": "🤖 KrishiNet AI is analyzing your situation...",
        "expert_plan_header": "Your Custom Action Plan:",
        "listen_plan": "Listen to this Plan",
        "audio_spinner": "Generating audio...",
        "audio_error": "Sorry, could not generate audio.",
        "chatbot_header": "💬 Quick Chat",
        "chat_input_placeholder": "Ask a quick question...",
    },
    "hi": {
        "header": "कृषि मित्र",
        "subheader": "भारत में स्मार्ट खेती के फैसलों के लिए आपका एआई-संचालित सहायक।",
        "bhashabuddy_header": "भाषाबडी",
        "choose_language": "भाषा चुनें:",
        "sidebar_info": "पूरी तरह से अनुवादित अनुभव के लिए एक भाषा चुनें।",
        "tab_expert_diagnosis": "👩‍⚕️ विशेषज्ञ निदान",
        "tab_mandi": "📈 मंडी कीमतें",
        "tab_health": "🌿 फसल स्वास्थ्य",
        "tab_schemes": "📜 सरकारी योजनाएं",
        "tab_recommendations": "🌍 फसल सिफारिशें",
        "expert_header": "🧠 विशेषज्ञ निदान और उत्पादकता योजना",
        "expert_desc": "हमारे एआई कृषि विज्ञानी से विस्तृत कार्य योजना प्राप्त करने के लिए अपनी फसल की स्थिति का वर्णन करें।",
        "enter_crop": "1. अपनी फसल दर्ज करें:",
        "crop_stage": "2. फसल की अवस्था चुनें:",
        "problem_desc": "3. समस्या का वर्णन करें (जैसे, 'निचली पत्तियों पर पीले धब्बे'):",
        "goal": "4. आपका प्राथमिक लक्ष्य क्या है?",
        "get_plan_button": "विशेषज्ञ योजना बनाएं",
        "ai_spinner": "🤖 कृषिनेत्र एआई आपकी स्थिति का विश्लेषण कर रहा है...",
        "expert_plan_header": "आपकी कस्टम कार्य योजना:",
        "listen_plan": "इस योजना को सुनें",
        "audio_spinner": "ऑडियो बना रहा है...",
        "audio_error": "क्षमा करें, ऑडियो नहीं बन सका।",
        "chatbot_header": "💬 त्वरित चैट",
        "chat_input_placeholder": "एक त्वरित प्रश्न पूछें...",
    },
    "mr": {
        "header": "कृषीमित्र",
        "subheader": "भारतातील स्मार्ट शेतीच्या निर्णयांसाठी तुमचा एआय-शक्ती असलेला सहाय्यक.",
        "bhashabuddy_header": "भाषाबडी",
        "choose_language": "भाषा निवडा:",
        "sidebar_info": "पूर्णपणे अनुवादित अनुभवासाठी एक भाषा निवडा.",
        "tab_expert_diagnosis": "👩‍⚕️ विशेषज्ञ निदान",
        "tab_mandi": "📈 मंडी भाव",
        "tab_health": "🌿 पीक आरोग्य",
        "tab_schemes": "📜 सरकारी योजना",
        "tab_recommendations": "🌍 पीक शिफारसी",
        "expert_header": "🧠 विशेषज्ञ निदान आणि उत्पादकता योजना",
        "expert_desc": "आमच्या एआय कृषीशास्त्रज्ञाकडून तपशीलवार कृती योजना मिळवण्यासाठी तुमच्या पिकाची परिस्थिती सांगा.",
        "enter_crop": "१. तुमचे पीक प्रविष्ट करा:",
        "crop_stage": "२. पिकाचा टप्पा निवडा:",
        "problem_desc": "३. समस्येचे वर्णन करा (उदा. 'खालच्या पानांवर पिवळे डाग'):",
        "goal": "४. तुमचे प्राथमिक ध्येय काय आहे?",
        "get_plan_button": "विशेषज्ञ योजना तयार करा",
        "ai_spinner": "🤖 कृषीनेट एआय तुमच्या परिस्थितीचे विश्लेषण करत आहे...",
        "expert_plan_header": "तुमची सानुकूल कृती योजना:",
        "listen_plan": "ही योजना ऐका",
        "audio_spinner": "ऑडिओ तयार होत आहे...",
        "audio_error": "क्षमस्व, ऑडिओ तयार करता आला नाही.",
        "chatbot_header": "💬 त्वरित गप्पा",
        "chat_input_placeholder": "एक त्वरित प्रश्न विचारा...",
    },
    "gu": {
        "header": "કૃષિમિત્ર",
        "subheader": "ભારતમાં સ્માર્ટ ખેતીના નિર્ણયો માટે તમારા એઆઈ-સંચાલિત સહાયક.",
        "bhashabuddy_header": "ભાષાબડી",
        "choose_language": "ભાષા પસંદ કરો:",
        "sidebar_info": "સંપૂર્ણ અનુવાદિત અનુભવ માટે ભાષા પસંદ કરો.",
        "tab_expert_diagnosis": "👩‍⚕️ નિષ્ણાત નિદાન",
        "tab_mandi": "📈 મંડીના ભાવ",
        "tab_health": "🌿 પાકનું આરોગ્ય",
        "tab_schemes": "📜 સરકારી યોજનાઓ",
        "tab_recommendations": "🌍 પાકની ભલામણો",
        "expert_header": "🧠 નિષ્ણાત નિદાન અને ઉત્પાદકતા યોજના",
        "expert_desc": "અમારા એઆઈ કૃષિવિજ્ઞાની પાસેથી વિગતવાર કાર્ય યોજના મેળવવા માટે તમારા પાકની પરિસ્થિતિનું વર્ણન કરો.",
        "enter_crop": "૧. તમારો પાક દાખલ કરો:",
        "crop_stage": "૨. પાકનો તબક્કો પસંદ કરો:",
        "problem_desc": "૩. સમસ્યાનું વર્ણન કરો (દા.ત., 'નીચલા પાંદડા પર પીળા ડાઘ'):",
        "goal": "૪. તમારું પ્રાથમિક લક્ષ્ય શું છે?",
        "get_plan_button": "નિષ્ણાત યોજના બનાવો",
        "ai_spinner": "🤖 કૃષિનેટ એઆઈ તમારી પરિસ્થિતિનું વિશ્લેષણ કરી રહ્યું છે...",
        "expert_plan_header": "તમારી કસ્ટમ કાર્ય યોજના:",
        "listen_plan": "આ યોજના સાંભળો",
        "audio_spinner": "ઓડિયો જનરેટ કરી રહ્યું છે...",
        "audio_error": "માફ કરશો, ઓડિયો જનરેટ કરી શકાયો નથી.",
        "chatbot_header": "💬 ઝડપી ચેટ",
        "chat_input_placeholder": "એક ઝડપી પ્રશ્ન પૂછો...",
    },
    "bn": {
        "header": "কৃষিমিত্র",
        "subheader": "ভারতে স্মার্ট কৃষি সিদ্ধান্তের জন্য আপনার এআই-চালিত সহকারী।",
        "bhashabuddy_header": "ভাষাসাথী",
        "choose_language": "ভাষা নির্বাচন করুন:",
        "sidebar_info": "একটি সম্পূর্ণ অনূদিত অভিজ্ঞতার জন্য একটি ভাষা নির্বাচন করুন।",
        "tab_expert_diagnosis": "👩‍⚕️ বিশেষজ্ঞ নির্ণয়",
        "tab_mandi": "📈 মন্ডি দর",
        "tab_health": "🌿 ফসল স্বাস্থ্য",
        "tab_schemes": "📜 সরকারি প্রকল্প",
        "tab_recommendations": "🌍 ফসল সুপারিশ",
        "expert_header": "🧠 বিশেষজ্ঞ নির্ণয় ও উৎপাদনশীলতা পরিকল্পনা",
        "expert_desc": "আমাদের এআই কৃষিবিদের কাছ থেকে একটি বিস্তারিত কর্ম পরিকল্পনা পেতে আপনার ফসলের পরিস্থিতি বর্ণনা করুন।",
        "enter_crop": "১. আপনার ফসল লিখুন:",
        "crop_stage": "২. ফসলের পর্যায় নির্বাচন করুন:",
        "problem_desc": "৩. সমস্যা বর্ণনা করুন (যেমন, 'নিচের পাতায় হলুদ দাগ'):",
        "goal": "৪. আপনার প্রাথমিক লক্ষ্য কি?",
        "get_plan_button": "বিশেষজ্ঞ পরিকল্পনা তৈরি করুন",
        "ai_spinner": "🤖 কৃষিনেট এআই আপনার পরিস্থিতি বিশ্লেষণ করছে...",
        "expert_plan_header": "আপনার কাস্টম কর্ম পরিকল্পনা:",
        "listen_plan": "এই পরিকল্পনাটি শুনুন",
        "audio_spinner": "অডিও তৈরি হচ্ছে...",
        "audio_error": "দুঃখিত, অডিও তৈরি করা যায়নি।",
        "chatbot_header": "💬 দ্রুত চ্যাট",
        "chat_input_placeholder": "একটি দ্রুত প্রশ্ন জিজ্ঞাসা করুন...",
    },
    "ta": {
        "header": "கிருஷிமித்ரா",
        "subheader": "இந்தியாவில் ஸ்மார்ட் விவசாய முடிவுகளுக்கு உங்கள் AI-இயங்கும் உதவியாளர்.",
        "bhashabuddy_header": "பாஷாபட்டி",
        "choose_language": "மொழியைத் தேர்ந்தெடுக்கவும்:",
        "sidebar_info": "முழுமையாக மொழிபெயர்க்கப்பட்ட அனுபவத்திற்கு ஒரு மொழியைத் தேர்ந்தெடுக்கவும்.",
        "tab_expert_diagnosis": "👩‍⚕️ நிபுணர் கண்டறிதல்",
        "tab_mandi": "📈 மண்டி விலைகள்",
        "tab_health": "🌿 பயிர் ஆரோக்கியம்",
        "tab_schemes": "📜 அரசாங்க திட்டங்கள்",
        "tab_recommendations": "🌍 பயிர் பரிந்துரைகள்",
        "expert_header": "🧠 நிபுணர் கண்டறிதல் மற்றும் உற்பத்தித்திறன் திட்டம்",
        "expert_desc": "எங்கள் AI விவசாய விஞ்ஞானியிடமிருந்து விரிவான செயல் திட்டத்தைப் பெற உங்கள் பயிர் நிலையை விவரிக்கவும்.",
        "enter_crop": "1. உங்கள் பயிரை உள்ளிடவும்:",
        "crop_stage": "2. பயிர் நிலையைத் தேர்ந்தெடுக்கவும்:",
        "problem_desc": "3. சிக்கலை விவரிக்கவும் (எ.கா., 'கீழ் இலைகளில் மஞ்சள் புள்ளிகள்'):",
        "goal": "4. உங்கள் முதன்மை இலக்கு என்ன?",
        "get_plan_button": "நிபுணர் திட்டத்தை உருவாக்கவும்",
        "ai_spinner": "🤖 கிருஷிநெட் AI உங்கள் நிலையை பகுப்பாய்வு செய்கிறது...",
        "expert_plan_header": "உங்கள் தனிப்பயன் செயல் திட்டம்:",
        "listen_plan": "இந்தத் திட்டத்தைக் கேட்கவும்",
        "audio_spinner": "ஆடியோ உருவாக்கப்படுகிறது...",
        "audio_error": "மன்னிக்கவும், ஆடியோவை உருவாக்க முடியவில்லை.",
        "chatbot_header": "💬 விரைவான அரட்டை",
        "chat_input_placeholder": "ஒரு விரைவான கேள்வியைக் கேட்கவும்...",
    },
    "te": {
        "header": "కృషిమిత్ర",
        "subheader": "భారతదేశంలో స్మార్ట్ వ్యవసాయ నిర్ణయాల కోసం మీ AI-ఆధారిత సహాయకుడు.",
        "bhashabuddy_header": "భాషాబడ్డీ",
        "choose_language": "భాషను ఎంచుకోండి:",
        "sidebar_info": "పూర్తిగా అనువదించబడిన అనుభవం కోసం ఒక భాషను ఎంచుకోండి.",
        "tab_expert_diagnosis": "👩‍⚕️ నిపుణుల నిర్ధారణ",
        "tab_mandi": "📈 మండి ధరలు",
        "tab_health": "🌿 పంట ఆరోగ్యం",
        "tab_schemes": "📜 ప్రభుత్వ పథకాలు",
        "tab_recommendations": "🌍 పంట సిఫార్సులు",
        "expert_header": "🧠 నిపుణుల నిర్ధారణ మరియు ఉత్పాదకత ప్రణాళిక",
        "expert_desc": "మా AI వ్యవసాయ శాస్త్రవేత్త నుండి వివరణాత్మక కార్యాచరణ ప్రణాళికను పొందడానికి మీ పంట పరిస్థితిని వివరించండి.",
        "enter_crop": "1. మీ పంటను నమోదు చేయండి:",
        "crop_stage": "2. పంట దశను ఎంచుకోండి:",
        "problem_desc": "3. సమస్యను వివరించండి (ఉదా., 'దిగువ ఆకులపై పసుపు మచ్చలు'):",
        "goal": "4. మీ ప్రాథమిక లక్ష్యం ఏమిటి?",
        "get_plan_button": "నిపుణుల ప్రణాళికను రూపొందించండి",
        "ai_spinner": "🤖 కృషిநெட் AI మీ పరిస్థితిని విశ్లేషిస్తోంది...",
        "expert_plan_header": "మీ కస్టమ్ కార్యాచరణ ప్రణాళిక:",
        "listen_plan": "ఈ ప్రణాళికను వినండి",
        "audio_spinner": "ఆడియో సృష్టించబడుతోంది...",
        "audio_error": "క్షమించండి, ఆడియోను సృష్టించడం సాధ్యం కాలేదు.",
        "chatbot_header": "💬 త్వరిత చాట్",
        "chat_input_placeholder": "ఒక శీఘ్ర ప్రశ్న అడగండి...",
    },
    "kn": {
        "header": "ಕೃಷಿಮಿತ್ರ",
        "subheader": "ಭಾರತದಲ್ಲಿ ಸ್ಮಾರ್ಟ್ ಕೃಷಿ ನಿರ್ಧಾರಗಳಿಗಾಗಿ ನಿಮ್ಮ AI-ಚಾಲಿತ ಸಹಾಯಕ.",
        "bhashabuddy_header": "ಭಾಷಾಬಡ್ಡಿ",
        "choose_language": "ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        "sidebar_info": "ಸಂಪೂರ್ಣ ಅನುವಾದಿತ ಅನುಭವಕ್ಕಾಗಿ ಒಂದು ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.",
        "tab_expert_diagnosis": "👩‍⚕️ ತಜ್ಞರ ರೋಗನಿರ್ಣಯ",
        "tab_mandi": "📈 ಮಂಡಿ ಬೆಲೆಗಳು",
        "tab_health": "🌿 ಬೆಳೆ ಆರೋಗ್ಯ",
        "tab_schemes": "📜 ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು",
        "tab_recommendations": "🌍 ಬೆಳೆ ಶಿಫಾರಸುಗಳು",
        "expert_header": "🧠 ತಜ್ಞರ ರೋಗನಿರ್ಣಯ ಮತ್ತು ಉತ್ಪಾದಕತೆ ಯೋಜನೆ",
        "expert_desc": "ನಮ್ಮ AI ಕೃಷಿ ವಿಜ್ಞಾನಿಯಿಂದ ವಿವರವಾದ ಕ್ರಿಯಾ ಯೋಜನೆಯನ್ನು ಪಡೆಯಲು ನಿಮ್ಮ ಬೆಳೆ ಪರಿಸ್ಥಿತಿಯನ್ನು ವಿವರಿಸಿ.",
        "enter_crop": "1. ನಿಮ್ಮ ಬೆಳೆಯನ್ನು ನಮೂದಿಸಿ:",
        "crop_stage": "2. ಬೆಳೆ ಹಂತವನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        "problem_desc": "3. ಸಮಸ್ಯೆಯನ್ನು ವಿವರಿಸಿ (ಉದಾ., 'ಕೆಳಗಿನ ಎಲೆಗಳ ಮೇಲೆ ಹಳದಿ ಚುಕ್ಕೆಗಳು'):",
        "goal": "4. ನಿಮ್ಮ ಪ್ರಾಥಮಿಕ ಗುರಿ ಏನು?",
        "get_plan_button": "ತಜ್ಞರ ಯೋಜನೆಯನ್ನು ರಚಿಸಿ",
        "ai_spinner": "🤖 ಕೃಷಿನೆಟ್ AI ನಿಮ್ಮ ಪರಿಸ್ಥಿತಿಯನ್ನು ವಿಶ್ಲೇಷಿಸುತ್ತಿದೆ...",
        "expert_plan_header": "ನಿಮ್ಮ ಕಸ್ಟಮ್ ಕ್ರಿಯಾ ಯೋಜನೆ:",
        "listen_plan": "ಈ ಯೋಜನೆಯನ್ನು ಕೇಳಿ",
        "audio_spinner": "ಆಡಿಯೋ ರಚಿಸಲಾಗುತ್ತಿದೆ...",
        "audio_error": "ಕ್ಷಮಿಸಿ, ಆಡಿಯೋ ರಚಿಸಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ.",
        "chatbot_header": "💬 ತ್ವರಿತ ಚಾಟ್",
        "chat_input_placeholder": "ಒಂದು ತ್ವರಿತ ಪ್ರಶ್ನೆ ಕೇಳಿ...",
    },
    "pa": {
        "header": "ਕ੍ਰਿਸ਼ੀਮਿੱਤਰ",
        "subheader": "ਭਾਰਤ ਵਿੱਚ ਸਮਾਰਟ ਖੇਤੀ ਦੇ ਫੈਸਲਿਆਂ ਲਈ ਤੁਹਾਡਾ AI-ਸੰਚਾਲਿਤ ਸਹਾਇਕ।",
        "bhashabuddy_header": "ਭਾਸ਼ਾਬੱਡੀ",
        "choose_language": "ਭਾਸ਼ਾ ਚੁਣੋ:",
        "sidebar_info": "ਪੂਰੀ ਤਰ੍ਹਾਂ ਅਨੁਵਾਦ ਕੀਤੇ ਅਨੁਭਵ ਲਈ ਇੱਕ ਭਾਸ਼ਾ ਚੁਣੋ।",
        "tab_expert_diagnosis": "👩‍⚕️ ਮਾਹਰ ਨਿਦਾਨ",
        "tab_mandi": "📈 ਮੰਡੀ ਦੀਆਂ ਕੀਮਤਾਂ",
        "tab_health": "🌿 ਫਸਲ ਦੀ ਸਿਹਤ",
        "tab_schemes": "📜 ਸਰਕਾਰੀ ਯੋਜਨਾਵਾਂ",
        "tab_recommendations": "🌍 ਫਸਲ ਦੀਆਂ ਸਿਫਾਰਸ਼ਾਂ",
        "expert_header": "🧠 ਮਾਹਰ ਨਿਦਾਨ ਅਤੇ ਉਤਪਾਦਕਤਾ ਯੋਜਨਾ",
        "expert_desc": "ਸਾਡੇ AI ਖੇਤੀ ਵਿਗਿਆਨੀ ਤੋਂ ਵਿਸਤ੍ਰਿਤ ਕਾਰਜ ਯੋਜਨਾ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਆਪਣੀ ਫਸਲ ਦੀ ਸਥਿਤੀ ਦਾ ਵਰਣਨ ਕਰੋ।",
        "enter_crop": "1. ਆਪਣੀ ਫਸਲ ਦਾਖਲ ਕਰੋ:",
        "crop_stage": "2. ਫਸਲ ਦਾ ਪੜਾਅ ਚੁਣੋ:",
        "problem_desc": "3. ਸਮੱਸਿਆ ਦਾ ਵਰਣਨ ਕਰੋ (ਜਿਵੇਂ, 'ਹੇਠਲੇ ਪੱਤਿਆਂ 'ਤੇ ਪੀਲੇ ਧੱਬੇ'):",
        "goal": "4. ਤੁਹਾਡਾ ਮੁੱਖ ਟੀਚਾ ਕੀ ਹੈ?",
        "get_plan_button": "ਮਾਹਰ ਯੋਜਨਾ ਬਣਾਓ",
        "ai_spinner": "🤖 ਕ੍ਰਿਸ਼ੀਨੈੱਟ AI ਤੁਹਾਡੀ ਸਥਿਤੀ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰ ਰਿਹਾ ਹੈ...",
        "expert_plan_header": "ਤੁਹਾਡੀ ਕਸਟਮ ਕਾਰਜ ਯੋਜਨਾ:",
        "listen_plan": "ਇਸ ਯੋਜਨਾ ਨੂੰ ਸੁਣੋ",
        "audio_spinner": "ਆਡੀਓ ਬਣਾਇਆ ਜਾ ਰਿਹਾ ਹੈ...",
        "audio_error": "ਮਾਫ ਕਰਨਾ, ਆਡੀਓ ਨਹੀਂ ਬਣਾਇਆ ਜਾ ਸਕਿਆ।",
        "chatbot_header": "� ਤੁਰੰਤ ਗੱਲਬਾਤ",
        "chat_input_placeholder": "ਇੱਕ ਤੁਰੰਤ ਸਵਾਲ ਪੁੱਛੋ...",
    }
    
}



# --- UI Components ---

import streamlit as st
import requests
from io import BytesIO

# -------------------------------
# Sidebar: Language Selector
# -------------------------------
with st.sidebar:
    st.header("BhashaBuddy (भाषाबडी)")

    language_options = {
        "English": "en", "हिन्दी (Hindi)": "hi", "বাংলা (Bengali)": "bn",
        "తెలుగు (Telugu)": "te", "मराठी (Marathi)": "mr", "தமிழ் (Tamil)": "ta",
        "ગુજરાતી (Gujarati)": "gu", "ಕನ್ನಡ (Kannada)": "kn", "ਪੰਜਾਬੀ (Punjabi)": "pa"
    }

    selected_language_name = st.selectbox(
        "Choose Language:",
        list(language_options.keys()),
        index=0
    )

    selected_language_code = language_options.get(selected_language_name, "en")

    # Safe translation fallback
    t = translations.get(selected_language_code) or translations["en"]

    st.markdown("---")
    st.info(t.get("sidebar_info", "AI-powered farming assistant"))

# -------------------------------
# Main Header
# -------------------------------
st.title(f"🌾 {t.get('header', 'KrishiMitra')}")
st.markdown(f"#### {t.get('subheader', '')}")

# -------------------------------
# Tabs
# -------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    t["tab_expert_diagnosis"],
    t["tab_mandi"],
    t["tab_health"],
    t["tab_schemes"],
    t["tab_recommendations"]
])

# ==========================================================
# TAB 1: Expert Diagnosis + Chatbot
# ==========================================================
with tab1:
    col1, col2 = st.columns([2, 1])

    # -------------------------------
    # Expert Diagnosis Panel
    # -------------------------------
    with col1:
        with st.container(border=True):
            st.header(t["expert_header"])
            st.markdown(t["expert_desc"])

            expert_crop = st.text_input(
                t["enter_crop"],
                value="Tomato",
                max_chars=50
            )

            crop_stages = ["Sowing", "Vegetative Growth", "Flowering", "Harvesting"]
            expert_stage = st.selectbox(t["crop_stage"], crop_stages)

            expert_problem = st.text_area(
                t["problem_desc"],
                value="Yellow spots with brown edges on lower leaves.",
                height=120
            )

            goals = ["Increase Yield", "Improve Quality", "Reduce Costs", "Control Pests"]
            expert_goal = st.selectbox(t["goal"], goals)

            if st.button(
                t["get_plan_button"],
                use_container_width=True,
                type="primary"
            ):
                if not expert_problem.strip():
                    st.warning("Please describe the problem clearly.")
                else:
                    api_endpoint = f"{BACKEND_URL}/api/v1/expert_advice"
                    payload = {
                        "crop": expert_crop.strip(),
                        "crop_stage": expert_stage,
                        "problem_description": expert_problem.strip(),
                        "goal": expert_goal,
                        "lang": selected_language_code
                    }

                    try:
                        with st.spinner(t["ai_spinner"]):
                            response = requests.post(
                                api_endpoint,
                                json=payload,
                                timeout=60
                            )
                            response.raise_for_status()
                            result = response.json()

                        expert_plan_text = (
                            result.get("data")
                            or result.get("expert_plan")
                            or ""
                        )

                        if not expert_plan_text:
                            st.warning("No expert plan generated.")
                        else:
                            st.subheader(t["expert_plan_header"])
                            st.markdown(expert_plan_text)

                            # -------------------------------
                            # Audio Advice
                            # -------------------------------
                            st.markdown("---")
                            st.subheader(t["listen_plan"])

                            try:
                                with st.spinner(t["audio_spinner"]):
                                    audio_response = requests.get(
                                        f"{BACKEND_URL}/api/v1/generate_audio",
                                        params={
                                            "text": expert_plan_text,
                                            "lang": selected_language_code
                                        },
                                        timeout=30
                                    )

                                if audio_response.status_code == 200:
                                    st.audio(
                                        BytesIO(audio_response.content),
                                        format="audio/mpeg"
                                    )
                                else:
                                    st.warning(t["audio_error"])

                            except requests.exceptions.RequestException:
                                st.warning("Audio service unavailable.")

                    except requests.exceptions.Timeout:
                        st.error("Request timed out. Please try again.")
                    except requests.exceptions.ConnectionError:
                        st.error("Backend server not reachable.")
                    except requests.exceptions.HTTPError as e:
                        st.error(f"Server error: {e.response.status_code}")
                    except Exception:
                        st.error("Unexpected error occurred.")

    # -------------------------------
    # Chatbot Panel
    # -------------------------------
    with col2:
        with st.container(border=True):
            st.header(t["chatbot_header"])

            if prompt := st.chat_input(t["chat_input_placeholder"]):
                with st.chat_message("user"):
                    st.markdown(prompt)

                with st.chat_message("assistant"):
                    try:
                        response = requests.post(
                            f"{BACKEND_URL}/api/v1/chatbot",
                            json={
                                "user_message": prompt,
                                "language": selected_language_code
                            },
                            timeout=30
                        )
                        response.raise_for_status()
                        reply = (
                            response.json().get("data")
                            or response.json().get("response")
                            or "🤖 ..."
                        )
                        st.markdown(reply)

                    except requests.exceptions.RequestException:
                        st.markdown("⚠️ Chat service unavailable.")
