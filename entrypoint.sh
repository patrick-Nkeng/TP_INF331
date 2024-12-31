#!/bin/bash/

    set -e

    source /env/bin/activate

    if [$1 == 'gunicorn']; then

        exec python manage.py makemigrations
        exec python manage.py migrate
        exec gunicorn repair_front.wsgi:application -b 0.0.0.0:8000
    else
        exec python manage.py makemigrations
        exec python manage.py migrate
        exec python manage.py runserver 0.0.0.0:8000

    fi