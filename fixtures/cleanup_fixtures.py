import pytest


@pytest.fixture(autouse=True)
def cleanup(db):
    yield
    if hasattr(db, "clear_orders"):
        db.clear_orders()
