from flask import Blueprint, request
from middleware.token_auth import token_required
from middleware.admin_auth import admin_required
from middleware.shop_identifier import handle_subdomain

from controller._ProductController import ProductController

product_route = Blueprint('product', __name__)

@handle_subdomain
@product_route.route('/', subdomain="<subdomain>", methods=['GET'])
def get_products(subdomain):
    return ProductController(request=request, shop_name=subdomain).get_products()

@product_route.route('/<productId>', subdomain="<subdomain>", methods=['GET'])
@handle_subdomain
def get_one_product(productId: int, subdomain: str):
    return ProductController(request=request, shop_name=subdomain).get_one_product(product_id=productId)

@product_route.route('/', subdomain="<subdomain>", methods=['POST'])
@handle_subdomain
@token_required
@admin_required
def add_product(subdomain):
    return ProductController(request=request, shop_name=subdomain).add_product()

@product_route.route('/<productId>', subdomain="<subdomain>", methods=['DELETE'])
@handle_subdomain
@token_required
@admin_required
def delete_product(productId: int, subdomain):
    return ProductController(request=request, shop_name=subdomain).delete_product(productId=productId)

@product_route.route('/<productId>', subdomain="<subdomain>", methods=['PATCH'])
@handle_subdomain
@token_required
@admin_required
def edit_product(productId: int, subdomain):
    return ProductController(request=request, shop_name=subdomain).edit_product(productId=productId)

@product_route.route('/variant/<productId>', subdomain="<subdomain>", methods=['POST'])
@handle_subdomain
@token_required
@admin_required
def add_variant_product(productId: int, subdomain):
    return ProductController(request=request, shop_name=subdomain).add_product()

@product_route.route('/variant/<productId>', subdomain="<subdomain>", methods=['DELETE'])
@handle_subdomain
@token_required
@admin_required
def delete_variant_product(productId: int, subdomain):
    return ProductController(request=request, shop_name=subdomain).delete_product(productId=productId)

@product_route.route('/variant/<productId>', subdomain="<subdomain>", methods=['PUT'])
@handle_subdomain
@token_required
@admin_required
def edit_variant_product(productId: int, subdomain):
    return ProductController(request=request, shop_name=subdomain).edit_product(productId=productId)