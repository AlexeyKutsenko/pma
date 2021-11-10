import json
from unittest import mock

from pma.domain.stock import Stock

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
    mock_use_case.return_value = stocks

    http_response = client.get("/stocks")

    assert http_response.json() == [stock_dict]
    mock_use_case.assert_called()
    assert http_response.status_code == 200
