""" Provides decorators for securing CRUD(and others) routes. """
from functools import wraps
from flask import redirect, flash, session, request

from catalog.services.security_service import SecurityService


def protected(func):
    """ Decorator that secures a method against anonymous users """
    @wraps(func)
    def is_authenticated(*args, **kwargs):
        """ Checks if users is allowed to operate  """
        authenticated = 'user' in session

        if not authenticated:
            flash('User is not authenticated.', 'danger')
            return redirect('/')
        else:
            return func(*args, **kwargs)

    return is_authenticated


def check_owner(model_type):
    """ Decorator checking if user is the owner of the resource. """

    def check_decorator(func):
        @wraps(func)
        def is_authorized(*args, **kwargs):
            """ Checks if user is the owner of a Game/Category  that he/she
            is trying to update/delete"""

            if not SecurityService().is_owner(model_type, **kwargs):
                flash('User is not authorized to modify specified resource.',
                      'danger')
                return redirect(request.referrer or '/')

            return func(*args, **kwargs)

        return is_authorized

    return check_decorator
