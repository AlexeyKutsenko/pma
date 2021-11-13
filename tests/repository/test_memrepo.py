from pma.domain.stock import Stock
from pma.repository.memrepo import MemRepo


def test_repository_list_without_parameters(stock_dicts):
    repo = MemRepo(stock_dicts)

    stocks = [Stock.from_dict(i) for i in stock_dicts]

    assert repo.list() == stocks


def test_repository_list_with_code_equal_filter(stock_dicts):
    repo = MemRepo(stock_dicts)

    stocks = repo.list(filters={'code__eq': 'eed76e77-55c1-41ce-985d-ca49bf6c0585'})

    assert len(stocks) == 1
    assert stocks[0].code == 'eed76e77-55c1-41ce-985d-ca49bf6c0585'


def test_repository_list_with_price_equal_filter(stock_dicts):
    repo = MemRepo(stock_dicts)

    stocks = repo.list(filters={'price__eq': 51.20})

    assert len(stocks) == 1
    assert stocks[0].code == '913694c6-435a-4366-ba0d-da5334a611b2'


def test_repository_list_with_price_less_than_filter(stock_dicts):
    repo = MemRepo(stock_dicts)

    stocks = repo.list(filters={'price__lt': 200})

    assert len(stocks) == 2
    assert set([s.code for s in stocks]) == {
        '913694c6-435a-4366-ba0d-da5334a611b2',
        'eed76e77-55c1-41ce-985d-ca49bf6c0585'
    }


def test_repository_list_with_price_greater_than_filter(stock_dicts):
    repo = MemRepo(stock_dicts)

    stocks = repo.list(filters={'price__gt': 200})

    assert len(stocks) == 2
    assert set([s.code for s in stocks]) == {
        'f853578c-fc0f-4e65-81b8-566c5dffa35a',
        'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a'
    }


def test_repository_list_with_price_between_filter(stock_dicts):
    repo = MemRepo(stock_dicts)

    stocks = repo.list(filters={'price__gt': 100, 'price__lt': 200})

    assert len(stocks) == 1
    assert stocks[0].code == 'eed76e77-55c1-41ce-985d-ca49bf6c0585'


def test_repository_list_price_as_strings(stock_dicts):
    repo = MemRepo(stock_dicts)

    repo.list(filters={"price__eq": "60"})
    repo.list(filters={"price__lt": "60"})
    repo.list(filters={"price__gt": "60"})
