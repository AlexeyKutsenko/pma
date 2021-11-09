#!/usr/bin/env python

from pma.repository.memrepo import MemRepo
from pma.use_cases.stock_list import stock_list_use_case

repo = MemRepo([])
result = stock_list_use_case(repo)

print(result)
