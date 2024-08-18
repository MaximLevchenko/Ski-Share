import os

from .base_config import BaseConfig


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
DB_DIR = os.path.join(PARENT_DIR, "databases")


class TestConfig(BaseConfig):
    """
    This class represents the testing configuration for the project, which inherits from the base configuration.

    It defines configuration settings specific to a testing environment, including the database URI,
    SQLALCHEMY_ECHO, and TESTING settings.

    :ivar SQLALCHEMY_DATABASE_URI: The URI for the testing database.
    :type SQLALCHEMY_DATABASE_URI: str

    :ivar SQLALCHEMY_ECHO: A setting that determines if SQLAlchemy should log SQL queries to the console.
    :type SQLALCHEMY_ECHO: bool

    :ivar TESTING: A setting that determines if the application should run in testing mode.
    :type TESTING: bool
    """
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(DB_DIR, 'test.db')
    SQLALCHEMY_ECHO = False
    TESTING = True
