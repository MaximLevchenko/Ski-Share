import os

from .base_config import BaseConfig


class ProdConfig(BaseConfig):
    """
    This class represents the production configuration for the project, which inherits from the base configuration.

    It defines configuration settings specific to a production environment, including the database URI,
    DEBUG, SQLALCHEMY_ECHO and SQLALCHEMY_TRACK_MODIFICATIONS settings.

    :ivar SQLALCHEMY_DATABASE_URI: The URI for the production database.
    :type SQLALCHEMY_DATABASE_URI: str

    :ivar DEBUG: A setting that determines if the application should run in debug mode.
    :type DEBUG: bool

    :ivar SQLALCHEMY_ECHO: A setting that determines if SQLAlchemy should log SQL queries to the console.
    :type SQLALCHEMY_ECHO: bool

    :ivar SQLALCHEMY_TRACK_MODIFICATIONS: A setting that determines if SQLAlchemy should track modifications to objects
                                          and emit signals.
    :type SQLALCHEMY_TRACK_MODIFICATIONS: bool
    """
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///prod.db")
    DEBUG = os.getenv("DEBUG", False)
    SQLALCHEMY_ECHO = os.getenv("ECHO", False)
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)

