from ...repositories import RentalsRepository, RentalRepository, ClientRepository, EmployeeRepository, \
    EquipmentRepository


class RentalsService:
    """
    The RentalsService class provides methods for managing multiple rentals' data.

    This class acts as a service for creating new rentals and preparing data related to all rentals.

    :ivar create_data: The data for creating a new rental.
    :type create_data: dict[str, any] or None
    """

    def __init__(self, create_data=None):
        """
        Initialize a new instance of the RentalsService class.

        :param create_data: The data for creating a new rental, defaults to None.
        :type create_data: dict[str, any] or None
        """
        self.create_data = create_data
        self.rentals_repository = RentalsRepository(self.create_data)

    def create_rental(self):
        """
        Create a new rental.

        This method uses the rentals repository to create a new rental with the provided data. If the rental is
        successfully created, it also rents all the equipment specified in the creation data.

        :return: True if the rental and all associated equipment rentals were successfully created, False otherwise.
        :rtype: bool
        """
        if not self.rentals_repository.create():
            return False

        for equipment_inventory_number in self.create_data.get("equipments"):
            equipment_repository = EquipmentRepository(equipment_inventory_number)
            equipment_repository.rent(self.rentals_repository.get_rental_id())

        return True

    def prepare_response_with_rentals_data(self):
        """
        Prepare a response containing data about all rentals.

        This method uses the rentals repository to retrieve data about all rentals. For each rental, it also retrieves
        additional data about the associated client and employee, and includes this data in the response.

        :return: A list of data about all rentals, with each rental's data including additional data about the
                 associated client and employee.
        :rtype: list[dict[str, any]]
        """
        rentals = self.rentals_repository.get_all()
        rentals_data = []

        for rental in rentals:
            rental_repository = RentalRepository(rental.id)
            client_repository = ClientRepository(rental.client_id)
            employee_repository = EmployeeRepository(rental.employee_id)

            rental_data = rental_repository.get_rental_all_data()
            client_data = client_repository.get_client_all_data()
            employee_data = employee_repository.get_employee_all_data()

            rental_data["client_name"] = client_data.get("name")
            rental_data["client_surname"] = client_data.get("surname")
            rental_data["employee_name"] = employee_data.get("name")
            rental_data["employee_surname"] = employee_data.get("surname")

            rentals_data.append(rental_data)

        return rentals_data
