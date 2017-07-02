import sys
import os


def application(environ, start_response):
    for key in ['CATALOG_PATH']:
        os.environ[key] = environ.get(key, '')

    sys.path.insert(0, environ['CATALOG_PATH'])
    from catalog.infra.flask_factory import app as _application
    return _application(environ, start_response)
