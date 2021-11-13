from pma.responses import (
    ResponseSuccess,
    ResponseFailure,
    ResponseTypes,
    build_response_from_invalid_request
)


def stock_list_use_case(repo, request):
    if not request:
        return build_response_from_invalid_request(request)
    try:
        stocks = repo.list(filters=request.filters)
        return ResponseSuccess(stocks)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
