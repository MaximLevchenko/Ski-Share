from flask import request
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
from flask_restx import Resource, Namespace

from .employees_serialization_models import create_employee_post_model, create_employee_get_model, \
    create_employee_update_model, create_employee_profile_model
from ...controllers import ControllerException, EmployeesController, EmployeesSortController, EmployeeController


employees_namespace = Namespace("employees", description="Employees related operations.")

employee_post_model = create_employee_post_model(employees_namespace)
employee_get_model = create_employee_get_model(employees_namespace)
employee_update_model = create_employee_update_model(employees_namespace)
employee_profile_model = create_employee_profile_model(employees_namespace)


@employees_namespace.route('/')
class EmployeesRouter(Resource):
    """
    This router handles operations related to all employees.
    """
    @employees_namespace.marshal_list_with(employee_get_model)
    @jwt_required()
    def get(self):
        """
        Returns a list of all employees.

        This method returns the details of all employees in the system.

        :return: A list with data of all employees and the HTTP status code 200.
        :rtype: tuple[list[dict[str, any]], int]
        """
        employees_controller = EmployeesController()

        return employees_controller.create_response_with_employees_data()

    @employees_namespace.expect(employee_post_model)
    @employees_namespace.response(400, "Invalid employee data.")
    @jwt_required()
    def post(self):
        """
        Creates a new employee.

        This method expects employee data in the request's body.
        If the data is valid, it creates a new employee in the system.

        :raises ControllerException: If the employee data is invalid.

        :return: A dictionary with a success message and the HTTP status code 200.
        :rtype: tuple[dict[str, str], int]
        """
        employees_controller = EmployeesController(request.get_json())

        try:
            employees_controller.create_employee()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return employees_controller.create_response_with_successful_create_message()


@employees_namespace.route('/sort')
class EmployeesSortRouter(Resource):
    """
    This router handles the operation of sorting all employees based on the provided criteria.
    """

    @employees_namespace.response(400, "Invalid sort QUERY parameters.")
    @employees_namespace.marshal_list_with(employee_get_model)
    @jwt_required()
    def get(self):
        """
        Returns a list of all employees sorted based on the provided parameters.

        This method expects sorting parameters in the request's query string.
        If the parameters are valid, it returns a list of all employees sorted accordingly.

        :raises ControllerException: If the sort parameters are invalid.

        :return: A list with data of all employees sorted accordingly and the HTTP status code 200.
        :rtype: tuple[list[dict[str, any]], int]
        """
        employees_sort_controller = EmployeesSortController(request.args.to_dict())

        try:
            employees_sort_controller.sort_employees()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return employees_sort_controller.create_response_with_sorted_employees_data()


@employees_namespace.route('/employee/<int:id>')
class EmployeeRouter(Resource):
    """
    This router handles operations related to a specific employee.
    """

    @employees_namespace.response(404, "Employee not found.")
    @employees_namespace.marshal_with(employee_profile_model)
    @jwt_required()
    def get(self, id):
        """
        Returns the data of a specific employee.

        This method returns the details of a specific employee based on their id.

        :raises ControllerException: If the employee does not exist.

        :return: A dictionary with the data of the employee and the HTTP status code 200.
        :rtype: tuple[dict[str, any], int]
        """
        employee_controller = EmployeeController(id)

        try:
            employee_controller.validate_employee()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return employee_controller.create_response_with_employee_profile_data()

    @employees_namespace.expect(employee_update_model)
    @employees_namespace.response(400, "Invalid employee update data.")
    @employees_namespace.response(404, "Employee not found.")
    @jwt_required()
    def put(self, id):
        """
        Updates a specific employee's data.

        This method expects the updated data for a specific employee in the request's body.
        If the employee exists and the updated data is valid, it updates the employee's data in the system.

        :raises ControllerException: If the employee does not exist, or the updated data is invalid.

        :return: A dictionary with a success message and the HTTP status code 200.
        :rtype: tuple[dict[str, str], int]
        """
        employee_controller = EmployeeController(id, request.get_json())

        try:
            employee_controller.validate_employee()
            employee_controller.update_employee()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return employee_controller.create_response_with_successful_update_message()

    @employees_namespace.response(201, "Employee deleted successfully.")
    @employees_namespace.response(404, "Employee not found.")
    @jwt_required()
    def delete(self, id):
        """
        Deletes a specific employee.

        This method deletes a specific employee based on their id.

        :raises ControllerException: If the employee does not exist.

        :return: A dictionary with a success message and the HTTP status code 200.
        :rtype: tuple[dict[str, str], int]
        """
        employee_controller = EmployeeController(id)

        try:
            employee_controller.validate_employee()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        employee_controller.delete_employee()

        return employee_controller.create_response_with_successful_delete_message()
