from flask import Blueprint, request
from middleware.token_auth import token_required
from middleware.shop_identifier import handle_subdomain
from middleware.admin_auth import admin_required
from middleware.webhook_auth_panel import handle_webhook_auth_panel

from controller._ShopControoller import ShopController

shop_route = Blueprint('shop', __name__)

@shop_route.route('/', subdomain="<subdomain>", methods=['GET'])
@handle_subdomain
def get_shop(subdomain: str):
    return ShopController(request=request, shop_name=subdomain).get_shop()

@shop_route.route('/', subdomain="<subdomain>", methods=['POST'])
@handle_subdomain
@token_required
@admin_required
def create_shop(subdomain):
    return ShopController(request=request, shop_name=subdomain).post_shop()

@shop_route.route('/', subdomain="<subdomain>", methods=['PATCH'])
@handle_subdomain
@token_required
@admin_required
def update_shop(userId: int, subdomain: str):
    pass
    # return ShopController(request=request, shop_name=subdomain).post_shop(userId=userId)