from jsonschema import validate

from src.validator.schema import schema

try:
    validate(instance={
        "name": "António Gabriel",
        "email": "test@gmail.com",
        "phone": 992322453,
    }, schema=schema)
except Exception as e:
    print(e)