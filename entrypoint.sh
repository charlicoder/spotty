#!/bin/bash

python manage.py migrate --no-input
# python manage.py collectstatic --noinput

#python manage.py runserver 0.0.0.0:8000
uvicorn core.asgi:application --host 0.0.0.0 --port 8000
