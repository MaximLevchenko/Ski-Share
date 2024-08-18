from ...repositories import EquipmentsRepository


class EquipmentsSortService:
    """
    The EquipmentsSortService class provides a method to sort equipment data.

    This class acts as a service for sorting data related to equipment.
    """

    def __init__(self, sort_data):
        """
        Initialize a new instance of the EquipmentsSortService class.

        :param sort_data: The data specifying how equipment should be sorted. This could include parameters like name,
                          model, manufacturer, etc., along with the sort direction ('asc' or 'desc').
        :type sort_data: dict[str, any]
        """
        self.sort_data = sort_data
        self.equipments_repository = EquipmentsRepository()

    def sort_equipments(self):
        """
        Sort equipment data based on the provided parameters.

        This method uses the EquipmentsRepository to sort all equipment based on the sorting data, which was
        provided when this instance of the EquipmentsSortService was created.

        :return: The sorted equipment data or None if the sort data wasn't valid.
        :rtype: list[dict[str, any]] or None
        """
        return self.equipments_repository.sort_all(self.sort_data)
