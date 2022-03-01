from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from db import get_session
from models.users import UserInput, UserOutput, User
from utils.authorization import get_current_user
from utils.permissions import write_permission_required

router = APIRouter(prefix='/users')


@router.get(
    '',
    summary='',
    response_model=List[UserOutput]
)
async def users_list(session: Session = Depends(get_session),
                     _: User = Depends(get_current_user)):
    query = select(User)
    users = session.exec(query).all()

    return users


@router.post(
    '',
    summary='',
    response_model=UserOutput
)
@write_permission_required
async def create(new_user: UserInput,
                 session: Session = Depends(get_session),
                 _: User = Depends(get_current_user)):
    new_user = User.validate(new_user)

    session.add(new_user)
    session.commit()

    return new_user

@router.patch(
    '/{user_id}',
    response_model=UserOutput
)
@write_permission_required
async def update_user(user_id: int,
                      updated_user: UserInput,
                      session: Session = Depends(get_session),
                      _: User = Depends(get_current_user)):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in updated_user.dict().items():
        setattr(db_user, key, value)
    session.add(db_user)
    session.commit()
    return db_user


@router.delete('/{user_id}')
@write_permission_required
async def delete_user(user_id: int,
                      session: Session = Depends(get_session),
                      _: User = Depends(get_current_user)):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(db_user)
    session.commit()
    return {'ok': True}