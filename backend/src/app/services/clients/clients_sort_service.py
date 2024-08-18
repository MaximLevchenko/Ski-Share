from ...repositories import ClientsRepository


class ClientsSortService:
    """
    The ClientsSortService class provides a method to sort client data.

    This class acts as a service for sorting data related to clients.

    :ivar sort_data: The data specifying how clients should be sorted.
    :type sort_data: dict[str, any]
    """

    def __init__(self, sort_data):
        """
        Initialize a new instance of the ClientsSortService class.

        :param sort_data: The data specifying how clients should be sorted. This could include parameters like name,
                          email, birthdate, etc., along with the sort direction ('asc' or 'desc').
        :type sort_data: dict[str, any]
        """
        self.sort_data = sort_data
        self.clients_repository = ClientsRepository()

    def sort_clients(self):
        """
        Sort client data based on the provided parameters.

        This method uses the ClientsRepository to sort all clients based on the sorting data.

        :return: The sorted list of dictionaries, where each dictionary contains data about a specific client,
                 or None if the sort data wasn't valid.
        :rtype: list[dict[str, any]] or None
        """
        return self.clients_repository.sort_all(self.sort_data)
