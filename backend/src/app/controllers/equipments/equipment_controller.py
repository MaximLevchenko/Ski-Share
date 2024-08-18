from ...services import EquipmentService
from ..exceptions import ControllerException


class EquipmentController:
    """
    The EquipmentController class provides methods for managing equipment data.

    This class acts as a controller for validating, updating, deleting,
    and preparing responses related to a piece of equipment.

    :ivar equipment_inventory_number: The inventory number of the equipment.
    :type equipment_inventory_number: int

    :ivar update_data: The data to update for the equipment.
    :type update_data: dict[str, any] or None

    :ivar equipment_service: An instance of the EquipmentService class for managing equipment data.
    :type equipment_service: EquipmentService
    """

    def __init__(self, equipment_inventory_number, update_data=None):
        """
        Initialize a new instance of the EquipmentController class.

        :param equipment_inventory_number: The inventory number of the equipment.
        :type equipment_inventory_number: int

        :param update_data: The data to update for the equipment, defaults to None.
        :type update_data: dict[str, any] or None
        """
        self.equipment_inventory_number = equipment_inventory_number
        self.update_data = update_data
        self.equipment_service = EquipmentService(self.equipment_inventory_number, self.update_data)

    def validate_equipment(self):
        """
        Validate the equipment's existence.

        This method uses the equipment service to validate the existence of the equipment based on its inventory number.
        If the equipment does not exist, it raises a ControllerException.

        :raises ControllerException: If the equipment does not exist. HTTP status code 404.
        """
        if not self.equipment_service.validate_equipment():
            raise ControllerException("Equipment not found.", 404)

    def update_equipment(self):
        """
        Update the equipment's data.

        This method uses the equipment service to update the equipment's data.
        If the update data is invalid, it raises a ControllerException.

        :raises ControllerException: If the equipment update data is invalid. HTTP status code 400.
        """
        if not self.equipment_service.update_equipment_data():
            raise ControllerException("Invalid equipment update data.", 400)

    def update_equipment_status_as_damaged(self):
        """
        Update the status of the equipment as damaged.

        This method uses the equipment service to update the status of the equipment.
        """
        self.equipment_service.update_equipment_status_as_damaged()

    def delete_equipment(self):
        """
        Delete the equipment.

        This method uses the equipment service to delete the equipment based on its inventory number.
        """
        self.equipment_service.delete_equipment()

    def create_response_with_equipment_data(self):
        """
        Create a response containing all data about the equipment.

        This method uses the equipment service to retrieve all data about the equipment and prepares a response.

        :return: A dictionary containing all data about the equipment and HTTP status code of 200.
        :rtype: tuple[dict[str, any], int]
        """
        return self.equipment_service.prepare_response_with_equipment_data(), 200

    def create_response_with_successful_update_message(self):
        """
        Create a response with a successful update message.

        :return: A dictionary containing a success message and HTTP status code of 200.
        :rtype: tuple[dict[str, str], int]
        """
        return {"message": "Equipment updated successfully."}, 200

    def create_response_with_successful_delete_message(self):
        """
        Create a response with a successful delete message.

        :return: A dictionary containing a success message and HTTP status code of 200.
        :rtype: tuple[dict[str, str], int]
        """
        return {"message": "Equipment deleted successfully."}, 200
