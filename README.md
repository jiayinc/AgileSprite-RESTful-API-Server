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
# Successfully created 
{
    "code": 105,
    "msg": "Account created successfully! Let's go!"
}
```
```
# Username exists
{
    "code": 106,
    "msg": "This email address is invalid or has been registered, a different email address is required."
}
```
```
# Invalid password
{
    "code": 107,
    "msg": "Password must contains at least a digit, a letter, a upper case letter and a symbol, and length is between 8 and 30"
}
```
```
# Errors
{
    "code": 108,
    "msg": "Unexpected errors occurred! Please refresh the page and try again!"
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
# Successfully signed in 
{
    "code": 100,
    "msg": "Login successfully! Let's go!",
    "token": "bb41305c3996ab47e4d729821b3c6232c003099d"
}
```
```
# Wrong login information
{
    "code": 101,
    "msg": "Wrong username/password!"
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
    "msg": "Log out performed, token was disabled."
}
# wrong token
{
    "code": 120,
    "msg": "Error! Token authentication failed."
}
```

#### Get User Detail
Users can get their information
- Request Type: POST
- Request Address: /account/get/  
- Request Fields:
    - token: String
- Return Fields:
    - code: Integer
    - msg: String
    - details:
      - first name: String
      - last name: String
      - email: String
      - birthday: Date
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
    "code": 125,
    "msg": "User information was retrieved successfully.",
    "details": {
        "email": "123",
        "birthday": "2021-10-25T09:40:23.207Z",
        "first_name": "gg",
        "last_name": "ww"
    }
}
```

#### Update Information (critical information included)
Users can update their general information
- Request Type: POST
- Request Address: /account/update/  
- Request Fields:
    - token: String, mandatory
    - with one of more of following parameter(s)
      - birthday: Date
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
    'birthday': '2011-01-02'
}
```
- Sample Return:

```
# Invalid password update attempt
{
    "code": 109,
    "msg": "Password must contains at least a digit, a letter, a upper case letter and a symbol, and length is between 8 and 30"
}
```

```
# Email update collision
{
    "code": 110,
    "msg": "This email address is invalid or has been registered, a different email address is required."
}
```
```
# Successfully updated 
{
    "code": 111,
    "msg": "User information was updated successfully."
}
```
```
# Unexpected error (Unused)
{
    "code": 112
    "msg": "Unexpected errors occurred! Please refresh the page and try again!"
}
```
```
# Invalid token
{
    "code": 120,
    "msg": "Error! Token authentication failed."
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
    - first_name: String
    - last_name: String
- Return Fields:
    - code: Integer
    - msg: String
    - details:
      - contact_id: Integer
- Sample Request:
```
{
    'token': '611088d71f3044dd640b9f9209e92d60786a0d5a',
    'first_name': 'gg',
    'last_name': 'uu',
}
```
- Sample Return:
```
# Successfully added 
{
    "code": 200,
    "msg": "add success"
    "details":{
        "contact_id": 1
    }
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

### Story
#### Add a Story
Users can add a contact's story
- Request Type: POST
- Request Address: /story/add/  
- Request Fields:
    - token: String
    - contact_id: Integer
    - location: String
    - date: Date
    - content: String
- Return Fields:
    - code: Integer
    - msg: String
- Sample Request:
```
{
    'token': '611088d71f3044dd640b9f9209e92d60786a0d5a',
    'contact_id': 3,
    'location': 'mel',
    'content': 'what???',
    'date': 2020-01-21
}
```
- Sample Return:
```
# Successfully added 
{
    "code": 400,
    "msg": "add success"
}
```

#### Get All Stories
Users can get stories of a contact
- Request Type: POST
- Request Address: /story/get_all/  
- Request Fields:
    - token: String
    - contact_id: Integer
- Return Fields:
    - code: Integer
    - msg: String
    - Stories: List of Stories, where each story contains
      - id: Integer, story's ID
      - contact_id: Integer
      - location: String
      - date: Date
      - content: String
- Sample Request:
```
{
    'token': '611088d71f3044dd640b9f9209e92d60786a0d5a',
    'contact_id': 5
}
```
- Sample Return:
```
{
    "code": 405,
    "msg": "get success",
    "Stories": [
        {
            "id": 2,
            "contact_id": 1,
            "location": "mel",
            "content": "what???",
            "date": 2020-01-21
        }
    ]
}
```

#### Get A Story
Users can get a story of a contact
- Request Type: POST
- Request Address: /story/get/  
- Request Fields:
    - token: String
    - contact_id: Integer
    - story_id: Integer
- Return Fields:
    - code: Integer
    - msg: String
    - Stories: List of Stories, where each story contains
      - id: Integer, story's ID
      - contact_id: Integer
      - location: String
      - date: Date
      - content: String
- Sample Request:
```
{
    'token': '611088d71f3044dd640b9f9209e92d60786a0d5a',
    'contact_id': 5,
    'story_id': 6
}
```
- Sample Return:
```
{
    "code": 410,
    "msg": "get success",
    "Stories": [
        {
            "id": 2,
            "contact_id": 1,
            "location": "mel",
            "content": "what???",
            "date": 2020-01-21
        }
    ]
}
```

#### Update Story Information
Users can update a contact's story information
- Request Type: POST
- Request Address: /story/update/  
- Request Fields:
    - token: String, mandatory
    - contact_id: Integer, contact's ID, mandatory
    - story_id: Integer, story's ID, mandatory
    - with one of more of following parameter(s)
      - location: String
      - date: String
      - content: Date
- Return Fields:
    - code: Integer
    - msg: String
- Sample Request:
```
{
    'token': '3b6a7f2885ecbaec38261c2cdf7be0b1263029f7',
    'contact_id': 2,
    'story_id': 5,
    'company': 'abc.co',
    'location': 'Melbourne',
    'date': 1999-08-01,
    'content': 'None',
}
```
- Sample Return:
```
# Wrong date format provided 
{
    "code": 416,
    "msg": "['“2011-01-” value has an invalid format. It must be in YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format.']"
}
```
```
# Successfully updated 
{
    "code": 415,
    "msg": "updated"
}
```

#### Delete a Story
Users can delete a story
- Request Type: POST
- Request Address: /story/delete/  
- Request Fields:
    - token: String
    - contact_id: Integer
    - story_id: Integer
- Return Fields:
    - code: Integer
    - msg: String
- Sample Request:
```
{
    'token': 'de99673b5ca9832e5a4f616c8ec81f563f4e0d84',
    'contact_id': 2,
    'story_id': 3
}
```
- Sample Return:
```
# Successfully deleted
{
    "code": 425,
    "msg": "delete success"
}
```
### Group

#### Create a Group

Users can create a group

- Request Type: POST
- Request Address: /group/create/  
- Request Fields:
  - token: String
  - name: String
- Return Fields:
  - code: Integer
  - msg: String
- Sample Request:

```
{
    "token":
"3067a0ce9c21c40dbd573695e517bcae186525d6",
    "name":"group_test"
}
```

- Sample Return:

```
# Successfully added 
{
    "code": 500,
    "msg": "create group success"
}
```

#### Add Contacts to Groups

Users can add contacts to different group

- Request Type: POST
- Request Address: /group/add_contact_group/  
- Request Fields:
  - token: String
  - group_id: Integer
  - contact_id: Integer
- Return Fields:
  - code: Integer
  - msg: String
- Sample Request:

```
{
    "token": "3067a0ce9c21c40dbd573695e517bcae186525d6",
    "group_id":"1",
    "contact_id":"1"
}
```

- Sample Return:

```
{
    "code": 507,
    "msg": "add contact success"
}
```

#### Delete Contacts From Groups

Users can delete a contact from a group

- Request Type: POST
- Request Address: /group/delete_contact_group/  
- Request Fields:
  - token: String
  - group_id: Integer
  - contact_id: Integer
- Return Fields:
  - code: Integer
  - msg: String
- Sample Request:

```
{
    "token": "3067a0ce9c21c40dbd573695e517bcae186525d6",
    "group_id":"1",
    "contact_id":"1"
}
```

- Sample Return:

```
{
    "code": 504,
    "msg": "delete contact success"
}
```

#### Delete a Group

Users can delete a group

- Request Type: POST
- Request Address: /group/delete/  
- Request Fields:
  - token: String
  - group_id: Integer
- Return Fields:
  - code: Integer
  - msg: String
- Sample Request:

```
{
    "token": "3067a0ce9c21c40dbd573695e517bcae186525d6",
    "id":"2"
}
```

- Sample Return:

```
# Successfully deleted
{
    "code": 503,
    "msg": "delete group sucess"
}
```
### Calendar

#### Create an Event

Users can create a  event in calendar.

- Request Type: POST
- Request Address: /calendar/create_event/  
- Request Fields:
  - token: String
  - location: String
  - start_time: Date
  - end_time: Date
  - related_people: String
  - comment: String
  - name: String
  - category: String
  - date: Date
- Return Fields:
  - code: Integer
  - msg: String
- Sample Request:

```
{
    "token": "3067a0ce9c21c40dbd573695e517bcae186525d6",
    "location":"baotou",
    "start_time":"2021-11-11 10:10",
    "end_time":"2021-11-11 10:10",
    "related_people":"dlx",
    "comment":"love", "name":"express love",
    "category":"life", "date":"2021-11-01"
}
```

- Sample Return:

```
{
    "code": 513, 
    "msg": "create event successfuly"
}
```



#### Get the day of an Event

Users can edit event's detail in case it may change in the future

- Request Type: POST
- Request Address: /calendar/get_day_events/  
- Request Fields:
  - token: String
  - date: Date
- Return Fields:
  - code: Integer
  - msg: String
- Sample Request:

```
{
    "token": "3067a0ce9c21c40dbd573695e517bcae186525d6",
    "date":"2021-11-01" 
}
```

- Sample Return:

```
{
"code": 517, "jobects": "[{"model": "mycalendar.event", "pk": 2, "fields": {"name": "express love", "user_id": "1", "location": "baotou", "start_time": "2021-11-11T10:10:00Z", "end_time": "2021-11-11T10:10:00Z", "related_people": "dlx", "date": "2021-11-01", "comments": "love", "category": "life"}}]"
}
```



#### Update the Event

Users can edit event's detail in case it may change in the future

- Request Type: POST
- Request Address: /calendar/update_event/  
- Request Fields:
  - token: String
  - location: String
  - start_time: Date
  - end_time: Date
  - related_people: String
  - comment: String
  - name: String
  - category: String
- Return Fields:
  - code: Integer
  - msg: String
- Sample Request:

```
{
"token":"3067a0ce9c21c40dbd573695e517bcae186525d6",
"id":"2","location":"baotou","name":"express love"
}
```

- Sample Return:

```
{
    "code": 519,
    "msg": "update event successfuly"
}
```



#### Delete an Event

Users can delete a event

- Request Type: POST
- Request Address: /calendar/delete_event/  
- Request Fields:
  - token: String
  - id: Integer
- Return Fields:
  - code: Integer
  - msg: String
- Sample Request:

```
{
    "token": "3067a0ce9c21c40dbd573695e517bcae186525d6",
    "id":"1" 
}
```

- Sample Return:

```
# Successfully deleted
{
    "code": 515,
    "msg": "delete event succ"
}
```

