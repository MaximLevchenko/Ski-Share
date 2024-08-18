from ...services import ClientsSortService
from ..exceptions import ControllerException


class ClientsSortController:
    """
    The ClientsSortController class provides methods for sorting clients and creating an appropriate response.

    This class acts as a controller for handling requests related to sorting clients.

    :ivar sort_data: The data specifying how clients should be sorted.
    :type sort_data: dict[str, any]

    :ivar sorted_clients: The sorted client data.
    :type sorted_clients: list[dict[str, any]] or None
    """

    def __init__(self, sort_data):
        """
        Initialize a new instance of the ClientsSortController class.

        :param sort_data: The data specifying how clients should be sorted.
        :type sort_data: dict[str, any]
        """
        self.sort_data = sort_data
        self.sorted_clients = None
        self.clients_sort_service = ClientsSortService(self.sort_data)

    def sort_clients(self):
        """
        Sort client data based on the provided parameters.

        This method uses the ClientsSortService to sort all clients based on the sorting data.
        If the sorting fails, it raises a ControllerException.

        :raise ControllerException: If the sorting fails due to invalid sort QUERY parameters.
        """
        self.sorted_clients = self.clients_sort_service.sort_clients()
        if self.sorted_clients is None:
            raise ControllerException("Invalid sort QUERY parameters.", 400)

    def create_response_with_sorted_clients_data(self):
        """
        Create a response containing the sorted client data.

        This method prepares a response with the sorted client data.
        The response includes a 200 status code.

        :return: The response containing the sorted client data and a 200 status code.
        :rtype: tuple[list[dict[str, any]], int]
        """
        return self.sorted_clients, 200
