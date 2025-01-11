from flask import Blueprint, request
from middleware.token_auth import token_required
from middleware.admin_auth import admin_required
from middleware.shop_identifier import handle_subdomain

from controller._CouponController import CouponController

coupon_route = Blueprint('coupon', __name__)

@coupon_route.route('/', subdomain="<subdomain>", methods=['POST'])
@handle_subdomain
def post_coupon(subdomain):
    return CouponController(request=request, shop_name=subdomain).post_coupon()