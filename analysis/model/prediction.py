from sqlalchemy import Column, Integer, DATETIME

from etl.load.db import Base


class Prediction(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DATETIME, nullable=False)
    real_diagnosis_count = Column(Integer, nullable=False)
    predicted_diagnosis_count = Column(Integer, nullable=False)
