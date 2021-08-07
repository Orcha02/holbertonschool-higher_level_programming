#!/usr/bin/python3
"""
Python file that contains the class definition of a State and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """Inherits from Base Tips and links to the MySQL table states"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

# cities = relationship("City")-> cities must represent a relationship with
#                                 the class City
# backref="state"-> The reference from a City object to his State will be
#                   named state
# cascade="all, delete"-> If the State object is deleted, all linked City
#                         objects must be automatically deleted.
