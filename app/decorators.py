from flask_login import current_user
from functools import wraps
from flask import abort


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated and current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)

    return decorated_function
