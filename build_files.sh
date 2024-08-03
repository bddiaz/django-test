#!/bin/bash
set -e

# Install dependencies
python3 -m pip install -r requirements.txt

# Run database migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput
