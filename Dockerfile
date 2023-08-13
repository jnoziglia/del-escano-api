FROM python:alpine3.18

# set environment variables
ENV APP_CONFIG_FILE /usr/src/app/config/production.py
ENV FLASK_APP app.py

# install python dependencies
RUN apk update
RUN pip install --upgrade pip
RUN pip install --no-cache-dir pipenv

# Defining working directory and adding source code
WORKDIR /usr/src/app
COPY Pipfile ./
COPY Pipfile.lock ./
COPY bootstrap.sh ./
COPY app.py ./
COPY api ./api
COPY config ./config

RUN chmod +x ./bootstrap.sh

# Install API dependencies
RUN pipenv install --system --deploy

EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]