FROM python:3.8-slim
WORKDIR /app

SHELL ["/bin/bash", "-c"]
RUN apt-get update && apt-get install -y --no-install-recommends curl vim \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
COPY ["pyproject.toml", "poetry.lock", "/app/"]
RUN $HOME/.poetry/bin/poetry config virtualenvs.in-project true \
    && $HOME/.poetry/bin/poetry install
RUN echo 'export PATH="$HOME/.poetry/bin:$PATH"' >> ~/.bashrc \
    && echo 'alias py="poetry run python"' >> ~/.bashrc
CMD [ "sh", "-c", "sleep infinity" ]