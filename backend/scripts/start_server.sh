#!/bin/bash

set -e

APP_DIR=/home/ubuntu/app
VENV_DIR=/home/ubuntu/venv

cd $APP_DIR

echo "Stopping old server if running..."
pkill -f uvicorn || true

echo "Creating virtual environment if missing..."
if [ ! -d "$VENV_DIR" ]; then
  python3 -m venv $VENV_DIR
fi

echo "Activating virtual environment..."
source $VENV_DIR/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing requirements..."
pip install -r requirements.txt

echo "Starting FastAPI server..."
nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 > server.log 2>&1 &

echo "Deployment completed and server started."
