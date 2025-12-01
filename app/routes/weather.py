from fastapi import APIRouter
from app.models import Weather
from datetime import date

router = APIRouter(prefix="/weather", tags=["weather"])

# Example endpoint
@router.get("/{query_date}")
def get_weather(query_date: str):
    # dummy response
    return Weather(date=date.today(), temperature=25.5, condition="sunny")
