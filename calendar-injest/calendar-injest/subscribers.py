from sqlalchemy import Integer, String, Datetime
from calendar_injest import Base


class Subscribers(Base):
    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True)
    email = Column(String)