from flask import Flask
from uuid import uuid4
from catalog.infra.db_factory import create
from catalog.infra.bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = str(uuid4())

import catalog.routes.main
import catalog.routes.category
import catalog.routes.game
import catalog.routes.access

create()
Bootstrap.create_categories()
