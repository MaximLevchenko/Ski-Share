from ...services import EmployeesSortService
from ..exceptions import ControllerException


class EmployeesSortController:
    """
    The EmployeesSortController class provides methods for sorting employees and creating an appropriate response.

    This class acts as a controller for handling requests related to sorting employees.

    :ivar sort_data: The data specifying how employees should be sorted.
    :type sort_data: dict[str, any]

    :ivar sorted_employees: The sorted employee data.
    :type sorted_employees: list[dict[str, any]] or None
    """

    def __init__(self, sort_data):
        """
        Initialize a new instance of the EmployeesSortController class.

        :param sort_data: The data specifying how employees should be sorted.
        :type sort_data: dict[str, any]
        """
        self.sort_data = sort_data
        self.sorted_employees = None
        self.employees_sort_service = EmployeesSortService(self.sort_data)

    def sort_employees(self):
        """
        Sort employee data based on the provided parameters.

        This method uses the EmployeesSortService to sort all employees based on the sorting data.
        If the sorting fails, it raises a ControllerException.

        :raise ControllerException: If the sorting fails due to invalid sort QUERY parameters.
        """
        self.sorted_employees = self.employees_sort_service.sort_employees()
        if self.sorted_employees is None:
            raise ControllerException("Invalid sort QUERY parameters.", 400)

    def create_response_with_sorted_employees_data(self):
        """
        Create a response containing the sorted employee data.

        This method prepares a response with the sorted employee data.
        The response includes a 200 status code.

        :return: The response containing the sorted employee data and a 200 status code.
        :rtype: tuple[list[dict[str, any]], int]
        """
        return self.sorted_employees, 200
