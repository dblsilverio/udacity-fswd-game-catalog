import base64
from flask import request, flash, redirect, session

from catalog import app
from catalog.services.facebook_service import FacebookService, RequestService


@app.route('/login')
def login():
    code = request.args.get('code')

    user_info = FacebookService().authenticate(code)
    session['user'] = new_session(user_info)

    return redirect('/')


@app.route('/logout')
def logout():
    user = session['user']['name']
    session.pop('user', None)

    flash("Goodbye, %s!" % user, 'login')

    return redirect('/')


@app.route('/auth')
def facebook_login():
    return redirect(FacebookService().login_url())


def new_session(user_info):
    username = user_info['name']

    flash("Welcome, %s!" % username, 'login')
    profile_img_url = user_info['picture']['data']['url']
    image_uri = (
        "data:image/png;base64," + base64.b64encode(RequestService()
                                                    .get(url=profile_img_url)))
    return {
        "name": user_info['name'],
        "email": user_info['email'],
        "picture": image_uri
    }
