from application.app import get_settings
from application.config import Config, TestingConfig


def test_get_settings():
    settings = get_settings()
    assert Config == type(settings)

    settings = get_settings('testing')
    assert settings.TESTING is True
    assert TestingConfig == type(settings)
