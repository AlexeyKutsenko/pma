from dataclasses import fields

from pma.repository.orm.session import DBSession


class RepoFactory:
    def __init__(self, domain_class, orm_class):
        self.domain_class = domain_class
        self.orm_class = orm_class
        self.attributes = [field.name for field in fields(self.domain_class)]
        self.session = DBSession()

    def _apply_filters(self, query, filters):
        for field__op, value in filters.items():
            field, op = field__op.split('__')
            if op == 'eq':
                query = query.filter(getattr(self.orm_class, field) == value)
            elif op == 'lt':
                query = query.filter(getattr(self.orm_class, field) < value)
            elif op == 'gt':
                query = query.filter(getattr(self.orm_class, field) > value)
        return query

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
        query = self._apply_filters(query, filters)

        return self._create_objects(query.all())
