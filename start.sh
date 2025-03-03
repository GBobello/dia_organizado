#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn dia_organizado.wsgi --bind 0.0.0.0:$PORT
