from app.core.settings.models.settings_definition import SettingsDefinition


class UnitTestSettings(SettingsDefinition):
    ENV: str = "test"
    LOG_LEVEL: str = "debug"
    DATABASE_URL: str = "mysql+pymysql://root:supersecret@localhost:3306/test"
