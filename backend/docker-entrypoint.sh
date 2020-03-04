#!/usr/bin/env sh

set -e

export PYTHONUNBUFFERED=1

python /usr/src/app/dbbackup.py "$@"

exec "$@"