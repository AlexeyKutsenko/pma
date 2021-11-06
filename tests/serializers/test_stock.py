import json
import uuid

from pma.serializers.stock import StockJsonEncoder
from pma.domain.stock import Stock


def test_serialize_domain_stock():
    code = uuid.uuid4()

    stock = Stock(
        code,
        ticker='AVGO',
        name='BROADCOM INC',
        sector='Information Technology',
        price=506,
    )

    expected_json = f"""
        {{
            "code": "{code}",
            "ticker": "AVGO",
            "name": "BROADCOM INC",
            "sector": "Information Technology",
            "price": 506
        }}
    """

    json_stock = json.dumps(stock, cls=StockJsonEncoder)

    assert json.loads(json_stock) == json.loads(expected_json)
