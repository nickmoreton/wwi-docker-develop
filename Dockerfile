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

RUN python -m venv $VIRTUAL_ENV
COPY pyproject.toml poetry.lock ./
# COPY --chown=wagtail pyproject.toml poetry.lock ./
RUN pip install --upgrade pip && poetry install ${POETRY_INSTALL_ARGS} --no-root

COPY . .
COPY ./docker/wagtail-init.sh /app/wagtail-init.sh
COPY ./docker/bashrc.sh /home/wagtail/.bashrc
RUN cd wagtail-wordpress-import && \
    pip install -e .["testing"]

# COPY --chown=wagtail . .
# COPY --chown=wagtail ./docker/wagtail-init.sh /app/wagtail-init.sh
# COPY --chown=wagtail ./docker/bashrc.sh /home/wagtail/.bashrc
# RUN cd wagtail-wordpress-import && \
#     mkdir -p test-media && \
#     chown -R wagtail test-media && \
#     pip install -e .["testing"]

# USER wagtail

RUN poetry install ${POETRY_INSTALL_ARGS}
