from datetime import datetime

from ....databases.exts import db
from ...models import BlacklistToken


class BlacklistTokensRepository:
    """
    The BlacklistTokensRepository class provides methods for creating and storing BlacklistToken objects.

    This class acts as a repository and uses the BlacklistToken model to perform operations
    related to blacklisted tokens.
    """

    def __init__(self, jti):
        """
        Initialize a new BlacklistToken Repository.

        :param jti: The jti of a token.
        :type jti: str
        """
        self.blacklist_token = BlacklistToken(jti=jti)

    def save(self):
        """
        Saves a BlacklistToken instance to the database.

        This method sets the adding_time attribute of the BlacklistToken instance to the current
        time, and then adds it to the database session and commits it.
        """
        self.blacklist_token.adding_time = datetime.utcnow()
        db.session.add(self.blacklist_token)
        db.session.commit()
