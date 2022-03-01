from typing import Optional

from sqlmodel import SQLModel, Field


class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    username: Optional[str] = None


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, title='Идентификатор')
    username: str
    password: str


class UserInput(SQLModel):
    username: str
    password: str


class UserInDB(User):
    hashed_password: str