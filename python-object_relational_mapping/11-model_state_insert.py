#!/usr/bin/python3
""" Task 11 """
import sys
from model_state import Base, State
from sqlalchemy.orm import (sessionmaker)
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    item = session.query(State).filter_by(name="Louisiana").first()
    print("{}".format(item.id))
    
    """ Close session """
    session.commit()
    session.close()
