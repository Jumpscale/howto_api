import json as JSON
import jsonschema
from jsonschema import Draft4Validator
from flask import Blueprint, jsonify, request


import os
dir_path = os.path.dirname(os.path.realpath(__file__))

Group_schema =  JSON.load(open('./schema/Group_schema.json'))
Group_schema_resolver = jsonschema.RefResolver('file://' + dir_path + '/schema/', Group_schema)
Group_schema_validator = Draft4Validator(Group_schema, resolver=Group_schema_resolver)


group_api = Blueprint('group_api', __name__)


@group_api.route('/group', methods=['GET'])
def group_get():
    '''
    Get a list of groups
    It is handler for GET /group
    '''
    
    return jsonify()


@group_api.route('/group/<id>', methods=['GET'])
def getGroup(id):
    '''
    Get group, id=int
    It is handler for GET /group/<id>
    '''
    
    return jsonify()


@group_api.route('/group/<id>', methods=['POST'])
def updateGroup(id):
    '''
    Update group
    It is handler for POST /group/<id>
    '''
    
    inputs = request.get_json()
    try:
        Group_schema_validator.validate(inputs)
    except jsonschema.ValidationError as e:
        return jsonify(errors="bad request body"), 400
    
    return jsonify()


@group_api.route('/group/<id>', methods=['DELETE'])
def deleteGroup(id):
    '''
    Delete group
    It is handler for DELETE /group/<id>
    '''
    
    return jsonify()
