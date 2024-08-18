from ...services import ClientsService
from ..exceptions import ControllerException


class ClientsController:
    """
    The ClientsController class provides methods for handling client-related requests.

    This class acts as a controller that uses the ClientsService for creating a new client
    and preparing data related to all clients.

    :ivar client_data: The data for creating a new client.
    :type client_data: dict[str, any] or None

    :ivar clients_service: An instance of the ClientsService class for managing clients' data.
    :type clients_service: ClientsService
    """

    def __init__(self, client_data=None):
        """
        Initialize a new instance of the ClientsController class.

        :param client_data: The data for creating a new client, defaults to None.
        :type client_data: dict[str, any] or None
        """
        self.client_data = client_data
        self.clients_service = ClientsService(client_data)

    def create_client(self):
        """
        Create a new client.

        This method uses the clients service to create a new client with the provided data.
        If the client data is invalid, it raises a ControllerException.

        :raise ControllerException: If the client data is invalid with HTTP code 400.
        """
        if not self.clients_service.create_client():
            raise ControllerException("Invalid client data.", 400)

    def create_response_with_clients_data(self):
        """
        Prepare a response containing data about all clients.

        This method uses the clients service to retrieve data about all clients.

        :return: A tuple where the first item is a list of data about all clients and
                 the second item is the HTTP status code 200.
        :rtype: tuple[list[dict[str, any]], int]
        """
        return self.clients_service.prepare_response_with_clients_data(), 200

    def create_response_with_successful_create_message(self):
        """
        Prepare a response containing a success message for client creation.

        :return: A tuple where the first item is a dictionary containing a success message and
                 the second item is the HTTP status code 200.
        :rtype: tuple[dict[str, str], int]
        """
        return {"message": "Client created successfully."}, 200
