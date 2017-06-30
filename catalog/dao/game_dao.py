from sqlalchemy.sql import text
from sqlalchemy.orm import joinedload

from flask import session

from catalog.models.game import Game
from catalog.models.user import User
from catalog.dao.base_dao import BaseDao, transacted
from catalog.services.user_service import UserService


class GameDao(BaseDao):
    """ Manages data access for Game entities. """

    INC_QUERY = 'UPDATE Game SET views = views + 1 WHERE id = :gid'

    def find_all(self):
        return self.session.query(Game).order_by(Game.name)

    def find_by_id(self, gid, join_category=False):
        query = self.session.query(Game)

        if join_category:
            query = query.options(joinedload(Game.category, innerjoin=True))

        return query.get(gid)

    @transacted
    def merge(self, game):
        self.associated_user(game)
        self.session.merge(game)

    def find_by_category(self, c, limit=0):
        query = self.session.query(Game).filter(Game.category == c)

        if limit:
            query = list(query.limit(limit))
        else:
            query = query.all()

        return query

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

    def associated_user(self, game):

        if 'user' in session:
            user = session['user']
            game.user = UserService().fetch(User.build(user))
        else:
            raise Exception("No valid user is in session")
