from test_base_config import unittest, TestBaseConfig


class TestAuthAPI(TestBaseConfig):
    """
    TestAuthAPI class tests the authentication module of the application.

    This class inherits from TestBaseConfig and tests login, current_user, refresh, and logout functionalities.
    """

    def test_login(self):
        """
        Test the login functionality.

        This method sends a post request with test user's login data to the '/auth/login' endpoint.
        Then, it asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

    def test_current_user(self):
        """
        Test the current_user functionality.

        This method first logs in the test user, then it sends a get request to the '/auth/current-employee' endpoint.
        It asserts that the response status code is 200 and the returned user email matches the test user's email.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        access_token = login_response.json["access_token"]
        current_user_response = self.client.get(
            "/auth/current-employee",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        self.assertEqual(current_user_response.status_code, 200)
        self.assertEqual(current_user_response.json["email"], "tester@test.com")

    def test_refresh(self):
        """
        Test the refresh functionality.

        This method first logs in the test user, then it sends a get request to the '/auth/refresh' endpoint.
        It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        refresh_token = login_response.json["refresh_token"]
        refresh_response = self.client.get(
            "/auth/refresh",
            headers={"Cookie": refresh_token}
        )
        self.assertEqual(refresh_response.status_code, 200)

    def test_logout(self):
        """
        Test the logout functionality.

        This method first logs in the test user, then it sends a get request to the '/auth/logout' endpoint.
        Then, it tries to access a jwt-required resource and asserts that the response status code is 401
        and the response message is 'Missing Authorization Header'.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        access_token = login_response.json["access_token"]
        logout_response = self.client.get(
            "/auth/logout",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        self.assertEqual(logout_response.status_code, 200)

        jwt_required_resource_response = self.client.get(
            "/clients/"
        )
        self.assertEqual(jwt_required_resource_response.status_code, 401)
        self.assertEqual(jwt_required_resource_response.json["msg"], "Missing Authorization Header")


if __name__ == "__main__":
    unittest.main()
