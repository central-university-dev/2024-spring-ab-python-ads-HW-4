import requests
from fastapi import APIRouter, HTTPException

from app.services.trees_service import fetch_trees_count, log_tree_count

from ..schemas.schema import RequestBody, TreeCountResponse

trees_router = APIRouter()


@trees_router.post("/trees", response_model=TreeCountResponse)
def get_trees(data: RequestBody):
    """
    Обрабатывает POST-запрос для получения количества деревьев в указанном городе.

    Параметры:
        data (RequestBody): Pydantic модель, содержащая данные запроса, включая
                            название города, страну и год.

    Возвращает:
        TreeCountResponse: Модель Pydantic с информацией о городе, стране, годе
                           и количестве деревьев.

    Исключения:
        HTTPException: Возвращается в случае неудачного запроса к внешнему API.
    """
    try:
        trees_count = fetch_trees_count(data)
    except requests.RequestException as e:
        raise HTTPException(
            status_code=400, detail=f"Error contacting Overpass API: {e}"
        )

    log_tree_count(data, trees_count)

    return TreeCountResponse(
        city=data.city, country=data.country, year=data.year, trees_count=trees_count
    )
