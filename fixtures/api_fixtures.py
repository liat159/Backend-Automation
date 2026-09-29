import pytest
from clients.order_client import OrderClient


@pytest.fixture
def api_client():
    return OrderClient()
