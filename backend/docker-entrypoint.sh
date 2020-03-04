#!/usr/bin/env sh

set -e

python /usr/src/app/dbbackup.py "$@" >> /backup/logs/dbbackup.log

exec "$@"