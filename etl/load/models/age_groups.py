from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AgeGroup(Base):
    __tablename__ = 'age_groups'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    range_start = Column(Float, nullable=True)
    range_end = Column(Float, nullable=True)
