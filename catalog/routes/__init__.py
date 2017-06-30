from flask import g
from catalog.infra.flask_factory import app
from catalog.services.utils import refresh_config


@app.before_request
def check_read_mode():
    """ Verifies readonly mode, according to catalog config file """
    g.read_only = refresh_config().getboolean('GameCatalog',
                                              'catalog.read_only')
