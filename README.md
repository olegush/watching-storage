# Watching storage

This site is a simple watching service.  It could help to watch for users activity in a bank storage, for example. Main page displays all users have access passcards, also there are list of active users right now and pages with every user's history visits. Based on [Django](https://djangoproject.com/) with PostgreSQL.


# How to Install

Python 3.6 and libraries from **requirements.txt** should be installed. Use virtual environment tool, for example **virtualenv**.

```bash

virtualenv virtualenv_folder_name
source virtualenv_folder_name/bin/activate
python3.6 -m pip install -r requirements.txt
```

Put vulnerable parameters to **.env** file.

```bash
DB_ENGINE=db_engine
DB_HOST=db_host
DB_PORT=db_port
DB_NAME=db_name
DB_USER=db_user
DB_PASSWORD=db_password
SECRET_KEY=secret_key
```


# Quickstart

1. Run **server.py**.

```bash

$ python3 manage.py runserver 0.0.0.0:8000

Performing system checks...

System check identified no issues (0 silenced).
June 26, 2019 - 13:44:48
Django version 1.11.21, using settings 'project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
[26/Jun/2019 13:44:52] "GET / HTTP/1.1" 200 43454

```

2. Goto [http://127.0.0.1:8000/ ](http://127.0.0.1:8000/ )


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
