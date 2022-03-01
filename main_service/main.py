import uvicorn
from fastapi import FastAPI, Request
from sqlmodel import SQLModel

from config import settings
from api.api_v1.api import api_router
from db import engine

application = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    openapi_url=f'{settings.API_V1_STR}/openapi.json',
)

application.include_router(api_router, prefix=settings.API_V1_STR)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == '__main__':
    create_db_and_tables()
    # DO NOT USE IN PRODUCTION!
    uvicorn.run('main:application',
                host=str(settings.HOST),
                port=settings.PORT,
                workers=settings.WORKERS,
                debug=settings.DEBUG,
                reload=True)
