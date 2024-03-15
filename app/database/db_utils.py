import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.config.config import settings
from app.database.models import RequestsLog
from app.schemas.schema import RequestBody
from app.sql.queries import CREATE_STORED_PROC, INIT_DB_QUERY

engine = create_engine(settings.database_url)


def init_stored_proc() -> None:
    """
    Инициализирует хранимые процедуры в базе данных.

    Выполняет SQL-запрос для создания хранимых процедур из предопределенной строки SQL.
    Логирует успешное создание хранимой процедуры.
    """
    with engine.begin() as connection:
        connection.execute(CREATE_STORED_PROC)
    logging.info("Stored procedure created successfully.")


def init_tables_from_sql() -> None:
    """
    Инициализирует таблицы в базе данных с использованием SQL-запроса.

    Выполняет SQL-запрос для создания таблиц из предопределенной строки SQL.
    Логирует успешное создание таблиц.
    """
    with engine.connect() as connection:
        connection.execute(INIT_DB_QUERY)
    logging.info("Tables have been initialized successfully.")


def insert_request_log(data: RequestBody, trees_count: int) -> None:
    """
    Записывает лог запроса в базу данных.

    Создает и добавляет запись лога в таблицу RequestsLog, используя данные запроса и количество деревьев.
    Фиксирует изменения в базе данных и логирует успешное добавление записи.

    Параметры:
        data (RequestBody): Данные запроса, включая город, страну и год.
        trees_count (int): Количество деревьев, полученное от API.
    """
    with Session(engine) as session:
        new_log = RequestsLog(
            city=data.city,
            country=data.country,
            year=data.year,
            trees_count=trees_count,
        )
        session.add(new_log)
        session.commit()
    logging.info("Insert request log successfully.")
