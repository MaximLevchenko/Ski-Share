from ...repositories import ClientRepository


class ClientService:
    """
    The ClientService class provides methods for managing client data.

    This class acts as a service for validating, updating, deleting, and preparing data related to a client.

    :ivar client_id: The ID of the client.
    :type client_id: int or str

    :ivar update_data: The data to update for the client.
    :type update_data: dict[str, any] or None

    :ivar client_repository: An instance of the ClientRepository class for interacting with client data.
    :type client_repository: ClientRepository
    """

    def __init__(self, client_id, update_data=None):
        """
        Initialize a new instance of the ClientService class.

        :param client_id: The ID of the client.
        :type client_id: int

        :param update_data: The data to update for the client, defaults to None.
        :type update_data: dict[str, any] or None
        """
        self.client_id = client_id
        self.update_data = update_data
        self.client_repository = ClientRepository(client_id=self.client_id)

    def update_client_data(self):
        """
        Update the client's data.

        This method uses the client repository to update the client's data.

        :return: The bool if the client was successfully updated.
        :rtype: bool
        """
        return self.client_repository.update(self.update_data)

    def validate_client(self):
        """
        Validate the client's existence.

        This method uses the client repository to validate the existence of the client based on their ID.

        :return: True if the client exists, False otherwise.
        :rtype: bool
        """
        return True if self.client_repository.get_client() else False

    def delete_client(self):
        """
        Delete the client.

        This method uses the client repository to delete the client based on their ID.
        """
        self.client_repository.delete()

    def prepare_response_with_client_data(self):
        """
        Prepare a response containing all data about the client.

        This method uses the client repository to retrieve all data about the client.

        :return: A dictionary containing all data about the client.
        :rtype: dict[str, any]
        """
        return self.client_repository.get_client_all_data()
