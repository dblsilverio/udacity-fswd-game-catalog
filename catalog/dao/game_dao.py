from catalog.dao.base_dao import BaseDao, transacted
from catalog.models.game import Game


class GameDao(BaseDao):
    """ Manages data access for Game entities. """

    def find_all(self):
        return self.session.query(Game).order_by(Game.name)

    def find_by_id(self, gid):
        return self.session.query(Game).get(gid)

    @transacted
    def merge(self, game):
        self.session.merge(game)

    def find_by_category(self, c):
        return self.session.query(Game).filter(Game.category == c).all()

    @transacted
    def delete(self, game):
        self.session.delete(game)
