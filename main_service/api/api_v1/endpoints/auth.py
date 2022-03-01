from datetime import timedelta, datetime
from typing import List, Optional

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from starlette import status

from config import settings
from db import get_session
from models.users import User, UserInput, AuthCredentials
from utils.authorization import authenticate_user, create_access_token

router = APIRouter(prefix='/auth')


@router.post(
    '/token', summary='',
)
async def token(credentials: AuthCredentials,
                session: Session = Depends(get_session)):

    user = authenticate_user(session, credentials.username, credentials.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token}