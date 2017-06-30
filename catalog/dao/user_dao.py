from catalog.dao.base_dao import BaseDao, transacted
from catalog.models.user import User


class UserDao(BaseDao):
    """ Manages user data """

    @transacted
    def merge(self, user):
        """ Inserts/merges a user. """
        return self.session.merge(user)

    def find_user(self, user):
        """ Finds users by email. """
        return self.session.query(User).filter(User.email == user.email)\
            .first()
