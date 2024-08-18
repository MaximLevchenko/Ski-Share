from ...services import EquipmentsSortService
from ..exceptions import ControllerException


class EquipmentsSortController:
    """
    The EquipmentsSortController class provides methods for sorting equipment and creating an appropriate response.

    This class acts as a controller for handling requests related to sorting equipment.

    :ivar sort_data: The data specifying how equipment should be sorted.
    :type sort_data: dict[str, any]

    :ivar sorted_equipments: The sorted equipment data.
    :type sorted_equipments: list[dict[str, any]] or None
    """

    def __init__(self, sort_data):
        """
        Initialize a new instance of the EquipmentsSortController class.

        :param sort_data: The data specifying how equipment should be sorted.
        :type sort_data: dict[str, any]
        """
        self.sort_data = sort_data
        self.sorted_equipments = None
        self.equipments_sort_service = EquipmentsSortService(self.sort_data)

    def sort_equipments(self):
        """
        Sort equipment data based on the provided parameters.

        This method uses the EquipmentsSortService to sort all equipment based on the sorting data.
        If the sorting fails, it raises a ControllerException.

        :raise ControllerException: If the sorting fails due to invalid sort QUERY parameters with HTTP code 400.
        """
        self.sorted_equipments = self.equipments_sort_service.sort_equipments()
        if self.sorted_equipments is None:
            raise ControllerException("Invalid sort QUERY parameters.", 400)

    def create_response_with_sorted_equipments_data(self):
        """
        Create a response containing the sorted equipment data.

        This method prepares a response with the sorted equipment data.
        The response includes a 200 status code.

        :return: The response containing the sorted equipment data and a 200 status code.
        :rtype: tuple[list[dict[str, any]], int]
        """
        return self.sorted_equipments, 200
