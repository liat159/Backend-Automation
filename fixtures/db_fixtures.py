import pytest

from core.database.db_client import DBClient


@pytest.fixture(scope="session")
def db():
    client = DBClient()
    yield client
    client.close()
