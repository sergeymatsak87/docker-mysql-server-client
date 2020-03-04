#!/bin/sh

set -e

host="$1"
shift
cmd="$@"

until mysql --user=$MYSQL_USER --password=$MYSQL_PASSWORD -h "$host" --execute "SHOW CREATE TABLE db.ticks" > /dev/null 2>&1; do
  echo "MYSQL table ticks - in progress to be created"
  sleep 1
done

  echo "MYSQL table ticks created - executing command"
exec $cmd
