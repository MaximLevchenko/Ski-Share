from ...repositories import EquipmentsRepository


class EquipmentsService:
    """
    The EquipmentsService class provides methods for managing data for multiple pieces of equipment.

    This class acts as a service for creating new pieces of equipment and preparing data
    related to all pieces of equipment.

    :ivar create_data: The data for creating a new piece of equipment.
    :type create_data: dict[str, any] or None
    """

    def __init__(self, create_data=None):
        """
        Initialize a new instance of the EquipmentsService class.

        :param create_data: The data for creating a new piece of equipment, defaults to None.
        :type create_data: dict[str, any] or None
        """
        self.create_data = create_data
        self.equipments_repository = EquipmentsRepository(self.create_data)

    def create_equipment(self):
        """
        Create a new piece of equipment.

        This method uses the equipments repository to create a new piece of equipment with the provided data.

        :return: True if the equipment was created, False otherwise. Returns False if no data was provided for creation.
        :rtype: bool
        """
        return self.equipments_repository.create()

    def prepare_response_with_equipments_data(self):
        """
        Prepare a response containing data about all pieces of equipment.

        This method uses the equipments repository to retrieve data about all pieces of equipment.

        :return: A list of data about all pieces of equipment. Can be empty if no equipment objects were created.
        :rtype: list[dict[str, any]]
        """
        return self.equipments_repository.get_all()
