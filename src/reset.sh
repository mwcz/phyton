#!/bin/bash

echo Resetting database for app 'Photos'

python manage.py sqlclear photos | python manage.py dbshell
python manage.py sqlclear posts | python manage.py dbshell
python manage.py syncdb

read -p "Delete all non-hidden files/dirs in the media/photos/ directory (rm -rfv ../media/photos/*)?  (yes/n)" proceed

if [ $proceed == yes ];
then
    rm -rfv ../media/photos/*
else
    echo "media/photos/ preserved"
fi

echo "Reset complete."
