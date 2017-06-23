from datetime import datetime
from catalog.infra.db_factory import Base
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Game(Base):
    """ An entity to map a single game. """
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False, unique=True)
    developer = Column(String(30), nullable=False)
    publisher = Column(String(30), nullable=False)
    platform = Column(String(10), nullable=False) #need table
    thumb = Column(String(500), nullable=True)
    synopsis = Column(Text, nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category", backref="games")
    created = Column(DateTime, default=datetime.now())
