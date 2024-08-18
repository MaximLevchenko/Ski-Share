from test_base_config import unittest, TestBaseConfig


class TestEmployeesAPI(TestBaseConfig):
    """
    TestEmployeesAPI class tests the employees module of the application.

    This class inherits from TestBaseConfig and tests create_employee, get_employees, get_employee,
    update_employee, delete_employee and sort_employees functionalities.
    """

    def test_create_employee(self):
        """
        Test the create_employee functionality.

        This method first logs in the test user, then it sends a post request with the new employee's data
        to the '/employees/' endpoint. It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        access_token = login_response.json["access_token"]
        create_employee_response = self.client.post(
            "/employees/",
            json={
                "name": "Tester2-Name",
                "surname": "Tester2-Surname",
                "email": "tester2@test.com",
                "password": "test2",
                "phone": "+111111111111",
                "salary": 4567,
                "position": "Assistant"
            },
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(create_employee_response.status_code, 200)

    def test_get_employees(self):
        """
        Test the get_employees functionality.

        This method first logs in the test user, then it sends a get request to the '/employees/' endpoint.
        It asserts that the response status code is 200 and the returned number of employees is 1.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        access_token = login_response.json["access_token"]
        get_employees_response = self.client.get(
            "/employees/",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(get_employees_response.status_code, 200)
        self.assertEqual(len(get_employees_response.json), 1)

    def test_get_employee(self):
        """
        Test the get_employee functionality.

        This method first logs in the test user, then it sends a get request to the '/employees/employee/1' endpoint.
        It asserts that the response status code is 200 and the returned employee's email matches the test user's email.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        access_token = login_response.json["access_token"]
        get_employee_response = self.client.get(
            "/employees/employee/1",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(get_employee_response.status_code, 200)
        self.assertEqual(get_employee_response.json["email"], "tester@test.com")

    def test_update_employee(self):
        """
        Test the update_employee functionality.

        This method first logs in the test user, then it sends a put request with the new data
        to the '/employees/employee/1' endpoint. It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        access_token = login_response.json["access_token"]
        update_employee_response = self.client.put(
            "/employees/employee/1",
            json={
                "new_phone": "+555555555555",
                "new_salary": 9876,
                "new_position": "Assistant"
            },
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(update_employee_response.status_code, 200)

    def test_delete_employee(self):
        """
        Test the delete_employee functionality.

        This method first logs in the test user, then it sends a delete request to the '/employees/employee/1' endpoint.
        It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"},
        )
        self.assertEqual(login_response.status_code, 200)

        access_token = login_response.json["access_token"]
        delete_employee_response = self.client.delete(
            "/employees/employee/1",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(delete_employee_response.status_code, 200)

    def test_sort_employees(self):
        """
        Test the sort_employees functionality.

        This method first logs in the test user, then it sends a get request with sorting parameters
        to the '/employees/sort' endpoint. It asserts that the response status code is 200.
        """
        login_response = self.client.post(
            "/auth/login",
            json={"email": "tester@test.com", "password": "test"}
        )
        self.assertEqual(login_response.status_code, 200)

        access_token = login_response.json["access_token"]
        sort_employees_response = self.client.get(
            "/employees/sort",
            headers={"Authorization": f"Bearer {access_token}"},
            query_string="name=abc&surname=zyx"
        )
        self.assertEqual(sort_employees_response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
