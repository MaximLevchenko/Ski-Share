# Ski Equipment Share Application

## Project Overview

The Ski Equipment Share Application is designed to facilitate the rental and management of ski equipment, along with supporting sales and reservations. This system allows users to manage clients, employees, equipment, rentals, and sales through a well-organized and intuitive API. The application includes robust authentication and authorization mechanisms, ensuring that all interactions are secure.

## Analytical Documentation Overview

This project was initially developed as part of a course project focusing on the management of ski equipment rentals and sales. The analytical documentation outlines the processes, domain models, and functional requirements for the application.

### Key Processes
1. **Rental and Return of Equipment**: The system supports the complete process of renting and returning ski equipment, ensuring accurate tracking and management of equipment status.
2. **Reservation Processing**: Users can reserve ski equipment, and the system manages the availability and notification of reserved items.
3. **Inventory Management**: The system handles the categorization, storage, and tracking of ski equipment, including details such as manufacturer, model, and warranty information.

### Domain Model Overview

#### Ski Equipment Inventory Management

- **Category**: Represents categories of ski equipment (e.g., skis, snowboards).
- **Equipment**: Describes specific models and production years of equipment available for rental or sale.
- **LocationAtStock**: Specifies where the equipment is stored within the warehouse.
- **Manufacturer**: Identifies the manufacturer details for the equipment.
- **Size**: Information on the physical dimensions of the equipment.
- **Warranty**: Details the warranty information for the equipment.

#### Rentals and Reservations Management

- **Client**: Stores customer data required for rental or reservation.
- **Employee**: Information about store employees managing rentals and reservations.
- **Fine**: Handles penalties for client violations.
- **Item**: Specific instances of equipment available for rent or purchase.
- **Optional Service**: Details additional services such as equipment maintenance.
- **Payment**: Manages payments for rental services.
- **Rental**: Data related to rental agreements.
- **Reservation**: Data related to equipment reservations.

## Key Directories and Files

- **app/controllers/**: Manages the business logic for each module (auth, clients, employees, equipment, and rentals).
- **app/models/**: Defines the database models corresponding to the application's entities such as `Client`, `Employee`, `Equipment`, `Rental`, and `BlacklistToken`.
- **app/repositories/**: Handles data access logic, providing a layer between the database models and the controllers.
- **app/routes/**: Defines the API endpoints and connects them to the corresponding controllers.
- **app/services/**: Contains the core business logic, split into services corresponding to each entity.
- **configurations/**: Contains configuration files, including database and environment settings.
- **databases/**: Handles migrations and database connections.
- **tests/**: Includes unit and integration tests for the application, covering all key modules and functionalities.
- **run.py**: The entry point to run the application.
- **Dockerfile**: A script to create a Docker image for the application.

### Backend Technologies Stack

- **Python language**.
- **Flask framework**: Creating REST APIs with Flask and Flask-RestX.
- **SQLite3 DB engine**: Carrying out database migrations with Flask-Migrate.
- **SQLAlchemy tools**: Using Flask-SQLAlchemy ORM.
- **JWT manager**: Working with JWT tokens - JWT Authentication with Flask-JWT-Extended.
- **Werkzeug security**: For working with password hashing.
- **Unittest**: Testing Flask API with Unittest.

## Directory Structure

```plaintext
backend/
│
├── src/
│   ├── app/
│   │   ├── controllers/
│   │   │   ├── auth/
│   │   │   ├── clients/
│   │   │   ├── employees/
│   │   │   ├── equipments/
│   │   │   ├── rentals/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── main.py
│   │
│   ├── configurations/
│   ├── databases/
├──tests/
│   ├── test_auth_api.py
│   ├── test_base_config.py
│   ├── test_clients_api.py
│   ├── test_employees_api.py
│   ├── test_equipments_api.py
│   ├── test_rentals_api.py
│
├── .env
├── .gitignore
├── Dockerfile
├── Pipfile
├── Pipfile.lock
├── README.md
├── requirements.txt
├── run.py
```

### CI/CD with GitLab

This project uses GitLab CI for continuous integration and deployment. The GitLab CI pipeline is defined in the `.gitlab-ci.yml` file, which includes stages for building the Docker image, pushing it to a container registry, running SonarQube for code analysis, generating documentation, and executing tests.

#### Pipeline Stages

- **Build Docker Image**: Builds the Docker image for the backend.
- **Container Registry Push**: Pushes the Docker image to the GitLab Container Registry.
- **SonarQube**: Runs static code analysis using SonarQube.
- **Docs**: Generates project documentation.
- **Test**: Runs unit and integration tests.

### SonarQube

To view the static code analysis, visit the following link: [SonarQube Dashboard for "ski-share"](https://sonarqube.software.geant.org/dashboard?id=ski-share). 

Please log in using your CVUT account to access the detailed analysis results. If you do not own a CVUT account, the project will not be available for you.


### DevOps Responsibilities

I was responsible for setting up and maintaining the CI/CD pipelines, ensuring that the application was built, tested, and deployed efficiently. The pipelines were configured to automatically build and push Docker images, run tests, and generate documentation.


### Running the Backend

To run the backend, first activate the virtual environment by running the following command:

```bash
source .venv/bin/activate
```
Then, start the application with:
```bash
python3 run.py
```

