import json as JSON
import jsonschema
from jsonschema import Draft4Validator
from flask import Blueprint, jsonify, request


import os
dir_path = os.path.dirname(os.path.realpath(__file__))

Member_schema =  JSON.load(open('./schema/Member_schema.json'))
Member_schema_resolver = jsonschema.RefResolver('file://' + dir_path + '/schema/', Member_schema)
Member_schema_validator = Draft4Validator(Member_schema, resolver=Member_schema_resolver)

Network_schema =  JSON.load(open('./schema/Network_schema.json'))
Network_schema_resolver = jsonschema.RefResolver('file://' + dir_path + '/schema/', Network_schema)
Network_schema_validator = Draft4Validator(Network_schema, resolver=Network_schema_resolver)


network_api = Blueprint('network_api', __name__)


@network_api.route('/network', methods=['GET'])
def network_get():
    '''
    Get a list of networks
    It is handler for GET /network
    '''
    
    return jsonify()


@network_api.route('/network/<id>', methods=['GET'])
def getNetwork(id):
    '''
    Get network, id=ZeroTier network ID (16 hex digits)
    It is handler for GET /network/<id>
    '''
    
    return jsonify()


@network_api.route('/network/<id>', methods=['POST'])
def updateNetwork(id):
    '''
    Update network
    It is handler for POST /network/<id>
    '''
    
    inputs = request.get_json()
    try:
        Network_schema_validator.validate(inputs)
    except jsonschema.ValidationError as e:
        return jsonify(errors="bad request body"), 400
    
    return jsonify()


@network_api.route('/network/<id>', methods=['DELETE'])
def deleteNetwork(id):
    '''
    Delete network
    It is handler for DELETE /network/<id>
    '''
    
    return jsonify()


@network_api.route('/network/<networkid>/member', methods=['GET'])
def network_byNetworkidmember_get(networkid):
    '''
    Get a list of members
    It is handler for GET /network/<networkid>/member
    '''
    
    return jsonify()


@network_api.route('/network/<networkid>/member/<id>', methods=['GET'])
def getMember(id, networkid):
    '''
    Get member, id=10-digit ZeroTier node ID (a.k.a. ZeroTier address)
    It is handler for GET /network/<networkid>/member/<id>
    '''
    
    return jsonify()


@network_api.route('/network/<networkid>/member/<id>', methods=['POST'])
def updateMember(id, networkid):
    '''
    Update member
    It is handler for POST /network/<networkid>/member/<id>
    '''
    
    inputs = request.get_json()
    try:
        Member_schema_validator.validate(inputs)
    except jsonschema.ValidationError as e:
        return jsonify(errors="bad request body"), 400
    
    return jsonify()
