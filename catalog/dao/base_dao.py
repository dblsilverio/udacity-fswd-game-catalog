from catalog.__init__ import DBSession


class BaseDao:

    def __init__(self):
        self.session = DBSession();

    def __del__(self):
        self.session.close()


def transacted(func):
    """ Decorator that wraps a commit around service methods """

    def commit_or_rollback(self, *args, **kwargs):
        """ Commit or rollback according to underlying  """
        try:
            result = func(self, *args, **kwargs)
            self.session.commit()
            return result
        except Exception as exception:
            print "Rollbacking due to error: %s" % exception.message
            self.session.rollback()
            raise

    return commit_or_rollback

