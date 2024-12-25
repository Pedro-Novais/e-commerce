from flask import Blueprint, request
from middleware.token_auth import token_required
from middleware.admin_auth import admin_required

from controller._ProductController import ProductController

product_route = Blueprint('product', __name__)

@product_route.route('/', methods=['GET'])
def get_products():
    return ProductController(request=request).get_products()

@product_route.route('/<productId>', methods=['GET'])
def get_one_product(productId: int):
    return ProductController(request=request).get_one_product(product_id=productId)

@product_route.route('/', methods=['POST'])
@token_required
@admin_required
def add_product():
    return ProductController(request=request).add_product()

@product_route.route('/<productId>', methods=['DELETE'])
@token_required
@admin_required
def delete_product(productId: int):
    return ProductController(request=request).delete_product(productId=productId)

@product_route.route('/<productId>', methods=['PATCH'])
@token_required
@admin_required
def edit_product(productId: int):
    return ProductController(request=request).edit_product(productId=productId)