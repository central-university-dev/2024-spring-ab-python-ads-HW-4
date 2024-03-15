from sqlalchemy import TextClause, text

from app.config.config import settings


def load_sql(file_path: str) -> TextClause:
    """Manager to load and read an SQL file."""
    with open(file_path, "r") as file:
        return text(file.read())


INIT_DB_QUERY = load_sql(settings.init_sql)
GET_MOST_COMMON_CITY = load_sql(settings.call_proc)
CREATE_STORED_PROC = load_sql(settings.init_proc)
