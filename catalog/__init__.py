from flask import Flask
from uuid import uuid4
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
app.secret_key = str(uuid4())

Base = declarative_base()
engine = create_engine('sqlite:///game-catalog.db')

import catalog.routes.main
import catalog.routes.category
import catalog.routes.game


Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
