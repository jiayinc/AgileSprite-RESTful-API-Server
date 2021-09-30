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

## Quick Start

### Base URL

```
http(s)://your_ip:your_port/
```

### Account
This app provides operations to manipulate an account.
#### Register
Users can create a new account
- Request Type: POST
- Request Address: /account/register/  
- Request Fields:
    - email: String
    - password: String
    - first_name: String
    - last_name: String
- Return Fields:
    - code: Integer
    - msg: String
- Sample Request:
```
{
    'email': 'test@qq.com',
    'password': '123',
    'first_name': 'test',
    'last_name': 'gg'
}
```
- Sample Return:
```
# Username exists
{
    "code": 0,
    "msg": "UNIQUE constraint failed: account_extendeduser.username"
}
```
```
# Successfully created 
{
    "code": 0,
    "msg": "create success"
}
```
#### Login
Users can sign in if they have registered before
- Request Type: POST
- Request Address: /account/login/  
- Request Fields:
    - email: String
    - password: String
- Return Fields:
    - code: Integer
    - msg: String
    - token: String, provided if sign in information is correct
- Sample Request:
```
{
    'email': 'test@qq.com',
    'password': '123',
}
```
- Sample Return:
```
# Wrong login information
{
    "code": 0,
    "msg": "wrong username/password"
}
```
```
# Successfully signed in 
{
    "code": 0,
    "msg": "login success",
    "token": "bb41305c3996ab47e4d729821b3c6232c003099d"
}
```
#### Logout
Users can sign out if they have signed in
- Request Type: POST
- Request Address: /account/logout/  
- Request Fields:
    - token: String
- Return Fields:
    - code: Integer
    - msg: String
- Sample Request:
```
{
    'token': 'de99673b5ca9832e5a4f616c8ec81f563f4e0d84',
}
```
- Sample Return:
```
# Successfully log out
{
    "code": 0,
    "msg": "log out performed, token was disabled"
}
```
#### Update Information (No critical information included)
Users can update their general information
- Request Type: POST
- Request Address: /account/update/  
- Request Fields:
    - token: String
    - dob: Date
    - first_name: String
    - last_name: String
- Return Fields:
    - code: Integer
    - msg: String
- Sample Request:
```
{
    'token': 'a8313daaf222e91d76dacd5ae4986b7f52b3c7d8',
    'first_name': '321',
    'last_name': '3333',
    'dob': '2011-01-02'
}
```
- Sample Return:
```
# Wrong date format provided 
{
    "code": 0,
    "msg": "['“2011-01-” value has an invalid format. It must be in YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format.']"
}
```
```
# Successfully updated 
{
    "code": 0,
    "msg": "updated"
}
```
#### Update Information (critical information)
Yet implemented

### Contact

To be updated soon