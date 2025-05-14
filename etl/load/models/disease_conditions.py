from sqlalchemy import Column, Integer, String

from etl.load.db import Base


class DiseaseCondition(Base):
    __tablename__ = 'disease_conditions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
