from sqlalchemy.orm import joinedload

from catalog.dao.base_dao import BaseDao, transacted
from catalog.models.category import Category


class CategoryDao(BaseDao):
    """ Manages data access for Category entities. """

    def find_all(self):
        return self.session.query(Category).order_by(Category.name)

    def find_by_id(self, cid, join_games=False):
        q = self.session.query(Category)

        if join_games:
            q = q.options(joinedload(Category.games, innerjoin=True))

        return q.filter_by(id=cid).first()

    @transacted
    def merge(self, category):
        self.session.merge(category)

    @transacted
    def delete(self, category):
        games = category.games

        for game in games:
            self.session.delete(game)

        self.session.delete(category)
