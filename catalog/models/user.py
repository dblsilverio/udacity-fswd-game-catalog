from sqlalchemy import Column, String, Integer
from catalog.infra.db_factory import Base


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(70), nullable=False)
    email = Column(String(70), nullable=False)
