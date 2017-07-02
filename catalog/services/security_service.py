from flask import session

from catalog.services.game_service import GameService
from catalog.services.category_service import CategoryService
from catalog.models.game import Game
from catalog.models.category import Category


class SecurityService(object):
    """ Facility for checking user's rights over models/resources. """

    @staticmethod
    def is_owner(model_type, **kwargs):

        if not SecurityService.is_authenticated():
            return False

        model = {}

        if model_type == Game:
            mid = kwargs['gid']
            model = GameService().find_by(mid, False)
        elif model_type == Category:
            mid = kwargs['cid']
            model = CategoryService().find_by_id(mid, False)
        else:
            return False

        return model.user_id == session['user']['id']

    @staticmethod
    def is_authenticated():
        return 'user' in session
