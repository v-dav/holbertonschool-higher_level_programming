#!/usr/bin/python3
"""A script that prints all City objects from the database hbtn_0e_14_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """Create an engine"""
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """Create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query the database and format output"""
    cities = session.query(State, City).join(State).order_by(City.id)
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    """Close the session"""
    session.close()
