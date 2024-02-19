#!/usr/bin/python3
"""
a script that changes the name of a State object in the database
 taking 3 arguments: mysql username, mysql password and database name
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
    # Create a Session class
    Session = sessionmaker(bind=dtbsengine)

    # Create a Sessioninstance
    dtbssession = Session()

    # Retrieve the State object
    rslt = dtbssession.query(State).get(2)

    # Change the name of the State
    # to a new name
    rslt.name = "New Mexico"

    # Commit the new changes to the dtbs
    dtbssession.commit()

    # Close
    dtbssession.close()
