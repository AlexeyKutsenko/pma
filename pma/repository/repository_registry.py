class RepositoryNotFound(Exception):
    pass


class RepositoryRegistry:
    repositories = {}

    def register(self, _type, repo):
        self.repositories[_type] = repo

    def register_many(self, collection):
        for name, repo in collection.items():
            self.register(name, repo)

    def get_for(self, _type):
        try:
            self.repositories
        except KeyError:
            raise RepositoryNotFound(f'Repository {_type} not registered')
