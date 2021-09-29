# AgileSprite-RESTful-API-Server

## Python Version
```
python 3.8.8
```

## Install Requirements

Using pip

```
pip install -r requirements.txt
```

## Generate Database (Fresh Start)

1. delete files under migrations folder, in each app, except '\_\_init\_\_.py'
2. perform following commands
```
python manage.py makemigrations
python manage.py migrate
```

## Run Server

```
python manage.py runserver
```
or with specific ip and port
```
python manage.py runserver ip:port
```