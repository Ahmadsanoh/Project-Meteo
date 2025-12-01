from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models import Weather
from app.services.weather_service import get_weather_for_city

router = APIRouter(prefix="/weather", tags=["weather"])

@router.get("/", response_model=Weather)
async def get_weather(city: Optional[str] = Query(None, description="City name to get weather for")):
    try:
        weather_data = await get_weather_for_city(city)
        return weather_data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
