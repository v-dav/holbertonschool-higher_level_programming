#!/usr/bin/python3
"""A script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """Create engine"""
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """Create session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query database and format output"""
    states = session.query(State)\
        .filter(State.name.ilike("%a%"))\
        .order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))

    """Close the session"""
    session.close()
