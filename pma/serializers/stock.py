import json
from typing import Any


class StockJsonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        to_serialize = {
            "code": str(o.code),
            "ticker": o.ticker,
            "name": o.name,
            "sector": o.sector,
            "price": o.price
        }
        return to_serialize
