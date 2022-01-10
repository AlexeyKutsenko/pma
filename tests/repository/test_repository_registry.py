from threading import Thread

import pytest

from pma import domain
from pma.repository import RepositoryRegistry, RepositoryNotFound, RepoFactory, orm


def test_repository_is_singleton():
    first_repository = RepositoryRegistry()
    second_repository = RepositoryRegistry()
    assert id(first_repository) == id(second_repository)

    first_new_repo_key = 'stock_duplicate'
    second_new_repo_key = 'stock_triplicate'
    threads = [
        Thread(
            target=RepositoryRegistry.register,
            args=(first_new_repo_key, RepoFactory(domain.stock.Stock, orm.Stock))
        ),
        Thread(
            target=RepositoryRegistry.register,
            args=(second_new_repo_key, RepoFactory(domain.stock.Stock, orm.Stock))
        )
    ]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    assert (first_new_repo_key in first_repository.repositories)
    assert (second_new_repo_key in first_repository.repositories)


def test_repository_for_type_not_registered():
    with pytest.raises(RepositoryNotFound):
        RepositoryRegistry.get_for(-1)
