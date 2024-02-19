#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a from database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    Entry point of the script.
    Main execution block
    Establishes a connection to the database
    using provided credentials
    """

    # Get MySQL credentials and database name
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    dtbsengine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    # Create Session class
    Session = sessionmaker(bind=dtbsengine)

    # Create Session instance
    dtbssession = Session()

    reslts = dtbssession.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)\
        .all()

    # Print the retrieved State objects
    for rslt in reslts:
        print(f"{rslt.id}: {rslt.name}")

    # Close
    dtbssession.close()
