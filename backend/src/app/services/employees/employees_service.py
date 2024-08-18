from ...repositories import EmployeesRepository


class EmployeesService:
    """
    The EmployeesService class provides methods for creating a new employee and retrieving data of all employees.

    :ivar create_data: The data for creating a new employee. This should be a dictionary that includes the fields
                       necessary for creating an Employee instance. It defaults to None.
    :type create_data: dict[str, any] or None
    """

    def __init__(self, create_data=None):
        """
        Initialize a new instance of the EmployeesService class.

        :param create_data: The data for creating a new employee. This should be a dictionary that includes the fields
                            necessary for creating an Employee instance. It defaults to None.
        :type create_data: dict[str, any] or None
        """
        self.create_data = create_data
        self.employees_repository = EmployeesRepository(self.create_data)

    def create_employee(self):
        """
        Create a new employee using the create_data provided when initializing the EmployeesService class.

        This method uses the EmployeesRepository to create a new Employee instance.

        :return: True if the employee was created successfully, False otherwise.
        :rtype: bool
        """
        return self.employees_repository.create()

    def prepare_response_with_employees_data(self):
        """
        Retrieve and prepare a list of data about all employees.

        This method uses the EmployeesRepository to get a list of all Employee instances, each represented as a
        dictionary of field values.

        :return: A list of dictionaries, where each dictionary contains data about a specific employee.
        :rtype: list[dict[str, any]]
        """
        return self.employees_repository.get_all()
