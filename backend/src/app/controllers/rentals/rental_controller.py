from ...services import RentalService
from ..exceptions import ControllerException


class RentalController:
    """
    The RentalController class provides methods for managing rental data.

    This class acts as a controller for validating, updating, deleting, and preparing responses related to a rental.

    :ivar rental_id: The ID of the rental.
    :type rental_id: int

    :ivar update_data: The data to update for the rental.
    :type update_data: dict[str, any] or None

    :ivar rental_service: An instance of the RentalService class for managing rental data.
    :type rental_service: RentalService
    """

    def __init__(self, rental_id, update_data=None):
        """
        Initialize a new instance of the RentalController class.

        :param rental_id: The ID of the rental.
        :type rental_id: int

        :param update_data: The data to update for the rental, defaults to None.
        :type update_data: dict[str, any] or None
        """
        self.rental_id = rental_id
        self.update_data = update_data
        self.rental_service = RentalService(self.rental_id, self.update_data)

    def validate_rental(self):
        """
        Validate the rental's existence.

        This method uses the rental service to validate the existence of the rental based on their ID.
        If the rental does not exist, it raises a ControllerException.

        :raises ControllerException: If the rental does not exist and HTTP status code 404.
        """
        if not self.rental_service.validate_rental():
            raise ControllerException("Rental not found.", 404)

    def update_rental(self):
        """
        Update the rental's data.

        This method uses the rental service to update the rental's data.
        If the update data is invalid, it raises a ControllerException.

        :raises ControllerException: If the rental update data is invalid and HTTP status code 400.
        """
        if not self.rental_service.update_rental_data():
            raise ControllerException("Invalid rental update data.", 400)

    def close_rental(self):
        """
        Close the rental.

        This method uses the rental service to close the rental.
        If the close data is invalid, it raises a ControllerException.

        :raises ControllerException: If the rental close data is invalid and HTTP status code 400.
        """
        if not self.rental_service.close_rental():
            raise ControllerException("Invalid rental close data.", 400)

    def delete_rental(self):
        """
        Delete the rental.

        This method uses the rental service to delete the rental based on their ID.
        """
        self.rental_service.delete_rental()

    def create_response_with_rental_data(self):
        """
        Create a response containing all data about the rental.

        This method uses the rental service to retrieve all data about the rental and prepares a response.

        :return: A dictionary containing all data about the rental and HTTP status code of 200.
        :rtype: tuple[dict[str, any], int]
        """
        return self.rental_service.prepare_response_with_rental_data(), 200

    def create_response_with_successful_update_message(self):
        """
        Create a response with a successful update message.

        :return: A dictionary containing a success message and HTTP status code of 200.
        :rtype: tuple[dict[str, str], int]
        """
        return {"message": "Rental updated successfully."}, 200

    def create_response_with_successful_delete_message(self):
        """
        Create a response with a successful delete message.

        :return: A dictionary containing a success message and HTTP status code of 200.
        :rtype: tuple[dict[str, str], int]
        """
        return {"message": "Rental deleted successfully."}, 200

    def create_response_with_successful_close_message(self):
        """
        Create a response with a successful close message.

        :return: A dictionary containing a success message and HTTP status code of 200.
        :rtype: tuple[dict[str, str], int]
        """
        return {"message": "Rental closed successfully."}, 200
