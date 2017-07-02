""" Module responsible for managing database configuration. """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql+psycopg2://catalog:catalog@127.0.0.1:5432'
                       '/catalog')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)


def create():
    """ Create tables in the target engine. """
    Base.metadata.create_all(engine)
