#!/bin/sh
python3 -m venv $PWD\venv
pip3 install -r requirements.txt
python3 setup.py
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser