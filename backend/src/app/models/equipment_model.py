from ...databases.exts import db


class Equipment(db.Model):
    """
    The Equipment class represents equipment in the rental system.

    :ivar inventory_number: The unique inventory number of the equipment. Acts as the primary key.
    :type inventory_number: int

    :ivar category: The category of the equipment (e.g., "Ski", "Snowboard", etc.).
    :type category: str

    :ivar manufacturer: The manufacturer of the equipment.
    :type manufacturer: str

    :ivar model: The model of the equipment.
    :type model: str

    :ivar size: The size of the equipment.
    :type size: str

    :ivar status: The current status of the equipment (e.g., "Free", "Rented", "Damaged").
    :type status: str

    :ivar price_per_hour: The rental price per hour for the equipment.
    :type price_per_hour: int

    :ivar description: A text description of the equipment.
    :type description: str

    :ivar registration_date: The date when the equipment was added to the system.
    :type registration_date: datetime.date

    :ivar current_rental_id: The ID of the current rental if the equipment is rented, otherwise None.
    :type current_rental_id: int or None

    :ivar EQUIPMENT_CATEGORIES: A list of valid categories that an equipment can belong to.
    :type EQUIPMENT_CATEGORIES: list[str]

    :ivar EQUIPMENT_STATUSES: A list of valid statuses that an equipment can have.
    :type EQUIPMENT_STATUSES: list[str]

    :ivar SORT_ATTRIBUTES: A list of attributes on which we can sort the equipments.
    :type SORT_ATTRIBUTES: list[str]

    :ivar QUERY_SORT_PARAMS: A dictionary defining the sort order based on certain key strings.
                             Each key string corresponds to a certain sort order.
    :type QUERY_SORT_PARAMS: dict[str, str]
    """
    inventory_number = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(40), nullable=False)
    manufacturer = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(25), nullable=False)
    status = db.Column(db.String(30), nullable=False)
    price_per_hour = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text(), nullable=False)
    registration_date = db.Column(db.Date(), nullable=False)
    current_rental_id = db.Column(db.Integer, nullable=True)

    EQUIPMENT_CATEGORIES = ["Ski", "Snowboard", "Ski boots", "Snowboard boots", "Helmet", "Ski poles", "Ski suit"]

    EQUIPMENT_STATUSES = ["Free", "Rented", "Damaged"]

    SORT_ATTRIBUTES = ["inventory_number", "category", "manufacturer", "model", "size", "price_per_hour",
                       "registration_date", "current_rental_id"]

    QUERY_SORT_PARAMS = {"abc": "asc", "zyx": "desc",
                         "lowest": "asc", "highest": "desc",
                         "oldest": "asc", "latest": "desc",
                         "Free": "asc", "Rented": "desc"}

    def __repr__(self):
        """
        Method that returns a string representation of the Equipment instance.

        :return: String representation of the Equipment instance.
        :rtype: Equipment
        """
        return f"<Equipment-{self.inventory_number}>"

    @staticmethod
    def validate_category(equipment_category):
        """
        Validate the category of the equipment.

        :param equipment_category: The category of the equipment.
        :type equipment_category: str

        :return: True if the category is one of the EQUIPMENT_CATEGORIES, False otherwise.
        :rtype: bool
        """
        return False if equipment_category is None or equipment_category not in Equipment.EQUIPMENT_CATEGORIES else True

    @staticmethod
    def validate_manufacturer(equipment_manufacturer):
        """
        Validate the manufacturer of the equipment.

        :param equipment_manufacturer: The manufacturer of the equipment.
        :type equipment_manufacturer: str

        :return: True if the manufacturer is non-empty string, False otherwise.
        :rtype: bool
        """
        return False if equipment_manufacturer is None or not isinstance(equipment_manufacturer, str) or \
            len(equipment_manufacturer) == 0 else True

    @staticmethod
    def validate_model(equipment_model):
        """
        Validate the model of the equipment.

        :param equipment_model: The manufacturer of the equipment.
        :type equipment_model: str

        :return: True if the model is non-empty string, False otherwise.
        :rtype: bool
        """
        return False if equipment_model is None or not isinstance(equipment_model, str) or len(equipment_model) == 0 \
            else True

    @staticmethod
    def validate_size(equipment_size):
        """
        Validate the size of the equipment.

        :param equipment_size: The size of the equipment.
        :type equipment_size: str

        :return: True if the size is non-empty string, False otherwise.
        :rtype: bool
        """
        return False if equipment_size is None or not isinstance(equipment_size, str) or len(equipment_size) == 0 \
            else True

    @staticmethod
    def validate_price_per_hour(equipment_price_per_hour):
        """
        Validate the price per hour of the equipment.

        :param equipment_price_per_hour: The price per hour of the equipment.
        :type equipment_price_per_hour: int

        :return: True if the size is non-negative integer, False otherwise.
        :rtype: bool
        """
        return False if equipment_price_per_hour is None or not isinstance(equipment_price_per_hour, int) or \
            equipment_price_per_hour < 0 else True

    @staticmethod
    def validate_description(equipment_description):
        """
        Validate the description of the equipment.

        :param equipment_description: The description of the equipment.
        :type equipment_description: str

        :return: True if the size is non-empty string, False otherwise.
        :rtype: bool
        """
        return False if equipment_description is None or not isinstance(equipment_description, str) or \
            len(equipment_description) == 0 else True

    @staticmethod
    def validate_sort_params(sort_data):
        """
        Validate the provided sorting parameters.

        :param sort_data: Dictionary of sorting parameters.
        :type sort_data: dict

        :return: Returns True if all keys and values are valid according to SORT_ATTRIBUTES and QUERY_SORT_PARAMS,
                 False otherwise.
        :rtype: bool
        """
        return all(key in Equipment.SORT_ATTRIBUTES and value in Equipment.QUERY_SORT_PARAMS.keys()
                   for key, value in sort_data.items())
