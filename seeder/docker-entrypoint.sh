#!/usr/bin/env sh

set -e

export PYTHONUNBUFFERED=0

python create_table.py \
     && python insert_data.py "$@"

exec "$@"