from test_base_config import unittest, TestBaseConfig


class TestEquipmentsAPI(TestBaseConfig):
    """
    TestEquipmentsAPI class tests the equipments module of the application.

    This class inherits from TestBaseConfig and tests create_equipment, get_equipments, get_equipment,
    update_equipment, delete_equipment, damaged_equipment and sorted_equipments functionalities.
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

    def test_get_equipments(self):
        """
        Test the get_equipments functionality.

        This method first logs in the test user, then it calls the test_create_equipment method to ensure there is
        equipment to get and sends a get request to the '/equipments/' endpoint.
        It asserts that the response status code is 200 and the returned number of equipments is 1.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_equipment()
        access_token = login_response.json["access_token"]
        get_equipments_response = self.client.get(
            "/equipments/",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(get_equipments_response.status_code, 200)
        self.assertEqual(len(get_equipments_response.json), 1)

    def test_get_equipment(self):
        """
        Test the get_equipment functionality.

        This method first logs in the test user, then it calls the test_create_equipment method to ensure there is
        equipment to get and sends a get request to the '/equipments/equipment/1' endpoint.
        It asserts that the response status code is 200 and the returned equipment's model matches
        the test equipment's model.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_equipment()
        access_token = login_response.json["access_token"]
        get_equipment_response = self.client.get(
            "/equipments/equipment/1",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(get_equipment_response.status_code, 200)
        self.assertEqual(get_equipment_response.json["model"], "Tester-equipment-Model")

    def test_update_equipment(self):
        """
        Test the update_equipment functionality.

        This method first logs in the test user, then it calls the test_create_equipment method to ensure there is
        equipment to update and sends a put request with the new data
        to the '/equipments/equipment/1' endpoint. It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_equipment()
        access_token = login_response.json["access_token"]
        update_equipment_response = self.client.put(
            "/equipments/equipment/1",
            json={
                "new_price_per_hour": 15,
                "new_description": "Tester-equipment-NewDescription"
            },
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(update_equipment_response.status_code, 200)

    def test_delete_equipment(self):
        """
        Test the delete_equipment functionality.

        This method first logs in the test user, then it calls the test_create_equipment method to ensure there is
        equipment to delete and sends a delete request to the '/equipments/equipment/1' endpoint.
        It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_equipment()
        access_token = login_response.json["access_token"]
        delete_equipment_response = self.client.delete(
            "/equipments/equipment/1",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(delete_equipment_response.status_code, 200)

    def test_damaged_equipment(self):
        """
        Test the damaged_equipment functionality.

        This method first logs in the test user, then it calls the test_create_equipment method to ensure there is
        an equipment to report as damaged and sends a get request to the '/equipments/equipment/1/damaged' endpoint.
        It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_equipment()

        access_token = login_response.json["access_token"]
        damaged_equipment_response = self.client.get(
            "/equipments/equipment/1/damaged",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(damaged_equipment_response.status_code, 200)

    def test_sorted_equipments(self):
        """
        Test the sorted_equipments functionality.

        This method first logs in the test user, then it calls the test_create_equipment method to ensure there is
        equipment to sort and sends a get request with sorting parameters
        to the '/equipments/sort' endpoint. It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_equipment()
        access_token = login_response.json["access_token"]
        sort_equipments_response = self.client.get(
            "/equipments/sort",
            headers={"Authorization": f"Bearer {access_token}"},
            query_string="price_per_hour=lowest"
        )
        self.assertEqual(sort_equipments_response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
