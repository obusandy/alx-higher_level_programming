#!/usr/bin/python3
""" 
a script that prints the first State object
from the database hbtn_0e_6_usa
script should take 3 arguments:
mysql username, mysql password and database name
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get MySQL credentials
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    dtbsengine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    # Create a Session class
    Session = sessionmaker(bind=dtbsengine)

    dtbssession = Session()

    # Retrieve the first State object
    head_state = dtbssession.query(State).order_by(State.id).first()

    if head_state:
        # Print the State object
        print(f"{head_state.id}: {head_state.name}")
    else:
        print("Nothing")

    # Close
    dtbssession.close()
