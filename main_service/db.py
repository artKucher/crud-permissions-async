from sqlalchemy import create_engine
from sqlmodel import Session

from config import settings

engine = create_engine(settings.DATABASE_URL,
                       echo=settings.DEBUG,
                       connect_args={'check_same_thread': False})


def get_session() -> Session:
    """
    Зависимость для получения новой сессии
    """
    with Session(engine, expire_on_commit=False) as new_session:
        yield new_session
