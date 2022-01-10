from typing import List

from fastapi import APIRouter, Request

from application.models.stock import StockModel
from pma.repository import RepositoryRegistry
from pma.requests.stock_list import build_stock_list_request
from pma.responses import ResponseTypes
from pma.use_cases.stock_list import stock_list_use_case

router = APIRouter()

STATUS_CODES = {
    ResponseTypes.SUCCESS: 200,
    ResponseTypes.RESOURCE_ERROR: 404,
    ResponseTypes.PARAMETERS_ERROR: 400,
    ResponseTypes.SYSTEM_ERROR: 500
}


@router.get('/stocks', response_model=List[StockModel])
def stock_list(request: Request):
    qrystr_params = {'filters': {}}

    if request.query_params:
        for key, value in dict(request.query_params).items():
            qrystr_params['filters'][key] = value

    request_object = build_stock_list_request(filters=qrystr_params['filters'])

    repo = RepositoryRegistry.get_for('stock')
    result = stock_list_use_case(repo, request_object)

    return result.value
