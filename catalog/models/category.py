from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import relationship
from catalog.infra.db_factory import Base


class Category(Base):
    """ An entity that aggregates games with common features and aspects. """
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(Text, nullable=False)
