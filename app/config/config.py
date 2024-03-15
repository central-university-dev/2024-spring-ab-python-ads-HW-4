from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Конфигурационные настройки приложения, загружаемые из файла .env.

    Атрибуты:
        database_url (str): Строка подключения к базе данных.
        init_sql (str): Путь к SQL файлу для инициализации базы данных.
        init_proc (str): Путь к SQL файлу, содержащему хранимые процедуры.
        call_proc (str): Путь к SQL файлу для вызова хранимых процедур.

    Класс Config:
        env_file: Определяет расположение файла .env, откуда загружаются настройки.
    """

    database_url: str
    init_sql: str
    init_proc: str
    call_proc: str

    class Config:
        env_file = ".env"


settings = Settings()
