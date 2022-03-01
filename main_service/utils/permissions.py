from functools import wraps

from fastapi import HTTPException
from starlette import status


class CurrentUserNotProvidedExeption(Exception):
    def __init__(self):
        message = 'Current user object does not provided'
        super().__init__(message)


def write_permission_required(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        current_user = kwargs.get('current_user')
        if not current_user:
            raise CurrentUserNotProvidedExeption()
        if current_user.read_only:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Insufficient permissions",
                                headers={"WWW-Authenticate": "Bearer"})
        return await func(*args, **kwargs)
    return inner