import asyncio
from app.services.activity_service import filter_activities_by_weather
from app.services.weather_service import get_weather_for_city

import pytest

@pytest.mark.asyncio
async def test_weather_service():
    weather = await get_weather_for_city("Paris")
    assert weather.temperature is not None
    assert weather.condition is not None
