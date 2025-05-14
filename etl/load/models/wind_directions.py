from sqlalchemy import Column, Integer, String

from etl.load.db import Base


class WindDirection(Base):
    __tablename__ = 'wind_directions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    direction = Column(String, nullable=False)
