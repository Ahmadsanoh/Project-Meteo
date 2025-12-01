from fastapi import APIRouter, Query, HTTPException
from typing import List
from datetime import datetime
from app.models import Activity, Weather, WeatherActivitiesResponse
from app.services.activity_service import list_activities, filter_activities_by_weather
from app.services.weather_service import get_weather_for_city

# ------------------------
# Router
# ------------------------
router = APIRouter(prefix="/activities", tags=["activities"])

# ------------------------
# Endpoint: list all activities
# ------------------------
@router.get("/", response_model=List[Activity])
def get_activities():
    return list_activities()


# ------------------------
# Endpoint: activities for a specific date (and optional city)
# ------------------------
@router.get("/for-date/", response_model=List[Activity])
async def get_activities_for_date(
    query_date: str = Query(..., description="Date in DD-MM-YYYY format"),
    city: str = Query(None, description="City name (default: Paris)")
):
    # Validate date
    try:
        parsed_date = datetime.strptime(query_date, "%d-%m-%Y").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use DD-MM-YYYY.")

    # Fetch real weather for the city
    weather: Weather = await get_weather_for_city(city)

    # Filter activities based on weather condition
    filtered_activities = filter_activities_by_weather(weather.condition)

    return filtered_activities


# ------------------------
# Endpoint: combined weather + filtered activities
# ------------------------
@router.get("/with-weather/", response_model=WeatherActivitiesResponse)
async def get_activities_with_weather(
    query_date: str = Query(..., description="Date in DD-MM-YYYY format"),
    city: str = Query(None, description="City name (default: Paris)")
):
    # Validate date
    try:
        parsed_date = datetime.strptime(query_date, "%d-%m-%Y").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use DD-MM-YYYY.")

    # Fetch real weather for the city
    weather: Weather = await get_weather_for_city(city)

    # Filter activities based on weather condition
    filtered_activities = filter_activities_by_weather(weather.condition)

    return WeatherActivitiesResponse(
        weather=weather,
        activities=filtered_activities
    )
