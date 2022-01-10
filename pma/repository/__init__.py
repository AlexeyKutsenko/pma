from threading import Lock

from pma import domain
from pma.repository import orm
from pma.repository.repos import RepoFactory


class RepositoryNotFound(Exception):
    pass


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class RepositoryRegistry(metaclass=SingletonMeta):
    repositories = {}

    @classmethod
    def register(cls, _type, repo):
        print(_type, repo)
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
