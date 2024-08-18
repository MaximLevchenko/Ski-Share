from ...databases.exts import db


class Employee(db.Model):
    """
    The Employee data model class describes the data structure of an employee in the database.

    :ivar id: Unique identifier for an employee.
    :type id: int

    :ivar name: Name of the employee.
    :type name: str

    :ivar surname: Surname of the employee.
    :type surname: str

    :ivar email: Unique email for the employee.
    :type email: str

    :ivar password: Hashed password for the employee.
    :type password: str

    :ivar phone: Unique phone number of the employee.
    :type phone: str

    :ivar salary: Salary of the employee.
    :type salary: int

    :ivar position: Position of the employee, can be one of EMPLOYEE_POSITIONS.
    :type position: str

    :ivar rentals: List of rentals that the employee has conducted.
    :type rentals: list[rental]

    :ivar LATEST_RENTALS_COUNT: The number of the latest rentals to return.
    :type LATEST_RENTALS_COUNT: int

    :ivar EMPLOYEE_POSITIONS: A list of valid positions that an employee can have.
    :type EMPLOYEE_POSITIONS: list[str]

    :ivar SORT_ATTRIBUTES: A list of attributes on which we can sort the employees.
    :type SORT_ATTRIBUTES: list[str]

    :ivar QUERY_SORT_PARAMS: A dictionary defining the sort order based on certain key strings.
                             Each key string corresponds to a certain sort order.
    :type QUERY_SORT_PARAMS: dict[str, str]
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    salary = db.Column(db.Integer, nullable=True)
    position = db.Column(db.String(20), nullable=False)
    rentals = db.relationship('Rental', backref='employee')

    LATEST_RENTALS_COUNT = 3

    EMPLOYEE_POSITIONS = ["Manager", "Assistant"]

    SORT_ATTRIBUTES = ["id", "name", "surname", "email", "phone", "salary", "position"]

    QUERY_SORT_PARAMS = {"abc": "asc", "zyx": "desc",
                         "lowest": "asc", "highest": "desc",
                         "oldest": "asc", "latest": "desc",
                         "Free": "asc", "Rented": "desc"}

    def __repr__(self):
        """
        Return a string representation of the employee instance.

        :return: String representation of the Employee object.
        :rtype: Employee
        """
        return f"<Employee-{self.id}>"

    @staticmethod
    def validate_name(employee_name):
        """
        Validate the provided employee name.

        :param employee_name: Name of the employee.
        :type employee_name: str

        :return: Returns True if the name is a non-empty string, False otherwise.
        :rtype: bool
        """
        return False if employee_name is None or not isinstance(employee_name, str) or len(employee_name) == 0 else True

    @staticmethod
    def validate_surname(employee_surname):
        """
        Validate the provided employee surname.

        :param employee_surname: Surname of the employee.
        :type employee_surname: str

        :return: Returns True if the surname is a non-empty string, False otherwise.
        :rtype: bool
        """
        return False if employee_surname is None or not isinstance(employee_surname, str) or len(employee_surname) == 0\
            else True

    @staticmethod
    def validate_email(employee_email):
        """
        Validate the provided employee email.

        :param employee_email: Email of the employee.
        :type employee_email: str

        :return: Returns True if the email is a string that contains both '@' and '.', False otherwise.
        :rtype: bool
        """
        return False if employee_email is None or not isinstance(employee_email, str) or len(employee_email) < 6 or \
            '@' not in employee_email or '.' not in employee_email else True

    @staticmethod
    def validate_phone(employee_phone):
        """
        Validate the provided employee phone.

        :param employee_phone: Phone number of the employee.
        :type employee_phone: str

        :return: Returns True if the phone number is a string of length at least 8 and contains '+', False otherwise.
        :rtype: bool
        """
        return False if employee_phone is None or not isinstance(employee_phone, str) or len(employee_phone) < 8 or \
            '+' not in employee_phone else True

    @staticmethod
    def validate_salary(employee_salary):
        """
        Validate the provided employee salary.

        :param employee_salary: Salary of the employee.
        :type employee_salary: int

        :return: Returns True if the salary is a non-negative integer, False otherwise.
        :rtype: bool
        """
        return False if employee_salary is None or not isinstance(employee_salary, int) or employee_salary < 0 else True

    @staticmethod
    def validate_position(employee_position):
        """
        Validate the provided employee position.

        :param employee_position: Position of the employee.
        :type employee_position: str

        :return: Returns True if the position is one of the valid EMPLOYEE_POSITIONS, False otherwise.
        :rtype: bool
        """
        return False if employee_position is None or employee_position not in Employee.EMPLOYEE_POSITIONS else True

    @staticmethod
    def validate_sort_params(sort_data):
        """
        Validate the provided sorting parameters.

        :param sort_data: Dictionary of sorting parameters.
        :type sort_data: dict

        :return: Returns True if all keys and values are valid according to SORT_ATTRIBUTES and QUERY_SORT_PARAMS,
                 False otherwise.
        :rtype: bool
        """
        return all(key in Employee.SORT_ATTRIBUTES and value in Employee.QUERY_SORT_PARAMS.keys()
                   for key, value in sort_data.items())
