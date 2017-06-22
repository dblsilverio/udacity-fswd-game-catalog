from sqlalchemy import Column, String, Integer, Text
from catalog.__init__ import Base


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(Text, nullable=False)
