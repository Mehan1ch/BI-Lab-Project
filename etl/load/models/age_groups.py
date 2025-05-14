from sqlalchemy import Column, Integer, String

from etl.load.db import Base


class AgeGroup(Base):
    __tablename__ = 'age_groups'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    range_start = Column(Integer, nullable=True)
    range_end = Column(Integer, nullable=True)
