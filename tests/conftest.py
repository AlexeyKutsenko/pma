import pytest
from fastapi.testclient import TestClient

from application.app import create_app
# noinspection PyUnresolvedReferences
from .fixtures.stocks import domain_stocks, stock_dicts


@pytest.fixture
def client():
    app = create_app('testing')
    client = TestClient(app)
    return client
