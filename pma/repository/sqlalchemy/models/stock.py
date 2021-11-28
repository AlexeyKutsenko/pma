from sqlalchemy import Column, Integer, Float, String

from pma.repository.sqlalchemy.base_class import Base


class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)

    code = Column(String(36), nullable=False)
    ticker = Column(String)
    name = Column(String)
    sector = Column(String)
    price = Column(Float)
