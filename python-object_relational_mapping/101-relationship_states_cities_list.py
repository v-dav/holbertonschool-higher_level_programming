#!/usr/bin/python3
"""a script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""

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

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in sorted(state.cities, key=lambda city: city.id):
            print("    {}: {}".format(city.id, city.name))

    session.close()
