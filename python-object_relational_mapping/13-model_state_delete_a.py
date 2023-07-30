#!/usr/bin/python3
"""A script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa"""

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

    """Query the database and remove data"""
    states = session.query(State).filter(State.name.ilike("%a%")).all()
    for state in states:
        session.delete(state)
    session.commit()

    """Close the session"""
    session.close()
