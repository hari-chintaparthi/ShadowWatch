#!/usr/bin/env bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input
