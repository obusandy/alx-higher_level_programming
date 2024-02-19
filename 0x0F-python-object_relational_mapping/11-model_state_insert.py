#!/usr/bin/python3
"""
Script that adds the State object "Louisiana"
to the database hbtn_0e_6_usa
script should take 3 arguments:
mysql username, mysql password and database name
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # retrieve MySQL credentials
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    dtbsengine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    # Create a Sessionclass
    Session = sessionmaker(bind=dtbsengine)

    # Create a Sessioninstance
    dtbssession = Session()

    # Create a new State object
    current_state = State(name="Louisiana")

    dtbssession.add(current_state)
    dtbssession.commit()

    # Print the id of the newly created State
    print(current_state.id)

    # Close
    dtbssession.close()
