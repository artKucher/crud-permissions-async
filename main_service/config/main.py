from typing import Union, List
from pydantic import BaseSettings, IPvAnyAddress, AnyUrl, AnyHttpUrl


class Settings(BaseSettings):

    DEBUG: bool = False

    # constants for swagger
    APP_DESCRIPTION: str = ''
    APP_VERSION: str = '0.0.1'
    APP_TITLE: str = 'CRUD Users + async ordering'
    API_V1_STR: str = '/api/v1'

    PORT: int = 5003
    HOST: Union[IPvAnyAddress, AnyUrl] = '0.0.0.0'
    WORKERS: int = 1

    DATABASE_URL: str = 'sqlite:///sqlite.db'

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24
    SECRET_KEY: str = 'developing_secret_key'

    SOURCES_URLS: List[AnyHttpUrl] = [
        f'http://localhost:5003{API_V1_STR}/second-task/first-source',
        f'http://localhost:5003{API_V1_STR}/second-task/second-source',
        f'http://localhost:5003{API_V1_STR}/second-task/third-source',
    ]
    SOURCES_REQUEST_TIMEOUT_SECONDS: int = 2

    DEFAULT_USER_USERNAME: str = 'admin'
    DEFAULT_USER_PASSWORD: str = 'admin'


settings = Settings(_env_file='../.environment')

