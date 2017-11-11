import json as JSON
import jsonschema
from jsonschema import Draft4Validator
from flask import Blueprint, jsonify, request


import os
dir_path = os.path.dirname(os.path.realpath(__file__))


self_api = Blueprint('self_api', __name__)


@self_api.route('/self', methods=['GET'])
def self_get():
    '''
    It is handler for GET /self
    '''
    
    return jsonify()
