FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code
RUN mkdir -p /sock
RUN mkdir -p /logs
WORKDIR /code

RUN apt-get -y update
RUN apt -y install \
    libpangocairo-1.0-0 libpq-dev \
	libproj-dev libc-dev binutils \
	gettext make cmake gcc g++ \
	python3-dev libgdal-dev \
	&& rm -rf /var/lib/apt/lists/* \
	&& apt autoremove \
	&& apt autoclean

COPY requirements.txt /code/
RUN pip install --no-cache-dir setuptools==74.1.0
RUN pip install --no-cache-dir -r requirements.txt
RUN rm /code/requirements.txt
