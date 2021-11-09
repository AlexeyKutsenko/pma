import uuid

import pytest

from pma.domain.stock import Stock


@pytest.fixture
def domain_stocks():
    stock_1 = Stock(
        code=uuid.uuid4(),
        ticker='NVDA',
        name='NVIDIA CORP',
        sector='Information Technology',
        price=306.57
    )
    stock_2 = Stock(
        code=uuid.uuid4(),
        ticker='AVGO',
        name='BROADCOM INC',
        sector='Information Technology',
        price=557.80
    )
    stock_3 = Stock(
        code=uuid.uuid4(),
        ticker='INTC',
        name='INTEL CORPORATION CORP',
        sector='Information Technology',
        price=51.20
    )
    stock_4 = Stock(
        code=uuid.uuid4(),
        ticker='QCOM',
        name='QUALCOMM INC',
        sector='Information Technology',
        price=166.74
    )

    return [stock_1, stock_2, stock_3, stock_4]


@pytest.fixture
def stock_dicts():
    return [
        {
            "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "ticker": "NVDA",
            "name": "NVIDIA CORP",
            "sector": "Information Technology",
            "price": 306.57
        },
        {
            "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
            "ticker": "AVGO",
            "name": "BROADCOM INC",
            "sector": "Information Technology",
            "price": 557.80
        },
        {
            "code": "913694c6-435a-4366-ba0d-da5334a611b2",
            "ticker": "INTC",
            "name": "INTEL CORPORATION CORP",
            "sector": "Information Technology",
            "price": 51.20
        },
        {
            "code": "eed76e77-55c1-41ce-985d-ca49bf6c0585",
            "ticker": "QCOM",
            "name": "QUALCOMM INC",
            "sector": "Information Technology",
            "price": 166.74
        }
    ]
