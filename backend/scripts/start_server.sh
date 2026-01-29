#!/bin/bash

cd /home/ubuntu/app

# stop old server if running
pkill -f uvicorn || true

# activate venv if exists
if [ -d "/home/ubuntu/venv" ]; then
  source /home/ubuntu/venv/bin/activate
fi

# start FastAPI server
nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 > server.log 2>&1 &
