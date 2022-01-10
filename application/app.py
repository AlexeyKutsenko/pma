from functools import lru_cache
from importlib import import_module

from fastapi import FastAPI

from application.rest import stock


def create_app():
    app = FastAPI()
    app.include_router(stock.router)
    return app


@lru_cache()
def get_settings(config_name=''):
    config = import_module('application.config')
    settings = getattr(config, f'{config_name.capitalize()}Config')
    return settings()
