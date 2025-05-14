from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Timezone(Base):
    __tablename__ = 'timezones'

    id = Column(Integer, primary_key=True, autoincrement=True)
    timezone = Column(String, nullable=False)
