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

### Return Code
Check /common/code.py

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
    "code": 106,
    "msg": "UNIQUE constraint failed: account_extendeduser.username"
}
```
```
# Successfully created 
{
    "code": 105,
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
    "code": 101,
    "msg": "wrong username/password"
}
```
```
# Successfully signed in 
{
    "code": 100,
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
    "code": 115,
    "msg": "log out performed, token was disabled"
}
# wrong token
{
    "code": 120,
    "msg": "token error"
}
```
#### Update Information (critical information included)
Users can update their general information
- Request Type: POST
- Request Address: /account/update/  
- Request Fields:
    - token: String, mandatory
    - with one of more of following parameter(s)
      - dob: Date
      - first_name: String
      - last_name: String
      - password: String
      - email: String, must be unique or failure on updating
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
    "code": 111,
    "msg": "['“2011-01-” value has an invalid format. It must be in YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format.']"
}
```
```
# Successfully updated 
{
    "code": 110,
    "msg": "updated"
}
```

### Contact
Contact feature
#### Add a Contact
Users can add a contact
- Request Type: POST
- Request Address: /contact/add/  
- Request Fields:
    - token: String
    - email: String
    - birthday: Date
    - name: String
- Return Fields:
    - code: Integer
    - msg: String
- Sample Request:
```
{
    'token': '611088d71f3044dd640b9f9209e92d60786a0d5a',
    'name': 'gg',
    'email': 'asd@qq.com',
    'birthday': 2020-01-21
}
```
- Sample Return:
```
# Successfully added 
{
    "code": 200,
    "msg": "add success"
}
```

#### Get All Contacts
Users can get all of contacts
- Request Type: POST
- Request Address: /contact/get_all/  
- Request Fields:
    - token: String
- Return Fields:
    - code: Integer
    - msg: String
    - contacts: List of Contacts, where each contact contains
      - id: Integer, contact's ID
      - user_id: Integer
      - name: String
      - email: String
      - birthday: Date
      - company: String
      - phone: String
      - mobile: String
      - address: String
      - relationship: String
      - notes: String
      - image_address: String
- Sample Request:
```
{
    'token': '611088d71f3044dd640b9f9209e92d60786a0d5a',
}
```
- Sample Return:
```
{
    "code": 215,
    "msg": "get success",
    "contacts": [
        {
            "id": 2,
            "user_id": 1,
            "name": "abc",
            "company": "abc.co",
            "email": "abc@qq.com",
            "phone": "123456",
            "mobile": "654321",
            "address": "Adddddressssss",
            "birthday": "1999-08-01",
            "relationship": "None",
            "notes": "no",
            "image_address": "http://wwwwwwww.qqqqqqqaaaa.com"
        }
    ]
}
```
#### Get a Contact
Users can a specific contact
- Request Type: POST
- Request Address: /contact/get/  
- Request Fields:
    - token: String
    - contact_id: Integer
- Return Fields:
    - code: Integer
    - msg: String
    - contacts: List of Contacts, where each contact contains
      - id: Integer, contact's ID
      - user_id: Integer
      - name: String
      - email: String
      - birthday: Date
      - company: String
      - phone: String
      - mobile: String
      - address: String
      - relationship: String
      - notes: String
      - image_address: String
- Sample Request:
```
{
    'token': '611088d71f3044dd640b9f9209e92d60786a0d5a',
    'contact_id': 2,
}
```
- Sample Return:
```
{
    "code": 220,
    "msg": "get success",
    "contacts": [
        {
            "id": 2,
            "user_id": 1,
            "name": "abc",
            "company": "abc.co",
            "email": "abc@qq.com",
            "phone": "123456",
            "mobile": "654321",
            "address": "Adddddressssss",
            "birthday": "1999-08-01",
            "relationship": "None",
            "notes": "no",
            "image_address": "http://wwwwwwww.qqqqqqqaaaa.com"
        }
    ]
}
```

#### Delete a Contact
Users can delete a contact
- Request Type: POST
- Request Address: /contact/delete/  
- Request Fields:
    - token: String
    - contact_id: Integer
- Return Fields:
    - code: Integer
    - msg: String
- Sample Request:
```
{
    'token': 'de99673b5ca9832e5a4f616c8ec81f563f4e0d84',
    'contact_id': 2,
}
```
- Sample Return:
```
# Successfully deleted
{
    "code": 205,
    "msg": "delete success"
}
```
#### Update Contact Information
Users can update a contact information
- Request Type: POST
- Request Address: /contact/update/  
- Request Fields:
    - token: String, mandatory
    - contact_id: Integer, contact's ID, mandatory
    - with one of more of following parameter(s)
      - name: String
      - email: String
      - birthday: Date
      - company: String
      - phone: String
      - mobile: String
      - address: String
      - relationship: String
      - notes: String
      - image_address: String
- Return Fields:
    - code: Integer
    - msg: String
- Sample Request:
```
{
    'token': '3b6a7f2885ecbaec38261c2cdf7be0b1263029f7',
    'contact_id': 2,
    'name': 'abc',
    'company': 'abc.co',
    'email': 'abc@qq.com',
    'phone': '123456',
    'mobile': '654321',
    'address': 'Adddddressssss',
    'birthday': 1999-08-01,
    'relationship': 'None',
    'notes': 'no',
    'image_address': 'http://wwwwwwww.qqqqqqqaaaa.com',
}
```
- Sample Return:
```
# Wrong date format provided 
{
    "code": 211,
    "msg": "['“2011-01-” value has an invalid format. It must be in YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format.']"
}
```
```
# Successfully updated 
{
    "code": 210,
    "msg": "updated"
}
```
