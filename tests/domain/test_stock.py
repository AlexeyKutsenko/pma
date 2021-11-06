import uuid

from pma.domain.stock import Stock


def test_stock_model_init():
    code = uuid.uuid4()
    stock = Stock(
        code,
        ticker='AVGO',
        name='BROADCOM INC',
        sector='Information Technology',
        price=506,
    )

    assert stock.code == code
    assert stock.ticker == 'AVGO'
    assert stock.name == 'BROADCOM INC'
    assert stock.sector == 'Information Technology'
    assert stock.price == 506
