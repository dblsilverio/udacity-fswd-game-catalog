from flask import redirect, flash


def protected(func):
    """ Decorator that secures a method against anonymous users """

    def is_authorized(*args, **kwargs):
        """ Checks if users is allowed to operate  """
        authorized = True

        if authorized:
            return func(*args, **kwargs)
        else:
            flash('User is not authenticated.', 'danger')
            return redirect('/')

    return is_authorized
