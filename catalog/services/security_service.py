from flask import session

from catalog.services.game_service import GameService
from catalog.models.game import Game


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
        else:
            return False

        return model.user_id == session['user']['id']

    @staticmethod
    def is_authenticated():
        return 'user' in session
