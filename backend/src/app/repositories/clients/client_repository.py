from ....databases.exts import db
from ...models import Client


class ClientRepository:
    """
    The ClientRepository class encapsulates the logic necessary to access the database and
    perform CRUD operations on the Client model.

    :ivar client_id: Unique identifier of the client.
    :type client_id: int

    :ivar client_email: Email of the client.
    :type client_email: str

    :ivar client: Instance of Client model. Default is None.
    :type client: Client or None
    """

    def __init__(self, client_id=None, client_email=None):
        """
        Initialize an instance of the ClientRepository class.

        The constructor tries to find a Client instance based on the provided client_id or client_email. If a
        Client instance is found, it is assigned to the client instance variable.

        :param client_id: Unique identifier of a client. Used to retrieve an existing client by ID.
        :type client_id: int or None

        :param client_email: Unique email of a client. Used to retrieve an existing client by email.
        :type client_email: str or None
        """
        self.client_id = client_id
        self.client_email = client_email
        self.client = None

        if self.client_id is not None:
            self.client = self._find_by_id()

        if self.client_email is not None:
            self.client = self._find_by_email()

    def delete(self):
        """
        Delete the current client instance from the database.
        """
        db.session.delete(self.client)
        db.session.commit()

    def update(self, update_data):
        """
        Update the current client instance based on the provided update data.

        :param update_data: Dictionary containing new values for the client's attributes.
        :type update_data: dict[str, any]

        :return: Returns True if the update was successful, False otherwise.
        :rtype: bool
        """
        if not self._validate_update_data(update_data):
            return False

        if update_data.get("new_email") is not None:
            self.client.email = update_data.get("new_email")

        if update_data.get("new_phone") is not None:
            self.client.phone = update_data.get("new_phone")

        if update_data.get("new_address") is not None:
            self.client.address = update_data.get("new_address")

        if update_data.get("new_passport_number") is not None:
            self.client.passport_number = update_data.get("new_passport_number")

        db.session.commit()
        return True

    def get_client(self):
        """
        Retrieve the current client instance.

        :return: Returns the current client instance or None if it doesn't exist.
        :rtype: Client or None
        """
        return None if self.client is None else self.client

    def get_client_all_data(self):
        """
        Retrieve all data of the current client instance.

        :return: Returns a dictionary containing all data of the current client instance. Contains following keys:
                    - id (int): The client's ID.
                    - name (str): The client's name.
                    - surname (str): The client's surname.
                    - email (str): The client's email.
                    - phone (str): The client's phone.
                    - passport_number (str): The client's passport_number.
                    - address (str): The client's address.
                    - birth_date (datetime.date): The client's birthdate.
                    - registration_date (datetime.date): The client's registration date.
        :rtype: dict[str, any]
        """
        return {"id": self.client.id, "name": self.client.name, "surname": self.client.surname,
                "email": self.client.email, "phone": self.client.phone,
                "passport_number": self.client.passport_number, "address": self.client.address,
                "birth_date": self.client.birth_date, "registration_date": self.client.registration_date}

    def _find_by_id(self):
        """
        Retrieve a client by his ID.

        :return: Returns the Client instance with the provided ID, or None if he doesn't exist.
        :rtype: Client or None
        """
        return Client.query.filter_by(id=self.client_id).first() if self.client_id else None

    def _find_by_email(self):
        """
        Retrieve a client by his email.

        :return: Returns the Client instance with the provided email, or None if his doesn't exist.
        :rtype: Client or None
        """
        return Client.query.filter_by(email=self.client_email).first() if self.client_email else None

    @staticmethod
    def _validate_update_data(client_data):
        """
        Validate the data provided for updating a client.

        :param client_data: Dictionary containing new values for the client's attributes.
        :type client_data: dict[str, any]

        :return: Returns True if the provided data is valid, False otherwise.
        :rtype: bool
        """
        return Client.validate_email(client_data.get("new_email")) or \
            Client.validate_phone(client_data.get("new_phone")) or \
            Client.validate_passport_number(client_data.get("new_passport_number")) or \
            Client.validate_address(client_data.get("new_address"))
