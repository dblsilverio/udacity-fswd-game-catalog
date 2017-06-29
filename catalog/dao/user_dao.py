from catalog.dao.base_dao import BaseDao, transacted
from catalog.models.user import User


class UserDao(BaseDao):
    """ Manages user data """

    @transacted
    def merge(self, user):
        return self.session.merge(user)

    def find_user(self, user):
        return self.session.query(User).filter(User.email == user.email).first()
