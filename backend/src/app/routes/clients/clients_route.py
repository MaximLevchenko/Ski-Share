from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource, Namespace

from .clients_serialization_models import create_client_post_model, create_client_get_model, create_client_update_model
from ...controllers import ControllerException, ClientsController, ClientsSortController, ClientController

clients_namespace = Namespace("clients", description="Clients related operations.")

client_post_model = create_client_post_model(clients_namespace)
client_get_model = create_client_get_model(clients_namespace)
client_update_model = create_client_update_model(clients_namespace)


@clients_namespace.route('/')
class ClientsRouter(Resource):
    """
    This router handles operations related to all clients.
    """

    @clients_namespace.marshal_list_with(client_get_model)
    @jwt_required()
    def get(self):
        """
        Returns a list of all clients.

        This method returns the details of all clients in the system.

        :return: A list with data of all clients and the HTTP status code 200.
        :rtype: tuple[list[dict[str, any]], int]
        """
        clients_controller = ClientsController()

        return clients_controller.create_response_with_clients_data()

    @clients_namespace.expect(client_post_model)
    @clients_namespace.response(400, "Invalid client data.")
    @jwt_required()
    def post(self):
        """
        Creates a new client.

        This method expects client data in the request's body.
        If the data is valid, it creates a new client in the system.

        :raises ControllerException: If the client data is invalid.

        :return: A dictionary with a success message and the HTTP status code 200.
        :rtype: tuple[dict[str, str], int]
        """
        clients_controller = ClientsController(request.get_json())

        try:
            clients_controller.create_client()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return clients_controller.create_response_with_successful_create_message()


@clients_namespace.route('/sort')
class ClientsSortRouter(Resource):
    """
    This router handles the operation of sorting all clients based on the provided criteria.
    """

    @clients_namespace.response(400, "Invalid sort QUERY parameters.")
    @clients_namespace.marshal_list_with(client_get_model)
    @jwt_required()
    def get(self):
        """
        Returns a list of all clients sorted based on the provided parameters.

        This method expects sorting parameters in the request's query string.
        If the parameters are valid, it returns a list of all clients sorted accordingly.

        :raises ControllerException: If the sort parameters are invalid.

        :return: A list with data of all clients sorted accordingly and the HTTP status code 200.
        :rtype: tuple[list[dict[str, any]], int]
        """
        clients_sort_controller = ClientsSortController(request.args.to_dict())

        try:
            clients_sort_controller.sort_clients()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return clients_sort_controller.create_response_with_sorted_clients_data()


@clients_namespace.route('/client/<int:id>')
class ClientRouter(Resource):
    """
    This router handles operations related to a specific client.
    """

    @clients_namespace.response(404, "Client not found.")
    @clients_namespace.marshal_with(client_get_model)
    @jwt_required()
    def get(self, id):
        """
        Returns the data of a specific client.

        This method returns the details of a specific client based on their id.

        :raises ControllerException: If the client does not exist.

        :return: A dictionary with the data of the client and the HTTP status code 200.
        :rtype: tuple[dict[str, any], int]
        """
        client_controller = ClientController(id)

        try:
            client_controller.validate_client()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return client_controller.create_response_with_client_data()

    @clients_namespace.expect(client_update_model)
    @clients_namespace.response(400, "Invalid client update data.")
    @clients_namespace.response(404, "Client not found.")
    @jwt_required()
    def put(self, id):
        """
        Updates a specific client's data.

        This method expects the updated data in the request's body.
        If the data is valid and the client exists, it updates the client's data in the system.

        :raises ControllerException: If the client does not exist or the update data is invalid.

        :return: A dictionary with a success message and the HTTP status code 200.
        :rtype: tuple[dict[str, str], int]
        """
        client_controller = ClientController(id, request.get_json())

        try:
            client_controller.validate_client()
            client_controller.update_client()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return client_controller.create_response_with_successful_update_message()

    @clients_namespace.response(404, "Client not found.")
    @jwt_required()
    def delete(self, id):
        """
        Deletes a specific client.

        This method deletes a specific client based on their id from the system.

        :raises ControllerException: If the client does not exist.

        :return: A dictionary with a success message and the HTTP status code 200.
        :rtype: tuple[dict[str, str], int]
        """
        client_controller = ClientController(id)

        try:
            client_controller.validate_client()
            client_controller.delete_client()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return client_controller.create_response_with_successful_delete_message()
