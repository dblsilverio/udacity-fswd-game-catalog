import httplib
import json

from StringIO import StringIO

from catalog.services.utils import parse_url


class RequestService:
    def __init__(self):
        pass

    @parse_url
    def get(self, url, is_json=False, **params):
        conn = RequestService.get_connection(url)
        conn.request(method='GET', url=RequestService.full_url(url), headers={'User-Agent': 'GameCatalog 1.0 Client'})

        resp = conn.getresponse().read()

        if is_json:
            resp = json.load(StringIO(resp))

        return resp

    @staticmethod
    def get_connection(url):
        if RequestService.is_https(url):
            conn = httplib.HTTPSConnection(url.netloc)
        else:
            conn = httplib.HTTPConnection(url.netloc)

        return conn

    @staticmethod
    def full_url(url):
        if url.query:
            return "%s?%s" % (url.path, url.query)

    @staticmethod
    def save_file(url, filename):
        pic_file = open(name=filename, mode='w')
        pic_file.write(RequestService().get(url=url))

    @staticmethod
    def is_https(url):
        return url.scheme == 'https'
