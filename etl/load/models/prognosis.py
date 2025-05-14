from sqlalchemy import Column, Integer, String

from etl.load.db import Base


class Prognosis(Base):
    __tablename__ = 'prognosis'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
