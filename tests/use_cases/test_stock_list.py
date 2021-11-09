from unittest import mock

from pma.use_cases.stock_list import stock_list_use_case


def test_stock_list_without_parameters(domain_stocks):
    repo = mock.Mock()
    repo.list.return_value = domain_stocks

    result = stock_list_use_case(repo)

    repo.list.assert_called_with()
    assert result == domain_stocks