from ....databases.exts import db
from ...models import Employee


class EmployeeRepository:
    """
    The EmployeeRepository class encapsulates the logic necessary to access the database and
    perform CRUD operations on the Employee model.

    :ivar employee_id: Unique identifier for an employee. Used for retrieving an existing employee by ID.
    :type employee_id: int or None

    :ivar employee_email: Unique email for an employee. Used for retrieving an existing employee by email.
    :type employee_email: str or None

    :ivar employee: Instance of the Employee model representing an employee in the database.
    :type employee: employee or None
    """

    def __init__(self, employee_id=None, employee_email=None):
        """
        Initialize an instance of the EmployeeRepository class.

        The constructor tries to find an Employee instance based on the provided employee_id or employee_email. If an
        Employee instance is found, it is assigned to the employee instance variable.

        :param employee_id: Unique identifier of an employee. Used to retrieve an existing employee by ID.
        :type employee_id: int or None

        :param employee_email: Unique email of an employee. Used to retrieve an existing employee by email.
        :type employee_email: str or None
        """
        self.employee_id = employee_id
        self.employee_email = employee_email
        self.employee = None

        if self.employee_id is not None:
            self.employee = self._find_by_id()

        if self.employee_email is not None:
            self.employee = self._find_by_email()

    def save(self):
        """
        Save the current employee instance to the database.
        """
        db.session.add(self.employee)
        db.session.commit()

    def delete(self):
        """
        Delete the current employee instance from the database.
        """
        db.session.delete(self.employee)
        db.session.commit()

    def update(self, update_data):
        """
        Update the current employee instance based on the provided update data.

        :param update_data: Dictionary containing new values for the employee's attributes.
        :type update_data: dict[str, any]

        :return: Returns True if the update was successful, False otherwise.
        :rtype: bool
        """
        if not self._validate_update_data(update_data):
            return False

        if update_data.get("new_phone") is not None:
            self.employee.phone = update_data.get("new_phone")

        if update_data.get("new_salary") is not None:
            self.employee.salary = update_data.get("new_salary")

        if update_data.get("new_position") is not None:
            self.employee.position = update_data.get("new_position")

        db.session.commit()
        return True

    def get_employee(self):
        """
        Retrieve the current employee instance.

        :return: Returns the current employee instance or None if it doesn't exist.
        :rtype: Employee or None
        """
        return None if self.employee is None else self.employee

    def get_employee_hash_password(self):
        """
        Retrieve the current employee hash password.

        :return: Returns the current employee hash password or None if it doesn't exist.
        :rtype: str or None
        """
        return None if self.employee is None else self.employee.password

    def get_employee_all_data(self):
        """
        Retrieve all data of the current employee instance.

        :return: Returns a dictionary containing all data of the current employee instance. Contains following keys:
                    - id (int): The employee's ID.
                    - name (str): The employee's name.
                    - surname (str): The employee's surname.
                    - email (str): The employee's email.
                    - phone (str): The employee's phone.
                    - salary (int): The employee's salary.
                    - position (str): The employee's position.
        :rtype: dict[str, any]
        """
        return {"id": self.employee.id, "name": self.employee.name, "surname": self.employee.surname,
                "email": self.employee.email, "phone": self.employee.phone,
                "salary": self.employee.salary, "position": self.employee.position}

    def get_employee_profile_data(self):
        """
        Retrieve profile data of the current employee instance.

        :return: Returns a dictionary containing profile data of the current employee instance. Contains following keys:
                    - id (int): The employee's ID.
                    - name (str): The employee's name.
                    - surname (str): The employee's surname.
                    - email (str): The employee's email.
                    - phone (str): The employee's phone.
                    - salary (int): The employee's salary.
                    - position (str): The employee's position.
                    - latest_rentals (list[int]): The employee's latest conducted rental IDs.
        :rtype: dict[str, any]
        """
        employee_profile_data = self.get_employee_all_data()
        employee_profile_data["latest_rentals"] = self._find_latest_rental_ids()

        return employee_profile_data

    def _find_by_id(self):
        """
        Retrieve an employee by his ID.

        :return: Returns the Employee instance with the provided ID, or None if he doesn't exist.
        :rtype: Employee
        """
        return Employee.query.filter_by(id=self.employee_id).first() if self.employee_id else None

    def _find_by_email(self):
        """
        Retrieve an employee by his email.

        :return: Returns the Employee instance with the provided email, or None if his doesn't exist.
        :rtype: Employee
        """
        return Employee.query.filter_by(email=self.employee_email).first() if self.employee_email else None

    def _find_latest_rental_ids(self):
        """
        Retrieve the IDs of the latest rentals of the current employee.

        :return: Returns a list of the IDs of the latest rentals of the current employee.
        :rtype: list[int]
        """
        latest_rentals_count = min(len(self.employee.rentals), Employee.LATEST_RENTALS_COUNT)
        latest_rentals = self.employee.rentals[-latest_rentals_count:][::-1]

        return [rental.id for rental in latest_rentals]

    @staticmethod
    def _validate_update_data(employee_data):
        """
        Validate the data provided for updating an employee.

        :param employee_data: Dictionary containing new values for the employee's attributes.
        :type employee_data: dict[str, any]

        :return: Returns True if the provided data is valid, False otherwise.
        :rtype: bool
        """
        return Employee.validate_phone(employee_data.get("new_phone")) or \
            Employee.validate_salary(employee_data.get("new_salary")) or \
            Employee.validate_position(employee_data.get("new_position"))
