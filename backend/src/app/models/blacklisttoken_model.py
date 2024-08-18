from ...databases.exts import db


class BlacklistToken(db.Model):
    """
    The BlacklistToken data model class describes the data structure of a blacklist token in the database.

    :ivar id: Unique identifier for a token.
    :type id: int

    :ivar jti: Unique JWT identifier (jti) for the token.
    :type jti: str

    :ivar adding_time: The time when the token was added to the blacklist.
    :type adding_time: datetime.datetime
    """
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120), unique=True, nullable=False, index=True)
    adding_time = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        """
        Method that returns a string representation of the BlacklistToken instance.

        :return: String representation of the BlacklistToken instance.
        :rtype: BlacklistToken
        """
        return f"<BlacklistToken-{self.id}>"
