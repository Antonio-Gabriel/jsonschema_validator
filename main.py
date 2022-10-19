from jsonschema import validate

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

try:
    validate(instance={
        "name": "António Gabriel",
        "email": "test@gmail.com",
        "phone": 992322453,
    }, schema=schema)
except Exception as e:
    print(e)