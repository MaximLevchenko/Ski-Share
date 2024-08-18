import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from backend.src.app import create_app
from backend.src.configurations import TestConfig
from backend.src.databases import db
from backend.src.app.repositories import EmployeesRepository


class TestBaseConfig(unittest.TestCase):
    """
    TestBaseConfig class serves as the base class for testing different modules of the application.

    This class sets up and tears down the database before and after each test.
    It uses the configuration from the TestConfig class.

    This class also creates a test client, that can be used to send requests to the application
    in the testing environment.

    :ivar app: The Flask application created for testing.
    :ivar client: The test client used for sending requests to the application.

    :param unittest.TestCase: A base class provided by the unittest module to create new test cases.
    """

    def setUp(self):
        """
        Set up the testing environment.

        This method is called before each test. It creates a new Flask application for testing,
        initializes the database, and adds a test employee record.
        """
        self.app = create_app(TestConfig)
        self.client = self.app.test_client(self)

        with self.app.app_context():
            db.create_all()

            employee_create_data = {"name": "Tester-Name", "surname": "Tester-Surname",
                                    "email": "tester@test.com", "password": "test",
                                    "phone": "+777777777777", "salary": 12345,
                                    "position": "Manager"}
            employees_repository = EmployeesRepository(employee_create_data)
            employees_repository.create()

    def tearDown(self):
        """
        Tear down the testing environment.

        This method is called after each test. It removes the session and drops the database.
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
