from pydantic import BaseSettings


class SettingsDefinition(BaseSettings):
    ENV: str

    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    HOT_RELOAD: bool = False
    LOG_LEVEL: str = "info"

    DATABASE_URL: str
