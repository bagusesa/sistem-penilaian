from flask import abort, make_response, jsonify, request
from marshmallow import ValidationError
from input_schema import *

def validate_schema(data):
    schema = InputSchema()
    try:
        return schema.load(data)
    except ValidationError as e:
        abort(make_response(jsonify(Status="Failed", Message=str(e.messages)), 400))