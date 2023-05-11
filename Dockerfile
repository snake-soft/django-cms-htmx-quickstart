FROM python:3.9
RUN groupadd -g 1000 -r django 
RUN useradd -r -m -u 1000 -g django django
ENV PATH="/home/django/.local/bin:${PATH}"
USER django:django
WORKDIR /app
RUN mkdir /app/staticfiles_collected
RUN mkdir /app/media

COPY --chown=django:django ./requirements.txt .
RUN pip install -r requirements.txt

COPY --chown=django:django ./requirements.override.txt .
RUN pip install -r requirements.override.txt

COPY --chown=django:django ./.bash_history /home/django/.bash_history
COPY --chown=django:django . /app

ARG HASH
RUN echo "${HASH}" > HASH
ARG VERSION=0.0.0
RUN echo "${VERSION}" > VERSION
