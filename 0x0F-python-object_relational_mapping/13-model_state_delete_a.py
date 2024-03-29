#!/usr/bin/python3
'''
script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
'''
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # get first state
    states = session.query(State).filter(State.name.like('%a%')).all()

    # delete any state have letter a.
    for state in states:
        session.delete(state)

    session.commit()

    # Close the session
    session.close()
