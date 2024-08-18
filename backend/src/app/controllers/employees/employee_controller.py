from ...services import EmployeeService
from ..exceptions import ControllerException


class EmployeeController:
    """
    The EmployeeController class provides methods for managing employee data.

    This class acts as a controller for validating, updating, deleting, and preparing responses related to an employee.

    :ivar employee_id: The ID of the employee.
    :type employee_id: int

    :ivar update_data: The data to update for the employee.
    :type update_data: dict[str, any] or None

    :ivar employee_service: An instance of the EmployeeService class for managing employee data.
    :type employee_service: EmployeeService
    """

    def __init__(self, employee_id, update_data=None):
        """
        Initialize a new instance of the EmployeeController class.

        :param employee_id: The ID of the employee.
        :type employee_id: int

        :param update_data: The data to update for the employee, defaults to None.
        :type update_data: dict[str, any] or None
        """
        self.employee_id = employee_id
        self.update_data = update_data
        self.employee_service = EmployeeService(self.employee_id, self.update_data)

    def validate_employee(self):
        """
        Validate the employee's existence.

        This method uses the employee service to validate the existence of the employee based on their ID.
        If the employee does not exist, it raises a ControllerException.

        :raises ControllerException: If the employee does not exist. HTTP status code 404.
        """
        if not self.employee_service.validate_employee():
            raise ControllerException("Employee not found.", 404)

    def update_employee(self):
        """
        Update the employee's data.

        This method uses the employee service to update the employee's data.
        If the update data is invalid, it raises a ControllerException.

        :raises ControllerException: If the employee update data is invalid. HTTP status code 400.
        """
        if not self.employee_service.update_employee_data():
            raise ControllerException("Invalid employee update data.", 400)

    def delete_employee(self):
        """
        Delete the employee.

        This method uses the employee service to delete the employee based on their ID.
        """
        self.employee_service.delete_employee()

    def create_response_with_employee_profile_data(self):
        """
        Create a response containing all data about the employee.

        This method uses the employee service to retrieve all data about the employee and prepares a response.

        :return: A dictionary containing all data about the employee and HTTP status code of 200.
        :rtype: tuple[dict[str, any], int]
        """
        return self.employee_service.prepare_response_with_employee_profile_data(), 200

    def create_response_with_successful_update_message(self):
        """
        Create a response with a successful update message.

        :return: A dictionary containing a success message and HTTP status code of 200.
        :rtype: tuple[dict[str, str], int]
        """
        return {"message": "Employee updated successfully."}, 200

    def create_response_with_successful_delete_message(self):
        """
        Create a response with a successful delete message.

        :return: A dictionary containing a success message and HTTP status code of 200.
        :rtype: tuple[dict[str, str], int]
        """
        return {"message": "Employee deleted successfully."}, 200
