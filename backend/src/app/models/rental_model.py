from ...databases.exts import db


class Rental(db.Model):
    """
    The Rental data model class describes the data structure of a rental in the database.

    :ivar id: Unique identifier for a rental.
    :type id: int

    :ivar date_start: Start date of the rental.
    :type date_start: datetime.datetime

    :ivar date_end: End date of the rental.
    :type date_end: datetime.datetime

    :ivar payment_type: Type of payment for the rental. Possible types are "Cash", "Card", "Bank transfer".
    :type payment_type: str

    :ivar base_price: Base price for the rental.
    :type base_price: int

    :ivar is_closed: Indicates whether the rental is closed.
    :type is_closed: bool

    :ivar damage_fee: Damage fee associated with the rental.
    :type damage_fee: int

    :ivar late_return_fee: Late return fee associated with the rental.
    :type late_return_fee: int

    :ivar description: Description of the rental.
    :type description: str

    :ivar employee_id: The id of the employee who handled the rental.
    :type employee_id: int

    :ivar client_id: The id of the client who made the rental.
    :type client_id: int

    :ivar equipments: List of equipment that were rented.
    :type equipments: str

    :ivar RENTAL_PAYMENT_TYPES: A list of possible payment types for the rental.
    :type RENTAL_PAYMENT_TYPES: list[str]

    :ivar SORT_ATTRIBUTES: A list of attributes on which we can sort the rentals.
    :type SORT_ATTRIBUTES: list[str]

    :ivar QUERY_SORT_PARAMS: A dictionary defining the sort order based on certain key strings.
                             Each key string corresponds to a certain sort order.
    :type QUERY_SORT_PARAMS: dict[str, str]
    """
    id = db.Column(db.Integer, primary_key=True)
    date_start = db.Column(db.DateTime(), nullable=False)
    date_end = db.Column(db.DateTime(), nullable=False)
    payment_type = db.Column(db.String(15), nullable=False)
    base_price = db.Column(db.Integer, nullable=False)
    is_closed = db.Column(db.Boolean, nullable=False)
    damage_fee = db.Column(db.Integer, nullable=False)
    late_return_fee = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text(), nullable=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    equipments = db.Column(db.Text(), nullable=False)

    RENTAL_PAYMENT_TYPES = ["Cash", "Card", "Bank transfer"]

    SORT_ATTRIBUTES = ["id", "date_start", "date_end", "payment_type", "base_price", "is_closed", "damage_fee",
                       "late_return_fee", "description"]

    QUERY_SORT_PARAMS = {"abc": "asc", "zyx": "desc",
                         "lowest": "asc", "highest": "desc",
                         "oldest": "asc", "latest": "desc",
                         "Free": "asc", "Rented": "desc"}

    def __repr__(self):
        """
        Method that returns a string representation of the Rental instance.

        :return: String representation of the Rental instance.
        :rtype: Rental
        """
        return f"<Rental-{self.id}>"

    @staticmethod
    def validate_payment_type(payment_type):
        """
        Validate the provided payment type for the rental.

        :param payment_type: Type of payment for the rental.
        :type payment_type: str

        :return: Returns True if the payment_type is a non-empty string and it's within the allowed payment types,
                 False otherwise.
        :rtype: bool
        """
        return False if payment_type is None or payment_type not in Rental.RENTAL_PAYMENT_TYPES else True

    @staticmethod
    def validate_equipments(equipments):
        """
        Validate the provided list of equipment for the rental.

        :param equipments: List of equipment for the rental.
        :type equipments: list[int]

        :return: Returns True if the list is not empty, False otherwise.
        :rtype: bool
        """
        return False if equipments is None or len(equipments) == 0 else True

    @staticmethod
    def validate_fee(fee):
        """
        Validate the provided fee.

        :param fee: The fee to be validated.
        :type fee: int

        :return: Returns True if the fee is an integer and is not less than zero, False otherwise.
        :rtype: bool
        """
        return False if fee is None or not isinstance(fee, int) or fee < 0 else True

    @staticmethod
    def validate_description(description):
        """
        Validate the provided description.

        :param description: Description to be validated.
        :type description: str

        :return: Returns True if the description is not an empty string, False otherwise.
        :rtype: bool
        """
        return False if description is None or len(description) == 0 else True

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
        return all(key in Rental.SORT_ATTRIBUTES and value in Rental.QUERY_SORT_PARAMS.keys()
                   for key, value in sort_data.items())
