from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DiseaseCondition(Base):
    __tablename__ = 'disease_conditions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
