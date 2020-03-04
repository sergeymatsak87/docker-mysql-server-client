#!/bin/sh

set -e

host="$1"
shift
cmd="$@"

until mysql --user=$MYSQL_USER --password=$MYSQL_PASSWORD -h "$host" --execute "SHOW DATABASES" > /dev/null 2>&1; do
  echo "MYSQL database is unavailable - checking availability of mysql:3306"
  sleep 1
done

  echo "MYSQL database is up - executing command"
exec $cmd
