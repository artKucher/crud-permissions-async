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
    summary='List of users',
    response_model=List[UserOutput]
)
async def users_list(session: Session = Depends(get_session),
                     _: User = Depends(get_current_user)):

    # RAW SQL will be 'SELECT * FROM users'
    query = select(User)
    users = session.exec(query).all()

    return users


@router.post(
    '',
    summary='Create new user',
    response_model=UserOutput
)
@write_permission_required
async def create(new_user: UserInput,
                 session: Session = Depends(get_session),
                 current_user: User = Depends(get_current_user)):
    new_user = User.validate(new_user)
    # RAW SQL will be 'INSERT INTO users (id, username, password, read_only)
    #                  VALUES (<id>, <username>, <password>, <read_only>)'
    session.add(new_user)
    session.commit()

    return new_user

@router.patch(
    '/{user_id}',
    summary='Update existing user',
    response_model=UserOutput
)
@write_permission_required
async def update_user(user_id: int,
                      updated_user: UserInput,
                      session: Session = Depends(get_session),
                      current_user: User = Depends(get_current_user)):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in updated_user.dict().items():
        if value != '':
            setattr(db_user, key, value)

    # RAW SQL will be 'UPDATE user SET edited_column_name=new_value WHERE id=db_user.id'
    session.add(db_user)
    session.commit()
    return db_user


@router.delete(
    '/{user_id}',
    summary='Delete user')
@write_permission_required
async def delete_user(user_id: int,
                      session: Session = Depends(get_session),
                      current_user: User = Depends(get_current_user)):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Item not found")

    # RAW SQL EXAMPLE
    statement = f'DELETE FROM user WHERE id={db_user.id}'
    session.execute(statement)
    session.commit()
    return {'ok': True}