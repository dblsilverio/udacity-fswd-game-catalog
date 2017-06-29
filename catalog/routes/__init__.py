from flask import g
from catalog import app
from catalog.services.utils import refresh_config


@app.before_request
def check_read_mode():
    g.read_only = refresh_config().getboolean('GameCatalog', 'catalog.read_only')
