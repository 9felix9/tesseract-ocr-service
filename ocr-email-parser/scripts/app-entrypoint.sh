#!/usr/bin/env bash

set -euo pipefail

# TODO trap exit
# worker count 2n+1; where n is cpu cores

# change end of line sequence to LF if working on windows
gunicorn -w 1 -k uvicorn.workers.UvicornWorker api:app --bind 0.0.0.0:8000 --max-requests 10000