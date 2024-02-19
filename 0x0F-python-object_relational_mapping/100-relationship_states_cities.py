#!/usr/bin/python3
"""
Creates  State "California" with City "San Francisco" from a DB
Improve the files model_city.py and model_state.py,
and save them as relationship_city.py and relationship_state.py:

"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """
    Entry point
    Main execution block of the program
    """
    dtbsengine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(dtbsengine)

    Session = sessionmaker(bind=dtbsengine)
    session = Session()

    currentState = State(name='California')
    currentCity = City(name='San Francisco')
    currentState.cities.append(currentCity)

    session.add(currentState)
    session.add(currentCity)
    session.commit()
