FROM python:3.9.4-slim

ARG APP_HOST_ARG
ARG APP_PORT_ARG

ENV APP_HOST ${APP_HOST_ARG}
ENV APP_PORT ${APP_PORT_ARG}

COPY app /src/app
COPY Pipfile /src

WORKDIR /src

RUN pip install --upgrade pip

RUN pip install pipenv

RUN pipenv lock -r > requirements.txt

RUN pip install -r requirements.txt

CMD uvicorn app.api.app:app --host ${APP_HOST} --port ${APP_PORT}