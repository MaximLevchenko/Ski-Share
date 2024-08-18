from ...services import RentalsSortService
from ..exceptions import ControllerException


class RentalsSortController:
    """
    The RentalsSortController class provides methods for sorting rentals and creating an appropriate response.

    This class acts as a controller for handling requests related to sorting rentals.

    :ivar sort_data: The data specifying how rentals should be sorted.
    :type sort_data: dict[str, any]

    :ivar sorted_rentals: The sorted rental data.
    :type sorted_rentals: list[dict[str, any]] or None
    """

    def __init__(self, sort_data):
        """
        Initialize a new instance of the RentalsSortController class.

        :param sort_data: The data specifying how rentals should be sorted.
        :type sort_data: dict[str, any]
        """
        self.sort_data = sort_data
        self.sorted_rentals = None
        self.rentals_sort_service = RentalsSortService(self.sort_data)

    def sort_rentals(self):
        """
        Sort rental data based on the provided parameters.

        This method uses the RentalsSortService to sort all rentals based on the sorting data.
        If the sorting fails, it raises a ControllerException.

        :raise ControllerException: If the sorting fails due to invalid sort QUERY parameters.
        """
        self.sorted_rentals = self.rentals_sort_service.sort_rentals()
        if not self.sorted_rentals:
            raise ControllerException("Invalid sort QUERY parameters.", 400)

    def create_response_with_sorted_rentals_data(self):
        """
        Create a response containing the sorted rental data.

        This method prepares a response with the sorted rental data.
        The response includes a 200 status code.

        :return: The response containing the sorted rental data and a 200 status code.
        :rtype: tuple[list[dict[str, any]], int]
        """
        return self.sorted_rentals, 200
