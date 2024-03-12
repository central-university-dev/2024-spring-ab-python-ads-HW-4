import datetime
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

user = os.getenv("POSTGRES_USER", "postgres")
password = os.getenv("POSTGRES_PASSWORD", "postgres")
engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@db/postgres", echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
