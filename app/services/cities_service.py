from sqlalchemy.engine import Engine

from app.sql.queries import GET_MOST_COMMON_CITY


def get_most_common_city(engine: Engine):
    """
    Извлекает наиболее часто встречающийся город и его количество из базы данных.

    Параметры:
        engine (Engine): Объект Engine от SQLAlchemy, который используется
                         для подключения к базе данных и выполнения запроса.

    Возвращает:
        tuple: Кортеж, содержащий наименование города (str) и количество его упоминаний (int).
    """
    with engine.begin() as connection:
        result = connection.execute(GET_MOST_COMMON_CITY)
    city, count = result.first()
    return city, count
