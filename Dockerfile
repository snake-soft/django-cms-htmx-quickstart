FROM python:3.11
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./.bash_history /root/.bash_history
COPY . /app

ARG HASH
RUN echo "${HASH}" > HASH
ARG VERSION=0.0.0
RUN echo "${VERSION}" > VERSION

RUN groupadd -g 1000 -r django && useradd -u 1000 -d /app -g django -r django
RUN chown -R django:django /app
USER django
