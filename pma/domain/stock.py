import uuid
import dataclasses


@dataclasses.dataclass
class Stock:
    code: uuid.UUID
    ticker: str
    name: str
    sector: str
    price: float

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
