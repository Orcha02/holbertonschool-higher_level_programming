#!/usr/bin/python3
"""
Python file similar to model_state.py named model_city.py
that contains the class definition of a City
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    mysql_usr = argv[1]
    mysql_pswd = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_usr, mysql_pswd, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
