import minecraft_data
mcd = minecraft_data("1.19")

from functools import wraps

import secrets
from flask import request, jsonify, json

from block_inventory.models import User

# import decimal



def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split(' ')[1]
            print(token)

        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        
        try:
            our_user = User.query.filter_by(token = token).first()
            print(our_user)
            if not our_user or our_user.token != token:
                return jsonify({'message': 'Token is invalid'})

        except:
            owner = User.query.filter_by(token=token).first()
            if token != owner.token and secrets.compare_digest(token, owner.token):
                return jsonify({'message': 'Token is invalid'})
        return our_flask_function(our_user, *args, **kwargs)
    return decorated


def find_block(block):
    block2 = block.lower().strip().replace(' ', '_')
    block = block.strip().title()
    for i in mcd.blocks.values():
        if i['displayName'] == block or i['name'] == block2:
            return i

# bruh = 'diamond'
# print(find_block('   Block of Diamond   '))