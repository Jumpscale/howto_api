import json as JSON
import jsonschema
from jsonschema import Draft4Validator
from flask import Blueprint, jsonify, request


import os
dir_path = os.path.dirname(os.path.realpath(__file__))

User_schema =  JSON.load(open('./schema/User_schema.json'))
User_schema_resolver = jsonschema.RefResolver('file://' + dir_path + '/schema/', User_schema)
User_schema_validator = Draft4Validator(User_schema, resolver=User_schema_resolver)


user_api = Blueprint('user_api', __name__)


@user_api.route('/user', methods=['GET'])
def user_get():
    '''
    Get a list of users
    It is handler for GET /user
    '''
    
    return jsonify()


@user_api.route('/user/<id>', methods=['GET'])
def getUser(id):
    '''
    Get user, id=int
    It is handler for GET /user/<id>
    '''
    
    return jsonify()


@user_api.route('/user/<id>', methods=['POST'])
def updateUser(id):
    '''
    Update user
    It is handler for POST /user/<id>
    '''
    
    inputs = request.get_json()
    try:
        User_schema_validator.validate(inputs)
    except jsonschema.ValidationError as e:
        return jsonify(errors="bad request body"), 400
    
    return jsonify()


@user_api.route('/user/<id>', methods=['DELETE'])
def deleteUser(id):
    '''
    Delete user
    It is handler for DELETE /user/<id>
    '''
    
    return jsonify()
