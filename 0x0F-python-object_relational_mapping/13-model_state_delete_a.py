#!/usr/bin/python3
"""
 a script that deletes all State objects with
 a name containing the letter a from the database hbtn_0e_6_usa
 Your script should take 3 arguments:
 mysql username, mysql password and database name
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # retrievses MySQL credentials and database name
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    dtbsengine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    # Create Session class
    Session = sessionmaker(bind=dtbsengine)

    # Createsession instance
    dtbssession = Session()

    # all Query State objects that contain the letter 'a'
    rslts = dtbssession.query(State).filter(State.name.like('%a%')).all()

    for rslt in rslts:
        dtbssession.delete(rslt)
    dtbssession.commit()

    # Close
    dtbssession.close()
