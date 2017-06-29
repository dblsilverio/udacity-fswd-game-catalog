from catalog.infra.db_factory import DBSession

from catalog.services.utils import refresh_config


class BaseDao:
    """ Base class for models. """

    def __init__(self):
        self.session = DBSession();
        self.read_only = refresh_config().getboolean('GameCatalog', 'catalog.read_only')

    def __del__(self):
        self.session.close()


def transacted(func):
    """ Decorator that wraps a commit around service methods """

    def commit_or_rollback(self, *args, **kwargs):
        """ Commit or rollback according to underlying  """
        try:
            result = func(self, *args, **kwargs)
            if not self.read_only:
                self.session.commit()
            else:
                self.session.rollback()

            return result
        except Exception as exception:
            print "Rollbacking due to error: %s" % exception.message
            self.session.rollback()
            raise

    return commit_or_rollback

