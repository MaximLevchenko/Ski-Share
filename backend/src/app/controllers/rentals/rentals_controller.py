from ...services import RentalsService
from ..exceptions import ControllerException


class RentalsController:
    """
    The RentalsController class provides methods for handling rental-related requests.

    This class acts as a controller that uses the RentalsService for creating a new rental
    and preparing data related to all rentals.

    :ivar rental_data: The data for creating a new rental.
    :type rental_data: dict[str, any] or None

    :ivar rentals_service: An instance of the RentalsService class for managing rentals' data.
    :type rentals_service: RentalsService
    """

    def __init__(self, rental_data=None):
        """
        Initialize a new instance of the RentalsController class.

        :param rental_data: The data for creating a new rental, defaults to None.
        :type rental_data: dict[str, any] or None
        """
        self.rental_data = rental_data
        self.rentals_service = RentalsService(rental_data)

    def create_client(self):
        """
        Create a new rental.

        This method uses the rentals service to create a new rental with the provided data.
        If the rental data is invalid, it raises a ControllerException.

        :raise ControllerException: If the rental data is invalid with HTTP code 400.
        """
        if not self.rentals_service.create_rental():
            raise ControllerException("Invalid rental data.", 400)

    def create_response_with_rentals_data(self):
        """
        Prepare a response containing data about all rentals.

        This method uses the rentals service to retrieve data about all rentals.

        :return: A tuple where the first item is a list of data about all rentals and
                 the second item is the HTTP status code 200.
        :rtype: tuple[list[dict[str, any]], int]
        """
        return self.rentals_service.prepare_response_with_rentals_data(), 200

    def create_response_with_successful_create_message(self):
        """
        Prepare a response containing a success message for rental creation.

        :return: A tuple where the first item is a dictionary containing a success message and
                 the second item is the HTTP status code 200.
        :rtype: tuple[dict[str, str], int]
        """
        return {"message": "Rental created successfully."}, 200
