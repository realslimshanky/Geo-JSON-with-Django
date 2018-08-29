For api overview and usages, check out [this page](overview.md).

[TOC]

# Authentication

## Login

```
POST /api/auth/login
```

**Parameters**

Name     | Description
---------|-------------------------------------
email    | email of the user. 
password | password of the user.

**Request**
```json
{
    "email": "hello@example.com",
    "password": "VerySafePassword0909"
}
```

**Response**
```json

Status: 200 OK
{
    "auth_token": "eyJ0eXAiOiJKV1QiL",
    "email": "hello@example.com",
    "id": "f9dceed1-0f19-49f4-a874-0c2e131abf79",
    "name": "Your name",
    "phone_number": "+999999999",
    "language": "en",
    "currency": "USD",
}
```

## Register

```
POST /api/auth/register
```

**Parameters**

Name         | Description
-------------|-------------------------------------
email        | email of the user. Errors out if email already registered.
password     | password of the user.
name         | full name of the user
phone_number | phone number in the format: '+999999999'. Up to 15 digits.
language     | Language choices as defined by ISO 639 https://en.wiktionary.org/wiki/Index:All_languages, currently the application supports, 'en', 'fr', 'de', 'it', 'ja', 'hi', 'ko'and 'ru'.
currency     | currency choices as defined by ISO 4217 https://en.wikipedia.org/wiki/ISO_4217#Active_codes, currtly the application supports, 'USD', 'EUR', 'JPY', 'INR', 'KPW', 'KRW' and 'RUB'.

**Request**
```json
{
    "email": "hello@example.com",
    "password": "VerySafePassword0909",
    "name": "New User",
    "phone_number": "+999999999",
    "language": "en",
    "currency": "USD",
}
```

**Response**
```json

Status: 201 Created
{
    "auth_token": "eyJ0eXAiOiJKV1QiLCJh",
    "email": "test@test.com",
    "id": "f9dceed1-0f19-49f4-a874-0c2e131abf79",
    "name": "New User",
    "phone_number": "+999999999",
    "language": "en",
    "currency": "USD",
}
```

## Change password

```
POST /api/auth/password_change (requires authentication)
```

**Parameters**

Name             | Description
-----------------|-------------------------------------
current_password | Current password of the user.
new_password     | New password of the user.

**Request**
```json
{
    "current_password": "NotSoSafePassword",
    "new_password": "VerySafePassword0909"
}
```

**Response**
```
Status: 204 No-Content
```


# Current user actions

## Get profile of current logged-in user
```
GET /api/me (requires authentication)
```

__Response__

```json
{
    "id": "629b1e03-53f0-43ef-9a03-17164cf782ac",
    "first_name": "John",
    "last_name": "Hawley",
    "email": "john@localhost.com"
}
```

## Update profile of current logged-in user
```
PATCH /api/me (requires authentication)
```

__Example__
```json
{
    "first_name": "James",
    "last_name": "Warner"
}
```

__Response__

```json
{
    "id": "629b1e03-53f0-43ef-9a03-17164cf782ac",
    "first_name": "James",
    "last_name": "Warner",
    "email": "john@localhost.com",
}
```
