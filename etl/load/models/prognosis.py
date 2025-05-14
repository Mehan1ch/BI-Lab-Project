from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Prognosis(Base):
    __tablename__ = 'prognosis'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
