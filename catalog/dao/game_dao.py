from sqlalchemy.sql import text

from catalog.dao.base_dao import BaseDao, transacted
from catalog.models.game import Game


class GameDao(BaseDao):
    """ Manages data access for Game entities. """

    INC_QUERY = 'UPDATE Game SET views = views + 1 WHERE id = :gid'

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

    def find_by_platform(self, plat):
        return self.session.query(Game).filter(Game.platform.like("%%%s%%" %
                                                                  plat))

    def latest(self, batch_num):
        return self.session.query(Game).order_by(Game.created.desc()).limit(
            batch_num)

    def top10(self):
        return self.session.query(Game).order_by(Game.views.desc(),
                                                 Game.name).limit(10)

    @transacted
    def increment(self, gid):
        self.session.execute(text(GameDao.INC_QUERY), {'gid': gid})
