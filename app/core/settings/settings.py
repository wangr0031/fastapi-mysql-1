import os

from app.core.settings.models.development_settings import DevelopmentSettings
from app.core.settings.models.enums.env_enum import Env
from app.core.settings.models.production_settings import ProductionSettings
from app.core.settings.models.settings_definition import SettingsDefinition
from app.core.settings.models.unit_test_settings import UnitTestSettings


def get_config(env: Env) -> SettingsDefinition:
    """
    Return the application settings
    :return: BaseSettings
    """
    if env == Env.DEVELOPMENT:
        return DevelopmentSettings()
    elif env == Env.PRODUCTION:
        return ProductionSettings()
    elif env == Env.TEST:
        return UnitTestSettings()


def set_config(env: Env) -> SettingsDefinition:
    """
    Update the settings
    :param env: Env
    :return:
    """
    global config
    config = get_config(env)
    return config


config: SettingsDefinition = set_config(Env(os.getenv("ENV", "development")))
