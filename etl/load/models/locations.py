from sqlalchemy import Column, Integer, Float, ForeignKey, String

from etl.load.db import Base


class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    timezone_id = Column(Integer, ForeignKey('timezones.id'), nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)
