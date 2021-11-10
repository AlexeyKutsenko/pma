import os

from pydantic import BaseSettings

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(BaseSettings):
    """
    Base configuration
    """


class ProductionConfig(Config):
    """
    Production configuration
    """


class DevelopmentConfig(Config):
    """
    Development configuration
    """


class TestingConfig(Config):
    """
    Testing configuration
    """
    TESTING: bool = True
