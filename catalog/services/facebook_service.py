from catalog.services.utils import Urls
from catalog.services.request_service import RequestService


class FacebookService(RequestService):

    def __init__(self):
        pass

    def login_url(self):
        return Urls.login_url()

    def authenticate(self, code):
        access_token = self.get(url=Urls.access_token_url(code), is_json=True)
        user_info = self.get(url=Urls.user_info(access_token), is_json=True)

        return user_info
