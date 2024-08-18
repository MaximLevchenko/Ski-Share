from ...repositories import ClientsRepository


class ClientsService:
    """
    The ClientsService class provides methods for managing multiple clients' data.

    This class acts as a service for creating new clients and preparing data related to all clients.

    :ivar create_data: The data for creating a new client.
    :type create_data: dict[str, any] or None
    """

    def __init__(self, create_data=None):
        """
        Initialize a new instance of the ClientsService class.

        :param create_data: The data for creating a new client, defaults to None.
        :type create_data: dict[str, any] or None
        """
        self.create_data = create_data
        self.clients_repository = ClientsRepository(self.create_data)

    def create_client(self):
        """
        Create a new client.

        This method uses the clients repository to create a new client with the provided data.

        :return: True if the client was created, False otherwise.
        :rtype: bool
        """
        return self.clients_repository.create()

    def prepare_response_with_clients_data(self):
        """
        Prepare a response containing data about all clients.

        This method uses the clients repository to retrieve data about all clients. The return value is a list
        of dictionaries, where each dictionary contains data about a specific client.

        :return: A list of dictionaries, where each dictionary contains data about a specific client.
        :rtype: list[dict[str, any]]
        """
        return self.clients_repository.get_all()
