FROM python:3.9.6-slim-buster

ENV IS_INSIDE_DOCKER=1

# Install poetry
RUN pip install --no-cache-dir poetry

# Install requirements
RUN mkdir /script
WORKDIR /script
COPY ./pyproject.toml /script/pyproject.toml
COPY ./poetry.lock /script/poetry.lock
RUN poetry export --output requirements.txt
RUN pip install -r requirements.txt
# Cant use poetry when using pycharm+docker ?
# RUN poetry install

# Copy work scripts
COPY ./main.py /script/main.py

# Run work script
#CMD [ "poetry", "run", "python", "/script/main.py" ]
# Launch container but don't shut down
CMD [ "sleep", "infinity" ]

