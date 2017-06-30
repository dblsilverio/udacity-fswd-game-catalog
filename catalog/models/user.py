from sqlalchemy import Column, String, Integer
from catalog.infra.db_factory import Base


class User(Base):
    """ An entity to map a catalog user. """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(70), nullable=False)
    email = Column(String(70), nullable=False)

    def to_json(self):
        """ Provides JSON representation. """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

    @staticmethod
    def build(user_info):
        """ Build an User with user info provided. """
        return User(name=user_info['name'], email=user_info['email'])
