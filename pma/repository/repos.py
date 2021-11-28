from dataclasses import fields

from pma import domain
from pma.domain import stock
from pma.repository import orm
from pma.repository.orm.session import DBSession


class RepoFactory:
    def __init__(self, domain_class, orm_class):
        self.domain_class = domain_class
        self.orm_class = orm_class
        self.attributes = [field.name for field in fields(self.domain_class)]
        self.session = DBSession()

    def _create_objects(self, results):
        return [
            self.domain_class(
                **{attribute: getattr(item, attribute) for attribute in self.attributes}
            )
            for item in results
        ]

    def list(self, filters=None):
        query = self.session.query(self.orm_class)

        if filters is None:
            return self._create_objects(query.all())



# class PostgresRepo:
#     def list(self, filters=None):
#         session = DBSession()
#
#         if filters is None:
#             return self._create_stock_objects(query.all())
#
#         if 'code__eq' in filters:
#             query = query.filter(Stock.code == filters['code__eq'])
#
#         if 'price__eq' in filters:
#             query = query.filter(Stock.price == filters['price__eq'])
#
#         if 'price__lt' in filters:
#             query = query.filter(Stock.price < filters['price__lt'])
#
#         if 'price__gt' in filters:
#             query = query.filter(Stock.price > filters['price__gt'])
#
#         return self._create_stock_objects(query.all())
