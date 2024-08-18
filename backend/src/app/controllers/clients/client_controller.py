from ...services import ClientService
from ..exceptions import ControllerException


class ClientController:
    """
    The ClientController class provides methods for managing client data.

    This class acts as a controller for validating, updating, deleting, and preparing responses related to a client.

    :ivar client_id: The ID of the client.
    :type client_id: int

    :ivar update_data: The data to update for the client.
    :type update_data: dict[str, any] or None

    :ivar client_service: An instance of the ClientService class for managing client data.
    :type client_service: ClientService
    """

    def __init__(self, client_id, update_data=None):
        """
        Initialize a new instance of the ClientController class.

        :param client_id: The ID of the client.
        :type client_id: int

        :param update_data: The data to update for the client, defaults to None.
        :type update_data: dict[str, any] or None
        """
        self.client_id = client_id
        self.update_data = update_data
        self.client_service = ClientService(self.client_id, self.update_data)

    def validate_client(self):
        """
        Validate the client's existence.

        This method uses the client service to validate the existence of the client based on their ID.
        If the client does not exist, it raises a ControllerException.

        :raises ControllerException: If the client does not exist and HTTP status code 404.
        """
        if not self.client_service.validate_client():
            raise ControllerException("Client not found.", 404)

    def update_client(self):
        """
        Update the client's data.

        This method uses the client service to update the client's data.
        If the update data is invalid, it raises a ControllerException.

        :raises ControllerException: If the client update data is invalid and HTTP status code 400.
        """
        if not self.client_service.update_client_data():
            raise ControllerException("Invalid client update data.", 400)

    def delete_client(self):
        """
        Delete the client.

        This method uses the client service to delete the client based on their ID.
        """
        self.client_service.delete_client()

    def create_response_with_client_data(self):
        """
        Create a response containing all data about the client.

        This method uses the client service to retrieve all data about the client and prepares a response.

        :return: A dictionary containing all data about the client and HTTP status code of 200.
        :rtype: tuple[dict[str, any], int]
        """
        return self.client_service.prepare_response_with_client_data(), 200

    def create_response_with_successful_update_message(self):
        """
        Create a response with a successful update message.

        :return: A dictionary containing a success message and HTTP status code of 200.
        :rtype: tuple[dict[str, str], int]
        """
        return {"message": "Client updated successfully."}, 200

    def create_response_with_successful_delete_message(self):
        """
        Create a response with a successful delete message.

        :return: A dictionary containing a success message and HTTP status code of 200.
        :rtype: tuple[dict[str, str], int]
        """
        return {"message": "Client deleted successfully."}, 200
