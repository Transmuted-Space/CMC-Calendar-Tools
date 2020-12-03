from sqlalchemy import Integer, String, Datetime, Float
from calendar_injest import Base


class Events(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    datetime = Column(Datetime)
    event_name = Column(String)
    status = Column(String)
    leader = Column(String)
    co_leader = Column(String)
    group_price = Column(Float)
    non_group_price = Column(Float)
    available_participants = Column(Integer)
    event_type = Column(String)
