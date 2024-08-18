from datetime import date
from sqlalchemy import text

from ....databases.exts import db
from ...models import Equipment


class EquipmentsRepository:
    """
    The EquipmentsRepository class provides methods for creating, retrieving, and sorting Equipment objects.

    This class acts as a repository and uses the Equipment model to perform operations related to equipment.
    """

    def __init__(self, create_data=None):
        """
        Initialize a new EquipmentsRepository.

        :param create_data: Optional dictionary containing the information about an equipment.
        :type create_data: dict[str, any], optional
        """
        self.create_data = create_data
        self.equipments_data = None

    def create(self):
        """
        Creates an Equipment instance.

        This method takes in a dictionary containing information about an equipment, validates this data, and if valid,
        creates an Equipment instance.

        :return: If the equipment was created.
        :rtype: bool
        """
        if not self._validate_create_data():
            return False

        new_equipment = Equipment(
            category=self.create_data["category"],
            manufacturer=self.create_data["manufacturer"],
            model=self.create_data["model"],
            size=self.create_data["size"],
            price_per_hour=self.create_data["price_per_hour"],
            description=self.create_data["description"],
            status="Free",
            registration_date=date.today()
        )
        db.session.add(new_equipment)
        db.session.commit()
        return True

    def get_all(self):
        """
        Retrieves all Equipment instances.

        :return: A list of all Equipment instances.
        :rtype: list[Equipment]
        """
        self.equipments_data = Equipment.query.all()
        return self.equipments_data

    def sort_all(self, sort_data):
        """
        Sorts all Equipment instances based on the provided sorting parameters.

        :param sort_data: Dictionary containing the sorting parameters.
        :type sort_data: dict[str, any]

        :return: A sorted list of all Equipment instances if the sorting parameters are valid, None otherwise.
        :rtype: list[Equipment] or None
        """
        self.equipments_data = None if not Equipment.validate_sort_params(sort_data) else \
            Equipment.query.order_by(self._prepare_equipments_text_query(sort_data)).all()

        return self.equipments_data

    def _prepare_equipments_text_query(self, sort_data):
        """
        Prepare a text query for sorting equipment data based on the provided parameters.

        This method generates a text query string using the sort_data dictionary.
        The sort_data items should contain the key-value pairs where the key is the column name
        and the value is the sort direction ('asc' or 'desc').

        :param sort_data: The data specifying how equipments should be sorted.
        :type sort_data: dict[str, any]

        :return: The text query string for sorting equipment data, converted into a SQL Alchemy TextClause.
        :rtype: str
        """
        sort_text_query = ", ".join(f"{key} {Equipment.QUERY_SORT_PARAMS[value]}" for key, value in sort_data.items())

        return text(sort_text_query)

    def _validate_create_data(self):
        """
        Validates the data for creating an Equipment instance.

        This method validates the creation data.

        :return: True if the input data is valid, False otherwise.
        :rtype: bool
        """
        return Equipment.validate_category(self.create_data.get("category")) and \
            Equipment.validate_manufacturer(self.create_data.get("manufacturer")) and \
            Equipment.validate_model(self.create_data.get("model")) and \
            Equipment.validate_size(self.create_data.get("size")) and \
            Equipment.validate_price_per_hour(self.create_data.get("price_per_hour")) and \
            Equipment.validate_description(self.create_data.get("description"))
