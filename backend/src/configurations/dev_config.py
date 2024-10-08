import os

from .base_config import BaseConfig


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
DB_DIR = os.path.join(PARENT_DIR, "databases")


class DevConfig(BaseConfig):
    """
    This class represents the development configuration for the project, which inherits from the base configuration.

    It defines configuration settings specific to a development environment, including the database URI,
    SQLALCHEMY_ECHO and DEBUG settings.

    :ivar SQLALCHEMY_DATABASE_URI: The URI for the development database.
    :type SQLALCHEMY_DATABASE_URI: str

    :ivar SQLALCHEMY_ECHO: A setting that determines if SQLAlchemy should log SQL queries to the console.
    :type SQLALCHEMY_ECHO: bool

    :ivar DEBUG: A setting that determines if the application should run in debug mode.
    :type DEBUG: bool
    """
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(DB_DIR, 'dev.db')
    SQLALCHEMY_ECHO = True
    DEBUG = True
