#!/usr/bin/python3
"""A script that changes the name of a
State object from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    """Create an engine"""
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """Create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query the database and update data"""
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()

    """Close the session"""
    session.close()
