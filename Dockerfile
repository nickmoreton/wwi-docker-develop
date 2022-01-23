FROM python:3.9
# I'm  not a docker expert, most of this is just a copy/paste from other peoples work :)

ARG POETRY_HOME=/opt/poetry
ARG POETRY_INSTALL_ARGS=""
ARG POETRY_VERSION=1.1.8
ARG POETRY_INSTALLER_SHA=eedf0fe5a31e5bb899efa581cbe4df59af02ea5f
ENV VIRTUAL_ENV=/venv

RUN useradd wagtail --create-home && mkdir /app $VIRTUAL_ENV && chown -R wagtail /app $VIRTUAL_ENV

WORKDIR /app

EXPOSE 8000

ENV PATH=${POETRY_HOME}/bin:$VIRTUAL_ENV/bin:$PATH \
    POETRY_INSTALL_ARGS=${POETRY_INSTALL_ARGS} \
    PYTHONUNBUFFERED=1 \
    PORT=8000

RUN wget https://raw.githubusercontent.com/python-poetry/poetry/${POETRY_VERSION}/get-poetry.py && \
    echo "${POETRY_INSTALLER_SHA} get-poetry.py" | sha1sum -c - && \
    python get-poetry.py && \
    rm get-poetry.py && \
    chown -R root:root ${POETRY_HOME} && \
    chmod -R 0755 ${POETRY_HOME}

USER wagtail

RUN python -m venv $VIRTUAL_ENV
COPY --chown=wagtailkit_repo_name pyproject.toml poetry.lock ./
RUN pip install --upgrade pip && poetry install ${POETRY_INSTALL_ARGS} --no-root

COPY --chown=wagtail:wagtail . .
COPY --chown=wagtail:wagtail ./docker/wagtail-init.sh /app/wagtail-init.sh
COPY --chown=wagtail:wagtail ./docker/bashrc.sh /home/wagtail/.bashrc
RUN pip install -e wagtail-wordpress-import

RUN poetry install ${POETRY_INSTALL_ARGS}

# RUN mkdir -p /app/xml /app/media /app/static /app/log

# Install system packages required by Wagtail and Django.
# RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
#     build-essential \
#     libpq-dev \
#     libmariadbclient-dev \
#     libjpeg62-turbo-dev \
#     zlib1g-dev \
#     libwebp-dev \
#     curl \
#     wget \
#     && rm -rf /var/lib/apt/lists/*

# Install the application server.
# RUN pip install "gunicorn==20.0.4"

# Install the project requirements.
# COPY requirements.txt /
# RUN pip install -U pip setuptools wheel -r /requirements.txt



# Set this directory to be owned by the "wagtail" user. This Wagtail project
# uses SQLite, the folder needs to be owned by the user that
# will be writing to the database file.
# RUN mkdir -p /app/xml /app/media /app/static /app/log
# RUN chown -R wagtail:wagtail /app
# RUN chown wagtail:wagtail /app/xml
# Copy the source code of the project into the container.
# COPY --chown=wagtail:wagtail . .








# Collect static files.
# RUN python manage.py collectstatic --noinput --clear

# Runtime command that executes when "docker run" is called, it does the
# following:
#   1. Migrate the database.
#   2. Start the application server.
# WARNING:
#   Migrating database at the same time as starting the server IS NOT THE BEST
#   PRACTICE. The database should be migrated manually or using the release
#   phase facilities of your hosting platform. This is used only so the
#   Wagtail instance can be started with a simple "docker run" command.
# CMD set -xe; python manage.py migrate --noinput; gunicorn {{ project_name }}.wsgi:application