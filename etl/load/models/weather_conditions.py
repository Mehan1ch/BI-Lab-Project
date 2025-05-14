from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WeatherCondition(Base):
    __tablename__ = 'weather_conditions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    condition = Column(String, nullable=False)
