"""main function"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import psycopg2
from psycopg2.extensions import connection as PgConnection
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Получение переменных окружения
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

app = FastAPI()

class TreeRequest(BaseModel):
    """Модель запроса для получения количества деревьев."""
    city: str
    country: str
    year: int

def log_request(city: str, country: str, year: int, tree_count: int) -> None:
    """Логирует информацию о запросе в базу данных.

    Args:
        city: Название города.
        country: Название страны.
        year: Год запроса.
        tree_count: Количество деревьев, найденных в запросе.
    """
    connection: PgConnection = psycopg2.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, database=DB_NAME)
    cursor = connection.cursor()
    insert_query = """INSERT INTO tree_requests_log (city, country, year, tree_count, query_date) VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(insert_query, (city, country, year, tree_count, datetime.now()))
    connection.commit()
    cursor.close()
    connection.close()

@app.post("/trees")
async def get_tree_count(request: TreeRequest) -> dict:
    """Возвращает количество деревьев в указанном городе и стране, используя Overpass API.

    Args:
        request: Объект запроса, содержащий город, страну и год.

    Returns:
        Словарь с информацией о городе, стране, годе и количестве деревьев.
    """
    overpass_url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    area[name="{request.city}"][is_in:country="{request.country}"];
    (node["natural"="tree"](area);
    );
    out count;
    """
    response = requests.get(overpass_url, params={'data': query})
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Error fetching data from OpenStreetMap")

    data = response.json()
    try:
        tree_count = int(data['elements'][0]['tags']['count'])
    except (IndexError, KeyError):
        raise HTTPException(status_code=500, detail="Could not parse the response from OpenStreetMap")

    log_request(request.city, request.country, request.year, tree_count)

    return {"city": request.city, "country": request.country, "year": request.year, "trees_count": tree_count}