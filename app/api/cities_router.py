from fastapi import APIRouter

from ..database.db import engine
from ..schemas.schema import MostCityResponse
from ..services.cities_service import get_most_common_city

cities_router = APIRouter()


@cities_router.get("/most_common_city", response_model=MostCityResponse)
def most_common_city():
    """
    Получает наиболее часто встречающийся город из базы данных.

    Возвращает:
        MostCityResponse: Объект Pydantic, содержащий информацию о городе
        и количестве его упоминаний.
    """
    city, count = get_most_common_city(engine)
    return MostCityResponse(city=city, count=count)
