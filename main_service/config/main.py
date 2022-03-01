from typing import Union, Optional, Tuple
from pydantic import BaseSettings, PostgresDsn, IPvAnyAddress, AnyUrl, FilePath, RedisDsn, HttpUrl, FileUrl


class Settings(BaseSettings):

    DEBUG: bool = False

    # constants for swagger
    APP_DESCRIPTION: str = ''
    APP_VERSION: str = '0.0.1'
    APP_TITLE: str = 'Сервис Пользователей'
    API_V1_STR: str = '/api/v1'

    PORT: int = 5003
    HOST: Union[IPvAnyAddress, AnyUrl] = '0.0.0.0'
    WORKERS: int = 1

    DATABASE_URL: str = 'sqlite:///sqlite.db'

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24
    SECRET_KEY: str = 'debug_secret_key'

settings = Settings(_env_file='../.environment')
