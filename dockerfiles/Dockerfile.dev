FROM python:3.8-slim
WORKDIR /app
SHELL ["/bin/bash", "-c"]
ENV HOME='/root'
ENV PATH="${HOME}/.poetry/bin:${PATH}"

RUN apt-get update && apt-get install -y --no-install-recommends curl vim \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
COPY ["pyproject.toml", "poetry.lock", "/app/"]
RUN $HOME/.poetry/bin/poetry install

RUN echo 'alias py="poetry run python"' >> ~/.bashrc

CMD [ "sh", "-c", "sleep infinity" ]