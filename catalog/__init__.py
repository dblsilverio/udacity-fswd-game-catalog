""" Game Catalog project for Full Stack Web Developer. """
import sys

from catalog.infra.db_factory import create
from catalog.infra.flask_factory import app
from catalog.infra.bootstrap import Bootstrap
import catalog.routes.main
import catalog.routes.category
import catalog.routes.game
import catalog.routes.access

reload(sys)
sys.setdefaultencoding('utf8')

create()
Bootstrap.create_categories()
