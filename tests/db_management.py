from sqlalchemy_utils import database_exists, create_database, drop_database

from app.core.db.database import set_engine
from app.core.settings import settings


def setup_test_db():
    """
    Create the test db
    :return:
    """
    db_url: str = settings.config.DATABASE_URL
    if not database_exists(db_url):
        create_database(db_url)
        set_engine()


def drop_test_db():
    """
    Delete the test db
    :return:
    """
    drop_database(settings.config.DATABASE_URL)
