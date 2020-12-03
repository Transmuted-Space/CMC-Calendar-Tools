from sqlalchemy import Integer, String, Datetime
from sqlalchemy.orm import declarative_base

Base = declaritive_base()

class Subscribers(Base):
    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True)
    email = Column(String)