from functools import wraps
from flask import request, g
from ..db.db import db_session


def inject_db_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with db_session() as session:
            g.db_session = session
            return func(*args, *kwargs)
        return wrapper
