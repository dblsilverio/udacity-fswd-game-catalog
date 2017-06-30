from catalog.services.utils import Urls
from catalog.services.request_service import RequestService


class FacebookService(RequestService):
    """ Provides login and authentication services from Facebook Login API. """

    def __init__(self):
        pass

    @staticmethod
    def login_url():
        """ Builds login url for user Facebook authentication. """
        return Urls.login_url()

    def authenticate(self, code):
        """ Processes user authorization code in order to obtain access token
        and user basic information, such as name, e-mail anda profile picture.
        """
        access_token = self.get(url=Urls.access_token_url(code), is_json=True)
        user_info = self.get(url=Urls.user_info(access_token), is_json=True)

        return user_info
