import json as JSON
import jsonschema
from jsonschema import Draft4Validator
from flask import Blueprint, jsonify, request


import os
dir_path = os.path.dirname(os.path.realpath(__file__))


status_api = Blueprint('status_api', __name__)


@status_api.route('/status', methods=['GET'])
def status_get():
    '''
    It is handler for GET /status
    '''
    
    return jsonify()
