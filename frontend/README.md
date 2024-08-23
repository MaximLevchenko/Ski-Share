# Ski Equipment Share Application - Frontend

## Project Overview

The frontend of the Ski Equipment Share Application provides an intuitive user interface for managing ski equipment rentals, reservations, and sales. The frontend interacts with the backend API to perform CRUD operations on clients, employees, equipment, and other entities.

## Features

- User-friendly interface for managing ski equipment inventory.
- Authentication and authorization for accessing different features.
- Filtering, sorting, and viewing of clients, employees, and equipment.
- Responsive design to support various devices.

## Technologies

- **React**: Frontend library for building user interfaces.
- **Redux**: State management for React applications.
- **React Router**: For navigation between views.
- **Axios**: For making HTTP requests to the backend API.
- **Bootstrap**: For responsive design and styling.

## Directory Structure

```plaintext
frontend/
│
├── public/
│   ├── index.html
│   ├── favicon.ico
│
├── src/
│   ├── components/
│   ├── pages/
│   ├── redux/
│   ├── services/
│   ├── App.js
│   ├── index.js
│   ├── config.js
│
├── .env
├── .gitignore
├── Dockerfile
├── package.json
├── README.md
```
## Key Commands

Run the application:

```bash
npm start
```

Runs the frontend application on port 3000.

Build the production version:

```bash
npm run build
```

Creates an optimized production build of the application.

Access the application:

The frontend will be available at:

```plaintext
http://localhost:3000
```

## Running with Docker

Build the Docker image:

```bash
docker build -t ski-share-frontend .
```

Run the Docker container:

```bash
docker run -d -p 3000:3000 --name ski-share-frontend ski-share-frontend
```