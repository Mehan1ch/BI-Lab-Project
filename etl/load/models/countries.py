from sqlalchemy import Column, Integer, String

from etl.load.db import Base


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    total_population = Column(Integer, nullable=False)
