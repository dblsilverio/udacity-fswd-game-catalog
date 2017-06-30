from sqlalchemy.orm import joinedload

from catalog.dao.base_dao import BaseDao, transacted
from catalog.models.category import Category


class CategoryDao(BaseDao):
    """ Manages data access for Category entities. """

    def find_all(self):
        """ Fetches all Categories. """
        return self.session.query(Category).order_by(Category.name)

    def find_by_id(self, cid, join_games=False):
        """ Find a category by its id number. """
        query = self.session.query(Category)

        if join_games:
            query = query.options(joinedload(Category.games, innerjoin=True))

        return query.filter_by(id=cid).first()

    @transacted
    def merge(self, category):
        """ Insert/Merges a category. """
        self.session.merge(category)

    @transacted
    def delete(self, category):
        """ Deletes a category and all associated games. """
        games = category.games

        for game in games:
            self.session.delete(game)

        self.session.delete(category)
