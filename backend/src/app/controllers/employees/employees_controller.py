from ...services import EmployeesService
from ..exceptions import ControllerException


class EmployeesController:
    """
    The EmployeesController class provides methods for handling employee-related requests.

    This class acts as a controller that uses the EmployeesService for creating a new employee
    and preparing data related to all employees.

    :ivar employee_data: The data for creating a new employee.
    :type employee_data: dict[str, any] or None

    :ivar employees_service: An instance of the EmployeesService class for managing employees' data.
    :type employees_service: EmployeesService
    """

    def __init__(self, employee_data=None):
        """
        Initialize a new instance of the EmployeesController class.

        :param employee_data: The data for creating a new employee, defaults to None.
        :type employee_data: dict[str, any] or None
        """
        self.employee_data = employee_data
        self.employees_service = EmployeesService(employee_data)

    def create_employee(self):
        """
        Create a new employee.

        This method uses the employees service to create a new employee with the provided data.
        If the employee data is invalid, it raises a ControllerException.

        :raise ControllerException: If the employee data is invalid with HTTP code 400.
        """
        if not self.employees_service.create_employee():
            raise ControllerException("Invalid employee data.", 400)

    def create_response_with_employees_data(self):
        """
        Prepare a response containing data about all employees.

        This method uses the employees service to retrieve data about all employees.

        :return: A tuple where the first item is a list of data about all employees and
                 the second item is the HTTP status code 200.
        :rtype: tuple[list[dict[str, any]], int]
        """
        return self.employees_service.prepare_response_with_employees_data(), 200

    def create_response_with_successful_create_message(self):
        """
        Prepare a response containing a success message for employee creation.

        :return: A tuple where the first item is a dictionary containing a success message and
                 the second item is the HTTP status code 200.
        :rtype: tuple[dict[str, str], int]
        """
        return {"message": "Employee created successfully."}, 200
