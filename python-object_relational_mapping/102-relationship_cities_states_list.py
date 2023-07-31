#!/usr/bin/python3
"""A script that lists all City objects from the database hbtn_0e_101_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    """Create an engine"""
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """Create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query the database and format output"""
    all_cities = session.query(City).order_by(City.id)
    for city in all_cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    """Close the session"""
    session.close()
