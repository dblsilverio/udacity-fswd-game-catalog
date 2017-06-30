from catalog.dao.category_dao import CategoryDao


class CategoryService:
    """ Provider of common services and operations for a Category entity. """

    def __init__(self):
        self.dao = CategoryDao()

    def new(self, category):
        try:
            self.dao.merge(category)
            return True
        except Exception as e:
            print "Error persisting category: %s" % e.message
            return False

    def find_by_id(self, cid, join_games=False):
        return self.dao.find_by_id(cid, join_games)

    def all(self):
        return self.dao.find_all()

    def delete(self, category):
        self.dao.delete(category)
