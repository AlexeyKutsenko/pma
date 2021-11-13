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


def pytest_addoption(parser):
    parser.addoption('--integration', action='store_true', help='run integration tests')


def pytest_runtest_setup(item):
    if 'integration' in item.keywords and not item.config.getvalue('integration'):
        pytest.skip('need --integration option to run')
