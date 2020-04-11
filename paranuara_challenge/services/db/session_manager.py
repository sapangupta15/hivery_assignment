import functools
from sqlalchemy.orm.session import Session
from paranuara_challenge.services.db import session_scope

def session_manager(func):
    """
    Check if session has been passed by calling function,
    if true, then reuse same session,
    else fetch a new session and handle session commit/rollback
    :param func:
    :return:
    """
    @functools.wraps(func)
    def wrapper_session_manager(*args, **kwargs):
        if len(args) > 0 and isinstance(args[0], Session):
            # reuse existing session
            value = func(*args, **kwargs)
            return value
        else:
            with session_scope() as session:
                value = func(session, *args, **kwargs)
                return value
    return wrapper_session_manager
