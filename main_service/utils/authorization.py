from datetime import timedelta, datetime
from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from jose.constants import ALGORITHMS
from passlib.context import CryptContext
from sqlmodel import Session, select
from starlette import status
from config import settings
from db import get_session
from models.users import User

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="token")
CREDENTIAL_EXCEPTION = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return PWD_CONTEXT.verify(plain_password, hashed_password)


def check_string_is_hash(value: str) -> bool:
    return bool(PWD_CONTEXT.identify(value))


def get_password_hash(password: str) -> str:
    return PWD_CONTEXT.hash(password)


def get_user(session: Session, username: str) -> User:
    query = select(User).where(User.username == username)
    user = session.exec(query).first()
    return user


def authenticate_user(session: Session, username: str, password: str) -> Optional[User]:
    user = get_user(session, username)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY)
    return encoded_jwt


async def get_current_user(session: Session = Depends(get_session),
                           token: str = Depends(OAUTH2_SCHEME)) -> User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHMS.HS256])
        username = payload.get("sub")
        if username is None:
            raise CREDENTIAL_EXCEPTION
    except JWTError:
        raise CREDENTIAL_EXCEPTION
    user = get_user(session, username)
    if user is None:
        raise CREDENTIAL_EXCEPTION
    return user
