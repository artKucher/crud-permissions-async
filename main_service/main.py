import uvicorn
from fastapi import FastAPI
from sqlmodel import SQLModel
from starlette.middleware.cors import CORSMiddleware

from config import settings
from api.api_v1.api import api_router
from db import engine, get_session
from models.users import User

application = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    openapi_url=f'{settings.API_V1_STR}/openapi.json',
)

application.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

application.include_router(api_router, prefix=settings.API_V1_STR)


def flush_db():
    SQLModel.metadata.drop_all(engine)


def create_db():
    SQLModel.metadata.create_all(engine)


def create_default_user():
    session = next(get_session())
    session.add(User(username=settings.DEFAULT_USER_USERNAME,
                     password=settings.DEFAULT_USER_PASSWORD,
                     read_only=False))
    session.commit()
    session.close()


if __name__ == '__main__':
    flush_db()
    create_db()
    create_default_user()
    uvicorn.run('main:application',
                host=str(settings.HOST),
                port=settings.PORT,
                workers=settings.WORKERS,
                debug=settings.DEBUG,
                reload=True)
