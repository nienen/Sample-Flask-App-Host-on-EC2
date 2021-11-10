#!/bin/bash
kill -9 $(lsof -t -i:80)
cd /home/ec2-user/sample-flask-app
pip3 install -r requirements.txt
pip3 install flask
gunicorn --workers=2 --threads=2 --bind 0.0.0.0:80 wsgi:app --daemon