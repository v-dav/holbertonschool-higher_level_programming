#!/usr/bin/python3
"""A script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""

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

    """Insert new data into the database table"""
    state1 = State(name="Louisiana")
    session.add(state1)
    session.commit()

    """Query the database and format output"""
    state = session.query(State).filter(State.name == "Louisiana").first()
    print(state.id)

    """Close the session"""
    session.close()
