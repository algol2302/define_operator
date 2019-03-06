#!/bin/sh

while ! nc -z db 5432; do
    echo "Waiting for PostgreSql to start..."
    sleep 1
done

while ! nc -z redis 6379; do
    echo "Waiting for Redis to start..."
    sleep 1
done


echo "$1"

if [ "$1" = "celery_worker" ]; then
    echo "Run celery WORKER..."
    cd /opt
    celery worker -l INFO -A md -c 4
elif [ "$1" = "celery_beat" ]; then
    echo "Run celery BEAT..."
    cd /opt
    celery beat -l INFO -A md
elif [ "$1" = "server" ]; then
    echo "Migrate..."
    python ./manage.py migrate --noinput

    echo "Run server..."
    python ./server.py
else
    echo "Empty command :("
fi
