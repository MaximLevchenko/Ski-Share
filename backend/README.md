# Ski Equipment Share Application - Backend

## Project Overview

The backend for the Ski Equipment Share Application is designed to manage the rental and sales processes for ski equipment. It provides a RESTful API for handling clients, employees, equipment, rentals, sales, and reservations. The backend is built with Flask and includes robust authentication and authorization mechanisms.

## Features

- User authentication and authorization using JWT.
- Filtering, deleting, updating of employees, clients, and equipment.
- Sorting new equipment in the inventory.
- Viewing individual pieces of equipment.
- Viewing individual profiles of clients and employees.
- Management of rentals and returns of equipment.
- Reservation processing for ski equipment.
- Inventory management including categorization, storage, and tracking of equipment.

## Technologies

- **Python 3.10**
- **Flask**: Web framework for creating RESTful APIs.
- **SQLite3**: Database engine for managing persistent data.
- **SQLAlchemy**: ORM for database interactions.
- **Flask-JWT-Extended**: For JWT-based authentication.
- **Flask-CORS**: To handle Cross-Origin Resource Sharing (CORS).
- **Unittest**: For unit and integration testing.

## Directory Structure

```plaintext
backend/
│
├── src/
│   ├── app/
│   │   ├── controllers/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── main.py
│   │
│   ├── configurations/
│   ├── databases/
│   ├── migrations/
│
├── tests/
│   ├── test_auth_api.py
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
## Key Commands

    Run the application:

    ```bash
    python3 run.py
    ```

    Runs the application on port 5000.

    Run tests:

    ```bash
    python3 test_api.py
    ```

    Runs the unit and integration tests.

    Access API Documentation:

    The Swagger documentation for the API is available at:

    ```plaintext
    http://127.0.0.1:5000/docs
    ```

## Running with Docker

    Build the Docker image:

    ```bash
    docker build -t ski-share-backend .
    ```

    Run the Docker container:

    ```bash
    docker run -d -p 5000:5000 --name ski-share-backend ski-share-backend
    ```

## API Documentation

The API documentation is available through Swagger UI at `http://127.0.0.1:5000/docs`.
