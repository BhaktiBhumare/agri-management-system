#!/usr/bin/env bash

pip install -r requirements.txt

cd agri_system

python manage.py migrate
python manage.py collectstatic --noinput
