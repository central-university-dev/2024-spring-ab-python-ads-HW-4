from .db_utils import engine, init_stored_proc, init_tables_from_sql
from .models import Base


def init_db():
    """
    Инициализирует базу данных для приложения.

    Эта функция отвечает за начальную настройку базы данных. Она создает таблицы,
    основываясь на определениях моделей SQLAlchemy
    """
    Base.metadata.create_all(engine)
    init_stored_proc()
    init_tables_from_sql()
