FROM python:2.7-slim
LABEL maintainer="Mike <mike@iterativesearch.com>"

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -b 0.0.0.0:5000 --access-logfile - "iSearchWsApi.app:create_app()"
