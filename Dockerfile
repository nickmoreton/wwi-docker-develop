FROM python:3.8
# I'm  not a docker expert, most of this is just a copy/paste from other peoples work :)

ARG POETRY_HOME=/opt/poetry
ARG POETRY_INSTALL_ARGS=""
ARG POETRY_VERSION=1.1.15
ARG POETRY_INSTALLER_SHA=eedf0fe5a31e5bb899efa581cbe4df59af02ea5f
ENV VIRTUAL_ENV=/venv

# RUN useradd cms --create-home && mkdir /app $VIRTUAL_ENV && chown -R cms /app $VIRTUAL_ENV

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

# USER cms

RUN python -m venv $VIRTUAL_ENV
COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip && poetry install ${POETRY_INSTALL_ARGS} --no-root

COPY . .
COPY ./docker/wagtail-init.sh ./wagtail-init.sh
RUN pip install -e ./wagtail-wordpress-import["testing"]
# RUN mkdir -p ./wagtail-wordpress-import/test-media && chown -R cms ./wagtail-wordpress-import/test-media
# RUN mkdir -p ./log && chown -R cms ./log


COPY ./docker/bashrc.sh /home/cms/.bashrc
RUN poetry install ${POETRY_INSTALL_ARGS}
