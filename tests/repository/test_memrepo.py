from pma.domain.stock import Stock
from pma.repository.memrepo import MemRepo


def test_repository_list_without_parameters(stock_dicts):
    repo = MemRepo(stock_dicts)

    stocks = [Stock.from_dict(i) for i in stock_dicts]

    assert repo.list() == stocks
