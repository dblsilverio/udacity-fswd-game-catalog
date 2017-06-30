import uuid

from flask import g, request, session, abort, redirect
from catalog.infra.flask_factory import app
from catalog.services.utils import refresh_config


@app.before_request
def check_read_mode():
    """ Verifies readonly mode, according to catalog config file """
    g.read_only = refresh_config().getboolean('GameCatalog',
                                              'catalog.read_only')

    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = str(uuid.uuid4())
    return session['_csrf_token']


@app.errorhandler(403)
def handle_bad_request(e):
    return redirect('/403')

app.jinja_env.globals['csrf_token'] = generate_csrf_token
