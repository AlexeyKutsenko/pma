from pma import domain
from pma.repository import orm
from pma.repository.repos import RepoFactory


class RepositoryNotFound(Exception):
    pass


class RepositoryRegistry:
    repositories = {}

    @classmethod
    def register(cls, _type, repo):
        cls.repositories[_type] = repo

    @classmethod
    def register_many(cls, collection):
        for name, repo in collection.items():
            cls.register(name, repo)

    @classmethod
    def get_for(cls, _type):
        try:
            return cls.repositories[_type]
        except KeyError:
            raise RepositoryNotFound(f'Repository {_type} not registered')


REPOS = {
    'stock': RepoFactory(domain.stock.Stock, orm.Stock)

}

RepositoryRegistry.register_many(REPOS)
