from datetime import date
from typing import Optional
import httpx
from app.models import Weather
from app.config import OPENWEATHER_API_KEY, DEFAULT_CITY

async def get_weather_for_city(city: Optional[str] = None) -> Weather:
    """
    Fetch weather from OpenWeatherMap API for a given city.
    Returns a Weather object.
    """
    if city is None:
        city = DEFAULT_CITY

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,  # Use key from config.py
        "units": "metric"
    }

    async with httpx.AsyncClient(timeout=10.0) as client:
        resp = await client.get(url, params=params)

        # Raise exception if HTTP request failed
        if resp.status_code != 200:
            data = resp.json()
            raise Exception(f"Error fetching weather for {city}: {data.get('message', 'Unknown error')}")

        data = resp.json()

    # Create Weather object from API response
    return Weather(
        date=date.today(),
        temperature=data["main"]["temp"],
        condition=data["weather"][0]["main"],
        air_quality=None  # Optional, integrate air quality later if needed
    )
