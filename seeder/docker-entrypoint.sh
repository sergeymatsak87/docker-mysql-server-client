#!/usr/bin/env sh

set -e

python create_table.py \
     && python insert_data.py "$@"

exec "$@"