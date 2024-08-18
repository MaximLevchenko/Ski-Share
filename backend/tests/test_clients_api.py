from test_base_config import unittest, TestBaseConfig


class TestClientsAPI(TestBaseConfig):
    """
    TestClientsAPI class tests the clients module of the application.

    This class inherits from TestBaseConfig and tests create_client, get_clients, get_client,
    update_client, delete_client and sort_clients functionalities.
    """

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

    def test_get_clients(self):
        """
        Test the get_clients functionality.

        This method first logs in the test user, then it calls the test_create_client method to ensure there is
        a client to get and sends a get request to the '/clients/' endpoint.
        It asserts that the response status code is 200 and the returned number of clients is 1.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_client()
        access_token = login_response.json["access_token"]
        get_clients_response = self.client.get(
            "/clients/",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(get_clients_response.status_code, 200)
        self.assertEqual(len(get_clients_response.json), 1)

    def test_get_client(self):
        """
        Test the get_client functionality.

        This method first logs in the test user, then it calls the test_create_client method to ensure there is
        a client to get and sends a get request to the '/clients/client/1' endpoint.
        It asserts that the response status code is 200 and the returned client's email matches the test client's email.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_client()
        access_token = login_response.json["access_token"]
        get_client_response = self.client.get(
            "/clients/client/1",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(get_client_response.status_code, 200)
        self.assertEqual(get_client_response.json["email"], "testerclient@test.com")

    def test_update_client(self):
        """
        Test the update_client functionality.

        This method first logs in the test user, then it calls the test_create_client method to ensure there is
        a client to update and sends a put request with the new data
        to the '/clients/client/1' endpoint. It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_client()
        access_token = login_response.json["access_token"]
        update_client_response = self.client.put(
            "/clients/client/1",
            json={
                "new_email": "Tester-client@new.email",
                "new_phone": "+988111111111"
            },
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(update_client_response.status_code, 200)

    def test_delete_client(self):
        """
        Test the delete_client functionality.

        This method first logs in the test user, then it calls the test_create_client method to ensure there is
        a client to delete and sends a delete request to the '/clients/client/1' endpoint.
        It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_client()
        access_token = login_response.json["access_token"]
        delete_client_response = self.client.delete(
            "/clients/client/1",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(delete_client_response.status_code, 200)

    def test_sort_clients(self):
        """
        Test the sort_clients functionality.

        This method first logs in the test user, then it calls the test_create_client method to ensure there is
        a client to sort and sends a get request with sorting parameters
        to the '/clients/sort' endpoint. It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        self.test_create_client()
        access_token = login_response.json["access_token"]
        sort_clients_response = self.client.get(
            "/clients/sort",
            headers={"Authorization": f"Bearer {access_token}"},
            query_string="name=abc&surname=zyx"
        )
        self.assertEqual(sort_clients_response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
