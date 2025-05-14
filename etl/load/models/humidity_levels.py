from sqlalchemy import Column, Integer, String, Float

from etl.load.db import Base


class HumidityLevel(Base):
    __tablename__ = 'humidity_levels'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    range_start = Column(Float, nullable=True)
    range_end = Column(Float, nullable=True)
