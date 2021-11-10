from typing import List

from fastapi import APIRouter

from application.models.stock import StockModel
from pma.repository.memrepo import MemRepo
from pma.use_cases.stock_list import stock_list_use_case
from tests.fixtures.stocks import raw_stock_dicts

router = APIRouter()

stocks = raw_stock_dicts


@router.get('/stocks', response_model=List[StockModel])
def stock_list():
    repo = MemRepo(stocks)
    result = stock_list_use_case(repo)

    return result
