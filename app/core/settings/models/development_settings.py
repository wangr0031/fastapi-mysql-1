from app.core.settings.models.settings_definition import SettingsDefinition


class DevelopmentSettings(SettingsDefinition):
    ENV: str = "development"
    LOG_LEVEL: str = "debug"
    APP_HOST: str = "127.0.0.1"
    DATABASE_URL: str = "mysql+pymysql://root:supersecret@localhost:3306/dbname"
    HOT_RELOAD = True
