from ...services import RefreshService
from ..exceptions import ControllerException


class RefreshController:
    """
    The RefreshController class provides methods for managing the refresh operation of JWT tokens.

    This class acts as a controller for the refresh token operation. It validates the refresh token
    and prepares a response containing the new access token.

    :ivar user_refresh_token: The refresh token of the user.
    :type user_refresh_token: str

    :ivar refresh_service: An instance of the RefreshService class for managing the refresh operation.
    :type refresh_service: RefreshService
    """

    def __init__(self, user_refresh_token):
        """
        Initialize a new instance of the RefreshController class.

        :param user_refresh_token: The refresh token of the user.
        :type user_refresh_token: str
        """
        self.user_refresh_token = user_refresh_token
        self.refresh_service = RefreshService(user_refresh_token)

    def validate_user_refresh_token(self):
        """
        Validate the user's refresh token.

        This method uses the RefreshService to validate the refresh token. If the refresh token is invalid,
        it raises a ControllerException.

        :raises ControllerException: If the refresh token is invalid.
        """
        if not self.refresh_service.validate_user_refresh_data():
            raise ControllerException("Invalid refresh token.", 401)

    def create_response(self):
        """
        Prepare a response containing the new access token.

        This method uses the RefreshService to prepare a response containing the new access token.

        :return: A dictionary containing the new access token and a 200 HTTP status code.
        :rtype: tuple(dict[str, str], int)
        """
        return self.refresh_service.prepare_refresh_response(), 200
