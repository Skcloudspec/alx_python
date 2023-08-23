#!/usr/bin/python3
"""Script that lists all State objects containing the letter 'a' from the database"""
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

    # Fetch all State objects containing the letter 'a' and sort by id
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
