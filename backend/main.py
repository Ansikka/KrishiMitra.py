# backend/main.py

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    HTTPException,
    Request,
    status
)
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional
import logging
import traceback

# Import feature modules
from backend.features import (
    weather,
    agri_advisor,
    location_info,
    mandi_prices,
    disease_detection,
    govt_schemes,
    tts,
    chatbot,
    productivity_booster
)

# ------------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger("KrishiMitra")

# ------------------------------------------------------------------
# FastAPI App Initialization
# ------------------------------------------------------------------
app = FastAPI(
    title="KrishiMitra 2.0+ Backend",
    version="2.1.0",
    description="AI-powered agricultural advisory platform"
)

# ------------------------------------------------------------------
# CORS (safe defaults)
# ------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------------------------
# Utility: Standard API Response
# ------------------------------------------------------------------
def success_response(data, message="Success"):
    return {
        "status": "success",
        "message": message,
        "data": data
    }

def error_response(message, details=None):
    return {
        "status": "error",
        "message": message,
        "details": details
    }

# ------------------------------------------------------------------
# Global Exception Handlers
# ------------------------------------------------------------------
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    traceback.print_exc()
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=error_response(
            "Internal server error",
            str(exc)
        )
    )

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=error_response(
            "Validation failed",
            exc.errors()
        )
    )

# ------------------------------------------------------------------
# Pydantic Models
# ------------------------------------------------------------------
class ChatMessage(BaseModel):
    user: str = Field(..., min_length=1)
    assistant: str = Field(..., min_length=1)

class ChatRequest(BaseModel):
    user_message: str = Field(..., min_length=1)
    history: List[ChatMessage] = []
    language: str = Field(default="en", min_length=2, max_length=5)

class FarmerProfile(BaseModel):
    gender: Optional[str] = Field(None)
    land_holding_acres: Optional[float] = Field(None, ge=0)
    is_loanee: Optional[bool] = None

class ExpertAdviceRequest(BaseModel):
    crop: str = Field(..., min_length=2)
    crop_stage: str = Field(..., min_length=2)
    problem_description: str = Field(..., min_length=10)
    goal: str = Field(..., min_length=5)
    lang: str = Field(default="en", min_length=2)

# ------------------------------------------------------------------
# Health Check
# ------------------------------------------------------------------
@app.get("/")
def read_root():
    return success_response(
        {"service": "KrishiMitra Backend", "status": "running"}
    )

# ------------------------------------------------------------------
# Weather API
# ------------------------------------------------------------------
@app.get("/api/v1/weather")
def get_weather(city: str = "Udaipur", state: str = "Rajasthan"):
    try:
        data = weather.get_weather_data(city, state)
        if not data:
            raise HTTPException(status_code=404, detail="Weather data not found")
        return success_response(data)
    except Exception as e:
        logger.error(f"Weather API error: {e}")
        raise HTTPException(status_code=500, detail="Weather service failed")

# ------------------------------------------------------------------
# Agricultural Advice
# ------------------------------------------------------------------
@app.get("/api/v1/agri_advice")
async def get_agri_advice(
    city: str = "Udaipur",
    state: str = "Rajasthan",
    crop: str = "wheat",
    crop_stage: str = "Sowing",
    lang: str = "en"
):
    try:
        advice = await agri_advisor.generate_agri_advice(
            city, state, crop, crop_stage, lang
        )
        return success_response(advice)
    except Exception as e:
        logger.error(f"Agri advice error: {e}")
        raise HTTPException(status_code=500, detail="Agri advisory failed")

# ------------------------------------------------------------------
# Expert Diagnosis & Productivity Booster
# ------------------------------------------------------------------
@app.post("/api/v1/expert_advice")
async def get_expert_advice(request: ExpertAdviceRequest):
    try:
        result = await productivity_booster.generate_expert_advice(
            crop=request.crop,
            crop_stage=request.crop_stage,
            problem_description=request.problem_description,
            goal=request.goal,
            lang=request.lang
        )
        return success_response(result)
    except Exception as e:
        logger.error(f"Expert advice error: {e}")
        raise HTTPException(status_code=500, detail="Expert advisory failed")

# ------------------------------------------------------------------
# Crop Recommendation
# ------------------------------------------------------------------
@app.get("/api/v1/crop_recommendation")
def get_crop_recommendation(city: str = "Udaipur", state: str = "Rajasthan"):
    try:
        zone = location_info.get_agro_climatic_zone_name(city, state)
        crops = location_info.get_recommended_crops(city, state)
        return success_response({
            "location": {
                "city": city,
                "state": state,
                "agro_climatic_zone": zone
            },
            "recommended_crops": crops
        })
    except Exception as e:
        logger.error(f"Crop recommendation error: {e}")
        raise HTTPException(status_code=500, detail="Crop recommendation failed")

# ------------------------------------------------------------------
# Mandi Prices
# ------------------------------------------------------------------
@app.get("/api/v1/mandi_prices")
def get_mandi_prices(state: str = "Rajasthan", commodity: str = "Wheat"):
    try:
        prices = mandi_prices.get_live_prices_for_commodity(state, commodity)
        if not prices:
            raise HTTPException(status_code=404, detail="No mandi data found")
        return success_response(prices)
    except Exception as e:
        logger.error(f"Mandi price error: {e}")
        raise HTTPException(status_code=500, detail="Mandi service failed")

# ------------------------------------------------------------------
# Disease Detection
# ------------------------------------------------------------------
@app.post("/api/v1/detect_disease")
async def detect_disease(image: UploadFile = File(...)):
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid image file")

    try:
        result = await disease_detection.simulate_disease_detection(image)
        return success_response(result)
    except Exception as e:
        logger.error(f"Disease detection error: {e}")
        raise HTTPException(status_code=500, detail="Disease detection failed")

# ------------------------------------------------------------------
# Government Schemes
# ------------------------------------------------------------------
@app.post("/api/v1/govt_schemes")
def get_govt_schemes(
    profile: FarmerProfile,
    state: str = "Rajasthan",
    lang: str = "en"
):
    try:
        schemes = govt_schemes.get_schemes_for_farmer(
            state,
            profile.dict(exclude_none=True),
            lang
        )
        return success_response(schemes)
    except Exception as e:
        logger.error(f"Govt schemes error: {e}")
        raise HTTPException(status_code=500, detail="Scheme service failed")

# ------------------------------------------------------------------
# Text-to-Speech
# ------------------------------------------------------------------
@app.get("/api/v1/generate_audio")
def generate_audio(text: str, lang: str = "en"):
    try:
        audio_stream = tts.generate_audio_from_text(text, lang)
        if not audio_stream:
            raise HTTPException(status_code=500, detail="Audio generation failed")
        return StreamingResponse(audio_stream, media_type="audio/mpeg")
    except Exception as e:
        logger.error(f"TTS error: {e}")
        raise HTTPException(status_code=500, detail="TTS service failed")

# ------------------------------------------------------------------
# Chatbot
# ------------------------------------------------------------------
@app.post("/api/v1/chatbot")
async def handle_chat(chat_request: ChatRequest):
    try:
        history = [msg.dict() for msg in chat_request.history]
        response = await chatbot.generate_chatbot_response(
            user_message=chat_request.user_message,
            history=history,
            language=chat_request.language
        )
        return success_response(response)
    except Exception as e:
        logger.error(f"Chatbot error: {e}")
        raise HTTPException(status_code=500, detail="Chatbot service failed")
