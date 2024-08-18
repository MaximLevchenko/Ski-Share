from ...repositories import EmployeeRepository


class EmployeeService:
    """
    The EmployeeService class provides methods for managing employee data.

    This class acts as a service for validating, updating, deleting, and preparing data related to an employee.

    :ivar employee_id: The ID of the employee.
    :type employee_id: int or str

    :ivar update_data: The data to update for the employee.
    :type update_data: dict[str, any] or None

    :ivar employee_repository: An instance of the EmployeeRepository class for interacting with employee data.
    :type employee_repository: EmployeeRepository
    """

    def __init__(self, employee_id, update_data=None):
        """
        Initialize a new instance of the EmployeeService class.

        :param employee_id: The ID of the employee.
        :type employee_id: int

        :param update_data: The data to update for the employee, defaults to None.
        :type update_data: dict[str, any] or None
        """
        self.employee_id = employee_id
        self.update_data = update_data
        self.employee_repository = EmployeeRepository(employee_id=self.employee_id)

    def update_employee_data(self):
        """
        Update the employee's data.

        This method uses the employee repository to update the employee's data.

        :return: A boolean indicating if the employee was successfully updated.
        :rtype: bool
        """
        return self.employee_repository.update(self.update_data)

    def validate_employee(self):
        """
        Validate the employee's existence.

        This method uses the employee repository to validate the existence of the employee based on their ID.

        :return: True if the employee exists, False otherwise.
        :rtype: bool
        """
        return True if self.employee_repository.get_employee() else False

    def delete_employee(self):
        """
        Delete the employee.

        This method uses the employee repository to delete the employee based on their ID.
        """
        self.employee_repository.delete()

    def prepare_response_with_employee_profile_data(self):
        """
        Prepare a response containing all data about the employee.

        This method uses the employee repository to retrieve all data about the employee.

        :return: A dictionary containing all data about the employee.
        :rtype: dict[str, any]
        """
        return self.employee_repository.get_employee_profile_data()
