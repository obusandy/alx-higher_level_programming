#!/usr/bin/python3
"""
Script that prints the State object with the name
passed as an argument from the database hbtn_0e_6_usa
script should take 4 arguments:
mysql username, mysql password, database name and
state name to search (SQL injection free)
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    dtbsengine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    # Create a Session class
    Session = sessionmaker(bind=dtbsengine)

    # Create Session instance
    dtbssession = Session()

    rslt = dtbssession.query(State).filter(State.name == state_name).first()

    if rslt:
        # Print the id of retrieved State object
        print(rslt.id)
    else:
        print("Not found")

    # Close
    dtbssession.close()
