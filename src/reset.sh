#!/bin/sh

echo Resetting database for app 'Photos'

python manage.py sqlclear photos | python manage.py dbshell
python manage.py syncdb

echo Deleting uploaded photos

rm -rfi ../media/photos/*
