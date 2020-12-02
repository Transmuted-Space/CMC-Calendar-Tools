from sqlalchemy import Integer, String, Datetime
from calendar_injest import Base


class Events(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    event_name = Column(String)
    datetime = Column(Datetime)