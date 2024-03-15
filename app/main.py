from fastapi import FastAPI

from app.api.cities_router import cities_router
from app.api.trees_router import trees_router
from app.database.db import init_db

app = FastAPI()


@app.on_event("startup")
def startup_event():
    """
    Инициализирует базу данных при запуске приложения.

    Он вызывает функцию init_db, которая отвечает за инициализацию структуры базы данных,
    включая создание таблиц и загрузку начальных данных.
    """

    init_db()


app.include_router(trees_router)
app.include_router(cities_router)
