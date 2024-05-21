# Loyalty Score Calculator 

This project is designed to calculate and manage loyalty scores for customers based on their purchases, reviews, and engagement activities. The project uses Django and Docker for development and deployment.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

### Setting Up the Environment

1. **Copy the environment file**:
if you are in linux you can use make command to make things more easier 
```sh
make up
``` 
or 
```sh
cp -f .env.dev-sample .env.dev
docker-compose up
```

### Running the Application
To run the application, you can use the following commands:

## Makefile Commands

| Command                 | Description                                         |
|-------------------------|-----------------------------------------------------|
| `make up`               | Copies `.env.dev-sample` to `.env.dev` and starts the Docker containers |
| `make down`             | Brings down the Docker containers                   |
| `make django-shell`     | Accesses the Django shell within the Docker container |
| `make django-createsuperuser` | Creates a Django superuser                     |
| `make django-migrate`   | Runs Django migrations                              |
| `make django-fixtures`  | Populates the database with sample data             |
| `make django-test`      | Runs Django tests                                   |
| `make django-calculate` | Updates loyalty scores for all customers            |
