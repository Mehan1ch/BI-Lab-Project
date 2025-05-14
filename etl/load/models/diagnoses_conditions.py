from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DiagnosisCondition(Base):
    __tablename__ = 'diagnoses_conditions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    diagnosis_id = Column(Integer, ForeignKey('diagnoses.id'), nullable=False)
    disease_condition_id = Column(Integer, ForeignKey('disease_conditions.id'), nullable=False)
