#!/bin/bash

export FLASK_APP=main.py
rm nohup.last.out
mv nohup.out nohup.last.out
nohup python3 -m flask run --port 5000 --host 0.0.0.0 &
echo "sprint_reporter_app server started in background"
