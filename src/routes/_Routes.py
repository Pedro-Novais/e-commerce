from flask import Blueprint, blueprints
from .UserRoute import user_route
from .ProductsRoute import product_route
from .OrdersRoute import order_route
from .CategoryRoute import category_route
from .WebHook import webhook
from .ShopsRoute import shop_route
from .CouponsRoute import coupon_route

class Routes:
    def __init__(self, app):
        self.app = app

    def start_routes(self):
        self.app.register_blueprint(user_route, url_prefix='/api/user')
        self.app.register_blueprint(product_route, url_prefix='/api/product')
        self.app.register_blueprint(order_route, url_prefix='/api/order')
        self.app.register_blueprint(category_route, url_prefix='/api/category')
        self.app.register_blueprint(webhook, url_prefix='/api/webhook')
        self.app.register_blueprint(shop_route, url_prefix='/api/shop')
        self.app.register_blueprint(coupon_route, url_prefix='/api/coupon')