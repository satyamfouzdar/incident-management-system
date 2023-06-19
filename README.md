# INCIDENT MANAGER

To install the project with docker.

1. Make sure you have docker installed on your machine
2. Exract the zip file
3. Change the directory to the project one
4. Run ```docker-compose up --build -d```
5. Wait for the build process to complete.
6. Browse to ```http://localhost:8000/``` (Have made a simple frontend to test all apis in a bit easier way.)


To install the project without docker.

1. Extract the zip file
2. Change the directory to the project one
3. Set up your mysql server and start the server
4. Create a database with user and add those credentials in the .env file
5. Then run ```apt-get update && apt-get install -y python3 netcat tzdata python3-pip python3-dev build-essential libmysqlclient-dev && rm -rf /var/lib/apt/lists/*```
6. ```python3 -m venv .venv```
7. ```pip install -r requirements.txt```
8. ```python3 manage.py migrate```
9. ```python3 manage.py runserver```