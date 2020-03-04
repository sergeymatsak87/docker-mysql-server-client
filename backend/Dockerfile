FROM python:3.8.1-alpine3.11

RUN apk add --update --no-cache mysql-client

RUN mkdir -p /backup/logs

WORKDIR /backup

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY . /usr/src/app

RUN chmod +x /usr/src/app/docker-entrypoint.sh \
    && ln -s /usr/src/app/docker-entrypoint.sh /docker-entrypoint.sh \
    && ln -s /usr/src/app/wait-for-mysql.sh /wait-for-mysql.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
