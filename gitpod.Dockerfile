FROM gitpod/workspace-postgres

RUN pip install poetry
RUN poetry config virtualenvs.create false