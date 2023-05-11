FROM python:3.9
RUN groupadd -g 1000 -r django 
RUN useradd -r -m -u 1000 -g django django
USER django:django
WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./requirements.override.txt .
RUN pip install -r requirements.override.txt

COPY ./.bash_history /home/django/.bash_history
COPY . /app

ENV PATH="/home/django/.local/bin:${PATH}"
ARG HASH
RUN echo "${HASH}" > HASH
ARG VERSION=0.0.0
RUN echo "${VERSION}" > VERSION
