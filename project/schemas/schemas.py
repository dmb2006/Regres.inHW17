post_users = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "id": {
            "type": "string"
        },
        "createdAt": {
            "type": "string"
        }
    },
    "additionalProperties": False,
    "required": [
        "name",
        "job",
        "id",
        "createdAt"
    ]
}

login_user = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "token": {
            "type": "string"
        }
    },
    "additionalProperties": True,
    "required": [
        "token"
    ]
}

single_user = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "email": {
                    "type": "string"
                },
                "first_name": {
                    "type": "string"
                },
                "last_name": {
                    "type": "string"
                },
                "avatar": {
                    "type": "string"
                }
            },
            "additionalProperties": False,
            "required": [
                "id",
                "email",
                "first_name",
                "last_name",
                "avatar"
            ]
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                }
            },
            "additionalProperties": False,
            "required": [
                "url",
                "text"
            ]
        }
    },
    "additionalProperties": False,
    "required": [
        "data",
        "support"
    ]
}