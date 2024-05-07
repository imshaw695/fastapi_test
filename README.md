# fastapi_test

This repository is a test project that demonstrates how to use FastAPI with a Flask structure.

## Description

The purpose of this project is to showcase the integration of FastAPI into an applications structure traditionally used for Flask apps.

## Features

- Integration of FastAPI with a traditional Flask structure
- Demonstrates best practices for structuring a FastAPI project
- Provides examples of how to handle routing, request validation, and response serialization

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository.
2. Install the required dependencies.
3. Run the application.

## Pydantic

- Pydantic works with FastAPI for data validation.
- For example, if we have a create_user API, we can create a UserCreate pydantic model, and then use it in this new API to validate the incoming JSON data before we attempt to create the user record.

## Challenges

- FastAPI does not include:
  - An equivalent to flask-migrate, just alembic
  - We need to add the db connection string to the alembic env.py
  - An equivalent to Flask-SQLAlchemy, so we need to do it manually.

## Alembic

- We need to get rid of our migrations folder and do a alembic init alembic, then create migration scripts with the commands written in this repos models.py
- The alembic env.py will need to have the sqlalchemy uri added to it as it is in this repos. Copy paste this env.py.
- models.py is different, as we don't have flask-sqlalchemy we need to create the db engine manually.

## init

- Many changes need to be done, as we do not have a lot of the flask libraries that did a lot of the manual work for us. Use this repos __init__.py and config.py as a reference to convert a flask init file.