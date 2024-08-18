from datetime import date

from ....databases.exts import db
from ...models import Equipment


class EquipmentRepository:
    """
    The EquipmentRepository class encapsulates the logic necessary to access the database and
    perform CRUD operations on the Equipment model.

    :ivar equipment_inventory_number: Unique inventory number of the equipment.
    :type equipment_inventory_number: int

    :ivar equipment: Instance of Equipment model.
    :type equipment: Equipment
    """

    def __init__(self, equipment_inventory_number):
        """
        Initialize an instance of the EquipmentRepository class.

        The constructor tries to find an Equipment instance based on the provided equipment_inventory_number.
        If an Equipment instance is found, it is assigned to the equipment instance variable.

        :param equipment_inventory_number: Unique inventory number of a piece of equipment.
                                           Used to retrieve existing equipment by inventory number.
        :type equipment_inventory_number: int or None
        """
        self.equipment_inventory_number = equipment_inventory_number
        self.equipment = self._find_by_inventory_number()

    def save(self):
        """
        Save the current equipment instance to the database. The equipment status is set to "Free" and
        the registration_date is set to the current date.
        """
        self.equipment.status = "Free"
        self.equipment.registration_date = date.today()
        db.session.add(self.equipment)
        db.session.commit()

    def delete(self):
        """
        Delete the current equipment instance from the database.
        """
        db.session.delete(self.equipment)
        db.session.commit()

    def update(self, update_data):
        """
        Update the current equipment instance based on the provided update data.

        :param update_data: Dictionary containing new values for the equipment's attributes.
        :type update_data: dict[str, any]

        :return: Returns True if the update was successful, False otherwise.
        :rtype: bool
        """
        if not self._validate_update_data(update_data):
            return False

        if update_data.get("new_price_per_hour") is not None:
            self.equipment.price_per_hour = update_data.get("new_price_per_hour")

        if update_data.get("new_description") is not None:
            self.equipment.description = update_data.get("new_description")

        db.session.commit()
        return True

    def damaged(self):
        """
        Set the status of the equipment to "Damaged".
        """
        self.equipment.status = "Damaged"
        db.session.commit()

    def rent(self, new_rental_id):
        """
        Set the current rental ID of the equipment and update its status to "Rented".

        :param new_rental_id: ID of the current rental.
        :type new_rental_id: int
        """
        self.equipment.current_rental_id = new_rental_id
        self.equipment.status = "Rented"
        db.session.commit()

    def unrent(self):
        """
        Clear the current rental ID of the equipment and update its status to "Free".
        """
        self.equipment.current_rental_id = None
        self.equipment.status = "Free"
        db.session.commit()

    def get_equipment(self):
        """
        Retrieve the current equipment instance.

        :return: Returns the current equipment instance or None if it doesn't exist.
        :rtype: Equipment or None
        """
        return None if self.equipment is None else self.equipment

    def get_equipment_all_data(self):
        """
        Retrieve all data of the current equipment instance.

        :return: Returns a dictionary containing all data of the current equipment instance. Contains following keys:
                    - inventory_number (int): The equipment's unique inventory number.
                    - category (str): The category of the equipment.
                    - manufacturer (str): The manufacturer of the equipment.
                    - model (str): The model of the equipment.
                    - size (str): The size of the equipment.
                    - price_per_hour (float): The rental price per hour for the equipment.
                    - description (str): The description of the equipment.
                    - registration_date (datetime.date): The equipment's registration date.
                    - status (str): The current status of the equipment ("Free", "Rented", or "Damaged").
        :rtype: dict[str, any]
        """
        return {"inventory_number": self.equipment.inventory_number, "category": self.equipment.category,
                "manufacturer": self.equipment.manufacturer, "model": self.equipment.model, "size": self.equipment.size,
                "price_per_hour": self.equipment.price_per_hour, "description": self.equipment.description,
                "registration_date": self.equipment.registration_date, "status": self.equipment.status}

    def _find_by_inventory_number(self):
        """
        Retrieve equipment by its inventory number.

        :return: Returns the Equipment instance with the provided inventory number, or None if it doesn't exist.
        :rtype: Equipment or None
        """
        return Equipment.query.filter_by(inventory_number=self.equipment_inventory_number).first()

    @staticmethod
    def _validate_update_data(equipment_data):
        """
        Validate the data provided for updating equipment.

        :param equipment_data: Dictionary containing new values for the equipment's attributes.
        :type equipment_data: dict[str, any]

        :return: Returns True if the provided data is valid, False otherwise.
        :rtype: bool
        """
        return Equipment.validate_price_per_hour(equipment_data.get("new_price_per_hour")) or \
            Equipment.validate_description(equipment_data.get("new_description"))
