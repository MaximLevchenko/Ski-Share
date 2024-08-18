from ...repositories import EquipmentRepository


class EquipmentService:
    """
    The EquipmentService class provides methods for managing equipment data.

    This class acts as a service for validating, updating, deleting, and preparing data related to a piece of equipment.

    :ivar equipment_inventory_number: The inventory number of the equipment.
    :type equipment_inventory_number: int

    :ivar update_data: The data to update for the equipment.
    :type update_data: dict[str, any] or None

    :ivar equipment_repository: An instance of the EquipmentRepository class for interacting with equipment data.
    :type equipment_repository: EquipmentRepository
    """

    def __init__(self, equipment_inventory_number, update_data=None):
        """
        Initialize a new instance of the EquipmentService class.

        :param equipment_inventory_number: The inventory number of the equipment.
        :type equipment_inventory_number: int

        :param update_data: The data to update for the equipment, defaults to None.
        :type update_data: dict[str, any] or None
        """
        self.equipment_inventory_number = equipment_inventory_number
        self.update_data = update_data
        self.equipment_repository = EquipmentRepository(equipment_inventory_number=self.equipment_inventory_number)

    def update_equipment_data(self):
        """
        Update the equipment's data.

        This method uses the equipment repository to update the equipment's data.

        :return: True if the equipment was successfully updated, False otherwise.
        :rtype: bool
        """
        return self.equipment_repository.update(self.update_data)

    def update_equipment_status_as_damaged(self):
        """
        Update the status of the equipment as damaged.

        This method uses the equipment repository to update the status of the equipment.
        """
        self.equipment_repository.damaged()

    def validate_equipment(self):
        """
        Validate the equipment's existence.

        This method uses the equipment repository to validate the existence of the equipment
        based on its inventory number.

        :return: True if the equipment exists, False otherwise.
        :rtype: bool
        """
        return True if self.equipment_repository.get_equipment() else False

    def delete_equipment(self):
        """
        Delete the equipment.

        This method uses the equipment repository to delete the equipment based on its inventory number.
        """
        self.equipment_repository.delete()

    def prepare_response_with_equipment_data(self):
        """
        Prepare a response containing all data about the equipment.

        This method uses the equipment repository to retrieve all data about the equipment.

        :return: A dictionary containing all data about the equipment.
        :rtype: dict[str, any]
        """
        return self.equipment_repository.get_equipment_all_data()
