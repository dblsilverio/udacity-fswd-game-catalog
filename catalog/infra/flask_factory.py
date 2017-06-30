""" Build Flask app object with secret key. """
from uuid import uuid4
from flask import Flask

app = Flask(__name__, template_folder='../templates',
            static_folder='../static')
app.secret_key = str(uuid4())
