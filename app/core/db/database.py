from sqlalchemy.engine import Engine
from sqlmodel import create_engine, Session, SQLModel

from app.core.settings import settings


def get_db_session() -> Session:
    """
    Get a db session
    :return:
    """
    with Session(engine) as session:
        yield session


def set_engine() -> Engine:
    """
    Set the db engine
    :return:
    """
    global engine
    engine = create_engine(settings.config.DATABASE_URL)
    SQLModel.metadata.create_all(engine)
    print(f"engine_url : {settings.config.DATABASE_URL}")
    return engine


engine = None
