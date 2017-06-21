from flask import Flask
app = Flask(__name__)

import catalog.routes.main
import catalog.routes.category
import catalog.routes.game
