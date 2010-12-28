#!/bin/sh

echo Resetting data for app 'Photos'

python manage.py sqlclear photos | python manage.py dbshell
python manage.py syncdb

