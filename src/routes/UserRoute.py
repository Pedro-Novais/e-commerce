from flask import Blueprint, request, jsonify
from middleware.token_auth import token_required

from domains.orders._CreateOrder import CreateOrder
from controller._UserController import UserController

user_route = Blueprint('user', __name__)

@user_route.route('/', methods=['GET'])
@token_required
def get_user(userId):
    return UserController(request=request).get_user(userId=userId)

@user_route.route('/', methods=['POST'])
def post_user():
    return UserController(request=request).create_user()

@user_route.route('/login', methods=['POST'])
def login_user():
    return UserController(request=request).login_user()

#implementação pendente
@user_route.route('/', methods=['PATCH'])
@token_required
def patch_user(userId):
    return UserController(request=request).update_user(userId=userId)

@user_route.route('/', methods=['DELETE'])
@token_required
def delete_user(userId: int):
    return UserController(request=request).delete_user(userId=userId)

@user_route.route('/address', methods=['POST'])
@token_required
def create_address(userId):
    return UserController(request=request).add_address_from_user(userId=userId)

@user_route.route('/address/<addressId>', methods=['PUT'])
@token_required
def update_address(userId, addressId):
    return UserController(request=request).update_address_from_user(userId=userId, address_id=addressId)

@user_route.route('/address/<addressId>', methods=['DELETE'])
@token_required
def delete_address(userId, addressId):
    return UserController(request=request).delete_address_from_user(user_id=userId, address_id=addressId)