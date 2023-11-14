# FastApi Mysql template

Simple fastapi template using mysql db

- Classic fastapi project architecture

# Author

[Imowt](https://github.com/Imowt)

## Dependencies:

- **sqlmodel**: model and database ORM for fastapi based on sqlalchemy (https://sqlmodel.tiangolo.com/)
- **pymysql**: to connect the mysql database
- **pre-commit**: for code quality
- **pytest**: to run tests

## Docker

- The present Dockerfile is here to build the server image

### docker-compose

#### db

The mysql container database on localhost:3306 use user 'root' with password 'supersecret' to connect

#### adminer

Useful database manager exposed on (http://localhost:8080)

#### api

The project fastapi on (http://localhost:8000)

## Tests

A temporary db will be created when running the test (take a look at the tests/conftest.py and tests/db_management.py files)