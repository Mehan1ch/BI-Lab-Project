from sqlalchemy import Column, Integer, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Diagnosis(Base):
    __tablename__ = 'diagnoses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    age = Column(Integer, nullable=True)
    age_group_id = Column(Integer, ForeignKey('age_groups.id'), nullable=True)
    gender = Column(Boolean, nullable=False)
    temperature_celsius = Column(Float, nullable=True)
    temperature_category_id = Column(Integer, ForeignKey('temperature_categories.id'), nullable=True)
    humidity = Column(Float, nullable=True)
    humidity_level_id = Column(Integer, ForeignKey('humidity_levels.id'), nullable=True)
    wind_kph = Column(Float, nullable=True)
    wind_level_id = Column(Integer, ForeignKey('wind_levels.id'), nullable=True)
    prognosis_id = Column(Integer, ForeignKey('prognosis.id'), nullable=True)
