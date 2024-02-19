#!/usr/bin/python3
"""
Defines the State class and the Base instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Define custom metadata
mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
     Represents a state with an id and name.
    """
    # Table name
    __tablename__ = 'states'
    # columns
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
