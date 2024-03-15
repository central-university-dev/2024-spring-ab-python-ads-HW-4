from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RequestsLog(Base):
    __tablename__ = "requests_log"

    id = Column(Integer, primary_key=True)
    city = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    trees_count = Column(Integer)
