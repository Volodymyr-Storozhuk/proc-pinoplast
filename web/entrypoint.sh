#!/bin/sh

if [ "$POSTGRES_DATABASE" = "postgres" ]
then
    echo "Waiting for PostgreSQL..."

    while ! nc -z $POSTGRES_DB_HOST $POSTGRES_DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started."
fi

exec "$@"
