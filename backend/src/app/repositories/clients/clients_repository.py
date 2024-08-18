from datetime import date, datetime
from sqlalchemy import text

from ...models import Client
from ....databases.exts import db


class ClientsRepository:
    """
    The ClientsRepository class provides methods for creating, retrieving, and sorting Client objects.

    This class acts as a repository and uses the Client model to perform operations related to clients.
    """

    def __init__(self, create_data=None):
        """
        Initialize a new Clients Repository.

        :param create_data: Optional dictionary containing the information about a client for creating a new client.
        :type create_data: dict[str, any] or None
        """
        self.create_data = create_data
        self.clients_data = None

    def create(self):
        """
        Creates a Client instance.

        This method takes the client data provided during the initialization of the repository, validates it,
        and if valid, creates a Client instance.

        :return: True if the client was created, False otherwise.
        :rtype: bool
        """
        if not self._validate_create_data():
            return False

        new_client = Client(
            name=self.create_data["name"],
            surname=self.create_data["surname"],
            email=self.create_data["email"],
            phone=self.create_data["phone"],
            passport_number=self.create_data["passport_number"],
            address=self.create_data["address"],
            birth_date=datetime.strptime(self.create_data["birth_date"], "%Y-%m-%d").date(),
            registration_date=date.today()
        )
        db.session.add(new_client)
        db.session.commit()
        return True

    def get_all(self):
        """
        Retrieves all Client instances.

        This method fetches all the Client instances from the database and stores the result.

        :return: A list of all Client instances.
        :rtype: list[Client]
        """
        self.clients_data = Client.query.all()
        return self.clients_data

    def sort_all(self, sort_data):
        """
        Sorts all Client instances based on the provided sorting parameters and stores the result.

        :param sort_data: Dictionary containing the sorting parameters.
        :type sort_data: dict[str, any]

        :return: A sorted list of all Client instances if the sorting parameters are valid, None otherwise.
        :rtype: list[Client] or None
        """
        self.clients_data = None if not Client.validate_sort_params(sort_data) else \
            Client.query.order_by(self._prepare_clients_text_query(sort_data)).all()

        return self.clients_data

    def _prepare_clients_text_query(self, sort_data):
        """
        Prepare a text query for sorting client data based on the provided parameters.

        This method generates a text query string using the sort_data dictionary.
        The sort_data items should contain the key-value pairs where the key is the column name
        and the value is the sort direction ('asc' or 'desc').

        :param sort_data: The data specifying how clients should be sorted.
        :type sort_data: dict[str, any]

        :return: The text query string for sorting client data.
        :rtype: str
        """
        sort_text_query = ", ".join(f"{key} {Client.QUERY_SORT_PARAMS[value]}" for key, value in sort_data.items())

        return text(sort_text_query)

    def _validate_create_data(self):
        """
        Validates the data for creating a Client instance.

        This method takes the client data provided during the initialization of the repository and validates this data.
        It checks the validation criteria defined in the Client model for each data field.

        :return: True if the input data is valid, False otherwise.
        :rtype: bool
        """
        return Client.validate_name(self.create_data.get("name")) and \
            Client.validate_surname(self.create_data.get("surname")) and \
            Client.validate_email(self.create_data.get("email")) and \
            Client.validate_phone(self.create_data.get("phone")) and \
            Client.validate_passport_number(self.create_data.get("passport_number")) and \
            Client.validate_address(self.create_data.get("address")) and \
            Client.validate_birth_date(self.create_data.get("birth_date")) and \
            Client.query.filter_by(email=self.create_data.get("email")).first() is None
