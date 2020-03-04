FROM python:3.8.1-alpine3.11

WORKDIR /var/www

COPY . /usr/src/app

RUN chmod +x /usr/src/app/docker-entrypoint.sh \
    && ln -s /usr/src/app/docker-entrypoint.sh /docker-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]