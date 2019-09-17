#!/bin/bash

#Create necessary tables and migrate database
python /code/manage.py migrate --noinput

#Run test to assure everything is OK
python /code/manage.py test

#Collect static files in order to serve statics with nginx
python /code/manage.py collectstatic --noinput

#Create a superuser in order to access Django admin IHM
#python /code/manage.py superuser --username admin --password changeme --noinput --email 'admin@email.com'

#start the server
python /code/manage.py runserver 0.0.0.0:8000
