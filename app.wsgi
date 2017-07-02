import sys
import os

sys.path.insert(0, "%s/../" % os.getcwd())

from catalog.infra.flask_factory import app as application
