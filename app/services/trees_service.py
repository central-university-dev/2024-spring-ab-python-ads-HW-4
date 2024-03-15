import requests
from fastapi import HTTPException

from app.database.db_utils import insert_request_log
from app.schemas.schema import RequestBody


def fetch_trees_count(data: RequestBody) -> int:
    """
    Получает количество деревьев в определённом городе, используя Overpass API.

    Параметры:
        data (RequestBody): Pydantic модель, содержащая город, страну и год.

    Возвращает:
        int: Количество деревьев в указанном городе.

    Исключения:
        HTTPException: Возникает, если данные о деревьях не найдены.
    """
    url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json][timeout:25];
    area[name="{data.city}"][admin_level=8];
    (node["natural"="tree"](area);
     way["natural"="tree"](area);
     rel["natural"="tree"](area);
    );
    out count;
    """

    response = requests.get(url, params={"data": query})
    response.raise_for_status()
    trees_count = response.json().get("elements", [{}])[0].get("tags", {}).get("nodes")

    if trees_count is None:
        raise HTTPException(status_code=404, detail="Cannot find trees data")

    return trees_count


def log_tree_count(data: RequestBody, trees_count: int):
    """
    Логирует количество деревьев в базу данных.
    """
    insert_request_log(data, trees_count)
