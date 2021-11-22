import os
from typing import List

from fastapi import APIRouter, Request

from application.models.stock import StockModel
from pma.repository.postgresrepo import PostgresRepo
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

postgres_configuration = {
    "POSTGRES_USER": os.environ["POSTGRES_USER"],
    "POSTGRES_PASSWORD": os.environ["POSTGRES_PASSWORD"],
    "POSTGRES_HOSTNAME": os.environ["POSTGRES_HOSTNAME"],
    "POSTGRES_PORT": os.environ["POSTGRES_PORT"],
    "APPLICATION_DB": os.environ["APPLICATION_DB"],
}


@router.get('/stocks', response_model=List[StockModel])
def stock_list(request: Request):
    qrystr_params = {'filters': {}}

    if request.query_params:
        for key, value in dict(request.query_params).items():
            qrystr_params['filters'][key] = value

    request_object = build_stock_list_request(filters=qrystr_params['filters'])

    repo = PostgresRepo(postgres_configuration)
    result = stock_list_use_case(repo, request_object)

    return result.value
