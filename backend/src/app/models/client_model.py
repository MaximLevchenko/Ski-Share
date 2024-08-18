from ...databases.exts import db


class Client(db.Model):
    """
    The Client data model class describes the data structure of a client in the database.

    :ivar id: Unique identifier for a client.
    :type id: int

    :ivar name: Name of the client.
    :type name: str

    :ivar surname: Surname of the client.
    :type surname: str

    :ivar email: Unique email for the client.
    :type email: str

    :ivar phone: Unique phone number of the client.
    :type phone: str

    :ivar passport_number: Unique passport number for the client.
    :type passport_number: str

    :ivar address: Address of the client.
    :type address: str

    :ivar birth_date: Date of birth of the client.
    :type birth_date: datetime.date

    :ivar registration_date: Date of registration for the client.
    :type registration_date: datetime.date

    :ivar rentals: List of rentals that the client has made.
    :type rentals: list[rental]

    :ivar SORT_ATTRIBUTES: A list of attributes on which we can sort the clients.
    :type SORT_ATTRIBUTES: list[str]

    :ivar QUERY_SORT_PARAMS: A dictionary defining the sort order based on certain key strings.
                             Each key string corresponds to a certain sort order.
    :type QUERY_SORT_PARAMS: dict[str, str]
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    passport_number = db.Column(db.String(40), unique=True, nullable=False)
    address = db.Column(db.String(60), nullable=False)
    birth_date = db.Column(db.Date(), nullable=False)
    registration_date = db.Column(db.Date(), nullable=False)
    rentals = db.relationship('Rental', backref='client')

    SORT_ATTRIBUTES = ["id", "name", "surname", "email", "phone", "passport_number", "address", "birth_date",
                       "registration_date"]

    QUERY_SORT_PARAMS = {"abc": "asc", "zyx": "desc",
                         "lowest": "asc", "highest": "desc",
                         "oldest": "asc", "latest": "desc",
                         "Free": "asc", "Rented": "desc"}

    def __repr__(self):
        """
        Method that returns a string representation of the Client instance.

        :return: String representation of the Client instance.
        :rtype: Client
        """
        return f"<Client-{self.id}>"

    @staticmethod
    def validate_name(client_name):
        """
        Validate the provided client name.

        :param client_name: Name of the client.
        :type client_name: str

        :return: Returns True if the name is a non-empty string, False otherwise.
        :rtype: bool
        """
        return False if client_name is None or not isinstance(client_name, str) or len(client_name) == 0 else True

    @staticmethod
    def validate_surname(client_surname):
        """
        Validate the provided client surname.

        :param client_surname: Surname of the client.
        :type client_surname: str

        :return: Returns True if the surname is a non-empty string, False otherwise.
        :rtype: bool
        """
        return False if client_surname is None or not isinstance(client_surname, str) or len(client_surname) == 0 \
            else True

    @staticmethod
    def validate_email(client_email):
        """
        Validate the provided client email.

        :param client_email: Email of the employee.
        :type client_email: str

        :return: Returns True if the email is a string that contains both '@' and '.', False otherwise.
        :rtype: bool
        """
        return False if client_email is None or not isinstance(client_email, str) or len(client_email) < 6 or \
            '@' not in client_email or '.' not in client_email else True

    @staticmethod
    def validate_phone(client_phone):
        """
        Validate the provided client phone.

        :param client_phone: Phone number of the client.
        :type client_phone: str

        :return: Returns True if the phone number is a string of length at least 8 and contains '+', False otherwise.
        :rtype: bool
        """
        return False if client_phone is None or not isinstance(client_phone, str) or len(client_phone) < 8 or \
            '+' not in client_phone else True

    @staticmethod
    def validate_passport_number(client_passport_number):
        return False if client_passport_number is None or not isinstance(client_passport_number, str) or \
            len(client_passport_number) < 6 else True

    @staticmethod
    def validate_address(client_address):
        """
        Validate the address of the client.

        :param client_address: Address of the client.
        :type client_address: str

        :return: True if the address is a string of length >= 5 signs, False otherwise.
        :rtype: bool
        """
        return False if client_address is None or not isinstance(client_address, str) or len(client_address) < 5 \
            else True

    @staticmethod
    def validate_birth_date(client_birth_date):
        """
        Validate the birthdate of the client.

        :param client_birth_date: Birthdate of the client.
        :type client_birth_date: str

        :return: True if the birthdate is a string of length of 10 signs, False otherwise.
        :rtype: bool
        """
        return False if client_birth_date is None or not isinstance(client_birth_date, str) or \
            len(client_birth_date) != 10 else True

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
        return all(key in Client.SORT_ATTRIBUTES and value in Client.QUERY_SORT_PARAMS.keys()
                   for key, value in sort_data.items())
