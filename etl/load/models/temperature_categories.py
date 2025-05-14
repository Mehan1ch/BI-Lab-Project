from sqlalchemy import Column, Integer, String, Float

from etl.load.db import Base


class TemperatureCategory(Base):
    __tablename__ = 'temperature_categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    range_start = Column(Float, nullable=True)
    range_end = Column(Float, nullable=True)
