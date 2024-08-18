from ...repositories import RentalsRepository, RentalRepository, ClientRepository, EmployeeRepository


class RentalsSortService:
    """
    The RentalsSortService class provides a method to sort rental data.

    This class acts as a service for sorting data related to rentals. It uses RentalsRepository to retrieve and sort
    rentals and other repositories to retrieve related data for each rental.
    """

    def __init__(self, sort_data):
        """
        Initialize a new instance of the RentalsSortService class.

        :param sort_data: The data specifying how rentals should be sorted. This could include parameters like
                          date_start, date_end, base_price, etc., along with the sort direction ('asc' or 'desc').
        :type sort_data: dict[str, any]
        """
        self.sort_data = sort_data
        self.rentals_repository = RentalsRepository()

    def sort_rentals(self):
        """
        Sort rental data based on the provided parameters.

        This method uses the RentalsRepository to sort all rentals based on the sorting data. Then, it enriches the
        rental data with additional information about the client and employee associated with each rental.

        :return: The sorted and enriched rental data or False if the sort data wasn't valid. Each item in the list
                 includes data about the rental, the client and the employee.
        :rtype: list[dict[str, any]] or False
        """
        rentals_sorted = self.rentals_repository.sort_all(self.sort_data)
        if rentals_sorted is None:
            return False

        rentals_data = []
        for rental in rentals_sorted:
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
