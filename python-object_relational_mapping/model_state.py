#!/usr/bin/python3
""" Task 6 """
import Column from sqlalchemy
import Integer from sqlalchemy
import String from sqlalchemy
import declarative_base from sqlalchemy.ext.declarative


Base = declarative_base()


class State(Base):
    """ Class for state, location for DB """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False,
                autoimcrement="auto",
                unique=True)
    name = Column(String(128), nullable=False)
