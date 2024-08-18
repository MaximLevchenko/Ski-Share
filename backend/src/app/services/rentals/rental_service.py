from ...repositories import RentalRepository, EquipmentRepository


class RentalService:
    """
    The RentalService class provides methods for managing rental data.

    This class acts as a service for validating, updating, deleting, and preparing data related to a rental.

    :ivar rental_id: The ID of the rental.
    :type rental_id: int

    :ivar update_data: The data to update for the rental.
    :type update_data: dict[str, any] or None

    :ivar rental_repository: An instance of the RentalRepository class for interacting with rental data.
    :type rental_repository: RentalRepository
    """

    def __init__(self, rental_id, update_data=None):
        """
        Initialize a new instance of the RentalService class.

        :param rental_id: The ID of the rental.
        :type rental_id: int

        :param update_data: The data to update for the rental, defaults to None.
        :type update_data: dict[str, any] or None
        """
        self.rental_id = rental_id
        self.update_data = update_data
        self.rental_repository = RentalRepository(rental_id=self.rental_id)

    def update_rental_data(self):
        """
        Update the rental's data.

        This method uses the rental repository to update the rental's data.

        :return: The bool if the rental was successfully updated.
        :rtype: bool
        """
        return self.rental_repository.update(self.update_data)

    def validate_rental(self):
        """
        Validate the rental's existence.

        This method uses the rental repository to validate the existence of the rental based on their ID.

        :return: True if the rental exists, False otherwise.
        :rtype: bool
        """
        return True if self.rental_repository.get_rental() else False

    def close_rental(self):
        """
        Close the rental.

        This method uses the rental repository to close the rental and the equipment repository
        to unrent the related equipment.

        :return: True if the rental was successfully closed, False otherwise.
        :rtype: bool
        """
        if not self.rental_repository.close(self.update_data):
            return False

        rented_equipments = self.rental_repository.get_rental_equipments()
        for equipment_inventory_number in rented_equipments:
            equipment_repository = EquipmentRepository(equipment_inventory_number)
            equipment_repository.unrent()

        return True

    def delete_rental(self):
        """
        Delete the rental.

        This method uses the rental repository to delete the rental based on their ID.
        """
        self.rental_repository.delete()

    def prepare_response_with_rental_data(self):
        """
        Prepare a response containing all data about the rental.

        This method uses the rental repository to retrieve all data about the rental.

        :return: A dictionary containing all data about the rental.
        :rtype: dict[str, any]
        """
        return self.rental_repository.get_rental_full_data()
