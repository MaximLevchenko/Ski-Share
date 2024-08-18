from flask import jsonify
from flask_jwt_extended import unset_jwt_cookies

from ...repositories import BlacklistTokensRepository


class LogoutService:
    """
    The LogoutService class provides methods for managing logout procedures.

    This class acts as a service for revoking tokens and preparing data related to logout.

    :ivar logout_data: The logout data of the user.
    :type logout_data: str

    :ivar revoke_token: An instance of the BlacklistToken model representing the token to be revoked.
    :type revoke_token: BlacklistToken
    """

    def __init__(self, logout_data):
        """
        Initialize a new instance of the LogoutService class.

        :param logout_data: The logout data of the user.
        :type logout_data: str
        """
        self.logout_data = logout_data
        self.revoke_token = BlacklistTokensRepository(self.logout_data)

    def remove_user_jti_to_blacklist(self):
        """
        Add the token to the blacklist.

        This method uses the BlacklistTokensRepository to add the token to the blacklist.
        """
        BlacklistTokensRepository.save(self.revoke_token)

    def prepare_logout_response(self, message):
        """
        Prepare a response containing a message and unset JWT cookies.

        This method prepares a response with a message indicating successful logout and unsets JWT cookies.

        :param message: A message indicating successful logout.
        :type message: dict[str, str]

        :return: A response containing the message and unset JWT cookies.
        :rtype: flask.Response
        """
        logout_response = jsonify(message)
        unset_jwt_cookies(logout_response)

        return logout_response
