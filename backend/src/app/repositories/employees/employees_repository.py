from werkzeug.security import generate_password_hash
from sqlalchemy import text

from ...models import Employee
from ....databases.exts import db


class EmployeesRepository:
    """
    The EmployeesRepository class provides methods for creating, retrieving, and sorting Employee objects.

    This class acts as a repository and uses the Employee model to perform operations related to employees.
    """

    def __init__(self, create_data=None):
        """
        Initialize a new EmployeesRepository.

        :param create_data: Optional dictionary containing the information about an employee.
        :type create_data: dict[str, any], optional
        """
        self.create_data = create_data
        self.employees_data = None

    def create(self):
        """
        Creates an Employee instance.

        This method takes the employee data provided during the initialization of the repository,
        validates it, and if valid, creates an Employee instance.

        :return: True if the employee was created, False otherwise.
        :rtype: bool
        """
        if not self._validate_create_data():
            return False

        new_employee = Employee(
            name=self.create_data["name"],
            surname=self.create_data["surname"],
            email=self.create_data["email"],
            password=generate_password_hash(self.create_data["password"]),
            phone=self.create_data["phone"],
            salary=self.create_data["salary"],
            position=self.create_data["position"]
        )
        db.session.add(new_employee)
        db.session.commit()
        return True

    def get_all(self):
        """
        Retrieves all Employee instances.

        This method fetches all the Employee instances from the database and stores the result in self.employees_data.

        :return: A list of all Employee instances.
        :rtype: list[Employee]
        """
        self.employees_data = Employee.query.all()
        return self.employees_data

    def sort_all(self, sort_data):
        """
        Sorts all Employee instances based on the provided sorting parameters and stores the result.

        :param sort_data: Dictionary containing the sorting parameters.
        :type sort_data: dict[str, any]

        :return: A sorted list of all Employee instances if the sorting parameters are valid, None otherwise.
        :rtype: list[Employee] or None
        """
        self.employees_data = None if not Employee.validate_sort_params(sort_data) else \
            Employee.query.order_by(self._prepare_employees_text_query(sort_data)).all()

        return self.employees_data

    def _prepare_employees_text_query(self, sort_data):
        """
        Prepare a text query for sorting employee data based on the provided parameters.

        This method generates a text query string using the sort_data dictionary.
        The sort_data items should contain the key-value pairs where the key is the column name
        and the value is the sort direction ('asc' or 'desc').

        :param sort_data: The data specifying how employees should be sorted.
        :type sort_data: dict[str, any]

        :return: The text query string for sorting employee data.
        :rtype: str
        """
        sort_text_query = ", ".join(f"{key} {Employee.QUERY_SORT_PARAMS[value]}" for key, value in sort_data.items())

        return text(sort_text_query)

    def _validate_create_data(self):
        """
        Validates the data for creating an Employee instance.

        This method takes in a dictionary containing information about an employee and validates this data.

        :return: True if the input data is valid, False otherwise.
        :rtype: bool
        """
        return Employee.validate_name(self.create_data.get("name")) and \
            Employee.validate_surname(self.create_data.get("surname")) and \
            Employee.validate_email(self.create_data.get("email")) and \
            Employee.validate_phone(self.create_data.get("phone")) and \
            Employee.validate_salary(self.create_data.get("salary")) and \
            Employee.validate_position(self.create_data.get("position")) and \
            Employee.query.filter_by(email=self.create_data.get("email")).first() is None
