import os
import time

from catalog.services.request_service import RequestService

from catalog.models.user import User
from catalog.dao.user_dao import UserDao

from catalog.services.utils import picture_age


class UserService:

    PICTURE_PATH = "catalog/static/img/p/%s.jpg"

    def __init__(self):
        self.dao = UserDao()

    def fetch_or_create(self, user_info):
        logged_user = User.build(user_info)
        u = self.dao.find_user(logged_user)

        if not u:
            print "User with e-mail '%s' does not exists. Registering..." % user_info['email']
            u = self.dao.merge(logged_user)

        if not UserService.picture_exists_or_not_old(u):
            print "Downloading '%s' profile picture" % u.name
            RequestService().save_file(user_info['picture']['data']['url'], UserService.PICTURE_PATH % u.id)

        return u

    @staticmethod
    def picture_exists_or_not_old(u):
        pic = UserService.PICTURE_PATH % u.id
        pic_exists = os.path.isfile(pic)

        if not pic_exists:
            print "Profile picture does not exists for '%s'" % u.name
            return False

        pic_date = os.path.getctime(pic)
        if not pic_date:
            pic_date = os.path.getmtime(pic)

        pic_old = (pic_date + picture_age) < int(round(time.time()))

        if pic_old:
            print "Profile picture for '%s' is too old" % u.name
            return False

        return True
