from uuid import UUID

from pydantic import BaseModel


class StockModel(BaseModel):
    code: UUID
    ticker: str
    name: str
    sector: str
    price: float
