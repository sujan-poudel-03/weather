from fastapi import APIRouter
from app.services.weather_services import get_weather_by_city_and_date

router = APIRouter()

@router.get("/weather")
async def get_weather(city: str, date: str):
    return await get_weather_by_city_and_date(city, date)
