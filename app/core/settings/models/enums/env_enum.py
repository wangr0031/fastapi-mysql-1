from enum import Enum


class Env(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"
