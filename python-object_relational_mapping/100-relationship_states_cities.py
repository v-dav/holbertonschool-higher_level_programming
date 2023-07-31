#!/usr/bin/python3
"""A script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    """Create an engine"""
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """Create the tables in the database"""
    Base.metadata.create_all(engine)

    """Create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Insert new data to the database table"""
    state1 = State(name="California")
    city1 = City(name="San Francisco", state=state1)
    session.add_all([state1, city1])
    session.commit()

    """Close the session"""
    session.close()
