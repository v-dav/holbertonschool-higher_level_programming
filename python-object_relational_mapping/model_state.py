#!/usr/bin/python3
"""A python file that contains the class definition of a State
and an instance Base = declarative_base()"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys

engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]))

Base = declarative_base()


class State(Base):
    """An object representation of the table States in our database"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
