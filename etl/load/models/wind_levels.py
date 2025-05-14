from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WindLevel(Base):
    __tablename__ = 'wind_levels'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    range_start = Column(Float, nullable=True)
    range_end = Column(Float, nullable=True)
