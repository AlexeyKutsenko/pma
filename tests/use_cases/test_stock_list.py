from unittest import mock

from pma.requests.stock_list import build_stock_list_request
from pma.responses import ResponseTypes
from pma.use_cases.stock_list import stock_list_use_case


def test_stock_list_without_parameters(domain_stocks):
    repo = mock.Mock()
    repo.list.return_value = domain_stocks

    request = build_stock_list_request()

    response = stock_list_use_case(repo, request)

    assert bool(request) is True
    repo.list.assert_called_with(filters=None)
    assert response.value == domain_stocks


def test_stock_list_with_filters(domain_stocks):
    repo = mock.Mock()
    repo.list.return_value = domain_stocks

    qry_filters = {'code__eq': 5}
    request = build_stock_list_request(filters=qry_filters)

    response = stock_list_use_case(repo, request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response.value == domain_stocks


def test_stock_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception('Just an error message')

    request = build_stock_list_request(filters={})

    response = stock_list_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        'type': ResponseTypes.SYSTEM_ERROR,
        'message': 'Exception: Just an error message'
    }


def test_stock_list_handles_bad_request():
    repo = mock.Mock()

    request = build_stock_list_request(filters=5)

    response = stock_list_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        'type': ResponseTypes.PARAMETERS_ERROR,
        'message': 'filters: Is not iterable'
    }
