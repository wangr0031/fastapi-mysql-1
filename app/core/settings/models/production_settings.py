from app.core.settings.models.settings_definition import SettingsDefinition


class ProductionSettings(SettingsDefinition):
    ENV: str = "production"
