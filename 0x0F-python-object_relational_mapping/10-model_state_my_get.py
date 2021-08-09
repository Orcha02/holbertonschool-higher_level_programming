#!/usr/bin/python3
"""
Script prints State object with name passed as argument from db: hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    mysql_usr = argv[1]
    mysql_pswd = argv[2]
    db_name = argv[3]
    state_result = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_usr, mysql_pswd, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    my_state = session.query(State).filter(State.name == state_result).first()

    print(my_state.id if my_state else "Not found")  # Python ternary
