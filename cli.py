#!/usr/bin/env python

from pma.repository.memrepo import MemRepo
from pma.use_cases.stock_list import stock_list_use_case
from pma.requests.stock_list import build_stock_list_request
from tests.fixtures.stocks import raw_stock_dicts

request = build_stock_list_request()
repo = MemRepo(raw_stock_dicts)
result = stock_list_use_case(repo, request)

print([stock.to_dict() for stock in result.value])
