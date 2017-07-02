import urlparse
import ConfigParser
import urllib
import os

config = ConfigParser.ConfigParser()
config.read(os.environ.get('CATALOG_PATH') + 'catalog/configs/catalog.ini')

app_id = config.get('Facebook', 'face.app_id')
secret = config.get('Facebook', 'face.secret')
login_path = config.get('GameCatalog', 'catalog.login')
picture_age = config.getint('GameCatalog', 'catalog.picture_age')


def refresh_config():
    config.read(os.environ.get('CATALOG_PATH') + 'catalog/configs/catalog.ini')
    return config


def parse_url(func):
    """ Decorator that parses a string url to ParseResult """

    def parse(self, *args, **kwargs):
        kwargs['url'] = urlparse.urlparse(kwargs['url'])
        return func(self, *args, **kwargs)

    return parse


class Urls(object):
    """ Wraps URLs creation, formatting and concatenating data when
    needed."""
    def __init__(self):
        pass

    @staticmethod
    def login_url():
        return "https://www.facebook.com/v2.9/dialog/oauth?" \
               "client_id=%s&redirect_uri=%s&scope=%s" % (
                   app_id, urllib.quote_plus(login_path),
                   'public_profile,email')

    @staticmethod
    def access_token_url(code):
        return "https://graph.facebook.com/v2.9/oauth/access_token?" \
               "client_id=%(appid)s&redirect_uri=%(redirecturi)s" \
               "&client_secret=%(appsecret)s&" \
               "code=%(codeparameter)s" % {'appid': app_id,
                                           'redirecturi': login_path,
                                           'appsecret': secret,
                                           'codeparameter': code}

    @staticmethod
    def user_info(access_token):
        return "https://graph.facebook.com/v2.9/me?" \
               "access_token=%s&fields=%s" % (access_token['access_token'],
                                              'id,name,picture,email')
