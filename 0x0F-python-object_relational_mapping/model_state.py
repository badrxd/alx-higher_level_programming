#!/usr/bin/python3
''' file that contains the class definition of a
State and an instance Base = declarative_base() '''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    '''
    State class that inherits from Base
    Att:
        id : id of state
        name: name of the state
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
