schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "email": {
            "type": "string",
            "pattern": "^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
        },
        "phone": {
            "type": "number"
        }
    }
}