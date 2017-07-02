import sys
import os

sys.path.insert(0, os.environ['CATALOG_PATH'] % os.getcwd())

from catalog.infra.flask_factory import app as application
