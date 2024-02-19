#!/usr/bin/python3
""" 
Write a script that lists all City objects from the database hbtn_0e_101_usa
script should take 3 arguments:
mysql username, mysql password and database name
using the module SQLAlchemy
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    # entry point
    # Configure a session class bound to the engine
    dtbsengine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(dtbsengine)
    Session = sessionmaker(bind=dtbsengine)
    dtbssession = Session()
     # Access associated City objects using the 'cities' relationship
    for instnc in dtbssession.query(State).order_by(State.id):
        for city_instnc in instnc.cities:
            # Print city details along with the corresponding state name
            print(city_instnc.id, city_instnc.name, sep=": ", end="")
            print(" -> " + instnc.name)
