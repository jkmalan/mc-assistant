import uuid, functools

from flask_login import current_user

from microcenter import lm
from microcenter.models.users import User


def permission(roles=None):
    def wrapper(fn):
        @functools.wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return lm.unauthorized()
            user_roles = current_user.get_roles()
            if not bool(set(user_roles) & set(roles)):
                return lm.unauthorized()
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


@lm.user_loader
def user_loader(user_id):
    if isinstance(user_id, str):
        user_id = uuid.UUID(user_id)
    return User.query.get(user_id)
