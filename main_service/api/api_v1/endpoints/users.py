from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from db import get_session
from models.users import User

router = APIRouter(prefix='/users')


@router.get(
    '',
    summary='',
    response_model=List[User]
)
async def users_list(session: Session = Depends(get_session)):
    query = select(User)
    users = session.exec(query).all()
    return users