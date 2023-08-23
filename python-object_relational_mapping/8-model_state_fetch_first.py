#!/usr/bin/python3
"""Script that prints the first State object from the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Retrieve MySQL connection credentials
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the first State object
    state = session.query(State).order_by(State.id).first()

    # Print the result
    if state is not None:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
