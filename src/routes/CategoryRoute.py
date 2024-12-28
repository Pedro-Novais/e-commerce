from flask import Blueprint, request
from middleware.token_auth import token_required
from middleware.admin_auth import admin_required
from middleware.shop_identifier import handle_subdomain

from controller._CategoryController import CategoryController

category_route = Blueprint('category', __name__)

@category_route.route('/', subdomain="<subdomain>", methods=['POST'])
@handle_subdomain
@token_required
@admin_required
def create_category(subdomain):
    return CategoryController(request=request, shop_name=subdomain).create_category()

@category_route.route('/<categoryId>', subdomain="<subdomain>", methods=['PATCH'])
@handle_subdomain
@token_required
@admin_required
def update_category(categoryId, subdomain):
    return CategoryController(request=request, shop_name=subdomain).update_category(category_id=categoryId)

@category_route.route('/<categoryId>', subdomain="<subdomain>", methods=['DELETE'])
@handle_subdomain
@token_required
@admin_required
def delete_category(categoryId, subdomain):
    return CategoryController(request=request, shop_name=subdomain).delete_category(category_id=categoryId)