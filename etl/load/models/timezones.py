from sqlalchemy import Column, Integer, String

from etl.load.db import Base


class Timezone(Base):
    __tablename__ = 'timezones'

    id = Column(Integer, primary_key=True, autoincrement=True)
    timezone = Column(String(255), nullable=False)
