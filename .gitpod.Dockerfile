FROM gitpod/workspace-postgres

USER gitpod

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - && \
    echo "export PATH=$PATH:/home/gitpod/.poetry/bin" >> ~/.bashrc && \
    echo "unset PIP_USER" >> ~/.bashrc

