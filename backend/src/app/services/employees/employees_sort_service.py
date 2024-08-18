from ...repositories import EmployeesRepository


class EmployeesSortService:
    """
    The EmployeesSortService class provides a method to sort employee data.

    This class acts as a service for sorting data related to employees.

    :ivar sort_data: The data specifying how employees should be sorted. This could include parameters like name,
                     email, salary, etc., along with the sort direction ('asc' or 'desc').
    :type sort_data: dict[str, any]
    """

    def __init__(self, sort_data):
        """
        Initialize a new instance of the EmployeesSortService class.

        :param sort_data: The data specifying how employees should be sorted.
        :type sort_data: dict[str, any]
        """
        self.sort_data = sort_data
        self.employees_repository = EmployeesRepository()

    def sort_employees(self):
        """
        Sort employee data based on the provided parameters.

        This method uses the EmployeesRepository to sort all employees based on the sorting data stored in `sort_data`
        during the initialization of the EmployeesSortService instance.

        :return: The sorted employee data or None if the sort data wasn't valid.
        :rtype: list[dict[str, any]] or None
        """
        return self.employees_repository.sort_all(self.sort_data)

