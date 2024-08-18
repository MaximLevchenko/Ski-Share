from ...repositories import EmployeeRepository


class CurrentUserService:
    """
    The CurrentUserService class provides methods for managing the current user.

    This class acts as a service for retrieving and preparing data related to the current user.

    :ivar current_user_identity_data: The identity data of the current user.
    :type current_user_identity_data: str

    :ivar employee_repository: An instance of the EmployeeRepository class for interacting with employee data.
    :type employee_repository: EmployeeRepository

    :ivar current_user: An instance of the Employee model representing the current user.
    :type current_user: Employee or None
    """

    def __init__(self, current_user_identity_data):
        """
        Initialize a new instance of the CurrentUserService class.

        :param current_user_identity_data: The identity data of the current user.
        :type current_user_identity_data: str
        """
        self.current_user_identity_data = current_user_identity_data
        self.employee_repository = EmployeeRepository(employee_email=self.current_user_identity_data)
        self.current_user = None

    def find_current_user_by_identity_data(self):
        """
        Find the current user by their identity data.

        This method uses the employee repository to retrieve the current user based on their identity data.
        The result is stored in the current_user attribute.
        """
        self.current_user = self.employee_repository.get_employee()

    def prepare_current_user_response(self):
        """
        Prepare a response containing all data about the current user.

        This method uses the employee repository to retrieve all data about the current user.

        :return: A dictionary containing all data about the current user.
        :rtype: dict[str, any]
        """
        return self.employee_repository.get_employee_profile_data()
