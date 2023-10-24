#!/usr/bin/python3
""" Task 7 """
import sys
from model_state import Base, model_state
from sqlalchemy.orm import (sessionmaker)
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for item in session.query(State).order_by(State.id):
        print("{}: {}".format(item.id, item.name))

    """ Close connection """
    session.close()
