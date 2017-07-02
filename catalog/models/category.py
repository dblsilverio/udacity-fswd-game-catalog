from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from catalog.infra.db_factory import Base


class Category(Base):
    """ An entity that aggregates games with common features and aspects. """
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref="categories", lazy="joined")

    def top_games(self, top):
        """ Slices game list to top N required. """
        return self.games[0:top]

    def to_json(self, load_game=True):
        """ Provides JSON representation. """
        me_as_json = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'link': "/category/%d" % self.id
        }

        if load_game:
            me_as_json['games'] = {
                'quantity': len(self.games),
                'available_titles': [{
                    'name': g.name,
                    'link': "/game/%d.json" % g.id
                }
                                     for g in self.games]
            }

        return me_as_json

    def to_short_json(self, load_games=True):
        """ Provides a shorter JSON representation. """
        j = self.to_json(load_games)
        j.pop('description', None)

        return j
