FROM python:3.12.7-alpine

WORKDIR /opt/api

ENV PYTHON_PATH=/opt/api/src

COPY requirements.txt gunicorn.conf.py alembic.ini /opt/api/
COPY ./alembic /opt/api/alembic
COPY ./src /opt/api/src

RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "--config", "gunicorn.conf.py", "src.app:app"]
