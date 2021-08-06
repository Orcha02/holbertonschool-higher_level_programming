#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
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
    my_states = session.query(State).order_by(State.id).all()

    for state_instance in my_states:
        print("{}: {}".format(state_instance.id, state_instance.name))

# pool_pre_ping=True-> Checks if the connection is still alive
#                      and re-connects if not
# create_engine-> Produces an Engine object based on a URL
# sessionmaker-> Session object to handle database
