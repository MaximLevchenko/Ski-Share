from ...services import EquipmentsService
from ..exceptions import ControllerException


class EquipmentsController:
    """
    The EquipmentsController class provides methods for handling equipment-related requests.

    This class acts as a controller that uses the EquipmentsService for creating new equipment
    and preparing data related to all equipment.

    :ivar equipment_data: The data for creating a new piece of equipment.
    :type equipment_data: dict[str, any] or None

    :ivar equipments_service: An instance of the EquipmentsService class for managing equipment data.
    :type equipments_service: EquipmentsService
    """

    def __init__(self, equipment_data=None):
        """
        Initialize a new instance of the EquipmentsController class.

        :param equipment_data: The data for creating a new piece of equipment, defaults to None.
        :type equipment_data: dict[str, any] or None
        """
        self.equipment_data = equipment_data
        self.equipments_service = EquipmentsService(equipment_data)

    def create_equipment(self):
        """
        Create a new piece of equipment.

        This method uses the equipments service to create a new piece of equipment with the provided data.
        If the equipment data is invalid, it raises a ControllerException.

        :raise ControllerException: If the equipment data is invalid with HTTP code 400.
        """
        if not self.equipments_service.create_equipment():
            raise ControllerException("Invalid equipment data.", 400)

    def create_response_with_equipments_data(self):
        """
        Prepare a response containing data about all equipment.

        This method uses the equipments service to retrieve data about all pieces of equipment.

        :return: A tuple where the first item is a list of data about all pieces of equipment and
                 the second item is the HTTP status code 200.
        :rtype: tuple[list[dict[str, any]], int]
        """
        return self.equipments_service.prepare_response_with_equipments_data(), 200

    def create_response_with_successful_create_message(self):
        """
        Prepare a response containing a success message for equipment creation.

        :return: A tuple where the first item is a dictionary containing a success message and
                 the second item is the HTTP status code 200.
        :rtype: tuple[dict[str, str], int]
        """
        return {"message": "Equipment created successfully."}, 200
