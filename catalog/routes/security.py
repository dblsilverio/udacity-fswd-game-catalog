from functools import wraps
from flask import redirect, flash, session


def protected(func):
    """ Decorator that secures a method against anonymous users """
    @wraps(func)
    def is_authorized(*args, **kwargs):
        """ Checks if users is allowed to operate  """
        authorized = 'user' in session

        if not authorized:
            flash('User is not authenticated.', 'danger')
            return redirect('/')
        else:
            return func(*args, **kwargs)

    return is_authorized
