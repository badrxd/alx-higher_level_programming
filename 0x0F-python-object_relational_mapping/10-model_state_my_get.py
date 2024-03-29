#!/usr/bin/python3
'''
script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
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
    state = session.query(State).filter(State.name == argv[4]).first()

    # print index if a State was found
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Close the session
    session.close()
