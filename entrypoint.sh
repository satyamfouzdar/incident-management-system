#!/bin/bash

# Wait for MySQL container to be up and ready
echo "Waiting for MySQL to start..."
until nc -z db 3306; do
  sleep 1
done
echo "MySQL started."

# Apply database migrations
python3 manage.py migrate

# Start the Django development server
python3 manage.py runserver 0.0.0.0:8000