#!/usr/bin/env sh

set -e

python -m http.server 8000 "$@"

exec "$@"