FROM python:3.13-slim-bookworm

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY . /code/


CMD ["fastapi", "run", "main.py", "--port", "80"]