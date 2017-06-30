""" Provides general purpose decorators. """
from catalog.services.game_service import GameService


def page_view(func):
    """ Decorator that counts page views """

    def increment_game_click(*args, **kwargs):
        """ Add 1 to game visualization and proceeds.  """
        try:
            GameService().increment(kwargs['gid'])
        except Exception as exc:
            print "Error counting page views: %s" % exc.message

        return func(*args, **kwargs)

    return increment_game_click
