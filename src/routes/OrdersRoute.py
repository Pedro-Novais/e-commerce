from flask import Blueprint, request
from middleware.token_auth import token_required
from middleware.admin_auth import admin_required
from middleware.shop_identifier import handle_subdomain

from controller._OrderController import OrderController

order_route = Blueprint('order', __name__)

@order_route.route('/', subdomain="<subdomain>", methods=['POST'])
@handle_subdomain
@token_required
def create_order(userId, subdomain):
    return OrderController(request=request, shop_name=subdomain).create_order(user_id=userId)