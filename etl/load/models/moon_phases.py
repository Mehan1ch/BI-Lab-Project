from sqlalchemy import Column, Integer, String

from etl.load.db import Base


class MoonPhase(Base):
    __tablename__ = 'moon_phases'

    id = Column(Integer, primary_key=True, autoincrement=True)
    phase = Column(String, nullable=False)
