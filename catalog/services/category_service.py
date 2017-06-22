from catalog.dao.category_dao import CategoryDao


class CategoryService:

    def __init__(self):
        self.dao = CategoryDao()

    def new(self, category):
        try:
            self.dao.merge(category)
            return True
        except Exception as e:
            print "Error persisting category: %s" % e.message
            return False

    def find_by(self, cid):
        return self.dao.find_by_id(cid)

    def all(self):
        return self.dao.find_all()
