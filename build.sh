#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

cd agri_system

python manage.py migrate

python manage.py createsuperuser --noinput || true

python manage.py collectstatic --noinput
