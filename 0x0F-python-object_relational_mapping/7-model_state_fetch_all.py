#!/bin/usr/python3
""""    All states via SQLAlchemy   """

if __name__ == "__main__":

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import inspect

def list_states(username, password, database):
    # Create engine
    engine = create_engine(f'mysql://{username}:{password}@localhost/{database}')
    
    # Import State and Base from model_state
    from model_state import Base, State
    
    # Create Base metadata
    Base.metadata.create_all(engine)
    
    # Inspect the table
    inspector = inspect(engine)
    table = inspector.get_table('states')
    
    # Get all rows from the table
    rows = table.select().execute()
    
    # Print the results
    for row in rows:
        print(row)
    

