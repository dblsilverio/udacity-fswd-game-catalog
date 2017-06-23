from catalog.dao.game_dao import GameDao

class GameService:
    """ Provider of common services and operations for a Game entity. """

    def __init__(self):
        self.dao = GameDao()

    def new(self, game):
        try:
            self.dao.merge(game)
            return True
        except Exception as e:
            print "Error persisting game: %s" % e.message
            return False

    def find_by(self, gid):
        return self.dao.find_by_id(gid)

    def find_by_category(self, c):
        return self.dao.find_by_category(c)

    def all(self):
        return self.dao.find_all()
