FROM python:3.8.1-alpine3.11

RUN apk add --update --no-cache mysql-client

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /usr/src/app/docker-entrypoint.sh \
    && ln -s /usr/src/app/docker-entrypoint.sh /docker-entrypoint.sh \
    && ln -s /usr/src/app/wait-for-mysql.sh /wait-for-mysql.sh

ENTRYPOINT ["/docker-entrypoint.sh"]