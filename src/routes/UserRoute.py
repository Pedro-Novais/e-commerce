from flask import Blueprint, request
from middleware.token_auth import token_required
from middleware.shop_identifier import handle_subdomain

from controller._UserController import UserController

user_route = Blueprint('user', __name__)

@user_route.route('/', subdomain="<subdomain>", methods=['GET'])
@handle_subdomain
@token_required
def get_user(userId: int, subdomain: str):
    return UserController(request=request, shop_name=subdomain).get_user(userId=userId)

@user_route.route('/', subdomain="<subdomain>", methods=['POST'])
@handle_subdomain
def post_user(subdomain):
    return UserController(request=request, shop_name=subdomain).create_user()

@user_route.route('/login', subdomain="<subdomain>", methods=['POST'])
@handle_subdomain
def login_user(subdomain):
    return UserController(request=request, shop_name=subdomain).login_user()

#implementação pendente
@user_route.route('/', methods=['PATCH'])
@token_required
def patch_user(userId):
    return UserController(request=request).update_user(userId=userId)

@user_route.route('/', subdomain="<subdomain>", methods=['DELETE'])
@handle_subdomain
@token_required
def delete_user(userId: int, subdomain: str):
    return UserController(request=request, shop_name=subdomain).delete_user(userId=userId)

@user_route.route('/address', subdomain="<subdomain>", methods=['POST'])
@handle_subdomain
@token_required
def create_address(userId, subdomain):
    return UserController(request=request, shop_name=subdomain).add_address_from_user(userId=userId)

@user_route.route('/address/<addressId>', subdomain="<subdomain>", methods=['PUT'])
@handle_subdomain
@token_required
def update_address(userId, addressId, subdomain):
    return UserController(request=request, shop_name=subdomain).update_address_from_user(userId=userId, address_id=addressId)

@user_route.route('/address/<addressId>', subdomain="<subdomain>", methods=['DELETE'])
@handle_subdomain
@token_required
def delete_address(userId, addressId, subdomain):
    return UserController(request=request, shop_name=subdomain).delete_address_from_user(user_id=userId, address_id=addressId)