from sqlalchemy import Column, Integer, ForeignKey

from etl.load.db import Base


class CountryPopulation(Base):
    __tablename__ = 'country_populations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)
    age_group_id = Column(Integer, ForeignKey('age_groups.id'), nullable=False)
    amount = Column(Integer, nullable=False)
