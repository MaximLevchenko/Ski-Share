from ...services import CurrentUserService


class CurrentUserController:
    """The CurrentUserController class provides methods for managing the current user on the controller level.

    This class acts as a controller for retrieving and preparing data related to the current user.

    :ivar current_user_identity_data: The identity data of the current user.
    :type current_user_identity_data: str

    :ivar current_user_service: An instance of the CurrentUserService class for performing operations
                                related to the current user.
    :type current_user_service: CurrentUserService
    """

    def __init__(self, current_user_identity_data):
        """
        Initialize a new instance of the CurrentUserController class.

        :param current_user_identity_data: The identity data of the current user.
        :type current_user_identity_data: str
        """
        self.current_user_identity_data = current_user_identity_data
        self.current_user_service = CurrentUserService(self.current_user_identity_data)

    def find_user_by_identity(self):
        """
        Find the current user by their identity data.

        This method uses the current user service to retrieve the current user based on their identity data.
        """
        self.current_user_service.find_current_user_by_identity_data()

    def create_response(self):
        """
        Prepare a response containing all data about the current user.

        This method uses the current user service to retrieve all data about the current user and prepare a response.

        :return: A response containing the current user data and a 200 status code.
        :rtype: tuple[flask.Response, int]
        """
        return self.current_user_service.prepare_current_user_response(), 200
