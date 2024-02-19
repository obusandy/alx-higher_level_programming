#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa.

"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get MySQL credentials
    """
    Returns:
        sqlalchemy.orm.session.Session:
        A configured SQLAlchemy session object.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    dtbsengine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    # Create Session class
    Session = sessionmaker(bind=dtbsengine)

    dtbssession = Session()
    rslts = dtbssession.query(State).order_by(State.id).all()

    # Print the resulting state
    for rslt in rslts:
        print(f"{rslt.id}: {rslt.name}")
