from test_base_config import unittest, TestBaseConfig


class TestRentalsAPI(TestBaseConfig):
    """
    TestRentalsAPI class tests the rentals module of the application.

    This class inherits from TestBaseConfig and tests create_rental, get_rentals, get_rental,
    delete_rental, close_rental, update_description_rental, and sort_rentals functionalities.
    """

    def test_create_equipment(self):
        """
        Test the create_equipment functionality.

        This method first logs in the test user, then it sends a post request with the new equipment's data
        to the '/equipments/' endpoint. It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        access_token = login_response.json["access_token"]
        create_equipment_response = self.client.post(
            "/equipments/",
            json={
                "category": "Ski boots",
                "manufacturer": "Tester-equipment-Manufacturer",
                "model": "Tester-equipment-Model",
                "size": "L",
                "price_per_hour": 10,
                "description": "Tester-equipment-Description"
            },
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(create_equipment_response.status_code, 200)

    def test_create_client(self):
        """
        Test the create_client functionality.

        This method first logs in the test user, then it sends a post request with the new client's data
        to the '/clients/' endpoint. It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        access_token = login_response.json["access_token"]
        create_client_response = self.client.post(
            "/clients/",
            json={
                "name": "Tester-client-Name",
                "surname": "Tester-client-Surname",
                "email": "testerclient@test.com",
                "phone": "+888111111111",
                "passport_number": "1234567890",
                "address": "Tester-client-Address",
                "birth_date": "2000-01-01"
            },
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(create_client_response.status_code, 200)

    def test_create_rental(self):
        """
        Test the create_rental functionality.

        This method first logs in the test user, creates a test equipment and a test client,
        then it sends a post request with the new rental's data
        to the '/rentals/' endpoint. It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_equipment()
        self.test_create_client()
        access_token = login_response.json["access_token"]
        create_rental_response = self.client.post(
            "/rentals/",
            json={
                "date_end": "2023-09-03T17:00:00.000Z",
                "payment_type": "Card",
                "base_price": 150,

                "employee_id": 1,
                "client_id": 1,
                "equipments": [1]
            },
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(create_rental_response.status_code, 200)

    def test_get_rentals(self):
        """
        Test the get_rentals functionality.

        This method first logs in the test user, then it calls the test_create_rental method to ensure there is
        a rental to get and sends a get request to the '/rentals/' endpoint.
        It asserts that the response status code is 200 and the returned number of rentals is 1.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_rental()
        access_token = login_response.json["access_token"]
        get_rentals_response = self.client.get(
            "/rentals/",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(get_rentals_response.status_code, 200)
        self.assertEqual(len(get_rentals_response.json), 1)

    def test_get_rental(self):
        """
        Test the get_rental functionality.

        This method first logs in the test user, then it calls the test_create_rental method to ensure there is
        a rental to get and sends a get request to the '/rentals/rental/1' endpoint.
        It asserts that the response status code is 200 and the returned rental's id matches the test rental's id.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_rental()
        access_token = login_response.json["access_token"]
        get_rental_response = self.client.get(
            "/rentals/rental/1",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(get_rental_response.status_code, 200)
        self.assertEqual(get_rental_response.json["id"], 1)

    def test_delete_rental(self):
        """
        Test the delete_rental functionality.

        This method first logs in the test user, then it calls the test_create_rental method to ensure there is
        a rental to delete and sends a delete request to the '/rentals/rental/1' endpoint.
        It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_rental()
        access_token = login_response.json["access_token"]
        delete_rental_response = self.client.delete(
            "/rentals/rental/1",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(delete_rental_response.status_code, 200)

    def test_close_rental(self):
        """
        Test the close_rental functionality.

        This method first logs in the test user, then it calls the test_create_rental method to ensure there is
        a rental to close and sends a put request with the new data
        to the '/rentals/rental/1/close' endpoint. It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_rental()
        access_token = login_response.json["access_token"]
        close_rental_response = self.client.put(
            "/rentals/rental/1/close",
            json={
                "new_damage_fee": 0,
                "new_late_return_fee": 40
            },
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(close_rental_response.status_code, 200)

    def test_update_description_rental(self):
        """
        Test the update_description_rental functionality.

        This method first logs in the test user, then it calls the test_create_rental method to ensure there is
        a rental to update and sends a put request with the new data
        to the '/rentals/rental/1/description' endpoint. It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_rental()
        access_token = login_response.json["access_token"]
        update_description_rental_response = self.client.put(
            "/rentals/rental/1/description",
            json={
                "new_description": "New description"
            },
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(update_description_rental_response.status_code, 200)

    def test_sort_rentals(self):
        """
        Test the sort_rentals functionality.

        This method first logs in the test user, then it calls the test_create_rental method to ensure there is
        a rental to sort and sends a get request with sorting parameters
        to the '/rentals/sort' endpoint. It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_rental()
        access_token = login_response.json["access_token"]
        sort_rentals_response = self.client.get(
            "/rentals/sort",
            headers={"Authorization": f"Bearer {access_token}"},
            query_string="date_end=latest"
        )
        self.assertEqual(sort_rentals_response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
