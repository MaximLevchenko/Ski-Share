from flask import jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, set_refresh_cookies
from werkzeug.security import check_password_hash

from ...repositories import EmployeeRepository


class LoginService:
    """
    The LoginService class provides methods for managing login procedures.

    This class acts as a service for validating and preparing data related to login.

    :ivar login_data: The login data of the user.
    :type login_data: dict[str, any]

    :ivar employee_repository: An instance of the EmployeeRepository class for interacting with employee data.
    :type employee_repository: EmployeeRepository

    :ivar login_employee: An instance of the Employee model representing the login user.
    :type login_employee: Employee or None
    """

    def __init__(self, login_data):
        """
        Initialize a new instance of the LoginService class.

        :param login_data: The login data of the user.
        :type login_data: dict[str, any]
        """
        self.login_data = login_data
        self.employee_repository = EmployeeRepository(employee_email=self.login_data.get("email"))
        self.login_employee = None

    def validate_user_login_data(self):
        """
        Validate the user login data.

        This method uses the employee repository to retrieve the employee based on their login data.
        The result is stored in the login_employee attribute. The method also checks password hash.

        :return: True if the login data is valid, False otherwise.
        :rtype: bool
        """
        self.login_employee = self.employee_repository.get_employee()

        return True if self.login_employee and check_password_hash(
            self.employee_repository.get_employee_hash_password(), self.login_data.get("password")) else False

    def prepare_login_response(self):
        """
        Prepare a response containing all data about the user.

        This method uses the employee repository to retrieve all data about the user,
        generates JWT access and refresh tokens, sets refresh cookies, and prepares a response.

        :return: A response containing all data about the employee including access and refresh tokens.
        :rtype: flask.Response
        """
        employee_all_data = self.employee_repository.get_employee_all_data()
        employee_all_data["access_token"] = create_access_token(identity=employee_all_data.get("email"))
        employee_all_data["refresh_token"] = create_refresh_token(identity=employee_all_data.get("email"))

        login_response = jsonify(employee_all_data)
        set_refresh_cookies(login_response, employee_all_data.get("refresh_token"))

        return login_response
