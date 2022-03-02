import utils
from typing import Optional
from pydantic import validator
from sqlalchemy import Column, BOOLEAN
from sqlmodel import SQLModel, Field


class Token(SQLModel):
    access_token: str
    token_type: str


class AuthCredentials(SQLModel):
    username: str
    password: str


class UserBase(SQLModel):
    username: str
    read_only: bool = Field(default=True, sa_column=Column(BOOLEAN, nullable=False))


class UserOutput(UserBase):
    id: Optional[int] = Field(default=None, primary_key=True, title='Идентификатор')


class UserInput(UserBase):
    password: str

    @validator('password')
    def hash_password(cls, v, values, **kwargs):
        if not v or utils.authorization.check_string_is_hash(v):
            return v
        return utils.authorization.get_password_hash(v)


class User(UserOutput, UserInput, table=True):
    pass
