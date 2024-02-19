#!/usr/bin/python3
""" 
Write a script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
Your script should take 3 arguments:
mysql username, mysql password and database name

"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    dtbsengine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(dtbsengine)
    Session = sessionmaker(bind=dtbsengine)
    dtbssession = Session()
    # prints all State objects
    for instance in dtbssession.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
        for city_instnc in instance.cities:
            print("    ", end="")
            print(city_instnc.id, city_instnc.name, sep=": ")
