from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource, Namespace

from .rentals_serialization_models import create_rental_post_model, create_rental_get_model, create_rental_full_model, \
    create_rental_fees_model, create_rental_description_model
from ...controllers import ControllerException, RentalsController, RentalsSortController, RentalController


rentals_namespace = Namespace("rentals", description="Rentals related operations.")

rental_post_model = create_rental_post_model(rentals_namespace)
rental_get_model = create_rental_get_model(rentals_namespace)
rental_full_model = create_rental_full_model(rentals_namespace)
rental_fees_model = create_rental_fees_model(rentals_namespace)
rental_description_model = create_rental_description_model(rentals_namespace)


@rentals_namespace.route('/')
class RentalsRouter(Resource):
    """
    Router for handling operations related to rental.

    Provides handlers for HTTP GET and POST requests made to the '/rentals/' endpoint.
    """

    @rentals_namespace.marshal_list_with(rental_get_model)
    @jwt_required()
    def get(self):
        """
        Retrieves all rental data.

        This method requires a JWT token. It creates a `RentalsController` instance and then generates a response
        containing data about all rentals.

        :return: A response object containing a list of all rental data.
        :rtype: tuple[list[dict[str, any]], int]
        """
        rentals_controller = RentalsController()

        return rentals_controller.create_response_with_rentals_data()

    @rentals_namespace.expect(rental_post_model)
    @rentals_namespace.response(400, "Invalid rental data.")
    @jwt_required()
    def post(self):
        """
        Creates a new rental.

        This method requires a JWT token and the rental data in the request body. It creates a `RentalsController`
        instance with the request data and attempts to create a new rental.

        :return: A response object containing a success message or an error message if an error occurs.
        :rtype: tuple[dict[str, str], int]

        :raises ControllerException: If an error occurs while creating the rental.
        """
        rentals_controller = RentalsController(request.get_json())

        try:
            rentals_controller.create_client()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return rentals_controller.create_response_with_successful_create_message()


@rentals_namespace.route('/sort')
class RentalsSortRouter(Resource):
    """
    Router for handling the operation related to sorting rental data.

    Provides a handler for HTTP GET requests made to the '/rentals/sort' endpoint.
    """

    @rentals_namespace.response(400, "Invalid sort QUERY parameters.")
    @rentals_namespace.marshal_list_with(rental_get_model)
    @jwt_required()
    def get(self):
        """
        Retrieves sorted rental data.

        This method requires a JWT token and the sort parameters in the query string. It creates a
        `RentalsSortController` instance with the request arguments and attempts to sort the rental data.

        :return: A response object containing a list of sorted rental data.
        :rtype: tuple[list[dict[str, any]], int]

        :raises ControllerException: If an error occurs while sorting the rental data.
        """
        rentals_sort_controller = RentalsSortController(request.args.to_dict())

        try:
            rentals_sort_controller.sort_rentals()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return rentals_sort_controller.create_response_with_sorted_rentals_data()


@rentals_namespace.route('/rental/<int:id>')
class RentalRouter(Resource):
    """
    Router for handling operations related to a specific rental record.

    Provides handlers for HTTP GET and DELETE requests made to the '/rentals/rental/<id>' endpoint.
    """

    @rentals_namespace.response(404, "Rental not found.")
    @rentals_namespace.marshal_with(rental_full_model)
    @jwt_required()
    def get(self, id):
        """
        Retrieves a specific rental record by ID.

        This method requires a JWT token and the ID of the rental. It creates a `RentalController` instance
        with the provided ID and attempts to validate the rental.

        :param id: The ID of the rental.
        :type id: int

        :return: A response object containing the rental data.
        :rtype: tuple[dict[str, str], int]

        :raises ControllerException: If the rental does not exist.
        """
        rental_controller = RentalController(id)

        try:
            rental_controller.validate_rental()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return rental_controller.create_response_with_rental_data()

    @rentals_namespace.response(404, "Rental not found.")
    @jwt_required()
    def delete(self, id):
        """
        Deletes a specific rental record by ID.

        This method requires a JWT token and the ID of the rental. It creates a `RentalController` instance
        with the provided ID and attempts to validate and delete the rental.

        :param id: The ID of the rental.
        :type id: int

        :return: A response object containing a successful deletion message.
        :rtype: tuple[dict[str, str], int]

        :raises ControllerException: If the rental does not exist.
        """
        rental_controller = RentalController(id)

        try:
            rental_controller.validate_rental()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        rental_controller.delete_rental()

        return rental_controller.create_response_with_successful_delete_message()


@rentals_namespace.route('/rental/<int:id>/description')
class RentalDescriptionRouter(Resource):
    """
    Router for handling operations related to a specific rental record's description.

    Provides a handler for HTTP PUT requests made to the '/rentals/rental/<id>/description' endpoint.
    """

    @rentals_namespace.expect(rental_description_model)
    @rentals_namespace.response(400, "Invalid rental update data.")
    @rentals_namespace.response(404, "Rental not found.")
    @jwt_required()
    def put(self, id):
        """
        Updates a specific rental record's description by ID.

        This method requires a JWT token and the ID of the rental. It creates a `RentalController` instance
        with the provided ID and attempts to validate the rental and update the description.

        :param id: The ID of the rental.
        :type id: int

        :return: A response object containing a successful update message.
        :rtype: tuple[dict[str, str], int]

        :raises ControllerException: If the rental does not exist or if the provided description data is invalid.
        """
        rental_controller = RentalController(id, request.get_json())

        try:
            rental_controller.validate_rental()
            rental_controller.update_rental()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return rental_controller.create_response_with_successful_update_message()


@rentals_namespace.route('/rental/<int:id>/close')
class RentalCloseRouter(Resource):
    """
    Router for handling operations related to closing a specific rental record.

    Provides a handler for HTTP PUT requests made to the '/rentals/rental/<id>/close' endpoint.
    """

    @rentals_namespace.expect(rental_fees_model)
    @rentals_namespace.response(400, "Invalid fees.")
    @rentals_namespace.response(404, "Rental not found.")
    @jwt_required()
    def put(self, id):
        """
        Closes a specific rental record by ID.

        This method requires a JWT token and the ID of the rental. It creates a `RentalController` instance
        with the provided ID and attempts to validate the rental and close it.

        :param id: The ID of the rental.
        :type id: int

        :return: A response object containing a successful closure message.
        :rtype: tuple[dict[str, str], int]

        :raises ControllerException: If the rental does not exist or if the provided fees data is invalid.
        """
        rental_controller = RentalController(id, request.get_json())

        try:
            rental_controller.validate_rental()
            rental_controller.close_rental()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return rental_controller.create_response_with_successful_close_message()
