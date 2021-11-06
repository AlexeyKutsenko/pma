import uuid
import dataclasses


@dataclasses.dataclass
class Stock:
    code: uuid.UUID
    ticker: str
    name: str
    sector: str
    price: float
