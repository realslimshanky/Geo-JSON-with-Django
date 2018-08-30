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
GET /api/user (requires authentication)
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
PATCH /api/user (requires authentication)
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

## List all active profiles
```
GET /api/user/all
```

__Response__

```json
[
    {
        "id": "a6959577-69d1-4c8f-9dc8-6caa5a86e847",
        "name": "New User",
        "phone_number": "9999999999",
        "language": "en",
        "currency": "USD",
        "email": "new@user.com"
    },
    {
        "id": "2a04d258-b6af-4fe8-8daa-95ccc8da336f",
        "name": "Shashank Kumar",
        "phone_number": "8888888888",
        "language": "hi",
        "currency": "INR",
        "email": "root@root.com"
    }
]
```

## Delete current user
```
DELETE /api/user (requires authentication)
```

__Response__


```
Status: 204 No-Content
```

# Service Region

## Create Service Region
```
POST /api/service (require authentication)
```

__Example__
```json
{
    "name": "Sea side apartments",
    "price": 300,
    "region_coordinates": "[(11.22, 13.11), (22.33, 22.33), (41.11, 42.22), (52.43, 5.22)]"
}
```

__Response__
```json
{
    "id": "f8652f56-7360-40a0-a10a-85c69c88e940",
    "provider": "Shashank Kumar",
    "name": "Sea side apartments",
    "price": 300,
    "region_coordinates": {
        "coordinates": [
            [
                [
                    11.22,
                    13.11
                ],
                [
                    22.33,
                    22.33
                ],
                [
                    41.11,
                    42.22
                ],
                [
                    52.43,
                    5.22
                ],
                [
                    11.22,
                    13.11
                ]
            ]
        ],
        "type": "Polygon"
    }
}
```

## List Service Region
```
GET /api/service
```

__Response__

```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "d8dbbfc1-cc98-45f2-b469-f57e750e77d9",
            "provider": "Shashank Kumar",
            "name": "Metropolis",
            "price": 0,
            "region_coordinates": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            30.21,
                            30.21
                        ],
                        [
                            21.22,
                            21.22
                        ],
                        [
                            53.45,
                            53.45
                        ],
                        [
                            60.00,
                            60.00
                        ],
                        [
                            30.21,
                            30.21
                        ]
                    ]
                ]
            }
        },
        {
            "id": "f8652f56-7360-40a0-a10a-85c69c88e940",
            "provider": "Shashank Kumar",
            "name": "plot no 13",
            "price": 100,
            "region_coordinates": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            20.00,
                            30.00
                        ],
                        [
                            15.12,
                            13.12
                        ],
                        [
                            34.34,
                            33.45
                        ],
                        [
                            65.32,
                            12.36
                        ],
                        [
                            20.00,
                            30.00
                        ]
                    ]
                ]
            }
        },
        {
            "id": "1b16a8d6-3892-4e0c-a7fd-cb4e990a3b3b",
            "provider": "Bhavesh Joshi",
            "name": "Garden Area",
            "price": 0,
            "region_coordinates": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            11.00,
                            11.00
                        ],
                        [
                            30.23,
                            50.56
                        ],
                        [
                            50.11,
                            50.23
                        ],
                        [
                            50.11,
                            10.23
                        ],
                        [
                            11.00,
                            11.00
                        ]
                    ]
                ]
            }
        }
    ]
}
```

## Retrieve Service Region
```
GET /api/service/:id
```

__Response__

```json
{
    "id": "f8652f56-7360-40a0-a10a-85c69c88e940",
    "provider": "Shashank Kumar",
    "name": "plot no 13",
    "price": 100,
    "region_coordinates": {
        "coordinates": [
            [
                [
                    20.00,
                    30.00
                ],
                [
                    15.12,
                    13.12
                ],
                [
                    34.34,
                    33.45
                ],
                [
                    65.32,
                    12.36
                ],
                [
                    20.00,
                    30.00
                ]
    ]
        ],
        "type": "Polygon"
    }
}
```

## Update Service Region
```
PUT /api/service/:id (requires authentication)
```

__Example__
```json
{
    "name": "South Villas",
    "price": 100,
    "region_coordinates": "[(11.22, 13.11), (22.33, 22.33), (41.11, 42.22), (52.43, 55.22)]"
}
```

__Response__
```json
{
    "id": "f8652f56-7360-40a0-a10a-85c69c88e940",
    "provider": "Shashank Kumar",
    "name": "South Villas",
    "price": 100,
    "region_coordinates": {
        "coordinates": [
            [
                [
                    11.22,
                    13.11
                ],
                [
                    22.33,
                    22.33
                ],
                [
                    41.11,
                    42.22
                ],
                [
                    52.43,
                    55.22
                ],
                [
                    11.22,
                    13.11
                ]
            ]
        ],
        "type": "Polygon"
    }
}
```

## Partial Update Service Region
```
PATCH /api/service/:id (requires authentication)
```

__Example__
```json
{
    "name": "Sea side villa"
}
```

__Response__
```json
{
    "id": "f8652f56-7360-40a0-a10a-85c69c88e940",
    "provider": "New User",
    "name": "Sea side villa",
    "price": 300,
    "region_coordinates": {
        "coordinates": [
            [
                [
                    11.22,
                    13.11
                ],
                [
                    22.33,
                    22.33
                ],
                [
                    41.11,
                    42.22
                ],
                [
                    52.43,
                    55.22
                ],
                [
                    11.22,
                    13.11
                ]
            ]
        ],
        "type": "Polygon"
    }
}
```

## Delete Service Region
```
DELETE /api/service/:id (requires authentication)
```

__Response__
```
204 No Content
```

## Search Service Region
```
POST /api/service/search
```

__Example__
```json
{
    "longitude": 30.00,
    "latitude": 38.00
}
```

__Response__
```json
[
    {
        "id": "d8dbbff1-cc98-45f2-b469-f57e750e77d9",
        "provider": "Mister Verma",
        "name": "Village Area",
        "price": 50,
        "region_coordinates": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        11.22,
                        13.11
                    ],
                    [
                        52.43,
                        55.22
                    ],
                    [
                        30.00,
                        40.00
                    ],
                    [
                        11.22,
                        13.11
                    ]
                ]
            ]
        }
    }
]
```
