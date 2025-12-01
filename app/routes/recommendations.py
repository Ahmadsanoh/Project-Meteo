from fastapi import APIRouter, HTTPException, Query
from typing import List
from datetime import datetime
from app.models import Activity, User, Weather
from app.services.activity_service import filter_activities_by_weather
from app.services.weather_service import get_weather_for_city

# ------------------------
# Router
# ------------------------
router = APIRouter(prefix="/recommendations", tags=["recommendations"])

# In-memory users (reuse the function from users.py)
from app.routes.users import get_users as get_all_users

# ------------------------
# Recommendation endpoint
# ------------------------
@router.get("/", response_model=List[Activity])
async def recommend_activities(
    user_id: int = Query(..., description="User ID for recommendations"),
    query_date: str = Query(..., description="Date in DD-MM-YYYY format"),
    city: str = Query(None, description="City name (default: Paris)")
):
    # 1️⃣ Validate date
    try:
        parsed_date = datetime.strptime(query_date, "%d-%m-%Y").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use DD-MM-YYYY.")

    # 2️⃣ Check user exists
    users_list = get_all_users()
    user = next((u for u in users_list if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail=f"User ID {user_id} not found")

    # 3️⃣ Get weather for the city
    weather: Weather = await get_weather_for_city(city)

    # 4️⃣ Filter activities by weather
    activities_weather_filtered: List[Activity] = filter_activities_by_weather(weather.condition)

    # 5️⃣ Further filter by user preference
    recommended_activities: List[Activity] = []
    for act in activities_weather_filtered:
        # Filter by prefers_outdoor
        if user.prefers_outdoor is not None and act.outdoor != user.prefers_outdoor:
            continue

        # Filter by tags (match activity name in user tags)
        if user.tags:
            user_tags = [t.strip().lower() for t in user.tags.split(",")]
            if not any(tag in act.name.lower() for tag in user_tags):
                continue

        recommended_activities.append(act)

    # 6️⃣ Fallback to weather-filtered activities if none match user preference
    if not recommended_activities:
        recommended_activities = activities_weather_filtered

    return recommended_activities
