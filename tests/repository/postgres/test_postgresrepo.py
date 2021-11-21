import pytest

from pma.repository import postgresrepo

pytestmark = pytest.mark.integration


def test_repository_list_without_parameters(app_configuration, pg_session, pg_test_data):
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_stocks = repo.list()

    assert set([s.code for s in repo_stocks]) == set([s['code'] for s in pg_test_data])


def test_repository_list_with_code_equal_filter(app_configuration, pg_session, pg_test_data):
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_stocks = repo.list(filters={'code__eq': 'f853578c-fc0f-4e65-81b8-566c5dffa35a'})

    assert len(repo_stocks) == 1
    assert repo_stocks[0].code == 'f853578c-fc0f-4e65-81b8-566c5dffa35a'


def test_repository_list_with_price_equal_filter(app_configuration, pg_session, pg_test_data):
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_stocks = repo.list(filters={'price__eq': 557.80})

    assert len(repo_stocks) == 1
    assert repo_stocks[0].code == 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a'


def test_repository_list_with_price_less_than_filter(app_configuration, pg_session, pg_test_data):
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_stocks = repo.list(filters={'price__lt': 200})

    assert len(repo_stocks) == 2
    assert set([s.code for s in repo_stocks]) == {'913694c6-435a-4366-ba0d-da5334a611b2',
                                                  'eed76e77-55c1-41ce-985d-ca49bf6c0585'}


def test_repository_list_with_price_greater_than_filter(
        app_configuration, pg_session, pg_test_data
):
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_stocks = repo.list(filters={'price__gt': 200})

    assert len(repo_stocks) == 2
    assert set([s.code for s in repo_stocks]) == {'f853578c-fc0f-4e65-81b8-566c5dffa35a',
                                                  'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a'}


def test_repository_list_with_price_between_filter(app_configuration, pg_session, pg_test_data):
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_stocks = repo.list(filters={'price__lt': 200, 'price__gt': 100})

    assert len(repo_stocks) == 1
    assert repo_stocks[0].code == 'eed76e77-55c1-41ce-985d-ca49bf6c0585'
