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


def test_stock_model_from_dict():
    code = uuid.uuid4()
    init_dict = {
        'code': code,
        'ticker': 'AVGO',
        'name': 'BROADCOM INC',
        'sector': 'Information Technology',
        'price': 506
    }

    stock = Stock.from_dict(init_dict)
    assert stock.to_dict() == init_dict


def test_stock_model_to_dict():
    init_dict = {
        'code': uuid.uuid4(),
        'ticker': 'AVGO',
        'name': 'BROADCOM INC',
        'sector': 'Information Technology',
        'price': 506
    }

    stock = Stock.from_dict(init_dict)
    assert stock.to_dict() == init_dict


def test_stock_model_comparison():
    init_dict = {
        'code': uuid.uuid4(),
        'ticker': 'AVGO',
        'name': 'BROADCOM INC',
        'sector': 'Information Technology',
        'price': 506
    }

    stock1 = Stock.from_dict(init_dict)
    stock2 = Stock.from_dict(init_dict)

    assert stock1 == stock2