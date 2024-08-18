from datetime import datetime

from ....databases.exts import db
from ...models import Rental


class RentalRepository:
    """
    The RentalRepository class encapsulates the logic necessary to access the database and
    perform CRUD operations on the Rental model.

    :ivar rental_id: Unique identifier of the rental.
    :type rental_id: int

    :ivar rental: Instance of Rental model.
    :type rental: Rental
    """

    def __init__(self, rental_id):
        """
        Initialize an instance of the RentalRepository class.

        The constructor tries to find a Rental instance based on the provided rental_id.
        If a Rental instance is found, it is assigned to the rental instance variable.

        :param rental_id: Unique identifier of a rental. Used to retrieve an existing rental by ID.
        :type rental_id: int
        """
        self.rental_id = rental_id
        self.rental = self._find_by_id()

    def save(self):
        """
        Save the current rental instance to the database.
        """
        self.rental.date_start = datetime.utcnow()
        self.rental.is_closed = False
        self.rental.damage_fee = 0
        self.rental.late_return_fee = 0
        db.session.add(self.rental)
        db.session.commit()

    def delete(self):
        """
        Delete the current rental instance from the database.
        """
        db.session.delete(self.rental)
        db.session.commit()

    def update(self, update_data):
        """
        Update the current rental instance based on the provided update data.

        :param update_data: Dictionary containing new values for the rental's attributes.
        :type update_data: dict[str, any]

        :return: Returns True if the update was successful, False otherwise.
        :rtype: bool
        """
        if not self._validate_update_data(update_data):
            return False

        self.rental.description = update_data.get("new_description")
        db.session.commit()
        return True

    def close(self, close_data):
        """
        Close the current rental instance in the database.

        :param close_data: Dictionary containing new values for the rental's attributes.
        :type close_data: dict[str, any]

        :return: Returns True if the closure was successful, False otherwise.
        :rtype: bool
        """
        if not self._validate_close_data(close_data):
            return False

        self.rental.is_closed = True

        if close_data.get("new_damage_fee") is not None:
            self.rental.damage_fee = close_data.get("new_damage_fee")

        if close_data.get("new_late_return_fee") is not None:
            self.rental.late_return_fee = close_data.get("new_late_return_fee")

        db.session.commit()
        return True

    def get_rental(self):
        """
        Retrieve the current rental instance.

        :return: Returns the current rental instance or None if it doesn't exist.
        :rtype: Rental or None
        """
        return self.rental

    def get_rental_all_data(self):
        """
        Retrieve all data of the current rental instance.

        :return: Returns a dictionary containing all data of the current rental instance. Contains following keys:
                    - id (int): The rental's ID.
                    - date_start (datetime.datetime): The rental's start date.
                    - date_end (datetime.datetime): The rental's end date.
                    - payment_type (str): The rental's payment type.
                    - base_price (int): The rental's base price.
                    - is_closed (bool): The rental's status.
                    - damage_fee (int): The rental's damage fee.
                    - late_return_fee (int): The rental's late return fee.
                    - description (str): The rental's description.
                    - employee_id (int): The ID of the employee who managed the rental.
                    - client_id (int): The ID of the client who made the rental.
        :rtype: dict[str, any]
        """
        return {"id": self.rental.id, "date_start": self.rental.date_start, "date_end": self.rental.date_end,
                "payment_type": self.rental.payment_type, "base_price": self.rental.base_price,
                "is_closed": self.rental.is_closed, "damage_fee": self.rental.damage_fee,
                "late_return_fee": self.rental.late_return_fee, "description": self.rental.description,
                "employee_id": self.rental.employee_id, "client_id": self.rental.client_id}

    def get_rental_full_data(self):
        """
        Retrieve full data of the current rental instance including rented equipments info.

        :return: Returns a dictionary containing all data of the current rental instance. Contains following keys:
                    - id (int): The rental's ID.
                    - date_start (datetime): The rental's start date.
                    - date_end (datetime): The rental's end date.
                    - payment_type (str): The rental's payment type.
                    - base_price (int): The rental's base price.
                    - is_closed (bool): The rental's status.
                    - damage_fee (int): The rental's damage fee.
                    - late_return_fee (int): The rental's late return fee.
                    - description (str): The rental's description.
                    - employee_id (int): The ID of the employee who managed the rental.
                    - client_id (int): The ID of the client who made the rental.
                    - equipments (list[int]): The list of rented equipments IDs.
        :rtype: dict[str, any]
        """
        rental_full_data = self.get_rental_all_data()
        rental_full_data["equipments"] = self._find_rented_equipments()

        return rental_full_data

    def get_rental_equipments(self):
        """
        Retrieve the list of equipment IDs related to the current rental.

        :return: A list of equipment IDs related to the current rental.
        :rtype: list[int]
        """
        return self._find_rented_equipments()

    def _find_by_id(self):
        """
        Retrieve a rental by its ID.

        :return: Returns the Rental instance with the provided ID, or None if it doesn't exist.
        :rtype: Rental
        """
        return Rental.query.filter_by(id=self.rental_id).first() if self.rental_id else None

    def _find_rented_equipments(self):
        """
        Retrieve the list of equipments related to the current rental.

        :return: Returns a list of equipments related to the current rental.
        :rtype: list[int]
        """
        return self.rental.equipments.split(", ")

    @staticmethod
    def _validate_update_data(rental_data):
        """
        Validate the data provided for updating a rental.

        :param rental_data: Dictionary containing new values for the rental's attributes.
        :type rental_data: dict[str, any]

        :return: Returns True if the provided data is valid, False otherwise.
        :rtype: bool
        """
        return Rental.validate_description(rental_data.get("new_description"))

    @staticmethod
    def _validate_close_data(rental_data):
        """
        Validate the data provided for closing a rental.

        :param rental_data: Dictionary containing new values for the rental's closing data.
        :type rental_data: dict[str, any]

        :return: Returns True if the provided data is valid, False otherwise.
        :rtype: bool
        """
        return True if rental_data.get("new_damage_fee") is None and rental_data.get("new_late_return_fee") is None \
            else Rental.validate_fee(rental_data.get("new_damage_fee")) or \
            Rental.validate_fee(rental_data.get("new_late_return_fee"))
