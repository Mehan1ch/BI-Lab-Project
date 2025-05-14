from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WindDirection(Base):
    __tablename__ = 'wind_directions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    direction = Column(String, nullable=False)
