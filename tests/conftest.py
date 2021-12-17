import pytest
from fastapi.testclient import TestClient

from application.app import create_app
from manage import read_json_configuration
from .fixtures.stocks import domain_stocks, stock_dicts  # noqa


@pytest.fixture
def client():
    app = create_app()
    client = TestClient(app)
    return client


@pytest.fixture(scope="session")
def app_configuration():
    return read_json_configuration("testing")


def pytest_addoption(parser):
    parser.addoption('--integration', action='store_true', help='run integration tests')


def pytest_runtest_setup(item):
    if 'integration' in item.keywords and not item.config.getvalue('integration'):
        pytest.skip('need --integration option to run')
