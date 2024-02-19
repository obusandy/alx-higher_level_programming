#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class State(Base):
    """ Represents a table class 
    within the database."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    cityname = Column(String(128), nullable=False)
