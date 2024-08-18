from flask import make_response

from ...services import LoginService
from ..exceptions import ControllerException


class LoginController:
    """
    The LoginController class provides methods for managing user login procedures.

    This class acts as a controller for validating and preparing login response.

    :ivar login_data: The login data of the user.
    :type login_data: dict[str, any]

    :ivar login_service: An instance of the LoginService class for interacting with login procedures.
    :type login_service: LoginService
    """

    def __init__(self, login_data):
        """
        Initialize a new instance of the LoginController class.

        :param login_data: The login data of the user.
        :type login_data: dict[str, any]
        """
        self.login_data = login_data
        self.login_service = LoginService(self.login_data)

    def validate_user(self):
        """
        Validate the user login data.

        This method uses the login service to validate the user login data.
        If the login data is invalid, raises a ControllerException.

        :raises ControllerException: If the login data is invalid.
        """
        if not self.login_service.validate_user_login_data():
            raise ControllerException("Invalid email or password.", 401)

    def create_response(self):
        """
        Prepare a response containing all data about the user.

        This method uses the login service to prepare a response containing all data about the user.

        :return: A response containing all data about the user, and the HTTP 200 status code.
        :rtype: tuple[flask.Response, int]
        """
        return make_response(self.login_service.prepare_login_response(), 200)
