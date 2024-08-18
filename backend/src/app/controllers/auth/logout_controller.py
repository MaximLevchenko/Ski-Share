from flask import make_response

from ...services import LogoutService


class LogoutController:
    """
    The LogoutController class provides methods for managing logout procedures.

    This class acts as a controller for handling logout operations.

    :ivar user_jti: The JWT token identifier (jti) of the user.
    :type user_jti: str

    :ivar logout_service: An instance of the LogoutService class for managing logout operations.
    :type logout_service: LogoutService
    """

    def __init__(self, user_jti):
        """
        Initialize a new instance of the LogoutController class.

        :param user_jti: The JWT token identifier (jti) of the user.
        :type user_jti: str
        """
        self.user_jti = user_jti
        self.logout_service = LogoutService(self.user_jti)

    def revoke_user_jti(self):
        """
        Revoke the user's JWT token.

        This method uses the LogoutService to add the user's token to the blacklist.
        """
        self.logout_service.remove_user_jti_to_blacklist()

    def create_response(self):
        """
        Create a response indicating successful logout.

        This method uses the LogoutService to prepare a response with a message indicating successful logout.

        :return: A response containing the message and a 200 status code.
        :rtype: tuple[flask.Response, int]
        """
        return make_response(self.logout_service.prepare_logout_response({"message": "Successfully logged out."}), 200)
