from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pma.domain import stock
from pma.repository.postgres_objects import Base, Stock


class PostgresRepo:
    def __init__(self, configuration):
        connection_string = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
            configuration["POSTGRES_USER"],
            configuration["POSTGRES_PASSWORD"],
            configuration["POSTGRES_HOSTNAME"],
            configuration["POSTGRES_PORT"],
            configuration["APPLICATION_DB"],
        )

        self.engine = create_engine(connection_string)
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine

    def _create_stock_objects(self, results):
        return [
            stock.Stock(
                code=q.code,
                ticker=q.ticker,
                name=q.name,
                sector=q.sector,
                price=q.price
            )
            for q in results
        ]

    def list(self, filters=None):
        DBSession = sessionmaker(self.engine)
        session = DBSession()

        query = session.query(Stock)

        if filters is None:
            return self._create_stock_objects(query.all())

        if 'code__eq' in filters:
            query = query.filter(Stock.code == filters['code__eq'])
            
        if 'price__eq' in filters:
            query = query.filter(Stock.price == filters['price__eq'])
            
        if 'price__lt' in filters:
            query = query.filter(Stock.price < filters['price__lt'])
            
        if 'price__gt' in filters:
            query = query.filter(Stock.price > filters['price__gt'])

        return self._create_stock_objects(query.all())