from catalog.dao.base_dao import BaseDao, transacted
from catalog.models.category import Category


class CategoryDao(BaseDao):
    """ Manages data access for Category entities. """

    def find_all(self):
        return self.session.query(Category).order_by(Category.name)

    def find_by_id(self, cid):
        return self.session.query(Category).get(cid)

    @transacted
    def merge(self, category):
        self.session.merge(category)


