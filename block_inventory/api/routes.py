from flask import Blueprint, request, jsonify, redirect, url_for
from block_inventory.helpers import token_required
from block_inventory.models import db, Blocks
from flask_login import login_required, current_user


api = Blueprint('api', __name__, template_folder = '../site/site_templates')


# @api.route('/getdata')
# @token_required
# def getdata(our_user):
#     return {'some': 'value'}

# #create drone endpoint
# @api.route('/drones', methods = ['POST'])
# @token_required
# def create_drone(our_user):
#     name = request.json['name']
#     description = request.json['description']
#     price = request.json['price']
#     camera_quality = request.json['camera_quality']
#     flight_time = request.json['flight_time']
#     max_speed = request.json['max_speed']
#     dimensions = request.json['dimensions']
#     weight = request.json['weight']
#     cost_of_production = request.json['cost_of_production']
#     series = request.json['series']
#     random_joke = random_joke_generator()
#     user_token = our_user.token

#     print(f"User Token: {our_user.token}")

#     drone = Drone(name, description, price, camera_quality, flight_time, max_speed, dimensions, weight, cost_of_production, series, random_joke, user_token=user_token)

#     db.session.add(drone)
#     db.session.commit()

#     response = drone_schema.dump(drone)

#     return jsonify(response)


# #Retrieve all drone endpoints
# @api.route('/drones', methods = ['GET'])
# @token_required
# def get_drones(our_user):
#     owner = our_user.token
#     drones = Drone.query.filter_by(user_token= owner).all()
#     response = drones_schema.dump(drones)

#     return jsonify(response)


# #Retrieve One Drone Endpoint
# @api.route('/drones/<id>', methods = ['GET'])
# @token_required
# def get_drone(our_user, id):
#     owner = our_user.token
#     if owner == our_user.token:
#         drone = Drone.query.get(id)
#         response = drone_schema.dump(drone)
#         return jsonify(response)
#     else:
#         return jsonify({'message': 'Valid Id Required'}), 401
    
# #Update Drone Endpoint
# @api.route('/drones/<id>', methods = ['PUT','POST'])
# @token_required
# def update_drone(our_user, id):
#     drone = Drone.query.get(id)
#     drone.name = request.json['name']
#     drone.description = request.json['description']
#     drone.price = request.json['price']
#     drone.camera_quality = request.json['camera_quality']
#     drone.flight_time = request.json['flight_time']
#     drone.max_speed = request.json['max_speed']
#     drone.dimensions = request.json['dimensions']
#     drone.weight = request.json['weight']
#     drone.cost_of_production = request.json['cost_of_production']
#     drone.series = request.json['series']
#     drone.random_joke = random_joke_generator()
#     drone.user_token = our_user.token

#     db.session.commit()
#     response = drone_schema.dump(drone)
#     return jsonify(response)

# #Delete Drone Endpoint
# @api.route('/blocks/<id>', methods = ['DELETE'])
# @token_required
# def delete_block(our_user, id):
#     drone = Drone.query.get(id)
#     db.session.delete(drone)
#     db.session.commit()

#     response = drone_schema.dump(drone)
#     return jsonify(response)








# @api.route('/delete_block/<block_id>', methods=['POST'])
# @login_required
# def delete_block(block_id):
#     print('test1')
#     # user_token = current_user.token
#     block = Blocks.query.get(block_id)
#     print('test2')
#     db.session.delete(block)
#     db.session.commit()
#     print('test3')
#     return redirect(url_for('site.profile'))