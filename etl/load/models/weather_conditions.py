from sqlalchemy import Column, Integer, String

from etl.load.db import Base


class WeatherCondition(Base):
    __tablename__ = 'weather_conditions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    condition = Column(String, nullable=False)
