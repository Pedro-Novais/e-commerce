from flask import Request
from middleware.error_handler import error_handler

class CouponController:
    def __init__(self, request: Request, shop_name: str):
        self.request = request
        self.shop = shop_name

    def post_coupon():
        try:
            # action = GetUser(userId=userId, shop_name=self.shop_name).action()
            # return jsonify(action), 201
            pass
        
        except Exception as e:
            return error_handler(error=e)