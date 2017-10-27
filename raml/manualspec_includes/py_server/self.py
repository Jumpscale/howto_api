from flask import Blueprint, jsonify, request



self_api = Blueprint('self_api', __name__)


@self_api.route('/self', methods=['GET'])
def self_get():
    '''
    It is handler for GET /self
    '''
    
    return jsonify()
