from sqlalchemy import Column, Integer, Float, ForeignKey, DATETIME, TIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True, autoincrement=True)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    last_updated_epoch = Column(Integer, nullable=False)
    last_updated = Column(DATETIME, nullable=False)
    temperature_celsius = Column(Float, nullable=True)
    temperature_category_id = Column(Integer, ForeignKey('temperature_categories.id'), nullable=True)
    weather_condition_id = Column(Integer, ForeignKey('weather_conditions.id'), nullable=True)
    wind_kph = Column(Float, nullable=True)
    wind_level_id = Column(Integer, ForeignKey('wind_levels.id'), nullable=True)
    wind_degree = Column(Integer, nullable=True)
    wind_direction_id = Column(Integer, ForeignKey('wind_directions.id'), nullable=True)
    pressure_mb = Column(Float, nullable=True)
    precip_mm = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)
    humidity_level_id = Column(Integer, ForeignKey('humidity_levels.id'), nullable=True)
    cloud = Column(Integer, nullable=True)
    feels_like_celsius = Column(Float, nullable=True)
    visibility_km = Column(Float, nullable=True)
    uv_index = Column(Float, nullable=True)
    gust_kph = Column(Float, nullable=True)
    air_quality_us_epa_index = Column(Float, nullable=True)
    air_quality_gb_defra_index = Column(Float, nullable=True)
    sunrise = Column(TIME, nullable=True)
    sunset = Column(TIME, nullable=True)
    moonrise = Column(TIME, nullable=True)
    moonset = Column(TIME, nullable=True)
    moon_phase_id = Column(Integer, ForeignKey('moon_phases.id'), nullable=True)
    moon_illumination = Column(Float, nullable=True)
