from datetime import datetime
from sqlalchemy import text

from ...models import Rental, Equipment
from ....databases.exts import db


class RentalsRepository:
    """
    The RentalsRepository class provides methods for creating, retrieving, and sorting Rental objects.

    This class acts as a repository and uses the Rental model to perform operations related to rentals.
    """

    def __init__(self, create_data=None):
        """
        Initialize a new RentalsRepository.

        :param create_data: Optional dictionary containing the information about a rental for creating a new rental.
        :type create_data: dict[str, any] or None
        """
        self.create_data = create_data
        self.rental_id = None
        self.rentals_data = None

    def create(self):
        """
        Creates a Rental instance.

        This method takes a dictionary containing information about a rental, validates this data, and if valid,
        creates a Rental instance in the database. It also records the ID of the newly created rental instance.

        :return: True if the input data is valid and the Rental instance is created in the database, False otherwise.
        :rtype: bool
        """
        if not self._validate_create_data():
            return False

        new_rental = Rental(
            date_start=datetime.utcnow(),
            date_end=datetime.strptime(self.create_data["date_end"], "%Y-%m-%dT%H:%M:%S.%fZ"),
            payment_type=self.create_data["payment_type"],
            base_price=self.create_data["base_price"],
            is_closed=False,
            damage_fee=0,
            late_return_fee=0,

            employee_id=self.create_data["employee_id"],
            client_id=self.create_data["client_id"],
            equipments=", ".join(map(str, self.create_data.get("equipments")))
        )
        db.session.add(new_rental)
        db.session.commit()
        self.rental_id = new_rental.id
        return True

    def get_rental_id(self):
        """
        Retrieve the ID of the last rental created by this repository instance.

        :return: The ID of the last rental created, or None if no rental has been created.
        :rtype: int or None
        """
        return self.rental_id

    def get_all(self):
        """
        Retrieves all Rental instances.

        This method fetches all Rental instances from the database, and stores them in memory for future sorting.

        :return: A list of all Rental instances fetched from the database.
        :rtype: list[Rental]
        """
        self.rentals_data = Rental.query.all()
        return self.rentals_data

    def sort_all(self, sort_data):
        """
        Sorts all Rental instances based on the provided sorting parameters.

        This method takes a dictionary specifying how rentals should be sorted and returns a sorted list
        of all Rental instances from the in-memory data.

        :param sort_data: Dictionary containing the sorting parameters.
        :type sort_data: dict[str, any]

        :return: A sorted list of all in-memory Rental instances if the sorting parameters are valid, None otherwise.
        :rtype: list[Rental] or None
        """
        self.rentals_data = None if not Rental.validate_sort_params(sort_data) else \
            Rental.query.order_by(self._prepare_rentals_text_query(sort_data)).all()

        return self.rentals_data

    def _prepare_rentals_text_query(self, sort_data):
        """
        Prepares a text query for sorting rentals.

        This method takes in a dictionary that specifies how rentals should be sorted and prepares a text query
        based on this input.

        :param sort_data: Dictionary specifying how rentals should be sorted.
        :type sort_data: dict[str, any]

        :return: A text query for sorting rentals.
        :rtype: str
        """
        sort_text_query = ", ".join(f"{key} {Rental.QUERY_SORT_PARAMS[value]}" for key, value in sort_data.items())

        return text(sort_text_query)

    def _validate_create_data(self):
        """
        Validates the data for creating a Rental instance.

        This method checks whether the data provided in the create_data dictionary is valid for
        creating a Rental instance.
        The validation process includes checking the validity of the payment type and the list of equipment.

        :return: True if the input data is valid for creating a Rental, False otherwise.
        :rtype: bool
        """
        return Rental.validate_payment_type(self.create_data.get("payment_type")) and \
            Rental.validate_equipments(self.create_data.get("equipments"))
