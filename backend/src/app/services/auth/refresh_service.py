from flask_jwt_extended import decode_token, create_access_token


class RefreshService:
    """
    The RefreshService class provides methods for managing JWT refresh procedures.

    This class acts as a service for validating and preparing data related to refresh operations.

    :ivar refresh_data: The refresh token data of the user.
    :type refresh_data: str

    :ivar user_identity: The identity of the user extracted from the refresh token.
    :type user_identity: str
    """

    def __init__(self, refresh_data):
        """
        Initialize a new instance of the RefreshService class.

        :param refresh_data: The refresh token data of the user.
        :type refresh_data: str
        """
        self.refresh_data = refresh_data
        self.user_identity = decode_token(self.refresh_data).get("sub")

    def validate_user_refresh_data(self):
        """
        Validate the user refresh token data.

        This method uses the JWT decode function to extract the user identity from the refresh token.

        :return: The identity of the user if the refresh token data is valid, None otherwise.
        :rtype: str or None
        """
        return self.user_identity

    def prepare_refresh_response(self):
        """
        Prepare a response containing the new access token.

        This method generates a new JWT access token using the user identity and prepares a response.

        :return: A dictionary containing the new access token.
        :rtype: dict[str, str]
        """
        return {"access_token": create_access_token(identity=self.user_identity)}
