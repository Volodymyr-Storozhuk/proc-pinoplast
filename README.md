# Eurobud technological resource
Web viewer for technological processes for the production of foam plastic.

## How to first run
1. $ docker compose build
2. $ docker compose up -d
3. $ docker compose exec web python manage.py migrate --noinput
4. $ docker compose exec web python manage.py collectstatic --no-input --clear
5. $ docker compose exec web python manage.py createsuperuser



