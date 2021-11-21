import sqlalchemy
import pytest

from pma.repository.postgres_objects import Base, Stock
from tests.fixtures.stocks import raw_stock_dicts


@pytest.fixture(scope='session')
def pg_session_empty(app_configuration):
    conn_str = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
        app_configuration['POSTGRES_USER'],
        app_configuration['POSTGRES_PASSWORD'],
        app_configuration['POSTGRES_HOSTNAME'],
        app_configuration['POSTGRES_PORT'],
        app_configuration['APPLICATION_DB']
    )
    engine = sqlalchemy.create_engine(conn_str)
    connection = engine.connect()

    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    DBSession = sqlalchemy.orm.sessionmaker(bind=engine)
    session = DBSession()

    yield session

    session.close()
    connection.close()


@pytest.fixture(scope='session')
def pg_test_data():
    return raw_stock_dicts


@pytest.fixture(scope='function')
def pg_session(pg_session_empty, pg_test_data):
    for s in pg_test_data:
        new_stock = Stock(
            code=s['code'],
            ticker=s['ticker'],
            name=s['name'],
            sector=s['sector'],
            price=s['price']
        )
        pg_session_empty.add(new_stock)
        pg_session_empty.commit()

    yield pg_session_empty

    pg_session_empty.query(Stock).delete()
