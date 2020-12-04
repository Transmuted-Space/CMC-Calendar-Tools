#!/usr/bin/env python3.8

from sqlalchemy import Integer, String, Text Datetime, Float
from sqlalchemy.orm import declarative_base

Base = declaritive_base()

class Events(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    group = Column(String)
    event_title = Column(String)
    start_time = Column(Datetime)
    end_time = Column(Datetime)
    status = Column(String)
    leader = Column(String)
    co_leader = Column(String)
    member_price = Column(Float)
    non_member_price = Column(Float)
    group_price = Column(Float)
    non_group_price = Column(Float)
    available_participants = Column(Integer)
    event_type = Column(String)
    location = Column(Text)
    contact_email = Column(String)
    details = Column(Text)
    registration_link = Column(String)