import warnings

import pytest
from sqlmodel import Session

from app.core.db import database
from app.core.settings.models.enums.env_enum import Env
from app.core.settings.settings import set_config
from tests.db_management import setup_test_db, drop_test_db

warnings.filterwarnings(
    "ignore", ".*Class SelectOfScalar will not make use of SQL compilation caching.*"
)  # Due to https://github.com/tiangolo/sqlmodel/issues/189


def pytest_sessionstart():
    set_config(Env.TEST)
    setup_test_db()


def pytest_sessionfinish():
    drop_test_db()


@pytest.fixture(name="session")
def session_fixture():
    with Session(database.engine) as session:
        yield session
