from unittest import mock

from pma.domain.stock import Stock
from pma.responses import ResponseSuccess

stock_dict = {
    "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
    "ticker": "NVDA",
    "name": "NVIDIA CORP",
    "sector": "Information Technology",
    "price": 306.57
}

stocks = [Stock.from_dict(stock_dict)]


@mock.patch('application.rest.stock.stock_list_use_case')
def test_get(mock_use_case, client):
    mock_use_case.return_value = ResponseSuccess(stocks)

    http_response = client.get('/stocks')

    assert http_response.json() == [stock_dict]

    mock_use_case.assert_called()
    args, kwargs = mock_use_case.call_args
    assert args[1].filters == {}

    assert http_response.status_code == 200


@mock.patch('application.rest.stock.stock_list_use_case')
def test_get_with_filters(mock_use_case, client):
    mock_use_case.return_value = ResponseSuccess(stocks)

    http_response = client.get('/stocks?price__gt=2&price__lt=6')

    assert http_response.json() == [stock_dict]

    mock_use_case.assert_called()
    args, kwargs = mock_use_case.call_args
    assert args[1].filters == {'price__gt': '2', 'price__lt': '6'}

    assert http_response.status_code == 200
