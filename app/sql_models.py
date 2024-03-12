from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Requests(Base):
    __tablename__ = "requests"

    req_id = Column(Integer, primary_key=True, autoincrement=True)
    req_time = Column(DateTime, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
